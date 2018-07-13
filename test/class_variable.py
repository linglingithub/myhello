# https://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide

class Bar(object):
    def __init__(self):
        self.__zap = 1  # double underscore means this is a private variable

a = Bar()
print(a.__dict__)

print(a._Bar__zap) # can access
#print a.__zap # will throw error

print("####################")

class Person(object):
    all_names = []

    def __init__(self, name):
        self.name = name
        Person.all_names.append(name)

joe = Person('Joe')
bob = Person('Bob')
print(Person.all_names)
## ['Joe', 'Bob']