#coding=utf-8

import unittest

"""

Build Post Office

Given a 2D grid, each cell is either an house 1 or empty 0 (the number zero, one), find the place to build a post 
office, the distance that post office to all the house sum is smallest. Return the smallest distance. Return -1 if it is
 not possible.

 Notice

You can pass through house and empty.
You only build post office on an empty.
Have you met this question in a real interview? Yes
Example
Given a grid:

0 1 0 0
1 0 1 1
0 1 0 0
return 6. (Placing a post office at (1,1), the distance that post office to all the house sum is smallest.)

Tags 
Binary Search Sort
Related Problems 
Hard Build Post Office II

Hard

"""


class Solution:
    # @param {int[][]} grid a 2D grid
    # @return {int} an integer
    def shortestDistance(self, grid):
        # Write your code here
        




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [
            [0, 1, 0, 0],
            [1, 0, 1, 1],
            [0, 1, 0, 0]
        ]
        answer = 6  # [1, 1]
        result = self.sol.shortestDistance(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
