#coding=utf-8

import unittest

"""

Continuous Subarray Sum

Given an integer array, find a continuous subarray where the sum of numbers is the biggest. Your code should return the 
index of the first number and the index of the last number. (If their are duplicate answer, return anyone)

Have you met this question in a real interview? Yes
Example
Give [-3, 1, 3, -3, 4], return [1,4].

Tags 
Subarray Array
Related Problems 
Medium Continuous Subarray Sum II 14 %
Easy Maximum Subarray

"""



class Solution:
    # @param {int[]} A an integer array
    # @return {int[]}  A list of integers includes the index of the
    #                  first number and the index of the last number

    def continuousSubarraySum(self, A):  # ref
        # Write your code here
        if not A:
            return [-1, -1]
        result = A[0]
        result2 = [0, 0]
        rsum = 0
        left, right = 0, 0
        for i in range(len(A)):
            x = A[i]
            rsum += x
            if rsum > result:
                result = rsum
                result2 = [left, right]
            if rsum <= 0:
                left = i+1
                right = left
                rsum = 0
                continue
            right += 1
        #return [left, right]
        return result2


    def continuousSubarraySum(self, A):
        # Write your code here
        if not A:
            return [-1, -1]
        result = A[0]
        result2 = [0, 0]
        n = len(A)
        dp = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + A[i - 1]
        for i in range(n):
            if A[i] <= 0:
                continue
            for j in range(i + 1, n + 1):
                if A[j - 1] <= 0:
                    continue

                tmp = dp[j] - dp[i]
                if tmp > result:
                    result = tmp
                    result2 = [i, j - 1]
        return result2

    def continuousSubarraySum_TLE(self, A): #TLE with 61% passed
        # Write your code here
        if not A:
            return [-1, -1]
        result = A[0]
        result2 = [0, 0]
        n = len(A)
        dp = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            dp[i] = dp[i-1] + A[i-1]
        for i in range(n):
            for j in range(i+1, n+1):
                tmp = dp[j]-dp[i]
                if tmp > result:
                    result = tmp
                    result2 = [i, j-1]
        return result2


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [-3, 1, 3, -3, 4]
        answer = [1, 4]
        result = self.sol.continuousSubarraySum(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
