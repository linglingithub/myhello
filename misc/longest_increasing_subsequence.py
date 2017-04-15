#coding=utf-8

import unittest

"""

Longest Increasing Subsequence

Given a sequence of integers, find the longest increasing subsequence (LIS).

You code should return the length of the LIS.

Have you met this question in a real interview? Yes
Clarification
What's the definition of longest increasing subsequence?

The longest increasing subsequence problem is to find a subsequence of a given sequence in which the subsequence's
elements are in sorted order, lowest to highest, and in which the subsequence is as long as possible. This subsequence
is not necessarily contiguous, or unique.

https://en.wikipedia.org/wiki/Longest_increasing_subsequence

Example
For [5, 4, 1, 2, 3], the LIS is [1, 2, 3], return 3
For [4, 2, 4, 5, 3, 7], the LIS is [2, 4, 5, 7], return 4

Challenge
Time complexity O(n^2) or O(nlogn)

Tags
Binary Search LintCode Copyright Dynamic Programming
Related Problems

"""



class Solution:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [5, 4, 1, 2, 3]
        answer = 3
        result = self.sol.longestIncreasingSubsequence(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [4, 2, 4, 5, 3, 7]
        answer = 4
        result = self.sol.longestIncreasingSubsequence(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
