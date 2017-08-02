#coding=utf-8
"""
(1) Examples of generator, how it works

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


"""

(2) diff in execution of yield vs return

The yield keyword is central to python generator functions but what does this yield keyword do? To understand the yield 
keyword, we contrast it with the return key word; the other keyword that gives back control to the caller of a 
function. When a function that is executing encounters the yield keyword, it suspends execution at that point, saves 
its context and returns to the caller along with any value in the expression_list; when the caller invokes next on the 
object, execution of the function continues till another yield or return is encountered or end of function is reached. 


(3) what use for generator

https://stackoverflow.com/questions/102535/what-can-you-use-python-generator-functions-for

Generators give you lazy evaluation. You use them by iterating over them, either explicitly with 'for' or implicitly by 
passing it to any function or construct that iterates. You can think of generators as returning multiple items, as if 
they return a list, but instead of returning them all at once they return them one-by-one, and the generator function 
is paused until the next item is requested.

Generators are good for calculating large sets of results (in particular calculations involving loops themselves) where 
you don't know if you are going to need all results, or where you don't want to allocate the memory for all results at 
the same time. Or for situations where the generator uses another generator, or consumes some other resource, and it's 
more convenient if that happened as late as possible.



(4) more example of using generator to read large files

https://www.oreilly.com/ideas/2-great-benefits-of-python-generators-and-how-they-changed-me-forever

And ideally without slurping in the entire large file. Each record is split over several lines, so you have to do 
something more sophisticated than "for line in myfile:". The nicest way I know to solve this problem in Python is 
using a generator:

def gen_records(path):
    with open(path) as handle:
        record = {}
        for line in handle:
            if line == "\n":
                yield record
                record = {}
                continue
            key, value = line.rstrip("\n").split(": ", 1)
            record[key] = value
That lets us do things like:

for record in gen_records('data.txt'):
    print("{} had {} requests in the past hour".format(
        record["article"], record["requests"]))
Someone using gen_records doesn't have to know, or care, that the source is a multiline-record format. There is 
complexity, yes, because that's necessary in this situation. But all that complexity is very nicely encapsulated in the 
generator function!

This pattern is especially valuable with continuous streams, like from a socket connection, or tailing a log file. 
Imagine a long-running program that listens on some source and continually working with the produced records - 
generators are perfect for this.

....

And it illustrates the other benefit of generators mentioned earlier: encapsulation. It provides new and useful ways 
for you to package and isolate internal code dependencies. You can do the same thing with classes, but only by 
spreading state across several methods, in a way that's not nearly as easy to understand.

....

Compared to using (say) a simple list, iterators tremendously reduce memory footprint; improve scalability; and make 
your code more responsive to the end user. Through this, Python taught me to be a better programmer in every language.




"""