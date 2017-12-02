#coding=utf-8

import unittest

"""

540. Zigzag Iterator 

 Description
 Notes
 Testcase
 Judge
Given two 1d vectors, implement an iterator to return their elements alternately.

Have you met this question in a real interview? Yes
Example
Given two 1d vectors:

v1 = [1, 2]
v2 = [3, 4, 5, 6]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].

Tags 
Google
Related Problems 
Medium Flatten 2D Vector 45 %
Medium Zigzag Iterator II 33 %
Medium Flatten Nested List Iterator 28 %
Hard Binary Search Tree Iterator

"""

from collections import deque


class ZigzagIterator:
    """
    @param: v1: A 1d vector
    @param: v2: A 1d vector
    """

    def __init__(self, v1, v2):
        # do intialization if necessary
        self.queue = deque()
        self.queue.append((0, v1))
        self.queue.append((0, v2))

    """
    @return: An integer
    """

    def next(self):
        # write your code here
        idx, vals = self.queue.popleft()
        res = vals[idx]
        idx += 1
        if idx < len(vals):
            self.queue.append((idx, vals))
        return res

    """
    @return: True if has next
    """

    def hasNext(self):
        # write your code here
        while self.queue:
            if self.queue[0][0] < len(self.queue[0][1]):
                return True
            self.queue.popleft()
        return False


# Your ZigzagIterator object will be instantiated and called as such:
# solution, result = ZigzagIterator(v1, v2), []
# while solution.hasNext(): result.append(solution.next())
# Output result




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = 1
        answer = 1
        result = self.sol.testm(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
