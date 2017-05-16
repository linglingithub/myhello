#coding=utf-8

import unittest

"""
Backpack V

Given n items with size nums[i] which an integer array and all positive numbers. An integer target denotes the size of 
a backpack. Find the number of possible fill the backpack.

Each item may only be used once

Have you met this question in a real interview? Yes
Example
Given candidate items [1,2,3,3,7] and target 7,

A solution set is: 
[7]
[1, 3, 3]
return 2

Tags 
Dynamic Programming
Related Problems 
Medium Backpack VI 30 %
Medium Backpack IV 41 %
Hard Backpack III 54 %
Medium Backpack II 39 %
Medium Backpack


"""


class Solution:
    # @param {int[]} nums an integer array and all positive numbers
    # @param {int} target an integer
    # @return {int} an integer
    def backPackV(self, nums, target):
        # Write your code here
        n = len(nums)
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        for i in range(n):
            stone = nums[i]
            for j in range(target, stone-1, -1):
                if dp[j-stone]>0:
                    dp[j] += dp[j-stone]
        return dp[target]




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,2,3,3,7]
        target = 7
        answer = 2  #[[1,3,3], [7]]
        result = self.sol.backPackV(nums, target)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [1, 2, 4]
        target = 4
        answer = 1 # [[4]]
        result = self.sol.backPackV(nums, target)
        self.assertEqual(answer, result)



def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""

class Solution:
    # @param {int[]} nums an integer array and all positive numbers
    # @param {int} target an integer
    # @return {int} an integer
    def backPackV(self, nums, target):
        # Write your code here
        dp = [0 for i in xrange(target + 1)]
        dp[0] = 1
        
        for a in nums:
            for j in xrange(target, a - 1, -1):
                dp[j] += dp[j - a]

        return dp[target]
  
        
"""

#-*- coding:utf-8 -*-
