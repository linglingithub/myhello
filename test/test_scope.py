class MyClass:
    def my_method(self, the_var):
        # the_var = [1,2, 3]   # this line makes a lot of difference
        print("inside: ", the_var)
        the_var[0] = 3
        print("inside: ", the_var)


if __name__ == '__main__':
    the_var = [5, 6]
    print(the_var)
    myobj = MyClass()
    myobj.my_method(the_var)
    print(the_var)

