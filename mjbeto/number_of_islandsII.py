#coding=utf-8

import unittest

"""

305. Number of Islands II

locked

Hard

========================================================================================================================

Given a n,m which means the row and column of the 2D matrix and an array of pair A( size k). Originally, the 2D matrix
is all 0 which means there is only sea in the matrix. The list pair has k operator and each operator has two integer
A[i].x, A[i].y means that you can change the grid matrix[A[i].x][A[i].y] from sea to island. Return how many island are
there in the matrix after each operator.

 Notice

0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island.
 We only consider up/down/left/right adjacent.

Have you met this question in a real interview? Yes
Example
Given n = 3, m = 3, array of pair A = [(0,0),(0,1),(2,2),(2,1)].

return [1,1,2,2].

Tags
Google Union Find
Related Problems
Medium Connecting Graph 40 %
Medium Surrounded Regions 21 %
Easy Number of Islands 24 %
Medium Find the Weak Connected Component in the Directed Graph


"""


# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param {int} n an integer
    # @param {int} m an integer
    # @param {Pint[]} operators an array of point
    # @return {int[]} an integer array
    def numIslands2(self, n, m, operators):
        # Write your code here






class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        n, m = 3,3
        operators = [(0,0),(0,1),(2,2),(2,1)]
        answer = [1,1,2,2]
        result = self.sol.numIslands2(n, m, operators)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
