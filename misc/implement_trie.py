#coding=utf-8

import unittest

"""
208. Implement Trie

 Description
 Notes
 Testcase
 Judge
Implement a trie with insert, search, and startsWith methods.

 Notice

You may assume that all inputs are consist of lowercase letters a-z.

Have you met this question in a real interview? Yes
Example
insert("lintcode")
search("code")
>>> false
startsWith("lint")
>>> true
startsWith("linterror")
>>> false
insert("linterror")
search("lintcode)
>>> true
startsWith("linterror")
>>> true

Tags
Trie Facebook Uber Google
Related Problems
Hard K Edit Distance 21 %
Medium Trie Service 39 %
Hard Trie Serialization 35 %
Medium Add and Search Word

"""



"""
Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("lintcode")
trie.search("lint") will return false
trie.startsWith("lint") will return true
"""


class TrieNode: # done.  TLE with 90% test cases passed if use ordereddict
    def __init__(self):
        # Initialize your data structure here.
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        if not word:
            return
        current = self.root
        for letter in word:
            if letter in current.children:
                pass
            else:
                current.children[letter] = TrieNode()
            current = current.children[letter]
        current.is_word = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        current = self.root
        for letter in word:
            if letter in current.children:
                current = current.children[letter]
            else:
                return False
        return current.is_word

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        current = self.root
        for letter in prefix:
            if letter in current.children:
                current = current.children[letter]
            else:
                return False
        return True


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Trie()

    def test_case1(self):
        result = []
        self.sol.insert("lintcode")
        result.append(self.sol.search("code"))
        result.append(self.sol.startsWith("lint"))
        result.append(self.sol.startsWith("linterror"))
        self.sol.insert("linterror")
        result.append(self.sol.search("lintcode"))
        result.append(self.sol.startsWith("linterror"))
        answer = [False, True, False, True, True]

        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
