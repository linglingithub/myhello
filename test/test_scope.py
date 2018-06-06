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
    current= type("OnTheFly",(),{'value': startNumber})()
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
    cnt_func = generateNextNumber4(1)
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


"""
