#coding=utf-8

import unittest

"""
Subarray Sum

Given an integer array, find a subarray where the sum of numbers is zero. Your code should return the index of the first 
number and the index of the last number.

 Notice

There is at least one subarray that it's sum equals to zero.

Have you met this question in a real interview? Yes
Example
Given [-3, 1, 2, -3, 4], return [0, 2] or [1, 3].

Tags 
Subarray Hash Table
Related Problems 
Medium Submatrix Sum 25 %
Hard Subarray Sum II 29 %
Medium Minimum Size Subarray Sum 27 %
Medium Subarray Sum Closest

"""



class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """

    def subarraySum(self, nums):  # ref, jiuzhang, smart idea, check case02, case03
        """
        Basic idea, if some sum repeat in dict, which mean the sum of [first-value-index, current-index] is zero. 
        To accommodate the case that a=0 in result [a, b], we put {0:-1} in dict.  
        :param nums: 
        :return: 
        """
        hs = {0:-1}
        sum = 0
        for i in range(len(nums)):
            # if A[i] == 0:
            #     return [i, i]
            sum += nums[i]
            if sum in hs:
                print "result: ====> ", [hs[sum] + 1, i]
                return [hs[sum] + 1, i]
            hs[sum] = i
        return

    def subarraySum1(self, nums):
        # write your code here
        if not nums:
            return [-1, -1]
        start, end = 0, 0
        n = len(nums)
        while start < n:
            ssum = nums[start]
            end = start + 1
            while ssum != 0 and end < n:
                ssum += nums[end]
                end += 1
            if ssum == 0:
                # return [start, end]
                return [start, end-1]
            start += 1
        return [-1, -1]


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()


    def test_case03(self):
        nums = [3, -1, -2, 3, 4]
        answer = [[0, 2], [1,3]]
        result = self.sol.subarraySum(nums)
        #self.assertEqual(answer, result)
        self.assertTrue(result in answer)


    def test_case02(self):
        nums = [-5, 1, 2, -3, 4]
        answer = [[0, 2], [1,3]]
        result = self.sol.subarraySum(nums)
        #self.assertEqual(answer, result)
        self.assertTrue(result in answer)


    def test_case1(self):
        nums = [-3, 1, 2, -3, 4]
        answer = [[0, 2], [1,3]]
        result = self.sol.subarraySum(nums)
        #self.assertEqual(answer, result)
        self.assertTrue(result in answer)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
