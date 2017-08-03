#coding=utf-8

import unittest

"""

Paint House 

 Description
 Notes
 Testcase
 Judge
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of 
painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses 
have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is 
the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... 
Find the minimum cost to paint all houses.

 Notice

All costs are positive integers.

Have you met this question in a real interview? Yes
Example
Given costs = [[14,2,11],[11,14,5],[14,3,10]] return 10

house 0 is blue, house 1 is green, house 2 is blue, 2 + 5 + 3 = 10

Tags 
LinkedIn Dynamic Programming
Related Problems 
Medium House Robber II 28 %
Hard Paint House II 26 %
Easy Paint Fence 30 %
Medium House Robber

"""



class Solution:
    # @param {int[][]} costs n x 3 cost matrix
    # @return {int} an integer, the minimum cost to paint all houses
    def minCost(self, costs):
        # Write your code here
        if not costs or not costs[0]:
            return 0
        # dp init
        m, n = len(costs), len(costs[0])
        if m < 2:
            return min(costs[0])
        # !!! need to check when there is only ONE row, otherwise wrong!!!
        # use rolling array
        dp = [[costs[i][j] for j in range(n)] for i in range(2)]
        for i in range(1, m):
            for j in range(n):
                dp[i%2][j] = costs[i][j] + min(x for x in dp[(i-1)%2][:j] + dp[(i-1)%2][j+1:])
        return min(dp[(m-1)%2])


    def minCost1(self, costs):
        # Write your code here
        if not costs or not costs[0]:
            return 0
        # dp init
        m, n = len(costs), len(costs[0])
        dp = [[costs[i][j] for j in range(n)] for i in range(m)]
        for i in range(1, m):
            for j in range(n):
                # dp[i][j] = costs[i][j] + min(x for x in [dp[i-1][col] for col in range(n) and col!=j])  # wrong expression
                dp[i][j] = costs[i][j] + min(x for x in dp[i-1][:j] + dp[i-1][j+1:])
        return min(dp[m-1])


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        costs = [[14,2,11],[11,14,5],[14,3,10]]
        answer = 10  # house 0 is blue, house 1 is green, house 2 is blue, 2 + 5 + 3 = 10
        result = self.sol.minCost(costs)
        self.assertEqual(answer, result)

    def test_case2(self):  #====>
        costs = [[1,2,3]]
        answer = 1
        result = self.sol.minCost(costs)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
