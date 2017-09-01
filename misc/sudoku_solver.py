#coding=utf-8

import unittest

"""

37. Sudoku Solver
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.

Difficulty:Hard
Total Accepted:78.1K
Total Submissions:258.1K
Contributor: LeetCode
Subscribe to see which companies asked this question.

Related Topics 
Backtracking Hash Table 
Similar Questions 
Valid Sudoku 
solveSudoku
"""


class Solution(object):
    def solveSudoku(self, board):  # 285ms, 71%
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        row_vals = [{} for _ in range(9)]
        col_vals = [{} for _ in range(9)]
        grid_vals = [[{} for _ in range(3)] for _ in range(3)]
        # init the existing values
        self.record_board_vals(row_vals, col_vals, grid_vals, board)
        # start to dfs
        self.solve(board, 0, 0, row_vals, col_vals, grid_vals)

    def solve(self, board, x, y, row_vals, col_vals, grid_vals):
        # print "Solving : x, y = {}, {}".format(x, y)
        if x == -1 and y == -1:
            return True
        tmp = board[x][y]
        nx, ny = self.get_next(x, y)
        if tmp != ".":
            return self.solve(board, nx, ny, row_vals, col_vals, grid_vals)   # need to add return here, otherwise wrong


        else:    # need to put following part in else, otherwise wrong

            # for ik in range(1,10):  # this is for leetcode input
            #     k = str(ik)
            for k in range(1,10):
            # for k in range(9): #--wrong, should be (1,10)
                if k not in row_vals[x] and k not in col_vals[y] and k not in grid_vals[x / 3][y / 3]:
                    board[x][y] = k
                    row_vals[x][k] = True
                    col_vals[y][k] = True
                    grid_vals[x / 3][y / 3][k] = True
                    if self.solve(board, nx, ny, row_vals, col_vals, grid_vals):
                        return True
                    else:
                        board[x][y] = '.'
                        del row_vals[x][k]
                        del col_vals[y][k]
                        del grid_vals[x / 3][y / 3][k]
            return False

    def get_next(self, x, y):
        if x == 8 and y == 8:
            return -1, -1
        else:
            ny = y+1 if y <8 else 0
            if ny == 0 and y == 8:
                nx = x + 1
            else:
                nx = x
            return nx, ny

    def record_board_vals(self, row_vals, col_vals, grid_vals, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    tmp = board[i][j]
                    row_vals[i][tmp] = True
                    col_vals[j][tmp] = True
                    grid_vals[i / 3][j / 3][tmp] = True


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums1 = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
        nums = [['.' if nums1[i][j] == '.' else int(nums1[i][j]) for j in range(9)] for i in range(9)]
        answer = ["519748632","783652419","426139875","357986241","264317598","198524367","975863124","832491756","641275983"]
        self.sol.solveSudoku(nums)
        self.assertEqual(answer, nums)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
