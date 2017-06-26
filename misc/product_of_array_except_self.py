#coding=utf-8

"""
 
238. Product of Array Except Self


Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of 
all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the 
purpose of space complexity analysis.)

"""

import unittest


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        left = [x for x in nums]
        n = len(nums)
        for i in range(1, n - 1):
            left[i] *= left[i - 1]
        right_pro = 1
        for i in range(n - 1, 0, -1):
            left[i] = left[i - 1] * right_pro
            right_pro *= nums[i]

        # deal with left[0]
        left[0] = right_pro
        return left


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,2,3,4]
        answer = [24,12,8,6]
        result = self.sol.productExceptSelf(nums)
        self.assertEqual(answer, result)



def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner.run(suite)


if __name__ == '__main__':
    main()