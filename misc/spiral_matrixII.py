"""
59. Spiral Matrix II

Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
Subscribe to see which companies asked this question

Hide Tags Array
Hide Similar Problems (M) Spiral Matrix


"""

import unittest


class Solution(object):
    def generateMatrix(self, n): # 39ms 93.75%
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n==0:
            return []
        if n==1:
            return [[1]]
        matrix = [[0] * n for i in range(n)]
        row_cnt = n
        idx = 0
        num = 1
        while row_cnt > 1:
            for i in range(0,row_cnt): # all the four sides, matrix index should consider the starting and ending point
                matrix[idx][idx+i] = num # not matrix[idx][i], same for other 3 sides
                num += 1
            for i in range(1, row_cnt):
                matrix[i+idx][n-idx-1] = num # not matrix[i+idx][row_cnt-idx-1] = num, same for bottom side
                num += 1
            for i in range(row_cnt-2, -1, -1):
                matrix[n-idx-1][i+idx] = num
                num += 1
            for i in range(row_cnt-2, 0, -1):
                matrix[i+idx][idx] = num
                num += 1
            row_cnt -= 2
            idx += 1
        if row_cnt == 1:
            matrix[idx][idx] = num # not matrix[idx][idx] =n here
        return matrix







class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        input = 3
        answer = [
         [ 1, 2, 3 ],
         [ 8, 9, 4 ],
         [ 7, 6, 5 ]
        ]
        result = self.sol.generateMatrix(input)
        self.assertEqual(answer, result)

    def test_case2(self): # =====>
        input = 4
        answer = [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]
        result = self.sol.generateMatrix(input)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8