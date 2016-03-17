__author__ = 'linglin'


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

"""
Minimum Path Sum

Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right which minimizes
the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

"""