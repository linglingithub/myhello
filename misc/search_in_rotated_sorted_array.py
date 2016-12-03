"""
33. Search in Rotated Sorted Array

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Subscribe to see which companies asked this question

Hide Tags Binary Search Array
Hide Similar Problems (M) Search in Rotated Sorted Array II (M) Find Minimum in Rotated Sorted Array


"""

import unittest

class Solution(object):
    def search(self, nums, target): #52ms, 50%
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right) / 2
            if nums[mid] == target:
                return mid
            if nums[mid]<nums[right]: # starting point in left half
                if nums[mid]<target<=nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:  # starting point in the right half
                if nums[left]<= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 1
        answer = 5
        result = self.sol.search(nums, target)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 8
        answer = -1
        result = self.sol.search(nums, target)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8