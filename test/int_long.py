#coding=utf-8
import sys
print("sys.maxsize: ", sys.maxsize)
print("type: ", type(sys.maxsize))
print("+1: ", sys.maxsize+1)
print("type after +1: ", type(sys.maxsize+1))
print("float(\"inf\"): ", float("inf"))
print(float("inf") > sys.maxsize)

"""
http://www.geeksforgeeks.org/what-is-maximum-possible-value-of-an-integer-in-python/

What is the maximum possible value of an integer in Python ?
Consider below Python program.

# A Python program to demonstrate that we can store
# large numbers in Python
 
x = 10000000000000000000000000000000000000000000;
x = x + 1
print (x)
Run on IDE
Output :

10000000000000000000000000000000000000000001
In Python, value of an integer is not restricted by the number of bits and can expand to the limit of the available 
memory (Sources : this and this). Thus we never need any special arrangement for storing large numbers (Imagine doing 
above arithmetic in C/C++).

As a side note, in Python 3, there is only one type “int” for all type of integers. In Python 2.7. there are two 
separate types “int” (which is 32 bit) and “long int” that is same as “int” of Python 3.x, i.e., can store arbitrarily 
large numbers.

# A Python program to show that there are two types in
# Python 2.7 : int and long int
# And in Python 3 there is only one type : int
 
x = 10
print(type(x))
 
x = 10000000000000000000000000000000000000000000
print(type(x))
Run on IDE
Output in Python 2.7 :

<type 'int'>
<type 'long'>
Output in Python 3 :

<type 'int'>
<type 'int'>
We may want to try more interesting programs like below :

# Printing 100 raise to power 100
print(100**100)


"""




"""

https://stackoverflow.com/questions/9860588/maximum-value-for-long-integer

maxint and maxsize:

The maximum value of an int can be found in Python 2.x with sys.maxint. It was removed in Python 3, but sys.maxsize can
 often be used instead. From the changelog:

The sys.maxint constant was removed, since there is no longer a limit to the value of integers. However, sys.maxsize can
 be used as an integer larger than any practical list or string index. It conforms to the implementation’s “natural” 
 integer size and is typically the same as sys.maxint in previous releases on the same platform (assuming the same build
  options).
  
  
and, for anyone interested in the difference (Python 2.x):

sys.maxint The largest positive integer supported by Python’s regular integer type. This is at least 2**31-1. The 
largest negative integer is -maxint-1 — the asymmetry results from the use of 2’s complement binary arithmetic.

sys.maxsize The largest positive integer supported by the platform’s Py_ssize_t type, and thus the maximum size lists, 
strings, dicts, and many other containers can have.
and for completeness, here's the Python 3 version:

sys.maxsize An integer giving the maximum value a variable of type Py_ssize_t can take. It’s usually 2^31 - 1 on a 
32-bit platform and 2^63 - 1 on a 64-bit platform.  


floats:

There's float("inf") and float("-inf"). These can be compared to other numeric types:

>>> import sys
>>> float("inf") > sys.maxsize
True

"""