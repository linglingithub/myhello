#coding=utf-8

import unittest

"""

Longest Increasing Continuous Subsequence

Give an integer array，find the longest increasing continuous subsequence in this array.

An increasing continuous subsequence:

Can be from right to left or from left to right.
Indices of the integers in the subsequence should be continuous.
 Notice

O(n) time and O(1) extra space.

Example
For [5, 4, 2, 1, 3], the LICS is [5, 4, 2, 1], return 4.

For [5, 1, 2, 3, 4], the LICS is [1, 2, 3, 4], return 4.


Tags
Enumeration Dynamic Programming Array
Related Problems
Hard Longest Increasing Continuous subsequence II

Easy

"""


class Solution(object):
    # @param {int[]} A an array of Integer
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequence(self, A):
        # Write your code here
        if not A:
            return 0
        ascending = True
        result = 1
        current = 1
        for i in range(1, len(A)):
            if ascending == (A[i] > A[i-1]): # need to add bracket, otherwise wrong
                current += 1
            else:
                result = max(result, current)
                current = 2
                ascending = not ascending
        result = max(result, current) # don't forget this, otherwise wrong for case 2
        return result




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [5, 4, 2, 1, 3]
        answer = 4
        result = self.sol.longestIncreasingContinuousSubsequence(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [5, 1, 2, 3, 4]
        answer = 4
        result = self.sol.longestIncreasingContinuousSubsequence(nums)
        self.assertEqual(answer, result)



def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
