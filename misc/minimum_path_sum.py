"""
64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum

of all numbers along its path.

Note: You can only move either down or right at any point in time.

Subscribe to see which companies asked this question

Hide Tags Array Dynamic Programming
Hide Similar Problems (M) Unique Paths (H) Dungeon Game

Medium

"""

import unittest


class Solution(object):
    def minPathSum(self, grid): #58ms, 85%
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid is None or len(grid)==0 or len(grid[0])==0:
            return 0
        m = len(grid)
        n = len(grid[0])
        dp = [ [ 0 for j in range(n)] for i in range(m) ]
        row_cost = 0
        for i in range(m):
            row_cost += grid[i][0]
            dp[i][0] = row_cost
        col_cost = 0
        for j in range(n):
            col_cost += grid[0][j]
            dp[0][j] = col_cost
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[m-1][n-1]

    def minPathSum_ref(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, n):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[m - 1][n - 1]




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        grid = [[1,2,3],[3,2,1],[1,1,1]]
        answer = 7
        result = self.sol.minPathSum(grid)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8



''' ---> old ----

class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    # DP, O(n^2) time, O(n^2) space
    def minPathSum(self, grid):
        m=len(grid)
        n=len(grid[0])
        dp=[[0 for i in range(n)] for j in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1,n):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        for j in range(1,m):
            dp[j][0] = dp[j-1][0] + grid[j][0]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]= min(dp[i-1][j]+grid[i][j],dp[i][j-1]+grid[i][j])
        result = dp[m-1][n-1]
        return result

    # DP, O(n^2) time, O(n) space
    def minPathSum_reduce(self, grid):
        m=len(grid)
        n=len(grid[0])
        dp=[0 for i in range(n)]
        dp[0] = grid[0][0]
        for i in range(1,n):
            dp[i] = dp[i-1] + grid[0][i]
        for i in range(1,m):
            dp[0] += grid[i][0]
            for j in range(1,n):
                dp[j] = min(dp[j],dp[j-1]) + grid[i][j]
        result = dp[n-1]
        return result

if __name__ == "__main__":
    mps = Solution()
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print mps.minPathSum(grid)
    print mps.minPathSum_reduce(grid)
'''
