__author__ = 'linglin'

"""

154. Find Minimum in Rotated Sorted Array II

Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.

Subscribe to see which companies asked this question

Hide Tags Array Binary Search
Hide Similar Problems (M) Find Minimum in Rotated Sorted Array

Hard

"""

import unittest


class Solution(object):
    def findMin(self, nums): #39ms, 82%
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        left, right = 0, len(nums)-1
        while left<right:
            mid = (left+right)/2
            if nums[left]<nums[mid]<nums[right]:
                return nums[left]
            elif nums[left]>nums[mid] and nums[mid]<nums[right]:
                right = mid
            elif nums[right] < nums[mid] and nums[mid]>nums[left]:
                left = mid+1
            elif nums[left]<nums[right]:
                right -= 1
            else:
                left += 1
        return nums[left]


    def findMin_ref(self, num): #42ms, 69%, simple code
        L = 0; R = len(num)-1
        while L < R and num[L] >= num[R]:
            M = (L+R)/2
            if num[M] > num[L]:
                L = M + 1
            elif num[M] < num[R]:
                R = M
            else:
                L += 1
        return num[L]



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()


    def test_case3(self):
        nums = [4,4,4,1,2,4,4,4,4,4,4]
        answer = 1
        result = self.sol.findMin(nums)
        self.assertEqual(answer, result)


    def test_case2(self):
        nums = [1,2,3]
        answer = 1
        result = self.sol.findMin(nums)
        self.assertEqual(answer, result)

    def test_case1(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        answer = 0
        result = self.sol.findMin(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8