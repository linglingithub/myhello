#coding=utf-8

import unittest

"""
Maximal Square

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.

Have you met this question in a real interview? Yes
Example
For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.

Tags 
Airbnb Dynamic Programming Facebook
Related Problems 
Medium Maximal Square II 29 %
Hard Maximal Rectangle

"""


class Solution:
    #param matrix: a matrix of 0 and 1
    #return: an integer
    def maxSquare(self, matrix):
        # write your code here
        if not matrix or not matrix[0]:
             return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[matrix[i][j] for j in range(n)] for i in range(m)]
        result = 0
        # !!! can't only init as 0, cause following start from row 1, col 1
        # miss the case of sinle row or single column
        for i in range(m):
            if matrix[i][0] == 1:
                result = 1
                break
        if result == 0:
            for j in range(n):
                if matrix[0][j] == 1:
                    result = 1
                    break
        # start propagating dp
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    continue
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                result = max(result, dp[i][j])
        return result * result


class Solution1:
    #param matrix: a matrix of 0 and 1
    #return: an integer
    def maxSquare(self, matrix):
        """
        Main idea is to understand the dp status and relationship for square of smaller neighbors
        1. dp[i][j] is the length of square whose bottom-right point is at (i,j)
        2. dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1
        3. Note the initial status of first row, col, and the init value of result
        
        :param matrix: 
        :return: 
        """
        # write your code here
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[matrix[i][j] for j in range(n)] for i in range(m)]
        result = 0
        for i in range(m):   # add the first row and col check to see if result's min should be 1 or not. case 2
            if matrix[i][0] == 1:
                result = 1
                break
        if result == 0:
            for j in range(n):
                if matrix[0][j] == 1:
                    result = 1
                    break
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==1:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1
                    result = max(result, dp[i][j]*dp[i][j])
        return result


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case2(self):  #======>, wrong out put as 0
        nums = [[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]]
        answer = 1
        result = self.sol.maxSquare(nums)
        self.assertEqual(answer, result)

    def test_case1(self):
        nums = [
            [1,0,1,0,0],
            [1,0,1,1,1],
            [1,1,1,1,1],
            [1,0,0,1,0]
        ]
        answer = 4
        result = self.sol.maxSquare(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""

jiujiang answer:


    def maxSquare(self, matrix):
        # write your code here
        m = len(matrix)
        n = len(matrix[0])
        f = []
        for i in xrange(m): f.append([])
        for i in xrange(m):
            for j in xrange(n): f[i].append(0)
        for i in xrange(n): f[0][i] = matrix[0][i]
        for i in xrange(1, m): f[i][0] = matrix[i][0]
        for i in xrange(1, m):
            for j in xrange(1, n): 
                if (matrix[i][j]==0): f[i][j] = 0
                else: f[i][j] = 1+min(f[i-1][j], min(f[i-1][j-1], f[i][j-1]))
        ans = 0        
        for i in xrange(m):
            for j in xrange(n): ans = max(ans, f[i][j])
        return ans*ans

"""
