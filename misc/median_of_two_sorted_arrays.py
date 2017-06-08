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
        if not nums1:
            nums1, nums2 = nums2, nums1
        #if not nums2:  # should be checking nums1 again, case 3
        if not nums1:
            return None
        m, n = len(nums1), len(nums2)
        if m < n:
            nums1, nums2 = nums2, nums1
            m, n = n, m
        # the above makes sure nums1 is the longer array, to simplify the following process
        mid = (m + n) / 2
        if (m + n) % 2 == 0:
            mid -= 1
        i, j, tag = 0, 0, 1
        #while i < m and j < n and i + j <= mid + 1: # should not be <= here, should be <
        while i < m and j < n and i + j < mid + 1:
            if nums1[i] < nums2[j]:
                i += 1
                tag = 1
            else:
                j += 1
                tag = 2
        if j >= n and i + j < mid + 1:
            tag = 1
            delta = mid + 1 - (i + j)
            i += delta

        if tag == 1:
            result = nums1[i-1]  # should be one step backward
        else:
            result = nums2[j-1]  # should be one step backward

        if (m + n) % 2 == 0:  # add consideration for even number, see case 2
            #next = min(nums1[i], nums2[j]) if i < m and j < n else nums1[i] , wrong when result is at the end of nums1, case2
            if i < m and j < n:
                next = min(nums1[i], nums2[j])
            elif i < m:
                next = nums1[i]
            else:
                next = nums2[j]
            result = (result + next) / 2.0
        return result




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case3(self):
        nums1 = [2]
        nums2 = []
        answer = 2.0   #wrong output None
        result = self.sol.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(answer, result)

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