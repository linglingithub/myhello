#coding=utf-8

import unittest

"""
211. Add and Search Word - Data structure design

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or '.' .
A '.' means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.

click to show hint.

You should be familiar with how a Trie works. If not, please work on this problem: Implement Trie (Prefix Tree) first.
Subscribe to see which companies asked this question.

Hide Tags Backtracking Trie Design
Hide Similar Problems (M) Implement Trie (Prefix Tree)

Medium

"""


class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        if not word:
            return
        node = self._root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children.get(char)
        node.is_word = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self._dfs(word, 0, self._root)

    def _dfs(self, word, idx, node):
        """
        Recursively search for the target word in trie tree
        """
        if not node:
            return False
        if idx >= len(word):
            return node.is_word
        char = word[idx]
        if char != '.':
            return self._dfs(word, idx + 1, node.children.get(char))
        else:
            for xchar in node.children.keys():
                if self._dfs(word, idx + 1, node.children.get(xchar)):
                    return True
        return False


class TrieNode:
    def __init__(self):
        """
        Initialize the trienode here.
        """
        self.children = {}
        self.is_word = False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


class WordDictionary1(object): #59%

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for l in word:
            if l not in cur.children:
                cur.children[l] = TrieNode()
            cur = cur.children[l]
        cur.is_word = True


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one
        letter.
        :type word: str
        :rtype: bool
        """
        return self.search_helper(self.root, word, 0)


    def search_helper(self, node, word, idx):
        if idx >= len(word):
            return node.is_word
        letter = word[idx]
        if letter in node.children:
            return self.search_helper(node.children[letter], word, idx+1)
        elif letter == ".":
            for child in node.children.values(): #remember to add values() here
                if self.search_helper(child, word, idx+1):
                    return True
            return False # remember to return false here!!! otherwise will return None for some case
        else:
            return False


class TrieNode1(object):
    def __init__(self):
        self.children = {}
        self.is_word = False



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = WordDictionary()

    def test_case1(self):
        result = []
        self.sol.addWord("bad")
        self.sol.addWord("dad")
        self.sol.addWord("mad")
        result.append(self.sol.search("pad"))
        result.append(self.sol.search("bad"))
        result.append(self.sol.search(".ad"))
        result.append(self.sol.search("b.."))
        answer = [False, True, True, True]

        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
