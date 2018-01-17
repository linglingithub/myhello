#coding=utf-8
# https://docs.python.org/3/tutorial/modules.html


# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    print("name: ", __name__)
    # when in python interactive mode, imoport test_name as fibo, fibo.fib(1), name is 'test_name'
    # just type fibo.__name__
    # when in terminal, python [-m] test_name.py 3, it is '__main__'
    a, b = 0, 1
    while b < n:
        #print(b, end=" ")
        print(b, " ")
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    print("this is fib2 in test_name.")
    print("name: ", __name__)
    print("__package__: ", __package__)
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

"""

LingLins-MacBook-Pro:test linglin$ python3
Python 3.6.2 (default, Jul 17 2017, 16:44:45) 
[GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.42)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import test_name
>>> fibo.fibo()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'fibo' is not defined
>>> fibo.fib(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'fibo' is not defined
>>> fib(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'fib' is not defined
>>> test_name.fib(3)
1 1 2 
>>> import test_name as fibo
>>> fibo.fib(3)
1 1 2 
>>> fibo.__name__
'test_name'
>>> fibo.fib(2)
name:  test_name
1 1 
>>> fibo.__package__
''
>>> 


"""


if __name__ == "__main__":
    import sys
    fib2(int(sys.argv[1]))
    print(sys.path[0], sys.path)
    print("argv[0]: ", sys.argv[0])

"""
6.1.1. Executing modules as scripts
When you run a Python module with

python fibo.py <arguments>
the code in the module will be executed, just as if you imported it, but with the __name__ set to "__main__". 
That means that by adding this code at the end of your module:


if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
    
you can make the file usable as a script as well as an importable module, because the code that parses the command line 
only runs if the module is executed as the “main” file:

"""



"""
LingLins-MacBook-Pro:testhello linglin$ python3 -m test.test_name 3
this is fib2 in test_name.
name:  __main__
 ['', '/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6/lib/python36.zip', '/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6/lib/python3.6', '/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynload', '/usr/local/lib/python3.6/site-packages']
argv[0]:  /Users/linglin/PycharmProjects/testhello/test/test_name.py

================

LingLins-MacBook-Pro:testhello linglin$ python3 test/test_name.py 3
this is fib2 in test_name.
name:  __main__
/Users/linglin/PycharmProjects/testhello/test ['/Users/linglin/PycharmProjects/testhello/test', '/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6/lib/python36.zip', '/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6/lib/python3.6', '/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynload', '/usr/local/lib/python3.6/site-packages']
argv[0]:  test/test_name.py

=======================

LingLins-MacBook-Pro:testhello linglin$ cd test
LingLins-MacBook-Pro:test linglin$ python3 test_name.py 3
this is fib2 in test_name.
name:  __main__
__package__:  None
/Users/linglin/PycharmProjects/testhello/test ['/Users/linglin/PycharmProjects/testhello/test', '/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6/lib/python36.zip', '/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6/lib/python3.6', '/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynload', '/usr/local/lib/python3.6/site-packages']
argv[0]:  test_name.py
LingLins-MacBook-Pro:test linglin$ 


"""