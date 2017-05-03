#coding=utf-8

import unittest

"""

Longest Increasing Continuous Subsequence II

Give you an integer matrix (with row size n, column size m)，find the longest increasing continuous subsequence in this
matrix. (The definition of the longest increasing continuous subsequence here can start at any row or column and go
up/down/right/left any direction).

Example
Given a matrix:

[
  [1 ,2 ,3 ,4 ,5],
  [16,17,24,23,6],
  [15,18,25,22,7],
  [14,19,20,21,8],
  [13,12,11,10,9]
]
return 25

Challenge
O(nm) time and memory.

Tags
Dynamic Programming
Related Problems
Easy Longest Increasing Continuous Subsequence

Hard

"""


class Solution:
    # @param {int[][]} A an integer matrix
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequenceII(self, A):
        # Write your code here
        if not A or not A[0]:
            return 0
        row, col = len(A), len(A[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]
        result = 0
        for i in range(row):
            for j in range(col):
                one_ans = self.find_LICS(A, i, j, dp)
                result = max(result, one_ans)
        return result

    def find_LICS(self, A, x, y, dp):
        if dp[x][y] != 0:
            return dp[x][y]
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        length = 1 # can't be 0 here, otherwise wrong, where d[x][y] is the largest value, then the length is 1 actually
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<len(A) and 0<=ny<len(A[0]) and A[nx][ny] > A[x][y]:
                length = max(length, 1+self.find_LICS(A, nx, ny, dp))
        dp[x][y] = length
        return dp[x][y]









class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [
          [1 ,2 ,3 ,4 ,5],
          [16,17,24,23,6],
          [15,18,25,22,7],
          [14,19,20,21,8],
          [13,12,11,10,9]
        ]
        answer = 25
        result = self.sol.longestIncreasingContinuousSubsequenceII(nums)
        self.assertEqual(answer, result)





def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
