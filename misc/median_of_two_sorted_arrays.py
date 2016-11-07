__author__ = 'linglin'

"""
4. Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
Subscribe to see which companies asked this question

Hide Tags Binary Search Array Divide and Conquer

Difficulty: Hard

"""


import unittest


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if (nums1 is None or len(nums1)==0) and (nums2 is None or len(nums2)==0):
            return None
        idx = 0
        mid = (len(nums1)+len(nums2)) / 2
        while


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums1 = [1, 3]
        nums2 = [2]
        answer = 2
        result = self.sol.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums1 = [1, 2]
        nums2 = [3, 4]
        answer = 2.5
        result = self.sol.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8