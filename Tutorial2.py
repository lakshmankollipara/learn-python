# # Versions and type
# import this   ## Print Python Quotes
# import platform
# from decimal import *
#
#
# def main():
#     print("Python Version is: {}".format(platform.python_version()))  ## Alternative to print + str(str.format())
#     print(f"Python Version is: {platform.python_version()}")  ## Alternative to print + str (3.6 and later)
#     print("Python Version is: %s" % platform.python_version())  ## Alternative to print (Deprectated)
#     if 10 < 20:
#         x = 5
#     print("x is : ", str(x))  ## Local variable inside loop can be accessed. If condition is not met, variable remains unassigned.
#                                 ## Blocks do not define scope. Methods do.
#     y = 5
#     print(type(x))      ## prints type <class Int>
#     print(type(x).__name__)  ## prints type name: int
#     n = None   ## None is same as void. If no return for a function return None
#     print(type(n))
#     mystr = "Lakshman"  ## Strings are objects
#     print(mystr.capitalize())  ## Can call member functions of String class
#     print("Numbers are {} and  {}".format(10, 20))
#     print("Numbers are {1} and  {0}".format(10, 20))  ##Can change order of formats, 0 being first index
#     mydiv = 7/3  ##gives 2 in python 2.7, gives 2.333in python 3.6
#     print(mydiv)
#     myarth = 0.1 + 0.1 + 0.1 - 0.3  ## Doesn't return 0. Need to import decimal module
#     print(myarth)
#     a = Decimal("0.1")  ## Should give decimal in quotes
#     b = Decimal("0.3")
#     myarth1 = a + a + a - b
#     print(myarth1)
#     myV = ''
#     if myV:  ## 0, None, False, empty string evaluates to false
#         print("True")
#     else:
#         print("False")
#
#
# if __name__ == "__main__":
#     main()
#
#
# # Collections
#
# def main():
#     x = [1, 2, 3, 4, 5]  ## Lists, List is mutable sequence, can re-assign values to index
#     ## List Methods: Access: x[1], x[1:5], x[1:5:2]- start, end, step; x.index(4) - Get index of search string;x.append(); x.remove();, x.insert(0, 2) - Insert at index 0; x.pop(4) - remove from end of the list/or specific position; del x[i]; del x[i:j]; ', '.join(x) - Prints list elements seperated by comma; len(x);
#     x[3] = -1
#     print(type(x))
#     y = [i * 2 for i in x if i % 2 == 0]  ## List comprehension. Creating a list from another list
#     print(y)
#     for i, val in enumerate(x):  ##enumerate to get index position
#         print(f"Value at index {i} is {val}")
#     x = {1, 2, 3, 4, 5}   ## Sets, Unique value, unordered, un-indexed. Cannot change existing value, but add new values.
#     print(type(x))
#     x = (1, 2, 3, 4, 5)  ## Tuple, Tuples are immutable
#     print(type(x))
#     for val in x:  ##enumerate to get index position
#         print(f"Value is {val}")
#     x = range(5)  ## Range, Immutable sequence
#     x = range(0,50,10)  ## range with step
#     print(type(x))
#     for val in x:
#         print(val)
#     x = list(range(10))  ## Converts Range to a mutable list
#     print(type(x))
#     x = {'one': 1, 'two': 2, 'three': 3}   ##Dictonary, Mutable,  like a hashmap (key-value). Can also created by dict(a = 1)
#     x['three'] = 42  ##Mutable, reassign a key
#     print(type(x))
#     for i in x:
#         print(f"Key is {i}")   ## prints just Keys
#     for k,v in x.items():    ##x.keys - to get list of keys, x.values - to get list of values
#         print(f"Value of key {k} is {v}")
#     print(x.get('one'))   ## get value of Key, returns None if key does not exist. Can use x['one']
#     print(x.get('four', -1))  ## get value if exists. if not get -1
#     x = (1, 'two', 3.0, [4, 'four'], 5)  ## Tuple can have different data types.
#     print(type(x))
#     print(type(x[2]))    ## Type of elements
#     x = [1, 'a', 5.6]  ## Tuple can have different data types.
#     print(type(x))
#     print(type(x[2]))  ## Type of elements
#     x = [1, 'a', 5.6]
#     y = [1, 'a', 5.6]
#     print(id(x))    ## IDs are different and types are same
#     print(id(y))
#     print(id(x[2]))     ##IDs of list/tuple elements is same because these are objects. There is only one object constant (1 or 5.6, 'a') therefore same id
#     print(id(y[2]))
#     if x[2] is y[2]:        ## is compares the ID i.e object to object address
#         print("They are same Objects")
#     else:
#         print("Not same")
#     if x is y:        ## x and y are two different list objects
#         print("They are same Objects")
#     else:
#         print("Not Same")
#     if isinstance(x, tuple):    ## isinstance to test the type of the variable
#         print("x is Tuple")
#     elif isinstance(x, list):
#         print("x is List")
#     else:
#         print("x is " + str(type(x)))
#
#
# if __name__ == "__main__":
#     main()
#
# # Operators
#
# def count_digits(x):       ## count number of digits in given number between 0 to 99999
#     d=1                     ## CHecks all if conditions, hence increments d
#     if (x >= 10): d=d+1
#     if (x >= 100): d=d+1
#     if (x >= 1000): d=d+1
#     if (x >= 10000): d=d+1
#     return d
#
# def main():
#     ## Conditional Operators: ==, !=, < ,>, <=, >=
#     ## Logical Operators: and,or,not
#     ## Identity Operator (To check if same object): is, is not
#     ## Membership Operator(member of a collection): in, not in
#     ## Arithematic Operators: +, -, *, / (Float divison), // (Integer divison), %, ** (Exponent)
#     ## Bit-Wise Operators: &, |, ^ (XOR), <<, >>
#     ## Operator Precedence: **, *, /, //, %, +, -
#     hungry = True
#     x = "Eat" if hungry else "Do not eat"      ## Terenary operator(only in 3.6): sets x to eat if true
#     print(x)
#     print(count_digits(99999))
#
#
# if __name__ == "__main__":
#     main()
#
# # Generators - yield
#
#
# def main():
#     try:
#         for i in my_range(10, 20, 0):
#             print(i)
#     except ValueError as err:
#         print(f"Value Error: {err}")
#     for i in my_range(10, 20, 2):
#         print(i)
#
#
# def my_range(start = 0, end = 10, step = 1):
#     if step == 0:
#         raise ValueError("Step Cannot be 0")
#     i = start
#     while i <= end:
#         yield i   ##Returns i but doesn't end loop. executes till last statement of loop
#         i += step
#
#
# if __name__ == "__main__":
#     main()
#
#
# #Decorators
#
#
# def main():
#     f1()
#     x = f1()  ## A function can be assigned another variable and called as a function
#     x()     ## prints f2 because f1 is returning f2. Cannot call f2 directly
#     f4(f3())  ## A function can be passed as an argument to function
#     f3()  ##Can be called, but, f3 cannot be called directly. It is used to pass to f4. Used to calculate running time. Pass a function to calculator and calculate time and return calcluated time
#
#
# def f1():
#     print("This is F1")
#
#     def f2():
#         print("This is F2")
#     return f2
#
#
# def f4(f):
#     print("This is F4")
#
#     def f2():
#         print("Before calling F")
#         f()
#         print("After calling F")
#     return f2
#
#
# @f4   ##Decorator: Decorators disable calling this function alone. if f3 is called independtly, it in-turn calls f4. Alternate way: f3 = f4(f3)
# def f3():
#     print("This is F3")
#
#
# f3 = f4(f3)  ## ALternate way of Decorator. calling f3 calls f4
#
# if __name__ == "__main__":
#     main()
#


## Classes


# class Duck:
#     name = "Donald"
#     sound = "QUACK..."                  ## Class variables/members
#     movement = "Walks like a Duck"
#
#     def quack(self):     ## Class methods. By default have self as parameter (self is same as "this" in java)
#         print(self.sound)
#
#     def move(self):
#         print(self.movement)
#
#
# class Animal:
#     rank = -1  ## Member variable. Can be accessed. Class Variable. Linked to a class.
#
#     def __init__(self, type, name, sound):  ## Constructor to create class members. Can give default values, Can use **kwargs such that we don't need to remember order
#         self._type = type                   ## If members are not there. Called as Object Variables (Python does not have private variables. Prefixed with '_' means dont access it outside.). (class variables if outside constructors), we can assign self._name
#         self._name = name
#         self._sound = sound
#
#     def type(self):                 ## Accessors: Getters & Setters
#         return self._type
#
#     def type(self, t = None):       ## Both Getter & Setter in same method.
#         if t:
#             self._type = t
#         return self._type
#
#     def name(self):
#         return self._name
#
#     def sound(self):
#         return self._sound
#
#     def get_rank(self):
#         return self.rank
#
#     def print(self):
#         return f"{self.name()} is a {self.type()} and says {self.sound()}"
#
#     def __str__(self):          ## Same as toString. Default inbuilt functions are usually with __name__
#         return f"{self.name()} is a {self.type()} and says {self.sound()}"
#
#
# def main():
#     d = Duck()        ## Object creation
#     print("Duck Name is " + d.name)
#     d.quack()
#     d.move()
#     tom = Animal('cat', 'Thomas', 'Meoww')
#     jer = Animal('mouse', 'Jerry', 'keech')
#     print(f"tom is a {tom.type()}")
#     print(f"jerry says {jer.sound()}")
#     tom.print()
#     tom.type("Kitten")          ## Setter & Getter
#     tom.print()
#     print(tom)  ## __str__ is used.
#     tom._type = "abc"  ## Must not be done. Changes for the object. Not for the class.
#     tom.rank = 12
#     print(f"Tom's rank is {tom.get_rank()}")
#
#
#
# if __name__ == "__main__":
#     main()


## Inheritence


# class Animal:
#     def __init__(self, **kwargs):
#         if 'type' in kwargs: self._type = kwargs['type']
#         if 'name' in kwargs: self._name = kwargs['name']
#         if 'sound' in kwargs: self._sound = kwargs['sound']
#
#     def type(self, t = None):
#         if t:
#             self._type = t
#         try: return self._type
#         except AttributeError: return None
#
#     def name(self, n = None):
#         if n:
#             self._name = n
#         try:
#             return self._name
#         except AttributeError:
#             return None
#
#     def sound(self, s = None):
#         if s:
#             self._sound = s
#         try:
#             return self._sound
#         except AttributeError:
#             return None
#
#     def __str__(self):
#         return f"{self.name()} is a {self.type()} and says {self.sound()}"
#
#
# class Cat(Animal):         ## Duck Inherits properties of Animal. Multiple Inheritence: Comma separated list of classes
#     def __init__(self, **kwargs):
#         self._type = 'Cat'
#         if 'type' in kwargs: del kwargs['type']    ##Cat class is for type of cats. Hence, We set type to Cat and ignore/delete any type user passes while object Creation. ex Cat(type = 'Dog') is not valid. Hence deleting type
#         super().__init__(**kwargs)
#
#     def prey(self, s):      ## THis function is only member of Cat. Not animal.
#         print(f"{self.name()} preyed upon {s}")
#
#
# class RevStr(str):      ## Class name is small because str is a built-in String class
#     def __str__(self):      ## We are overriding .toString method to print in reverse order
#         return self[::-1]  ## String reverse. THere is no reverse in python. Use slice operation from start to end with a step of -1. i.e from backword
#
#
# def main():
#     tom = Cat(name = 'Tom', sound = 'Meow')
#     print(tom)
#     tom.prey("Jerry")
#     rev_str = RevStr("Lakshman")
#     print(rev_str)
#
#
# if __name__ == "__main__":
#     main()


## Exceptions

# import sys  ## gives more information about execution system
# import traceback  ##to print stack trace of exception
#
# def main():
#     #x = int("Hello")  ## ERROR: Value Error
#     try:
#         x = int("Hello")
#         x = 5/0
#     except ValueError as e:     ## Specific Error handling.
#         print(f"Value Error in converting to Int: {str(e)}")  ##e.message is not always available
#     except Exception as e:      ## Common generic Exception. Default Exception
#         print(f"Unknown Error in converting to Int: {str(e)}")
#         print(f"Exec Info: {str(sys.exc_info()[1])}")
#     else:       ## Executes only if no errors
#         print(x)
#
#     try:
#         divide(10, 0)
#     except Exception as e:
#         print("Error: " + str(e))
#
#     try:
#         raise_exception()
#     except Exception as e:
#         #traceback.print_exc()  ## To print stack trace
#         print("Error: " + str(e))
#
#
# def divide(a, b):
#     if b == 0:
#         raise ZeroDivisionError("Cannot Divide by Zero")    ## Raising Exceptions
#     return a/b
#
#
# def raise_exception():
#     raise MyException("This is MY custom Exception")
#
#
# class MyException(Exception):   ## Creating a Custom exception
#     def __init__(self, message):
#         super().__init__(message)
#
#
# if __name__ == "__main__":
#     main()


## String functions

# def main():
#     x = "Hello"
#     print("String: " + x)
#     print("Upper: " + x.upper())
#     print("Swap Case: " + x.swapcase())
#     print("Lower: " + x.lower())
#     print("Capitalize: " + x.capitalize())
#     print("Title Case: " + x.title())  ## First letter of every word seperated by space
#     print("Case Fold: " + x.casefold()) ## Removes all case distinctions (Always lower in all languages)
#     print("Concat: " + x + " World!")
#     print("Format: {}".format(42 * 7))  ## Replaces {} with whatever in format
#     print("{:,}".format(100000000))
#     print("{:.4f}".format(33.025698))
#     print("{:b}".format(10)) ## Binary
#     print("{:x}".format(10)) ##Hexa
#     print("{:o}".format(8))  ##Octa
#     print(f"{1000000000:,}")
#     print("""THis is a Multi
#     line
#     String which is "Enclosed in Double quotes".""")
#     hello = MyStr("hello")
#     print(hello)
#     x = "This is a long string"
#     print(x.split())  ##Default: Split by Space
#     print(x.split('a'))
#     str_list = x.split()
#     joined_str = '_'.join(str_list)  ## Alt to list.mkString()
#     print(joined_str)
#
#
# class MyStr(str):       ## Custom String class. Can override String methods
#     def __str__(self):
#         return self.capitalize()
#
#
# if __name__ == "__main__":
#     main()


##  Standard Library (Modules)

# import os
# import sys
# import random
# from my_module import MyClass
#
#
# def main():
#     print(sys.platform)
#     print(os.name)
#     print(os.getcwd())
#     print(os.get_exec_path())
#     print(random.randint(1, 10))
#     m = MyClass("Message", 10)  ## Custom Module which  prints message n times
#     m.n_times()     ## Prints  given message n times
#
#
# if __name__ == "__main__":
#     main()


## Database APIs

import sqlite3  ##Default SQL Module


def main():
    db = sqlite3.connect('db-api.db')
    cur = db.cursor()
    cur.execute("DROP TABLE IF EXISTS test;")
    cur.execute("CREATE TABLE IF NOT EXISTS test(id INT PRIMARY KEY, name varchar);")
    cur.execute("INSERT INTO test(id, name) VALUES ('123', 'Lakshman'), ('234', 'Keerthana');")
    cur.fetchone()
    for row in cur.execute("SELECT * FROM test;"):
        print(row)


if __name__ == "__main__":
    main()
