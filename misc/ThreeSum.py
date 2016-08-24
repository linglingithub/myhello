__author__ = 'linglin'

"""
The problem presented by Project Euler in Problem 18 is an optimization problem
where you need to find the route through a triangle which maximizes the sum.
The problem reads

By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.
3
7 4
2 4 6
8 5 9 3
That is, 3 + 7 + 4 + 9 = 23.
"""

class Solution:
    # @param triang, a list of lists of integers
    # @return an integer
    # DP, O(n^2) time, O(n) space
    def minPathSum(self, triang):
        h=len(triang)
        w=len(grid[h-1])
        dp=[0 for i in range(h)]
        for i in range(0,w):
            dp[i] = triang[h-1][i]
        for i in range(h-2,-1,-1):
            for j in range(0,len(triang[i])):
                dp[j] = max(dp[j],dp[j+1]) + triang[i][j]
        result = dp[0]
        return result

if __name__ == "__main__":
    mps = Solution()
    grid = [[3], [7,4], [2,4,6],[8,5,9,3]]
    print mps.minPathSum(grid)