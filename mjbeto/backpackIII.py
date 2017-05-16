#coding=utf-8

import unittest

"""
Backpack III

Given n kind of items with size Ai and value Vi( each item has an infinite number available) and a backpack with size m. 
What's the maximum value can you put into the backpack?

 Notice

You cannot divide item into small pieces and the total size of items you choose should smaller or equal to m.

Have you met this question in a real interview? Yes
Example
Given 4 items with size [2, 3, 5, 7] and value [1, 5, 2, 4], and a backpack with size 10. The maximum value is 15.

Tags 
Dynamic Programming
Related Problems 
Medium Partition Equal Subset Sum 29 %
Medium Backpack VI 30 %
Medium Backpack V 45 %
Medium Backpack IV 41 %
Medium Backpack II 39 %
Medium Backpack
"""



class Solution:
    # @param {int[]} A an integer array
    # @param {int[]} V an integer array
    # @param {int} m an integer
    # @return {int} an array
    def backPackIII(self, nums, vals, m): #1105ms, 758ms
        # Write your code here
        dp = [0 for _ in range(m+1)]
        self.fill(nums, vals, m, dp)
        return dp[m]

    def fill(self, nums, vals, size, dp):
        if size == 0 or size>0 and dp[size] != 0:
            return dp[size]
        for i in range(len(nums)):
            weight = nums[i]
            val = vals[i]
            if size >= weight:
                dp[size] = max(self.fill(nums, vals, size-weight, dp) + val, dp[size])
        return dp[size]  # don't forget to return value here






class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [2, 3, 5, 7]
        vals = [1, 5, 2, 4]
        m = 10
        answer = 15
        result = self.sol.backPackIII(nums, vals, m)
        self.assertEqual(answer, result)



def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""

Following is a very simple and smart way

class Solution:
    # @param {int[]} A an integer array
    # @param {int[]} V an integer array
    # @param {int} m an integer
    # @return {int} an array
    def backPackIII(self, A, V, m):  #590ms
        # Write your code here
        f = [0 for i in xrange(m+1)]
        for (a, v) in zip(A, V):
            for j in xrange(a, m+1):
                if f[j - a] + v > f[j]:
                    f[j] = f[j - a] + v
        return f[m]
"""

#-*- coding:utf-8 -*-
