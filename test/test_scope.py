class MyClass:
    def my_method(self, the_var):
        # the_var = [1,2, 3]   # this line makes a lot of difference
        print("inside: ", the_var)
        the_var[0] = 3
        print("inside: ", the_var)


def test_myclass():
    the_var = [5, 6]
    print(the_var)
    myobj = MyClass()
    myobj.my_method(the_var)
    print(the_var)

# Use a function attribute
def generateNextNumber(startNumber):
    def tempFunction():
        tempFunction.current += 1
        return tempFunction.current
    tempFunction.current= startNumber
    return tempFunction

# Force the name to be assumed non-local
def generateNextNumber2(startNumber):
    """
    This was already explained in the previous section. By using the member access operator .
    we are saying "current already exists", and thus it's searched in the enclosing scope.
    In this particular case, we are creating a class using the type function and immediately creating an instance
    of it (with the second set of parantheses).
    Instead of a general object, we could have also used a list or a dictionary.
    The second case was a very common solution.
    """
    current = type("MyType", (), {'value': startNumber})()
    print(current, type(current))
    #current.value= startNumber
    def tempFunction():
        current.value += 1
        return current.value
    return tempFunction

# Use a function object
def generateNextNumber3(startNumber):
    class TempFunction:
        def __call__(self):
            self.current += 1
            return self.current
    tempFunction= TempFunction()
    tempFunction.current= startNumber
    return tempFunction


# Use a nonlocal declaration
# In the same way that global means...
# well, global, nonlocal means "in the immediately preceding scope". Valid in Python 3 and maybe later versions of Python 2.
def generateNextNumber4(startNumber):
    current= startNumber
    def tempFunction():
        nonlocal current
        current += 1
        return current
    return tempFunction

# Use generators
def generateNextNumber5(current, stop=10):
    while current < stop:
        current += 1
        yield current



if __name__ == '__main__':
    # test_myclass()
    cnt_func = generateNextNumber2(1)
    for i in range(10):
        print(cnt_func())    # expecting 2, 3, ...11

    cnt_gen = generateNextNumber5(1)
    try:
        for i in range(10):
            print(next(cnt_gen))
            # print(cnt_gen.next())  # does not work
    #except FileExistsError as e:
    except StopIteration as e:
        print("catched exception of generator: ", repr(e))
    else:   # this line won't catch any exceptions..... if above doe not catch any exceptions
        print("other situations: ")
    # for i in cnt_gen:
    #     print(i)




"""

https://stackoverflow.com/questions/18502095/python-closure-vs-javascript-closure



Python assumes that all variables in a function are local. This is to avoid accidental use of a global variable of the same name, or in an enclosing scope. In some important way, this difference is consequence of the fact that in Python local variable declaration is automatic/implicit while in JavaScript it is not (you have to use var). Solutions:

Use a global declaration
def generateNextNumber(startNumber):
    global current
    current= startNumber
    def tempFunction():
        global current
        current += 1
        return current
    return tempFunction
Valid in some cases, but in yours only one instance of tempFunction could be active at the same time.

Use a function attribute
def generateNextNumber(startNumber):
    def tempFunction():
        tempFunction.current += 1
        return tempFunction.current
    tempFunction.current= startNumber
    return tempFunction
Uses the fact that functions are objects (and thus can have attributes), that they are instantiated when they are declared, and that they become local to the enclosing function (or module, in which case they are really global). This also works because the name tempFunction is used for the first time inside its own definition with a "member access" . operator and thus not assumed local. Something similar happens with the "call" (), and "element access" [] operators. The later case explains why your code works.

Force the name to be assumed non-local
def generateNextNumber(startNumber):
    current= type("OnTheFly",(),{})()
    current.value= startNumber
    def tempFunction():
        current.value += 1
        return current.value
    return tempFunction
This was already explained in the previous section. By using the member access operator . we are saying "current already exists", and thus it's searched in the enclosing scope. In this particular case, we are creating a class using the type function and immediately creating an instance of it (with the second set of parantheses). Instead of a general object, we could have also used a list or a dictionary. The second case was a very common solution.

Use a function object
def generateNextNumber(startNumber):
    class TempFunction:
        def __call__(self):
            self.current += 1
            return self.current
    tempFunction= TempFunction()
    tempFunction.current= startNumber
    return tempFunction
Any object whose class has a call method is a function and thus can be called with the function call operator (). This is extremely related to the two previous cases.

Use a nonlocal declaration
def generateNextNumber(startNumber):
    current= startNumber
    def tempFunction():
        nonlocal current
        current += 1
        return current
    return tempFunction
In the same way that global means... well, global, nonlocal means "in the immediately preceding scope". Valid in Python 3 and maybe later versions of Python 2.

Use generators
def generateNextNumber(current):
    while True :
        current+= 1
        yield current
This is probably the most "Pythonic" way to approach not the general problem of nonlocal variable access, but the specific case you used to explain it. I couldn't finish without mentioning it. You need to call it with a minor change, though:

getNextNumber = generateNextNumber(10)
for i in range(10):
    print (getNextNumber.next())
When driving a for the call to next() is implicit (but the generator can not be infinite as in my example).

"""
