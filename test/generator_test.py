#coding=utf-8
"""
http://anandology.com/python-practice-book/iterators.html

5.2. Generators
Generators simplifies creation of iterators. A generator is a function that produces a sequence of results instead of 
a single value.

def yrange(n):
    i = 0
    while i < n:
        yield i
        i += 1
Each time the yield statement is executed the function generates a new value.

>>> y = yrange(3)
>>> y
<generator object yrange at 0x401f30>
>>> y.next()
0
>>> y.next()
1
>>> y.next()
2
>>> y.next()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
So a generator is also an iterator. You don’t have to worry about the iterator protocol.

The word “generator” is confusingly used to mean both the function that generates and what it generates. In this 
chapter, I’ll use the word “generator” to mean the genearted object and “generator function” to mean the function that 
generates it.

Can you think about how it is working internally?

When a generator function is called, it returns a generator object without even beginning execution of the function. 
When next method is called for the first time, the function starts executing until it reaches yield statement. 
The yielded value is returned by the next call.

The following example demonstrates the interplay between yield and call to next method on generator object.

>>> def foo():
...     print "begin"
...     for i in range(3):
...         print "before yield", i
...         yield i
...         print "after yield", i
...     print "end"
...
>>> f = foo()
>>> f.next()
begin
before yield 0
0
>>> f.next()
after yield 0
before yield 1
1
>>> f.next()
after yield 1
before yield 2
2
>>> f.next()
after yield 2
end
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>

"""


def integers():
    """Infinite sequence of integers."""
    i = 1
    while True:
        print "integers | inside integer: ", i
        yield i
        print "integers | to increase i: ", i
        i = i + 1

def squares():
    for i in integers():
        print "inside squares: ", i
        yield i * i

def take(n, seq):
    """Returns first n values from the given sequence."""
    seq = iter(seq)
    result = []
    try:
        for i in range(n):
            print "--> loop of take: ", i
            result.append(seq.next())
            print "<-- loop one done."
    except StopIteration:
        print "--- inside StopIteration! ",
        pass
    return result

print take(5, squares()) # prints [1, 4, 9, 16, 25]