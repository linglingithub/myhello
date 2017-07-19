#coding=utf-8
import copy


li = [1,2,3]

def change(li):
    li = ['a', 'b','c']
    li[1] = 54835
    print "inside: ", li
    #li = copy.deepcopy(li)
    #return li
print li
x = change(li)
print li
print x
#x[1] = 123
li[1] = 123
print li, x


"""

https://www.quora.com/Are-arguments-passed-by-value-or-by-reference-in-Python

The parameter passed in is actually a reference to an object, as opposed to reference to a fixed memory location but 
the reference is passed by value. In addition, some data types (like strings, tuples etc) are immutable whereas others 
are mutable.

=============================

http://www.python-course.eu/passing_arguments.php

To come back to our initial question what is used in Python: The authors who call the mechanism call-by-value and those 
who call it call-by-reference are stretching the definitions until they fit. 
Correctly speaking, Python uses a mechanism, which is known as "Call-by-Object", sometimes also called "Call by Object 
Reference" or "Call by Sharing".

ParamterÃ¼bergabe If you pass immutable arguments like integers, strings or tuples to a function, the passing acts like 
call-by-value. The object reference is passed to the function parameters. They can't be changed within the function, 
because they can't be changed at all, i.e. they are immutable. It's different, if we pass mutable arguments. They are 
also passed by object reference, but they can be changed in place in the function. If we pass a list to a function, we 
have to consider two cases: Elements of a list can be changed in place, i.e. the list will be changed even in the 
caller's scope. If a new list is assigned to the name, the old list will not be affected, i.e. the list in the caller's 
scope will remain untouched.


"""