"""
212. Word Search II

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally
or vertically neighboring. The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Return ["eat","oath"].
Note:
You may assume that all inputs are consist of lowercase letters a-z.

click to show hint.

You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?

If the current candidate does not exist in all words' prefix, you could stop backtracking immediately. What kind of
data structure could answer such query efficiently? Does a hash table work? Why or why not? How about a Trie?
If you would like to learn how to implement a basic trie, please work on this problem: Implement Trie (Prefix Tree)
first.



Subscribe to see which companies asked this question.

Hide Tags Backtracking Trie
Hide Similar Problems (M) Word Search

Hard

"""

import unittest

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.new_word = True  # add this for case4, duplicated results


class TrieTree(object):
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode()
            cur = cur.children.get(letter)
        cur.is_word = True


    # def check_word(self, root, letter):
    #     return root.children.get(letter, None)
    #
    #
    # def is_word(self, word):
    #     cur = self.root
    #     for letter in word:
    #         if letter in cur.children:
    #             cur = cur.children.get(letter)
    #         else:
    #             return False
    #     return cur.is_word
    #
    # def is_prefix(self, word):
    #     cur = self.root
    #     for letter in word:
    #         if letter in cur.children:
    #             cur = cur.children.get(letter)
    #         else:
    #             return False
    #     return True



class Solution(object): #722ms, 28% --> TLE (once) --> 24% --> 22%, 35%, 29%, 27%
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not board[0] or not words:
            return []
        self.dict = TrieTree()
        for word in words:
            self.dict.add_word(word)

        result = []
        self.visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[i])):
                #print "Debug -- ", i, j
                self.search(i, j, board, "", self.dict.root, result)
        return result

    def search(self, x, y, board, chars, parent, result):
        # if node.is_word:  #can't check here, may get duplicated appends
        #     result.append(chars)

        newchar = board[x][y]
        # if newchar == '0': #case 3 format does not support this way
        #     return
        # board[x][y] = '0'


        node = parent.children.get(newchar, None)
        if not node:
            return
        if node.is_word:
            if node.new_word:
                result.append(chars+newchar)
                node.new_word = False    # add this for case4, duplicated results

        self.visited[x][y] = True
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and not self.visited[nx][ny]:
                self.search(nx, ny, board, chars+newchar, node, result)
        # board[x][y] = newchar
        self.visited[x][y] = False






class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()


    def test_case1(self):
        board = [
          ['o','a','a','n'],
          ['e','t','a','e'],
          ['i','h','k','r'],
          ['i','f','l','v']
        ]
        words = ["oath","pea","eat","rain"]
        answer = ["eat","oath"]
        result = self.sol.findWords(board, words)
        self.assertEqual(sorted(answer), sorted(result))

    def test_case2(self):  # self designed, think about 'oat' and 'oath', can not return after first is_word found
        board = [
          ['o','a','a','n'],
          ['e','t','a','e'],
          ['i','h','k','r'],
          ['i','f','l','v']
        ]
        words = ["oat", "oath","pea","eat","rain"]
        answer = ["eat","oath", "oat"]
        result = self.sol.findWords(board, words)
        self.assertEqual(sorted(answer), sorted(result))


    def test_case3(self): #=====>
        board = [
            "oaan",
            "etae",
            "ihkr",
            "iflv"
        ]
        words = ["oath","pea","eat","rain"]
        answer = ["eat","oath"]
        result = self.sol.findWords(board, words)
        self.assertEqual(sorted(answer), sorted(result))

    def test_case4(self): #=====>
        board = [
            "aa"
        ]
        words = ["a"]
        answer = ["a"]
        result = self.sol.findWords(board, words)
        self.assertEqual(sorted(answer), sorted(result))

    def test_case5(self): #=====>
        board = [
            "aa"
        ]
        words = ["a"]
        answer = ["a"]
        result = self.sol.findWords(board, words)
        self.assertEqual(sorted(answer), sorted(result))


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8

"""

#27ms, 67%

public class Solution {
public List<String> findWords(char[][] board, String[] words) {
    List<String> res = new ArrayList<>();
    TrieNode root = buildTrie(words);
    for (int i = 0; i < board.length; i++) {
        for (int j = 0; j < board[0].length; j++) {
            dfs (board, i, j, root, res);
        }
    }
    return res;
}

public void dfs(char[][] board, int i, int j, TrieNode p, List<String> res) {
    char c = board[i][j];
    if (c == '#' || p.next[c - 'a'] == null) return;
    p = p.next[c - 'a'];
    if (p.word != null) {   // found one
        res.add(p.word);
        p.word = null;     // de-duplicate
    }

    board[i][j] = '#';
    if (i > 0) dfs(board, i - 1, j ,p, res);
    if (j > 0) dfs(board, i, j - 1, p, res);
    if (i < board.length - 1) dfs(board, i + 1, j, p, res);
    if (j < board[0].length - 1) dfs(board, i, j + 1, p, res);
    board[i][j] = c;
}

public TrieNode buildTrie(String[] words) {
    TrieNode root = new TrieNode();
    for (String w : words) {
        TrieNode p = root;
        for (char c : w.toCharArray()) {
            int i = c - 'a';
            if (p.next[i] == null) p.next[i] = new TrieNode();
            p = p.next[i];
       }
       p.word = w;
    }
    return root;
}

class TrieNode {
    TrieNode[] next = new TrieNode[26];
    String word;
}
}


======================================================================================================
simple and elegant

 StefanPochmann
Reputation:  14,598
I first build the tree of words with root root and also represent the board a different way, namely as one-dimensional
dictionary where the keys are complex numbers representing the row/column indexes. That makes further work with it
easier. Looping over all board positions is just for z in board, the four neighbors of a board position z are just
z + 1j**k (for k in 0 to 3), and I don't need to check borders because board.get just returns "None" if I request an
invalid position.

After this preparation, I just take the tree and recursively dive with it into each board position. Similar to how you'd
 search a single word, but with the tree instead.


class Solution(object):  # 58%, 609ms
    def findWords(self, board, words):
        root = {}
        for word in words:
            node = root
            for c in word:
                node = node.setdefault(c, {})
            node[None] = True
        board = {i + 1j*j: c
                 for i, row in enumerate(board)
                 for j, c in enumerate(row)}

        found = []
        def search(node, z, word):
            if node.pop(None, None):
                found.append(word)
            c = board.get(z)
            if c in node:
                board[z] = None
                for k in range(4):
                    search(node[c], z + 1j**k, word + c)
                board[z] = c
        for z in board:
            search(root, z, '')

        return found

"""

