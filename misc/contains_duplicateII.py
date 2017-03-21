#coding=utf-8

import unittest

"""
219. Contains Duplicate II

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such
that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Subscribe to see which companies asked this question.

Hide Tags Array Hash Table
Hide Similar Problems (E) Contains Duplicate (M) Contains Duplicate III


Easy

"""



class Solution(object):
    def containsNearbyDuplicate(self, nums, k): #52ms, 98%
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return False
        if k==0:
            return False #True # see case 3, defined this case to be False
        rev = {}
        for idx, num in enumerate(nums):
            if num in rev:
                if idx - rev[num] <= k:
                    return True
                else:
                    rev[num] = idx
            else:
                rev[num] = idx
        return False





class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,1,1]
        k = 2
        answer = True
        result = self.sol.containsNearbyDuplicate(nums, k)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [1,0,1]
        k = 1
        answer = False
        result = self.sol.containsNearbyDuplicate(nums, k)
        self.assertEqual(answer, result)

    def test_case3(self): #====>
        nums = [1,2,1]
        k = 0
        answer = False
        result = self.sol.containsNearbyDuplicate(nums, k)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
