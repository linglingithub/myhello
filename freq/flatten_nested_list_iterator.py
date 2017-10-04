#coding=utf-8

import unittest

"""
Flatten Nested List Iterator

Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

 Notice

You don't need to implement the remove method.

Have you met this question in a real interview? Yes
Example
Given the list [[1,1],2,[1,1]], By calling next repeatedly until hasNext returns false, the order of elements returned 
by next should be: [1,1,2,1,1].

Given the list [1,[4,[6]]], By calling next repeatedly until hasNext returns false, the order of elements returned by 
next should be: [1,4,6].

Tags 
Stack Recursion Data Structure Design Snapchat Google
Related Problems 
Medium Flatten 2D Vector 46 %
Easy Nested List Weight Sum 45 %
Medium Zigzag Iterator II 30 %
Medium Zigzag Iterator 42 %
Easy Flatten Binary Tree to Linked List

"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return {boolean} True if this NestedInteger holds a single integer,
#        rather than a nested list.
#        """
#
#    def getInteger(self):
#        """
#        @return {int} the single integer that this NestedInteger holds,
#        if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self):
#        """
#        @return {NestedInteger[]} the nested list that this NestedInteger holds,
#        if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator(object):
    def __init__(self, nestedList):
        # Initialize your data structure here.
        # if not nestedList:
            # raise Exception("Can't create iterator over None or empty inputs!")
        # # ok to raise exception in lintcode, on leetcode just ignore
        self.data = []
        self.idx = 0
        _tmp = [ele for ele in nestedList]
        while _tmp:
            cur = _tmp.pop(0)
            if cur.isInteger():
                self.data.append(cur.getInteger())
            else:
                cur_list = cur.getList()
                for idx, ele in enumerate(cur_list):
                    _tmp.insert(idx, ele)

    # @return {int} the next element in the iteration
    def next(self):
        # Write your code here
        if self.hasNext():
            self.idx += 1
            return self.data[self.idx - 1]

    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        # Write your code here
        return self.idx < len(self.data)




class NestedIterator_wrong(object):
    """
    Input
    [[1,1],2,[1,1]]
    Expected
    [1,1,2,1,1]
    Error Message
    Traceback (most recent call last): File "Main.py", line 12, in i, v = NestedIterator(nestedList), [] 
    File "NestedIterator.py", line 38, in __init__ for idx, ele in enumerate(tmp): TypeError: 'NestedInteger' object is 
    not iterable EXITCODE=1
    
    """
    def __init__(self, nestedList):
        # Initialize your data structure here.
        self.data = []
        self.idx = -1
        while nestedList:
            tmp = nestedList.pop(0)
            if isinstance(tmp, int):
                self.data.append(tmp)
            else:
                for idx, ele in enumerate(tmp):
                    nestedList.insert(idx, ele)

    # @return {int} the next element in the iteration
    def next(self):
        # Write your code here
        tmp = self.data.pop(0)
        return tmp

    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        # Write your code here
        return len(self.data) > 0


# Write your code here


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case2(self):
        nums = [4,[3,[2,[1]]]]
        answer = [4,3,2,1]
        result = self.sol.flatten(nums)
        self.assertEqual(answer, result)


    def test_case1(self):
        nums = [1,2,[1,2]]
        answer = [1,2,1,2]
        result = self.sol.flatten(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
