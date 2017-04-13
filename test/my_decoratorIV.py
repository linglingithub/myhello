#coding=utf-8
__author__ = 'linglin'


# http://python-3-patterns-idioms-test.readthedocs.io/en/latest/PythonDecorators.html


class my_decorator(object):

    def __init__(self, f):
        print("inside my_decorator.__init__()")
        f() # Prove that function definition has completed

    def __call__(self):
        print("inside my_decorator.__call__()")

@my_decorator
def aFunction():
    print("inside aFunction()")

print("Finished decorating aFunction()")

aFunction()


"""
When you run this code, you see:

inside my_decorator.__init__()
inside aFunction()
Finished decorating aFunction()
inside my_decorator.__call__()
Notice that the constructor for my_decorator is executed at the point of decoration of the function. Since we can
call f() inside __init__(), it shows that the creation of f() is complete before the decorator is called. Note also that
 the decorator constructor receives the function object being decorated. Typically, you’ll capture the function object
 in the constructor and later use it in the __call__() method (the fact that decoration and calling are two clear phases
  when using classes is why I argue that it’s easier and more powerful this way).

When aFunction() is called after it has been decorated, we get completely different behavior;
the my_decorator.__call__() method is called instead of the original code. That’s because the act of decoration replaces
 the original function object with the result of the decoration – in our case, the my_decorator object replaces
 aFunction. Indeed, before decorators were added you had to do something much less elegant to achieve the same thing:

def foo(): pass
foo = staticmethod(foo)
With the addition of the @ decoration operator, you now get the same result by saying:

@staticmethod
def foo(): pass
This is the reason why people argued against decorators, because the @ is just a little syntax sugar meaning “pass a
function object through another function and assign the result to the original function.”

The reason I think decorators will have such a big impact is because this little bit of syntax sugar changes the way you
 think about programming. Indeed, it brings the idea of “applying code to other code” (i.e.: macros) into mainstream
 thinking by formalizing it as a language construct.


"""

print "################################################################################################################"


class entry_exit(object):

    def __init__(self, f):
        self.f = f

    def __call__(self):
        print("Entering", self.f.__name__)
        self.f()
        print("Exited", self.f.__name__)

@entry_exit
def func1():
    print("inside func1()")

@entry_exit
def func2():
    print("inside func2()")

func1()
func2()

"""

The output is:

Entering func1
inside func1()
Exited func1
Entering func2
inside func2()
Exited func2
You can see that the decorated functions now have the “Entering” and “Exited” trace statements around the call.

The constructor stores the argument, which is the function object. In the call, we use the __name__ attribute of the
function to display that function’s name, then call the function itself.

"""