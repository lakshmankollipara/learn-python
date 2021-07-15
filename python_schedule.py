#!/usr/bin/python

import schedule
import psycopg2
import re
import argparse
import time
import logging
import os
import subprocess
from os import listdir
from os.path import isfile, join
from datetime import datetime

logging.basicConfig(format='%(asctime)s.%(msecs)03d %(levelname)s [%(funcName)s] %(message)s', datefmt='%Y-%m-%d,%H:%M:%S', level=logging.INFO)

parser = argparse.ArgumentParser(description='Read TMF Env and tenant')
parser.add_argument('--env', '-e', required=True, dest='env', help='TMF Environment(WSPT_TMF_ENV) (Should always end with version. ex: qa28, load27, prod28)')
parser.add_argument('--tenant', '-t', required=True, dest='tenant', help='TMF Tenant (ex: tenant01, tenant2, archive etc.)')
args = parser.parse_args()
env = args.env
tenant = args.tenant


host = "127.0.0.1"
port = "6432"
database = "app"
schema = "stark"
user = "postgres"
password = "postgres"

dc_directory = "OPS-6378"
failure_text = "Total Failure"

job_iteration_limit = 15
query_iteration_limit = 5


if (not env or not tenant):
	logging.error("Env and Tenant cannot be empty")
	exit(1)

## Extract version(last 2 digits) from TMF Environment(qa28)
try:
	version = re.search(r"\d{2}$", env).group()
except:
	logging.error(f"Invalid Enviroment: {env}")
	exit(1)

logging.info(f"Executing on {env} with version {version} for Tenant {tenant}")


install_dir = f"/etc/ops/tmf/{version}/etmf_installer/"
dc_files_directory = f"{dc_directory}/input_files"
dc_logs_directory = f"{dc_directory}/logs"
files_processed_dir = f"{dc_directory}/processed_files"
files_failed_dir = f"{dc_directory}/failed_files"

## Counter variables. Do not change
query_count = -1
iteration = 1
query_iter = 1


if not os.path.isdir(dc_files_directory):
	logging.error(f"ERROR: Input files directory '{dc_files_directory}' does not exist")
	exit(1)

#if not os.path.isdir(install_dir):
#	logging.error(f"ERROR: Install directory '{install_dir}' does not exist")
#	exit(1)

#os.system(f"cd {install_dir}")
os.system(f"mkdir -p {dc_logs_directory}")
os.system(f"mkdir -p {files_processed_dir}")
os.system(f"mkdir -p {files_failed_dir}")

def is_failure(command_output, log_file):
	try:
		if (command_output.returncode != 0):
			return True
		else:
			log_with_failures = subprocess.check_output(f"tail -1000 {log_file} | grep -i \"{failure_text}\" | tail -1", shell=True, text=True);
			if(re.search(failure_text, log_with_failures, re.IGNORECASE)):
				failure_count = int(re.findall(r'\d+', log_with_failures)[-1])
				logging.info(f"Failure Count: {failure_count}")
				return failure_count > 0
			else:
				logging.error(f"No failure text '{failure_text}' found in the log file")
				return True
	except Exception as e:
		logging.error(f"Error determining Failure for log file {log_file}: {str(e)}")
		return True


def run_rendition_query():
	conn = None
	global query_count
	global query_iter
	try:
		conn = psycopg2.connect(database=database, user = user, password = password, host = host, port = port, options=f'-c search_path={schema}')
		cur = conn.cursor()
		cur.execute("SELECT COUNT(*)  from test")
		rows = cur.fetchone()
		query_count = rows[0]
		logging.info(f"{query_iter}/{query_iteration_limit}: Rendition Query Count: {query_count}")
		query_iter += 1
		return query_count
	except (Exception, psycopg2.DatabaseError) as error:
		raise error
	finally:
		if conn is not None:
			conn.close()


def run_dc1(run_id):
	log_file_name = f"{dc_logs_directory}/dc-1_{run_id}"
	with open(log_file_name, "wb") as log_file:
		#command = f"WSPT_TMF_CONFIG_ROOT=/etc/ops/tmf/config WSPT_TMF_ENV={env} ./runtmf com.wingspan.tmf.DataCorrectionCompleteSpecificActionItemTasks -f tmf -t {tenant} -user uid=sysadmin14 -dataFile {dc_file} --forceDisconnectedCache"
		command = f"./scp.sh dc-1_{run_id}"
		## Subprocess ensures that the next run is executed only after current run is completed.
		## If a run executes for more than 24 hrs, the next schedule will wait till this process is complete
		execute_command = subprocess.run([command], shell=True, stdout=log_file, stderr=log_file)
		if is_failure(execute_command, log_file_name):
			logging.error(f"Processing of dc-1_{run_id} failed")
			return False
			#os.system(f"mv -f {dc_files_directory}/{dc_file} {files_failed_dir}")
		else:
			#os.system(f"mv -f {dc_files_directory}/{dc_file} {files_processed_dir}")
			logging.info(f"Processing of dc-1_{run_id} completed")
			return True


def check_rendition():
	global query_count
	global query_iter
	try:
		rendition_query_scheduler = schedule.Scheduler()
		rendition_query_scheduler.every(5).seconds.do(run_rendition_query)
		while (query_count != 0 and query_iter <= query_iteration_limit):
			rendition_query_scheduler.run_pending()
			time.sleep(1)
		return True
	except Exception as e:
		logging.error(f"Unable to run rendition query: \n {e}")
		return False


def run_dc2(run_id):
	global iteration
	log_file_name = f"{dc_logs_directory}/dc-2_{run_id}"
	with open(log_file_name, "wb") as log_file:
		#command = f"WSPT_TMF_CONFIG_ROOT=/etc/ops/tmf/config WSPT_TMF_ENV={env} ./runtmf com.wingspan.tmf.DataCorrectionCompleteSpecificActionItemTasks -f tmf -t {tenant} -user uid=sysadmin14 -dataFile {dc_file} --forceDisconnectedCache"
		command = f"./scp.sh dc-2_{run_id}"
		## Subprocess ensures that the next run is executed only after current run is completed.
		## If a run executes for more than 24 hrs, the next schedule will wait till this process is complete
		execute_command = subprocess.run([command], shell=True, stdout=log_file, stderr=log_file)
		if is_failure(execute_command, log_file_name):
			logging.error(f"Processing of dc-2_{run_id} failed")
			return False
			#os.system(f"mv -f {dc_files_directory}/{dc_file} {files_failed_dir}")
		else:
			#os.system(f"mv -f {dc_files_directory}/{dc_file} {files_processed_dir}")
			logging.info(f"Processing of dc-2_{run_id} completed")
			iteration += 1
			return True


def job():
	global query_count
	global query_iter
	logging.info(f"Iteration: {iteration}")
	now = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
	run_id = f"EXE_{now}"
	logging.info(f"Running Job {run_id}...")
	if run_dc1(run_id) and check_rendition():
		run_dc2(run_id)
	else:
		logging.error(f"{run_id} for DC-1 failed or Unable to check rendition query")
	logging.info(f"Job Completed {run_id}...")
	query_count = -1
	query_iter = 1



# Every Week Day at 2 AM UTC (10 PM EST)
job_scheduler = schedule.Scheduler()
job_scheduler.every(5).seconds.do(job)

while iteration < job_iteration_limit:
	job_scheduler.run_pending()
	time.sleep(1)