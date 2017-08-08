#coding=utf-8

import unittest

"""
283. Move Zeroes
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the 
non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

Related Topics 
Array Two Pointers 
Similar Questions 
Remove Element 


Easy



"""


class Solution(object):
    def moveZeroes_ref(self, nums):  # ref idea, simple and fast, # 80+%
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        i = 0
        for num in nums:
            if num != 0:
                nums[i] = num
                i += 1
        for k in range(i, len(nums)):
            nums[k] = 0

    def moveZeroes(self, nums):  # 52%
        """
        use i to track idx of non-zero index, j to find the faster non-zero elements to feed to i, 
        and in the end, put remaining [i:] to all zeros.
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        i = 0
        while i < len(nums) and nums[i] != 0:
            i += 1
        j = i+1
        while j < len(nums):
            while j < len(nums) and nums[j] == 0:
                j += 1
            if j >= len(nums):
                break
            nums[i] = nums[j]
            i += 1
            j += 1
        for k in range(i, len(nums)):
            nums[k] = 0


    def moveZeroes_wrong(self, nums):  # this basically move the zero to the end, but did not maintain the order of non-0 elements
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        i, j = 0, len(nums) - 1
        while j > i and nums[j] == 0:
            j -= 1
        while i < j:
            if nums[i] != 0:
                i += 1
                continue
            while j > i and nums[j] == 0:
                j -= 1
            nums[j], nums[i] = nums[i], nums[j]
            j -= 1
            i += 1


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [0, 1, 0, 3, 12]
        answer = [1, 3, 12, 0, 0]
        result = self.sol.moveZeroes(nums)
        self.assertEqual(answer, nums)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
