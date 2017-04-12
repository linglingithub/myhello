"""
62. Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Subscribe to see which companies asked this question

Hide Tags Array Dynamic Programming
Hide Similar Problems (M) Unique Paths II (M) Minimum Path Sum (H) Dungeon Game

Medium

"""

import unittest


class Solution(object):
    def uniquePaths(self, m, n): #48ms, 42%, reduce to 1d dp
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m <= 0 or n <= 0:
            return 0
        dp = [1 for _ in range(n)]
        for row in range(1,m):
            for col in range(1,n):
                dp[col] = dp[col] + dp[col-1]
        return dp[n-1]

    def uniquePaths1(self, m, n): #36ms, 82%, reduce to 1d dp
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[n-1]


    def uniquePaths_2d_dp(self, m, n): # 33ms, 9075% <---- 66ms, 15.94%
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # dp = [ [0]* n ] * m
        # for i in range(m):
        #     dp[i][0] = 1
        # for i in range(n):
        #     dp[0][i] = 1
        dp = [ [1] *n ] * m
        for i in range(1, m):
            for j in range(1, n):
                # dp[i][j] = dp[i-1] + dp[j-1]  # be careful, no typo like this.
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case2(self): # ====>
        m = 2
        n = 2
        answer = 2
        result = self.sol.uniquePaths(m, n)
        self.assertEqual(answer, result)

    def test_case1(self):
        m = 1
        n = 1
        answer = 1
        result = self.sol.uniquePaths(m, n)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8