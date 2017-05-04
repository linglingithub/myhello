#coding=utf-8

import unittest

"""

Maximum Average Subarray

Given an array with positive and negative numbers, find the maximum average subarray which length should be greater or
equal to given length k.

 Notice

It's guaranteed that the size of the array is greater or equal to k.

Have you met this question in a real interview? Yes
Example
Given nums = [1, 12, -5, -6, 50, 3], k = 3

Return 15.667 // (-6 + 50 + 3) / 3 = 15.667

Tags
Binary Search Subarray Google
Related Problems
Easy Maximum Subarray

Medium

"""



class Solution:
    # @param {int[]} nums an array with positive and negative numbers
    # @param {int} k an integer
    # @return {double} the maximum average
    def maxAverage(self, nums, k):
        # Write your code here



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1, 12, -5, -6, 50, 3]
        k = 3
        answer = 15.667
        result = self.sol.maxAverage(nums, k)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
