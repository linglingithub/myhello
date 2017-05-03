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
"""
题 Longest Increasing Continuous subsequence 的 follow up, 变成一道比较难的题了。从之前的一维 DP 变为现在的二维 DP，自增方向可从
上下左右四个方向进行。需要结合 DFS 和动态规划两大重量级武器。
根据二维 DP 的通用方法，我们首先需要关注状态及状态转移方程，状态转移方程相对明显一点，即上下左右四个方向的元素值递增关系，根据此转移方程，
不难得到我们需要的状态为dp[i][j]——表示从坐标(i, j)出发所得到的最长连续递增子序列。根据状态及转移方程我们不难得到初始化应该为1或者0，这要
视具体情况而定。
这里我们可能会纠结的地方在于自增的方向，平时见到的二维 DP 自增方向都是从小到大，而这里的增长方向却不一定。这里需要突破思维定势的地方在于我
们可以不理会从哪个方向自增，只需要处理自增和边界条件即可。根据转移方程可以知道使用递归来解决是比较好的方式，这里关键的地方就在于递归的终止条
件。比较容易想到的一个递归终止条件自然是当前元素是整个矩阵中的最大元素，索引朝四个方向出发都无法自增，因此返回1. 另外可以预想到的是如果不进
行记忆化存储，递归过程中自然会产生大量重复计算，根据记忆化存储的通用方法，这里可以以结果是否为0(初始化为0时)来进行区分。


"""