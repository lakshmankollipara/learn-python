# Print Hello Wolrd.


##__name__ gives the name of the current module. It tells the interpreter to execute main function when interpreting this file. __main__ keyword tells this is the main module
## THis ensures that all the defined functions are intrepreted and then the main func is executed. Python doesn't support forward declaration
print(__name__)

def main():
    print("Hello World")


if __name__ == "__main__":
    main()

# Variables


x = 1
print(x)
a = "abc"
print(a)

##print("this is string " + 123)  # ERROR: Concatinating string and Int. No implicit type conversion
print("this is string " + str(123))  # str() converts int to string


def foo():
    a = "def"
    print(a)


foo()  # prints local variable inside function (def)
print(a)  # prints global variable (abc)


def bar():
    global a
    a = "def"
    print(a)


bar()
print(a)  # global <v_name> lets you access global variable name inside a function

del a  ## deleting/Unassigning a variable
##print(a)  ## throws error because variable no longer exists after delete


# Functions


def func():
    print ("Hello")  ## ":" defines scope of function and Indentation for function body


func()  ## Calling a function prints Hello
print (func())  ## prints Hello and outer print prints None (because func is not returning any value, so None)
print (func)  ## Function is not executed. func def is printed like an object


def func1(arg1, arg2):  ## Function with arguments
    print (arg1, " ", arg2)


func1("abc", "def")  ## applies function on String arguments
func1(3,4)  ## applies function on Int arguments


def square(arg1):
    return arg1 * arg1


print (square(5))  ## Function returning a value can be printed with print
##square("abc")  ## ERROR: Function * can't be applied to Strings


def cube(arg1=3):
    return arg1 * arg1 * arg1


print (cube())  ## default argument is given. returns 3^3
print (cube(5))  ## over rides default value with 5


def increment(num, inc=1):
    return num + inc


print (increment(3))
print (increment(3, 2))
print (increment(inc=2, num=3))  ## We can give arguments in any order by mentioning their names


def sum_all(*args):  ## *args represents we can any number of arguments as a list
    result = 0
    for i in args:
        result = result + i
    return result

def print_map(**kwargs):  ## **kwargs represents key-worded multi arguments list like a dictonary
    for k in kwargs:
        print(f"Value at Key {k} is {kwargs[k]}")

## Mutable values are call by reference Value changed (same id). Immutable values are call by value. Value changes (new id)

print (sum_all())  ## prints 0 (result)
print (sum_all(1))
print (sum_all(1, 2, 3, 4))
abc = (2,3,4)
print(sum_all(*abc))  ## Variable can be passed to multi args functions with a * prefix
print_map(one = 1, two = 2, three = 3)
## print_map({'a': 1, 'b': 2, 'c': 3})  ## THis is Wrong. This is one value of Hashmap/Dict. Not a multi argument
abc = dict(one = 1, two = 2, three = 3) #3 Another way of creating a dict
abc = {'a': 1, 'b': 2, 'c': 3}  ## DIctionary
print_map(**abc)  ## Variable can be passed to multi args key-worded args with a * prefix

def inc_by_x(x=1, *args):
    return [i + x for i in args]  ##  Increments each element of args by x


print (inc_by_x(2, 3, 4, 5, 6))  # We can have fixed args and variable args combined but, variable args should always be last


##IF- Statements


def main():
    x, y = 100, 100
    if x < y:       # No Switch-Case in Python
        st = "X is less than Y"
    elif x < y:
        st = "X is greater than Y"
    else:
        st = "X is equal to Y"
    print (st)
    st = "X is less than Y" if x < y else "X is greater than or equal to Y"
    # If just 2 conditions need to be checked, a simple syntactic sugar
    print (st)

if __name__ == "__main__":
    main()


# Loops

def main():
    x = 6
    while x < 5:  # No Do-while. Python has only for and while
        print(x)
        x = x + 1
    else:     ## Else can be used with WHile loop. Executes else condition if while condition is false
        print("x is not less than 5")
    for i in range(1, 10, 2):  # iterate through 1 until 10(exclusive) by 2
        print(i)

    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for d in days:
        if d == "Fri":
            break       ## Breaks the loop when Fri is encountered
        print (d)
    for d in days:
        if d == "Fri":
            continue  ## Skip the execution if its friday and continue further execution
        print (d)
    for i, d in enumerate(days):  # Enumerates each list element with an index
        print ("Element at " + str(i) + " is " + d)

if __name__ == "__main__":
    main()


# Classes


class MyClass():
    def method1(self):      ## Always self is first argument. Same as this. passing current instance
        print ("My Class method1")

    def method2(self, str="Hello"):
        print ("My Class method2: " + str)


class AnotherClass(MyClass):  ##Inheritence. anotherClass inherits myClass
    def method1(self):
        sum
        MyClass.method1(self)   # Calling a prent class method in child class. Should pass self

    def method2(self, str="Bye"):
        print ("Another Class method2: " + str)  # Method Overriding


def main():
    c = MyClass()
    c.method1()
    c.method2()
    c.method2("Lakshman")
    c1 = AnotherClass()
    c1.method1()
    c1.method2()

if __name__ == "__main__":
    main()


#Dates

from datetime import *


def main():
    today = date.today()
    print (today)
    print(today.day, today.month, today.year)
    now = datetime.now()
    print (now)
    print(now.hour, now.minute, now.second)
    print (now.strftime("%Y-%B-%d"))
    print (now.strftime("%y-%b-%d"))
    print (now.strftime("%c"))
    print (now.strftime("%x"))
    print (now.strftime("%X"))
    print (now.strftime("%I"))  # 12-hour
    print (now.strftime("%H"))
    print (now.strftime("%M"))
    print (now.strftime("%S"))
    print (now.strftime("%p"))  # AM/PM
    print (timedelta(minutes=15))
    print (timedelta(hours=5, minutes=15))
    print (timedelta(days=365, hours=5, minutes=1))
    print (str(now), str(now + timedelta(minutes=15)))
    print (str(now), str(now - timedelta(minutes=15)))
    fools_day = date(today.year, 4, 1)
    print (fools_day) # Get Fools day date
    if fools_day > date.today():
        print("Aprils Fool day is " + str(fools_day))
    else:
        print("Aprils Fool day is " + str(fools_day.replace(year=today.year + 1)))


if __name__ == "__main__":
    main()

# Files

import os
from os import path
import datetime
import time
import shutil
from shutil import make_archive
from zipfile import ZipFile


def main():
    f = open("textfile.txt", "w+")  ## file open in write mode. creates if file not exists
    for i in range(10):
        f.write("This is line " + str(i) + "\n")  ## or print("This is line " + str(i) + "\n", file = f) - print to file
    f.close()
    f1 = open("textfile.txt", "a")  ## Append to existing file
    for i in range(10, 20):
        f1.write("This is line " + str(i) + "\n")
    f1.close()
    f2 = open("textfile.txt", "r")  ##Read file, rt- read text file, rb - read binary file
    if f2.mode == 'r':  ## TO make sure file is in read format
        contents = f2.read()
        print(contents)  ## Entire file content
    f2.close()
    f3 = open("textfile.txt", "r")  ##Read file
    if f3.mode == 'r':  ## TO make sure file is in read format
        lines = f3.readlines()
        for line in lines:
            print ("Line: " + line.rstrip())    ## Print line by line and strip white spaces
    f3.close()
    print(os.name)  ##OS Utils to work with path, files, directories.
    print(os.getcwd())  ## Get current working directory
    print("Item exists: " + str(path.exists("textfile.txt")))  ## Check if path/file exists
    print("Item is file: " + str(path.isfile("textfile.txt")))  ## Check if item is file
    print("Item is directory: " + str(path.isdir("textfile.txt")))  ## Check if item is file
    print("Full path is: " + str(path.realpath("textfile.txt")))  ## Check if item is file
    print("Split path and name is: " + str(path.split(path.realpath("textfile.txt"))))  ## Check if item is file
    m_time = time.ctime(path.getmtime("textfile.txt"))  ## Get File modification time
    print ("Modification Time is " + str(m_time))
    m_datetime = datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print ("Modification Date Time is " + str(m_datetime))

    if path.exists("textfile.txt"):
        src = path.realpath("textfile.txt")
        dest = src + ".bkp"  ## Create a backup file
        shutil.copy(src,dest)  ##Shell commands to copy the file
        shutil.copystat(src, dest)  ## Copies file statistics as well
        os.rename("textfile.txt", "newfile.txt")  ##Renaming file
        shutil.move("newfile.txt", "newfile2.txt")  ##Renaming file
        root_dir, file = path.split(path.realpath("newfile2.txt"))
        make_archive("ArchivedFiles", "zip", root_dir)  ## Zip a directory
        with ZipFile("ZippedNewFile.zip", "w") as newzip:  ## Create a new zip directory and add files. Same as newZip = ZipFile()
            newzip.write("newfile2.txt")
            newzip.write("textfile.txt.bkp")


if __name__ == "__main__":
    main()


# HTTP Requests

import urllib.request
import json

def main():
    weburl = urllib.request.urlopen("http://www.google.com")
    print("Response Code: " + str(weburl.getcode()))
    data = weburl.read()
    print(data)
    api_url = urllib.request.urlopen("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.geojson")
    if api_url.getcode() == 200:
        api_data = api_url.read()
        json_data = json.loads(api_data)
        print (json_data)  ## print entire JSON
        if "title" in json_data["metadata"]:
            print("Title is " + json_data["metadata"]["title"])  ##Extract JSON keys
        for i in json_data["features"]:  ## Loop through array of JSON objects
            print("Place is " + i["properties"]["place"])
    else:
        print("Cannot parse Response, Response Code: " + str(api_url.getcode()))


if __name__ == "__main__":
    main()

# Parsing HTML
import urllib
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered Start Tag: ", tag)
        pos = self.getpos()
        print(" At Line: ", pos[0], " and position: ", pos[1])

    def handle_endtag(self, tag):
        print("Encountered End Tag: ", tag)
        pos = self.getpos()
        print(" At Line: ", pos[0], " and position: ", pos[1])

    def handle_data(self, data):
        if data.isspace():  ## Remove lines with white spaces or empty lines
            return
        print("Encountered data: ", data)
        pos = self.getpos()
        print(" At Line: ", pos[0], " and position: ", pos[1])

def main():
    parser = MyHTMLParser()
    weburl = urllib.request.urlopen("http://www.google.com")
    if weburl.getcode() == 200:
        contents = weburl.read().decode(weburl.headers.get_content_charset())
        parser.feed(contents)
    else:
        print("Error Response Code: " + str(weburl.getcode()))


if __name__ == "__main__":
    main()
