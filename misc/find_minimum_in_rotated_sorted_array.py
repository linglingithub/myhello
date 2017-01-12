__author__ = 'linglin'

"""

153. Find Minimum in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

Subscribe to see which companies asked this question

Hide Tags Array Binary Search
Hide Similar Problems (H) Search in Rotated Sorted Array (H) Find Minimum in Rotated Sorted Array II

Medium

"""


import unittest


class Solution(object):
    def findMin(self, nums): #39ms, 68%
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right)/2
            if nums[mid]<nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]






    def findMin1(self, nums): #42ms, 52% without printing, actually no need to do recursive way, just loop will do
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        self.nums = nums
        self.min_num = None
        self.findMin_helper(0, len(nums)-1)
        return self.min_num

    def findMin_helper(self, left, right):
        print "left, right: ", self.nums[left], self.nums[right], left, right
        if left>=right:
            self.min_num = self.nums[left]
            return
        if left + 1 == right: # need to deal with this case, otherwise infinite loop with case 1.
            self.min_num = min(self.nums[left], self.nums[right])
            return
        mid = (left+right) / 2
        if self.nums[left] > self.nums[mid] and self.nums[mid] < self.nums[right]: # need to add the left, mid, right check, otherwise wrong for case 2
            print "===> left half"
            self.findMin_helper(left, mid)
        elif self.nums[left] < self.nums[mid] and self.nums[mid] > self.nums[right]:
            print "===> right half"
            self.findMin_helper(mid, right)
        else: # no rotate actually, left < mid < right,
            self.min_num = self.nums[left]
            return


    def findMin_ref(self, nums): # simple and efficient code
        if len(nums) == 0:
            return 0

        start, end = 0, len(nums) - 1
        target = nums[-1]
        while start + 1 < end:
            mid = (start + end) / 2
            if nums[mid] <= target:
                end = mid
            else:
                start = mid
        return min(nums[start], nums[end])





class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case2(self): #====>
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