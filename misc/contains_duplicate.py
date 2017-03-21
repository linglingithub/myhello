#coding=utf-8

import unittest

"""
217. Contains Duplicate

Given an array of integers, find if the array contains any duplicates. Your function should return true if any value
appears at least twice in the array, and it should return false if every element is distinct.

Subscribe to see which companies asked this question.

Hide Tags Array Hash Table
Hide Similar Problems (E) Contains Duplicate II (M) Contains Duplicate III

Easy

"""



class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        rev = {}
        for num in nums:
            if num in rev:
                return True
            else:
                rev[num] = 1
        return False
        




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,1,1]
        answer = True
        result = self.sol.containsDuplicate(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [0]
        answer = False
        result = self.sol.containsDuplicate(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
