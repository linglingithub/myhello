#coding=utf-8
"""

73. Set Matrix Zeroes


Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

Subscribe to see which companies asked this question

Hide Tags Array
Hide Similar Problems (M) Game of Life

Medium

"""

import unittest


class Solution(object):
    def setZeroes(self, matrix): #225ms, 10% ~ 175ms, 41% ~ 159ms, 71%
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m, n, flag_row, flag_col = len(matrix), len(matrix[0]), False, False
        for i in range(n):
            if matrix[0][i] == 0:
                flag_row = True
                break
        for i in range(m):
            if matrix[i][0] == 0:
                flag_col = True
                break

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1,m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        for j in range(1,n):
            if matrix[0][j] == 0:
                for i in range(1,m):
                    matrix[i][j] = 0

        if flag_row:
            for i in range(n):
                matrix[0][i] = 0
        if flag_col:
            for j in range(m):
                matrix[j][0] = 0


    def setZeroes_ref(self, matrix): # O(m+n) solution, 146ms, 90%
        # write your code here
        if len(matrix)==0:
            return
        rownum = len(matrix)
        colnum = len(matrix[0])
        row = [False for i in range(rownum)]
        col = [False for i in range(colnum)]
        for i in range(rownum):
            for j in range(colnum):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True
        for i in range(rownum):
            for j in range(colnum):
                if row[i] or col[j]:
                    matrix[i][j] = 0





class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [[1,0,2],[2,3,4]]
        answer = [[0,0,0],[2,0,4]]
        self.sol.setZeroes(nums)
        self.assertEqual(answer, nums)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()


"""
非常无聊的一道题。解题点就在于清空标志位存在哪里的问题。可以创建O(m+n)的数组来存储，但此题是希望复用已有资源。这里可以选择第一行和第一列来
存储标志位。

1.先确定第一行和第一列是否需要清零
2.扫描剩下的矩阵元素，如果遇到了0，就将对应的第一行和第一列上的元素赋值为0
3.根据第一行和第一列的信息，已经可以讲剩下的矩阵元素赋值为结果所需的值了
4.根据1中确定的状态，处理第一行和第一列。

"""


#-*- coding:utf-8 -*-
#coding=utf-8