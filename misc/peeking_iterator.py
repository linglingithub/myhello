#coding=utf-8

import unittest

"""
284. Peeking Iterator
DescriptionHintsSubmissionsDiscussSolution
Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that
support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().

Example:

Assume that the iterator is initialized to the beginning of the list: [1,2,3].

Call next() gets you 1, the first element in the list.
Now you call peek() and it returns 2, the next element. Calling next() after that still return 2.
You call next() the final time and it returns 3, the last element.
Calling hasNext() after that should return false.
Follow up: How would you extend your design to be generic and work with all types, not just integer?


Difficulty:Medium
Total Accepted:56.6K
Total Submissions:159.5K
Contributor:porker2008
Companies

Related Topics

Similar Questions
Binary Search Tree IteratorFlatten 2D VectorZigzag Iterator
Python


"""

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """


class PeekingIterator(object): # this method, when doing peek, already call one next, then check hasNext how to handle?
    """
    Key points:
    how to handle peek and next? pay attention to when to move the pointer!!!
    Main idea:
    when peek, no moving of the iterator, except the first time
    when next, get from peek (which is the current), then move the iterator

    """
    PeekingIteratorNone = 'PeekingIteratorNone'

    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        if iterator is None:
            raise ValueError("Can not initializae an iterator over None!")
        self._iter = iterator
        self._cache = iterator.next()  # !!! need to init here, otherwise peek() will have 'NPE'
        # self._cache = self._next()   # may make a hasnext wrong

    def _next(self):
        if self._iter.hasNext():
            return self._iter.next()
        else:
            return PeekingIterator.PeekingIteratorNone   # Line 45: NameError: global name 'PeekingIteratorNone' is not defined

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self._cache != PeekingIterator.PeekingIteratorNone:
            return self._cache
        else:
            return None # or check what to return with interviewer

    def next(self):
        """
        :rtype: int
        """
        tmp = self._cache
        self._cache = self._next()
        return tmp

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._iter.hasNext() or self._cache != PeekingIterator.PeekingIteratorNone

class PeekingIterator_WRONG_ShouldHandleIteratorNotList(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        if iterator == None:
            raise ValueError("Can not initializae an iterator over None!")
        self._data = iterator
        self._idx = 0
        self._end = len(iterator)   # object of type 'Iterator' has no len()


    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.hasNext():
            return iterator[self._idx]
        else:
            return None # or raise an Exception?


    def next(self):
        """
        :rtype: int
        """
        tmp = iterator[self._idx]
        self._idx += 1
        return tmp


    def hasNext(self):
        """
        :rtype: bool
        """
        return self._idx < self._end



# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].

class SolutionTester(unittest.TestCase):
    def setUp(self):
        pass

    def test_case1(self):
        nums = [1, 2, 3, 4]
        answer = ["True","1","1","1","2","3","3","3","True","4","True","4","False"]
        piter = PeekingIterator(nums)
        result.append(str(piter.hasNext()))  # true
        result.append(str(piter.peek()))     # 1
        result.append(str(piter.peek()))     # 1
        result.append(str(piter.next()))     # 1
        result.append(str(piter.next()))     # 2
        result.append(str(piter.peek()))     # 3
        result.append(str(piter.peek()))     # 3
        result.append(str(piter.next()))     # 3
        result.append(str(piter.hasNext()))  # True
        result.append(str(piter.peek()))     # 4
        result.append(str(piter.hasNext()))  # True
        result.append(str(piter.next()))     # 4
        result.append(str(piter.hasNext()))  # False
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""
class PeekingIterator(object):
    def __init__(self, iterator):
        self.iter, self.pk = iterator, None
    def peek(self):
        if self.pk:
            return self.pk
        else:
            self.pk = self.iter.next()
            return self.pk
    def next(self):
        if self.pk:
            ans = self.pk
            self.pk = None
            return ans
        else:
            return self.iter.next()
    def hasNext(self):
        return self.iter.hasNext() or self.pk != None

"""

#-*- coding:utf-8 -*-
