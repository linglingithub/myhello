"""
79. Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally
or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
Subscribe to see which companies asked this question

Hide Tags Array Backtracking
Hide Similar Problems (H) Word Search II

Medium

"""

import unittest


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]:
            return False
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(board, word, i, j, 0):
                    return True
        return False

    def dfs(self, board, word, x, y, idx):
        res = False
        if idx == len(word):
            return True
        delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        if board[x][y] == word[idx]:
            if idx == len(word) - 1:  # add this check so [["a"]], "a" case is good
                return True
            tmp = board[x][y]
            board[x][y] = '.'
            for dx, dy in delta:

                nx, ny = x + dx, y + dy
                # print("nx, ny: ", x, y, nx, ny)
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] != '.':  # not system design
                    res = self.dfs(board, word, nx, ny, idx + 1)
                    if res:
                        break
            board[x][y] = tmp
        return res

class Solution1(object):
    def exist(self, board, word):  #315ms, 79%, use matrix as mask to save time, use
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def find_word(i, j, idx):
            if idx==len(word):
                return True
            if i < 0 or i >= m or j<0 or j>=n or used[i][j]:
                return False
            if board[i][j] == word[idx]:
                used[i][j] = True
                if find_word(i-1,j, idx+1) or find_word(i+1,j, idx+1) or find_word(i, j-1, idx+1) or find_word(i, j+1, idx+1):
                    return True
                # else:
                used[i][j] = False
            return False

        if board is None or len(board) == 0 or len(board[0]) == 0:
            return False
        if word is None or len(word) == 0:
            return True
        m, n = len(board), len(board[0])
        used = [ [False for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if find_word(i,j,0):
                    return True
        return False







    def exist_dict_slower(self, board, word): #435ms, 36%
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if board is None or len(board) == 0 or len(board[0]) == 0:
            return False
        if word is None or len(word) == 0:
            return True
        used = {}

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    tmp = self.make_key(i,j)
                    used[tmp] = 1
                    # remember to remove the used position when backtracking, otherwise wrong for case 5
                    if self.match_word(board, i, j, word, 1, used):
                        return True
                    else:
                        del used[tmp]
        return False

    def make_key(self, i, j):
        return str(i)+','+str(j)

    def match_word(self, board, i, j, word, idx, used): #remember to track the used position
        # remember to remove the used position when backtracking, otherwise wrong for case 5
        if idx == len(word):
            return True
        # top
        tmp = self.make_key(i-1, j)
        if i - 1 >= 0 and tmp not in used:
            if board[i - 1][j] == word[idx]:
                used[tmp] = 1
                if self.match_word(board, i - 1, j, word, idx + 1, used):
                    return True
                else:
                    del used[tmp]
        # bottom
        tmp = self.make_key(i+1, j)
        if i + 1 <= len(board) - 1 and tmp not in used:
            if board[i + 1][j] == word[idx]:
                used[tmp] = 1
                if self.match_word(board, i + 1, j, word, idx + 1, used):
                    return True
                else:
                    del used[tmp]
        # left
        tmp = self.make_key(i, j-1)
        if j - 1 >= 0 and tmp not in used:
            if board[i][j-1] == word[idx]:
                used[tmp] = 1
                if self.match_word(board, i, j - 1, word, idx + 1, used):
                    return True
                else:
                    del used[tmp]
        # right
        tmp = self.make_key(i, j+1)
        if j + 1 <= len(board[0]) - 1 and tmp not in used:
            if board[i][j + 1] == word[idx]:
                used[tmp] = 1
                if self.match_word(board, i, j + 1, word, idx + 1, used):
                    return True
                else:
                    del used[tmp]
        return False


    def match_word_wrong(self, board, i, j, word, idx): # NOTE!!! Only 4 neighbors to check.
        if idx==len(word):
            return True
        #top
        if i-1>=0:
            if j-1>=0:
                if board[i-1][j-1]==word[idx]:
                    self.match_word(board, i-1,j-1, word, idx+1)
            if board[i-1][j]==word[idx]:
                self.match_word(board, i-1,j, word, idx+1)
            if j+1 <= len(board[0])-1:
                if board[i-1][j+1]==word[idx]:
                    self.match_word(board,i-1,j+1, word, idx+1)
        #bottom
        if i+1 <= len(board)-1:
            if j-1>=0:
                if board[i+1][j-1]==word[idx]:
                    self.match_word(board, i+1,j-1, word,idx+1)
            if board[i+1][j]==word[idx]:
                self.match_word(board, i+1,j, word,idx+1)
            if j+1 <= len(board[0])-1:
                if board[i+1][j+1]==word[idx]:
                    self.match_word(board,i+1,j+1, word, idx+1)
        # left and right
        if j-1>=0:
            if board[i][j-1]==word[idx]:
                self.match_word(board, i, j-1, word, idx+1)
        if j+1 <= len(board[0])-1:
            if board[i][j+1]==word[idx]:
                self.match_word(board, i, j+1, word, idx+1)
        return False




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case5(self): #=======>
        board = ["CAA","AAA","BCD"]
        word = "AAB"
        answer = True
        result = self.sol.exist(board, word)
        self.assertEqual(answer, result)

    def test_case1(self):
        board = [
          ['A','B','C','E'],
          ['S','F','C','S'],
          ['A','D','E','E']
        ]
        word = 'ABCCED'
        answer = True
        result = self.sol.exist(board, word)
        self.assertEqual(answer, result)

    def test_case2(self):
        board = [
          ['A','B','C','E'],
          ['S','F','C','S'],
          ['A','D','E','E']
        ]
        word = 'SEE'
        answer = True
        result = self.sol.exist(board, word)
        self.assertEqual(answer, result)

    def test_case3(self):
        board = [
          ['A','B','C','E'],
          ['S','F','C','S'],
          ['A','D','E','E']
        ]
        word = 'ABCB'
        answer = False
        result = self.sol.exist(board, word)
        self.assertEqual(answer, result)

    def test_case4(self):
        board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]
        word = 'ASZ'
        answer = False
        result = self.sol.exist(board, word)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""
public boolean exist(char[][] board, String word) {
    char[] w = word.toCharArray();
    for (int y=0; y<board.length; y++) {
    	for (int x=0; x<board[y].length; x++) {
    		if (exist(board, y, x, w, 0)) return true;
    	}
    }
    return false;
}

private boolean exist(char[][] board, int y, int x, char[] word, int i) {
	if (i == word.length) return true;
	if (y<0 || x<0 || y == board.length || x == board[y].length) return false;
	if (board[y][x] != word[i]) return false;
	board[y][x] ^= 256;
	boolean exist = exist(board, y, x+1, word, i+1)
		|| exist(board, y, x-1, word, i+1)
		|| exist(board, y+1, x, word, i+1)
		|| exist(board, y-1, x, word, i+1);
	board[y][x] ^= 256;
	return exist;
}

"""

#-*- coding:utf-8 -*-
#coding=utf-8