"""
Valid Sudoku

Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

Subscribe to see which companies asked this question

Hide Tags Hash Table
Hide Similar Problems (H) Sudoku Solver


"""

import unittest
import re
import collections



class Solution(object):
    """
    a 9 * 9 grid board. valid if :
     each [ row / column / subbox(3*3) ] has 1-9 once not repeatedly

    """

    def isValidSudoku_ref5(self, board): # 106ms, 43.96%
        def isValid(x, y, tmp):
            for i in range(9):
                if board[i][y]==tmp:return False
            for i in range(9):
                if board[x][i]==tmp:return False
            for i in range(3):
                for j in range(3):
                    if board[(x/3)*3+i][(y/3)*3+j]==tmp: return False
            return True
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':continue
                tmp=board[i][j]
                board[i][j]='D'
                if isValid(i,j,tmp)==False: return False
                else:
                    board[i][j]=tmp
        return True

    def isValidSudoku(self, board): #99ms, 55%
        return 1 == max(collections.Counter(
            x for i, row in enumerate(board)
            for j, c in enumerate(row)
            if c != '.'
            for x in ((c, i), (j, c), (i / 3, j / 3, c))
        ).values() + [1])

    def isValidSudoku_ref3(self, board): # 85ms, 79.3%
        seen = sum(([(c, i), (j, c), (i / 3, j / 3, c)]
                    for i, row in enumerate(board)
                    for j, c in enumerate(row)
                    if c != '.'), [])
        return len(seen) == len(set(seen))

    def isValidSudoku_ref2(self, board): #69ms, 97.07%
        seen = set()
        return not any(x in seen or seen.add(x)
                       for i, row in enumerate(board)
                       for j, c in enumerate(row)
                       if c != '.'
                       for x in ((c, i), (j, c), (i / 3, j / 3, c)))

    def isValidSudoku_ref(self, board): # a very smart and fast way, 68ms, 97.62%
        seen = sum(([(c, i), (j, c), (i / 3, j / 3, c)]
                    for i in range(9) for j in range(9)
                    for c in [board[i][j]] if c != '.'), [])
        return len(seen) == len(set(seen))

    def isValidSudoku_self(self, board): # code simpler, encode as digit faster !! 106ms, 43.96%
        """
        try to think of a way to encode the row, column and subgrid postion of each one
        since every position is single digit, try to just encode as
        :type board: List[List[str]]
        :rtype: bool
        """
        pos = {}
        for i in range(9):
            for j in range(9):
                tmp = board[i][j]
                if tmp == '.':
                    continue
                if not re.match('[1-9]',tmp):
                    return False
                tmp = int(tmp)
                row = i*10+tmp
                col = (j+1)*100+tmp
                grid = (i/3+1)*1000 + (j/3)*100 + tmp
                if row in pos or col in pos or grid in pos:
                    return False
                else:
                    pos[row] = 1
                    pos[col] = 1
                    pos[grid] = 1
        return True


    def isValidSudoku_encode_str(self, board): # code simpler, but much slower, 182ms, 7.87%
        """
        try to think of a way to encode the row, column and subgrid postion of each one
        :type board: List[List[str]]
        :rtype: bool
        """
        pos = {}
        for i in range(9):
            for j in range(9):
                tmp = board[i][j]
                if tmp == '.':
                    continue
                if not re.match('[1-9]',tmp):
                    return False
                row = "({}){}".format(i, tmp)
                col = "{}({})".format(tmp, j)
                grid = "({})({}){}".format(i/3, j/3, tmp)
                if row in pos or col in pos or grid in pos:
                    return False
                else:
                    pos[row] = 1
                    pos[col] = 1
                    pos[grid] = 1
        return True




    def isValidSudoku_ac_butnotgoodengou(self, board): # 109ms, 40.29%
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        result = True
        for i in range(9):
            row = {}
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if int(board[i][j]) not in range(1, 10): # case 1 and 2, need to transform to int
                    return False
                if board[i][j] in row:
                    return False
                else:
                    row[board[i][j]] = 1

        for j in range(9):
            col = {}
            for i in range(9):
                if board[i][j] == '.':
                    continue
                if int(board[i][j]) not in range(1, 10):
                    return False
                if board[i][j] in col:
                    return False
                else:
                    col[board[i][j]] = 1

        for row_base in range(3):
            for col_base in range(3):
                grid = {}
                for i in range(3):
                    for j in range(3):
                        if board[row_base*3+i][col_base*3+j]==".": # forgot to * 3, case 3
                            continue
                        if int(board[row_base*3+i][col_base*3+j]) not in range(1, 10):
                            return False
                        if board[row_base*3+i][col_base*3+j] in grid:
                            return False
                        else:
                            grid[board[row_base*3+i][col_base*3+j]] = 1
        return result







class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        board = [".........","......3..","...18....","...7.....","....1.97.",".........","...36.1..",".........",".......2."]
        answer = True
        result = self.sol.isValidSudoku(board)
        self.assertEqual(answer, result)

    def test_case2(self):
        board = [".87654321", "2........", "3........", "4........", "5........", "6........", "7........", "8........",
         "9........"]
        answer = True
        result = self.sol.isValidSudoku(board)
        self.assertEqual(answer, result)

    def test_case3(self):
        board = [".........","......3..","...18....","...7.....","....1.97.",".........","...36.1..",".........",".......2."]
        answer = True
        result = self.sol.isValidSudoku(board)
        self.assertEqual(answer, result)




def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()