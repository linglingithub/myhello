#coding=utf-8

def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print "list1 = %s" % list1
print "list2 = %s" % list2
print "list3 = %s" % list3


"""
answer:

list1 = [10, 'a']
list2 = [123]
list3 = [10, 'a']

What actually happens is that the new default list is created only once when the function is defined, and that same

list is then used subsequently whenever extendList is invoked without a list argument being specified. This is

because expressions in default arguments are calculated when the function is defined, not when it’s called.

"""

print "====== compare ======="


def extendList(val, list=None):
  if list is None:
    list = []
  list.append(val)
  return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print "list1 = %s" % list1
print "list2 = %s" % list2
print "list3 = %s" % list3