#coding=utf-8
# https://laike9m.com/blog/pythonxiang-dui-dao-ru-ji-zhi-xiang-jie,60/


# https://docs.python.org/3/tutorial/modules.html
# http://codingpy.com/article/python-import-101/
# https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time#answer-14132912

# when "python -m myfile.py" is wrong, with -m should not add .py, ==> "python -m myfile"
"""
When use python -m xxx, xxx.py is loaded as a module (with a __package__ of prefix with ., non-NONE, and similar to be loaded with import), 
then run as the top-level script.
the xxx.py directory will NOT be added as first [0] of sys.path.

有两种方式加载一个 py 文件：作为 top-level 脚本或者作为 module。前者指的是直接运行脚本，比如 python myfile.py。
如果执行 python -m myfile，或者在其它 py 文件中用 import 语句来加载，那么它就会被当作一个 module。有且只能有一个 top-level 脚本，
就是最开始执行的那个（比如 python myfile.py 中的 myfile.py，译者注）。

当一个 py 文件被加载之后，它会被赋予一个名字，保存在 __name__ 属性中。如果是 top-level 脚本，那么名字就是 __main__。如果是作为 module，
名字就是把它所在的 packages/subpackages 和文件名用 . 连接起来。

====> import 是否成功，取决于：
1）where to type 'python abcxyz'
2) how to run 'abcxyz' ,  (-m, -c, etc)
"""

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
__package__:  test
 ['', '/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6/lib/python36.zip', '/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6/lib/python3.6', '/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynload', '/usr/local/lib/python3.6/site-packages']
argv[0]:  /Users/linglin/PycharmProjects/testhello/test/test_name.py

================

LingLins-MacBook-Pro:testhello linglin$ python3 test/test_name.py 3
this is fib2 in test_name.
name:  __main__
__package__:  None
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

=======================

LingLins-MacBook-Pro:test linglin$ python3 -m test_name.py 3
/usr/local/opt/python3/bin/python3.6: Error while finding module specification for 'test_name.py' (AttributeError: module 'test_name' has no attribute '__path__')

LingLins-MacBook-Pro:test linglin$ python3 -m .test_name.py 3
/usr/local/opt/python3/bin/python3.6: Relative module names not supported

LingLins-MacBook-Pro:test linglin$ python3 -m test_name 3
this is fib2 in test_name.
name:  __main__
__package__:  
 ['', '/usr/local/Cellar/python3/3.6.4_2/Frameworks/Python.framework/Versions/3.6/lib/python36.zip', '/usr/local/Cellar/python3/3.6.4_2/Frameworks/Python.framework/Versions/3.6/lib/python3.6', '/usr/local/Cellar/python3/3.6.4_2/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynload', '/usr/local/lib/python3.6/site-packages']
argv[0]:  /Users/linglin/PycharmProjects/testhello/test/test_name.py

=======================

LingLins-MacBook-Pro:testhello linglin$ cd ..
LingLins-MacBook-Pro:PycharmProjects linglin$ python3 testhello//test/test_name.py 3
this is fib2 in test_name.
name:  __main__
__package__:  None
/Users/linglin/PycharmProjects/testhello/test ['/Users/linglin/PycharmProjects/testhello/test', '/usr/local/Cellar/python3/3.6.4_2/Frameworks/Python.framework/Versions/3.6/lib/python36.zip', '/usr/local/Cellar/python3/3.6.4_2/Frameworks/Python.framework/Versions/3.6/lib/python3.6', '/usr/local/Cellar/python3/3.6.4_2/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynload', '/usr/local/lib/python3.6/site-packages']
argv[0]:  testhello//test/test_name.py
LingLins-MacBook-Pro:PycharmProjects linglin$ 


LingLins-MacBook-Pro:PycharmProjects linglin$ python3 -m testhello.test.test_name 3
this is fib2 in test_name.
name:  __main__
__package__:  testhello.test
 ['', '/usr/local/Cellar/python3/3.6.4_2/Frameworks/Python.framework/Versions/3.6/lib/python36.zip', '/usr/local/Cellar/python3/3.6.4_2/Frameworks/Python.framework/Versions/3.6/lib/python3.6', '/usr/local/Cellar/python3/3.6.4_2/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynload', '/usr/local/lib/python3.6/site-packages']
argv[0]:  /Users/linglin/PycharmProjects/testhello/test/test_name.py


LingLins-MacBook-Pro:PycharmProjects linglin$ cd ..
LingLins-MacBook-Pro:~ linglin$ python3 -m PycharmProjects.testhello.test.test_name 3
this is fib2 in test_name.
name:  __main__
__package__:  PycharmProjects.testhello.test
 ['', '/usr/local/Cellar/python3/3.6.4_2/Frameworks/Python.framework/Versions/3.6/lib/python36.zip', '/usr/local/Cellar/python3/3.6.4_2/Frameworks/Python.framework/Versions/3.6/lib/python3.6', '/usr/local/Cellar/python3/3.6.4_2/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynload', '/usr/local/lib/python3.6/site-packages']
argv[0]:  /Users/linglin/PycharmProjects/testhello/test/test_name.py


"""