__author__ = 'linglin'

class MyClass(object):
    def __init__(self):
        self.x = 1
        self.y = "hello world"

    def printMyClass(self):
        print self.x
        print self.y

if __name__ == '__main__':
    mc = MyClass()
    mc.printMyClass()
