"""
54. Spiral Matrix

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].

Subscribe to see which companies asked this question

Hide Tags Array
Hide Similar Problems (M) Spiral Matrix II


"""


import math
import unittest



class Solution(object):
    def spiralOrder(self, matrix): #33ms, 98%
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        def get_one_round(idx):
            row_cnt = len(matrix)-2*(idx)
            col_cnt = len(matrix[0])-2*(idx)
            if row_cnt < 1 or col_cnt < 1:
                return []
            if row_cnt == 1:  # need to special deal with single column and single row
                return matrix[idx][idx:idx+col_cnt]
            if col_cnt == 1:
                return [matrix[idx+j][idx] for j in range(row_cnt)]
            tmp = []
            for j in range(col_cnt):
                tmp.append(matrix[idx][idx+j])
            for i in range(1, row_cnt):   # for the right, bottom, remember to avoid the first elements already added
                tmp.append(matrix[idx+i][idx+col_cnt-1]) # don't forget IDX+i, otherwise wrong index.
            for j in range(col_cnt-2,-1, -1):
                tmp.append(matrix[idx+row_cnt-1][idx+j])
            for i in range(row_cnt-2, 0, -1): # for the left edge, remember to avoid the FIRST and LAST elements
                tmp.append(matrix[idx+i][idx])
            return tmp

        if matrix is None or len(matrix) == 0:
            return []
        result = []
        for i in range(int(math.ceil(len(matrix)))):
            result += get_one_round(i)
        return result




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        input = [
         [ 1, 2, 3 ],
         [ 4, 5, 6 ],
         [ 7, 8, 9 ]
        ]
        answer = [1,2,3,6,9,8,7,4,5]
        result = self.sol.spiralOrder(input)
        self.assertEqual(answer, result)

    def test_case2(self): # =====>
        input = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
        answer = [1, 2, 3, 4, 5, 6,7,8,9,10]
        result = self.sol.spiralOrder(input)
        self.assertEqual(answer, result)

    def test_case3(self):  # =====>
        input = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
        answer = [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]
        result = self.sol.spiralOrder(input)
        self.assertEqual(answer, result)




def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8