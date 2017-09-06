#coding=utf-8

import unittest

"""
Flatten 2D Vector

Implement an iterator to flatten a 2d vector.

Example
Given 2d vector =

[
  [1,2],
  [3],
  [4,5,6]
]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].

Tags 
Airbnb Google Zenefits Twitter
Related Problems 
Medium Zigzag Iterator 43 %
Medium Flatten Nested List Iterator 28 %
Easy Flatten Binary Tree to Linked List 33 %
Easy Flatten List

"""


class Vector2D(object):
    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        # Initialize your data structure here
        from collections import deque
        self._data = deque()
        for item in vec2d:
            if isinstance(item, int):
                self._data.append(item)
            else:
                for nest_item in item:
                    self._data.append(nest_item)

    # @return {int} a next element
    def next(self):
        # Write your code here
        _tmp = self._data.popleft()
        return _tmp

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        # Write your code here
        if self._data:
            return True
        else:
            return False


# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = 1
        answer = 1
        result = self.sol.searchInsert(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
