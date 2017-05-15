#coding=utf-8

import unittest

"""
Backpack II

Given n items with size Ai and value Vi, and a backpack with size m. What's the maximum value can you put into the 
backpack?

 Notice

You cannot divide item into small pieces and the total size of items you choose should smaller or equal to m.

Have you met this question in a real interview? Yes
Example
Given 4 items with size [2, 3, 5, 7] and value [1, 5, 2, 4], and a backpack with size 10. The maximum value is 9.

Challenge
O(n x m) memory is acceptable, can you do it in O(m) memory?

Tags
LintCode Copyright Dynamic Programming Backpack
Related Problems
Medium Backpack VI 30 %
Medium Backpack V 44 %
Medium Backpack IV 40 %
Hard Backpack III 53 %
Medium Backpack

"""



class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A & V: Given n items with size A[i] and value V[i]
    # @return: The maximum value
    def backPackII(self, m, nums, vals):
        dp = [0 for _ in range(m+1)]
        for i in range(len(nums)):
            for j in range(m, 0, -1):
                weight = nums[i]
                val = vals[i]
                size = j
                if size >= weight:
                    dp[size] = max(dp[size], dp[size-weight] + val)
        #return max(dp)  # result can directly be dp[m]
        return dp[m]




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        vals = [1, 5, 2, 4]
        sizes = [2, 3, 5, 7]
        m = 10
        answer = 9
        result = self.sol.backPackII(m, sizes, vals)
        self.assertEqual(answer, result)



def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""
class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A & V: Given n items with size A[i] and value V[i]
    def backPackII(self, m, A, V):
        # write your code here
        f = [0 for i in xrange(m+1)]
        n = len(A)
        for i in range(n):
            for j in xrange(m, A[i]-1, -1):
                f[j] = max(f[j] , f[j-A[i]] + V[i])
        return f[m]
"""

#-*- coding:utf-8 -*-
