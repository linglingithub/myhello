def add_number(num):
    def adder(number):
        'adder is a closure'
        print('num: ', num, 'number', number)
        return num + number
    return adder

a_10 = add_number(10)
print(a_10)
print(a_10(21))
print(a_10(34))

a_5 = add_number(5)
print(a_5)
print(a_5(6))
print(a_5(100))

print('=============================================')

'''
try my own closure here, quite different from Javascript closure
python closure won't allow to keep internal state, 
javascript function can keep internal var 

In python, if want to keep state, use class, function is more like pure function
In Javascript, everything is function, so very different
'''

print('=============================================')

def my_counter1():
    inner_val = 0

    def increase():
        return inner_val + 1
    return increase

def my_counter2(val):
    def increase():
        # val = val + 1  # can't do this, won't keep state of val, val on the right can't be resolved
        #val += 1   # can't do this, won't keep state of val
        return val + 3
    return increase

def my_counter(start=0):
    def increase():
        i = 0
        while True:
            yield start + i
            i += 1
    return increase

a = my_counter()
#a = my_counter(5)
for i in range(3):
    print("my_counter:", my_counter(4))     # only return a function, will see different function are created for 3 and 4
    print("a: ", a, a())                    # here the real inner function is executed.
for x in a():
    print(x)
    if x >= 10:
        break

# two different ways to use generator
b = a()
for i in range(3):
    print("using next: ", next(b))


"""

http://pymbook.readthedocs.io/en/latest/igd.html

Closures
Closures are nothing but functions that are returned by another function. We use closures to remove code duplication. 
In the following example we create a simple closure for adding numbers.


adder is a closure which adds a given number to a pre-defined one.

"""

print('=============================================')

'''
decorator is also a closure, 

but a closure can take in any parameter, that parameter is accessed by inner function,
and the inter function is returned, other parameters are passed when inner function is executed. 

a decorator itself is a function (dfunc), typically takes a function (afunc)  as a parameter, 
a inner wrapper function (wfunc) will do somthing before and after, and execute the afunc, wfunc will return the
result of executing afunc. 

dfunc will return wfunc

when 


'''

print('=============================================')

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before call")
        result = func(*args, **kwargs)
        print("After call")
        return result
    return wrapper


@my_decorator
def add(a, b):
    print("Our add function")
    return a + b

print(add(1, 3))

""""


Decorators
Decorator is way to dynamically add some new behavior to some objects. We achieve the same in Python by using closures.

In the example we will create a simple example which will print some statement before and after the execution of a function.

>>> def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before call")
        result = func(*args, **kwargs)
        print("After call")
        return result
    return wrapper
...
>>> @my_decorator
def add(a, b):
    "Our add function"
    return a + b
...
>>> add(1, 3)
Before call
After call
4

"""