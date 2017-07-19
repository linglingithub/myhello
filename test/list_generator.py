"""
Show me three different ways of fetching every third item in the list
"""


# thelist = [1,2,3,4,5,6]
#
# a = [x for i, x in enumerate(thelist) if i%3 == 2]
# print "a = ", a
#
# def get_thirds(thelist):
#     for i, x in enumerate(thelist):
#         if i % 3 != 2:
#             continue
#         yield x
#
# def get_thirds1(thelist):
#     a = 0
#     for x in thelist:
#         if a%3 != 2:
#             a += 1
#             continue
#         yield x
#         a += 1
#
# b = get_thirds(thelist)  # b is a generator object
# print "b = ", b, thelist
# for bi in b:
#     print bi
# c = get_thirds1(thelist) # c is another generator object
# print "c = ", c
# for ci in c:
#     print ci



#========================================================
from collections import Counter

L = [1,2,3,4,5,6]
a = L[::3] # actually first element every three elements
b = [L[i] for i in xrange(len(L)) if not i%3]
#c = list(map(lambda e, i: e if i%3==2 , L, [x for x in range(len(L))]))
#d = filter(lambda (e, i): not i%3, zip(L, count()))
#d = map(lambda (e, i): e, filter(lambda (e, i): not i%3, zip(L, Counter(L))))
d = map(lambda (e, i): e, filter(lambda (e, i): not i%3, zip(L, range(len(L)))))
# details of d
# lambda -- pick only first ele from tuple , tuple is from the iterable ( the tuple is from a list of tuples ) --> ouput a list of single ele
# filter -- when not i%3 keep the elements from the list --> output a sub list of tuples)
# zip -- create a list of tuples, with every element and its index

c = map(lambda (idx, x): x, filter(lambda (idx, x): not idx%3, enumerate(L)))

print "a = ", a
print "b = ", b
print "c = ", c
print "d = ", d

#, ... a lot of other (bad) solutions here.