#coding=utf-8

import unittest

"""
773. Sliding Puzzle

DescriptionHintsSubmissionsDiscussSolution
On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given a puzzle board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

Examples:

Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.
Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.
Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]
Input: board = [[3,2,4],[1,5,0]]
Output: 14
Note:

board will be a 2 x 3 array as described above.
board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].


"""


class Solution:
    TARGET = "123450"
    # 4 neighbor directions
    DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    ROWS = 2
    COLS = 3

    def slidingPuzzle(self, board):
        """
        Basic idea: use BFS to find the min steps of move. If not possible, return -1.
        every state of the move will be recorded as a string key in the queue,
        the state is expanded by moving 0 to 4 neighboring place ( swap with 4 neighbors )
        and check
        1. if the target state --> yes, return the current steps
        2. if visited --> no, put to queue for next

        if queue is empty and not target reached, return -1

        Assumption: input if valid. Since board is 2 * 3, numbers will be only 0 - 5, single digit

        :type board: List[List[int]]
        :rtype: int
        """
        from collections import deque
        queue = deque()
        result = 0

        first_key = self.to_key(board)
        if first_key == Solution.TARGET:
            return result
        queue.append(first_key)
        visited = set()
        visited.add(first_key)

        while queue:
            # increase the move count
            result += 1
            level_size = len(queue)
            for i in range(level_size):
                cur_key = queue.popleft()
                for j in range(len(Solution.DIRS)):
                    next_key = self.move_dir(cur_key, Solution.DIRS[j])
                    # invalid swap
                    if next_key == "":
                        continue
                    # hit target
                    if next_key == Solution.TARGET:
                        return result
                    if next_key in visited:
                        continue
                    else:
                        visited.add(next_key)
                        queue.append(next_key)
        # when no target is reached and queue is empty
        return -1

    def to_key(self, board):
        return "".join(["".join(str(board[i][j]) for j in range(len(board[i]))) for i in range(len(board))])

    def to_board(self, key):
        board = []
        zero_row = -1
        zero_col = -1
        for i in range(Solution.ROWS):
            board.append([])
            for j in range(Solution.COLS):
                cur = int(key[i * Solution.COLS + j])
                board[i].append(cur)
                if cur == 0:
                    zero_row = i
                    zero_col = j
        return board, zero_row, zero_col

    def move_dir(self, cur_key, direction):
        # get board situation and 0 row and col
        board, row, col = self.to_board(cur_key)
        nrow, ncol = row + direction[0], col + direction[1]
        if not (0 <= nrow < len(board) and 0 <= ncol < len(board[0])):
            return ""
        # swap 0 with neighbor
        board[row][col], board[nrow][ncol] = board[nrow][ncol], board[row][col]
        # return the key of new state
        return self.to_key(board)

class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [[1,2,3],[4,0,5]]
        answer = 1
        result = self.sol.slidingPuzzle(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [[1,2,3],[5,4,0]]
        answer = -1
        result = self.sol.slidingPuzzle(nums)
        self.assertEqual(answer, result)

    def test_case3(self):
        nums = [[4,1,2],[5,0,3]]
        answer = 5
        result = self.sol.slidingPuzzle(nums)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
