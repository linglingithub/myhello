#coding=utf-8

"""

289. Game of Life

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by
the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight
 neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.

Follow up:
Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells
first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause
problems when the active area encroaches the border of the array. How would you address these problems?
Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

Subscribe to see which companies asked this question

Hide Tags Array
Hide Similar Problems (M) Set Matrix Zeroes

Medium

"""

import unittest


class Solution(object):
    def gameOfLife(self, board): #42ms, 62%
        """
        use a second bit to store the next status of a cell
        ?? how to deal with boarder cells when there is no 8 neighbors?
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.updateStatus(board, i, j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = (board[i][j] >> 1)

    def updateStatus(self, board, i, j):
        live_nb_cnt = 0
        neighbors = [(-1,-1), (-1,0), (-1,1), (0,-1),(0,1),(1,-1),(1,0),(1,1)]
        for nb in neighbors:
            x = i+nb[0]
            y = j+nb[1]
            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
                continue
            if board[x][y]&1:
                live_nb_cnt += 1
        if ((board[i][j]&1) == 0 and live_nb_cnt == 3) or ((board[i][j]&1) and 2<=live_nb_cnt<=3):
            next_status = 1
        elif (board[i][j]&1) and (live_nb_cnt>3 or live_nb_cnt<2):
            next_status = 0
        else:
            next_status = (board[i][j]&1)
        board[i][j] = ((next_status<<1) | (board[i][j]&1))





    def gameOfLife_ref(self, board): #59ms, 24.68%
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        dx = (1, 1, 1, 0, 0, -1, -1, -1)
        dy = (1, 0, -1, 1, -1, 1, 0, -1)
        for x in range(len(board)):
            for y in range(len(board[0])):
                lives = 0
                for z in range(8):
                    nx, ny = x + dx[z], y + dy[z]
                    lives += self.getCellStatus(board, nx, ny)
                if lives + board[x][y] == 3 or lives == 3:
                    board[x][y] |= 2
        for x in range(len(board)):
            for y in range(len(board[0])):
                board[x][y] >>= 1
    def getCellStatus(self, board, x, y):
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
            return 0
        return board[x][y] & 1



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [[0,1,0],[1,1,1],[0,1,1,]]
        answer = [[1, 1, 1], [1, 0, 0], [1, 0, 1]]
        self.sol.gameOfLife(nums)
        self.assertEqual(answer, nums)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8

"""
这道题的关键在于 in-place，只能开辟常数级别的新空间。因此现有的状态需要包含上个状态的信息，设计中间信息格式以求增加信息量。最后将中间信息
格式解码成正常格式。是一种时间换空间的做法。

因此0，1两种状态不够，我们需要定义更多的状态：


除此之外，我还想特别说一个问题：邻域检测，尤其当不知道邻域元素个数的情况（图像处理中尤其常见）。

我以前比较笨的方法单独处理各种情况：角落元素、边界非角落元素、非边界元素……非常麻烦而且容易错。

正确的处理方法：循环访问，但是循环范围起始点可变。每次计算 minrow~maxrow，mincol~maxcol。注意：请不要计算该元素自身。



"""