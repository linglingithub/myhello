#coding=utf-8

import unittest

"""
Partition Array

Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:

All elements < k are moved to the left
All elements >= k are moved to the right
Return the partitioning index, i.e the first index i nums[i] >= k.

 Notice

You should do really partition in array nums instead of just counting the numbers of integers smaller than k.

If all elements in nums are smaller than k, then return nums.length

Example
If nums = [3,2,2,1] and k=2, a valid answer is 1.

Challenge 
Can you partition the array in-place and in O(n)?

Tags 
Two Pointers Sort Array
Related Problems 
Easy Partition Array by Odd and Even 41 %
Medium Interleaving Positive and Negative Numbers 22 %
Easy Partition List

Medium

"""



class Solution:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        # you should partition the nums by k
        # and return the partition index as description
        if not nums:
            return 0
        left, right = 0, len(nums)-1
        while left < right:
            while left < right and nums[left] < k:
                left += 1
            while right > left and nums[right] >= k:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
        if nums[right] < k:
            return right + 1
        else:
            return right




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [3,2,2,1]
        k = 2
        answer = 1
        result = self.sol.partitionArray(nums, k)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [3,2,2,1]
        k = 4
        answer = 4
        result = self.sol.partitionArray(nums, k)
        self.assertEqual(answer, result)

    def test_case3(self): # ===> should return 0, not -1 here
        nums = []
        k = 9
        answer = 0
        result = self.sol.partitionArray(nums, k)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""
    reference
    def partitionArray(self, nums, k):
        start, end = 0, len(nums) - 1
        while start <= end:
            while start <= end and nums[start] < k:
                start += 1
            while start <= end and nums[end] >= k:
                end -= 1
            if start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        return start

"""