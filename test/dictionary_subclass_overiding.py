"""

Given the following subclass of dictionary:

class DefaultDict(dict):
  def __missing__(self, key):
    return []

Will the code below work? Why or why not?

d = DefaultDict()
d['florp'] = 127

"""

class DefaultDict(dict):
  def __missing__(self, key):
    return []


d = DefaultDict()
d['florp'] = 127
print(d)
print(d['hfjd'])  # i thinks this is the difference, when a key is missing, no error will happen and [] is returned.
# compare with the nomal dict than trying to access a key and value where the key is missing.


"""
Yes, it will work. With this implementation of the DefaultDict class, whenever a key is missing, the instance of the
dictionary will automatically be instantiated with a list.

"""

print()

a = {}
a['florp'] = 231
print(a)
print(a['32321'])  # this will result in a KeyError