__author__ = 'linglin'
"""
1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
UPDATE (2016/2/13):
The return format had been changed to zero-based indices. Please read the above updated description carefully.

Array Hash Table
(M) 3Sum (M) 4Sum (M) Two Sum II - Input array is sorted (E) Two Sum III - Data structure design

"""

import unittest


class Solution(object):
    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums), 1):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum(self, nums, target):
        vals = {}
        for i in range(len(nums)):
            a = nums[i]
            b = target - a
            if b in vals:
                return [i, vals[b]] if i < vals[b] else [vals[b], i]
            vals[a] = i



class TwoSumTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [2, 7, 11, 15]
        target = 9
        result = self.sol.twoSum(nums, target)
        self.assertEqual([0,1], result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TwoSumTester)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()

