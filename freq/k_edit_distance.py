#coding=utf-8

import unittest

"""
K Edit Distance

Given a set of strings which just has lower case letters and a target string, output all the strings for each the edit 
distance with the target no greater than k.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Have you met this question in a real interview? Yes
Example
Given words = ["abc", "abd", "abcd", "adc"] and target = "ac", k = 1
Return ["abc", "adc"]

Tags 
Airbnb Trie Google
Related Problems 
Hard Boggle Game 20 %
Hard Word Squares 47 %
Medium Add and Search Word 22 %
Medium Implement Trie 31 %
Medium Edit Distance


Hard

"""


class Solution:
    # @param {string[]} words a set of strings
    # @param {string} target a target string
    # @param {int} k an integer
    # @return {string[]} output all the stirngs that meet the requirements
    def kDistance(self, words, target, k):
        #if not words or not target:    # wrong for case 3, when target is ""
        if not words:
            return []
        trie = TrieNode()
        for word in words:
            TrieNode.add_word(trie, word)
        n = len(target)
        dp = [i for i in range(n + 1)]
        res = []
        self.check_edit_distance(trie, target, k, res, dp)
        return res

    def check_edit_distance(self, node, target, k, res, dp):
        if node.is_word and dp[len(target)] <= k:
            res.append(node.word)
        for char, child in node.children.items():
            next_dp = [x for x in dp]   # here can be 0 for _ in range, no need to copy dp
            next_dp[0] = dp[0] + 1    # !!!! important, otherwise wrong, case 4
            for j in range(1, len(target)+1):
                if char == target[j-1]:
                    next_dp[j] = dp[j-1]
                else:
                    next_dp[j] = min(dp[j-1], dp[j], next_dp[j-1]) + 1
            self.check_edit_distance(child, target, k, res, next_dp)


class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = ""

    @classmethod
    def add_word(cls, root, word):
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
        node.word = word



class Solution1:
    # @param {string[]} words a set of strings
    # @param {string} target a target string
    # @param {int} k an integer
    # @return {string[]} output all the stirngs that meet the requirements
    def kDistance(self, words, target, k):
        # Write your code here
        trie_root = TrieNode()
        for word in words:
            TrieNode.add_word(trie_root, word)
        result = []
        self.n = len(target)
        dp = [i for i in range(self.n + 1)]
        self.find(trie_root, target, k, dp, result)
        return result

    def find(self, trie_node, target, k, dp, result):
        """
        Usuall edit distance dp[][] is calced with i, j iterations.
        Now with Trie, i loop is run on DFS of a trie tree.
        and the i-th row [] is now actually associated with each trie node.
        
        :param trie_node: 
        :param target: 
        :param k: 
        :param dp: 
        :param result: 
        :return: 
        """

        if trie_node.is_word and dp[self.n] <= k:
            result.append(trie_node.str)
        node_ed = [0 for _ in range(self.n+1)]
        node_ed[0] = dp[0] + 1
        for char, child in trie_node.children.items():
            for j in range(1, self.n+1):
                if char == target[j-1]:
                    node_ed[j] = dp[j-1]
                else:
                    node_ed[j] = min(dp[j-1], dp[j], node_ed[j-1]) + 1
            self.find(child, target, k, node_ed, result)


class TrieNode1(object):
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.str = None

    @classmethod
    def add_word(cls, root, word):
        # if not word:
        #     return
        # should not exclude empty word here, see case 2
        current = root
        for char in word:
            if char not in current.children:
                child = TrieNode()
                current.children[char] = child
            current = current.children.get(char)
        current.is_word = True
        current.str = word



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case4(self):   #===>
        words = ["abc","abd","abcd","adc","mart","ka","rma","kaarmmaa","km","kpm","kmp","pmaa"]
        target = "karma"
        k = 3
        answer = ["ka","kaarmmaa","km","kmp","kpm","mart","rma"]
        result = self.sol.kDistance(words, target, k)
        self.assertEqual(sorted(answer), sorted(result))

    def test_case3(self):
        words = ["a","b","ab","cd","abc","defg"]
        target = ""
        k = 2
        answer =["a","ab","b","cd"]
        result = self.sol.kDistance(words, target, k)
        self.assertEqual(sorted(answer), sorted(result))

    def test_case2(self):
        words = ["a","b","ba","babbab", ""]
        target = ""
        k = 5
        answer = ["","a","b","ba"]   # wrong output was ["a","b","ba"]
        result = self.sol.kDistance(words, target, k)
        self.assertEqual(sorted(answer), sorted(result))


    def test_case1(self):
        words = ["abc", "abd", "abcd", "adc"]
        target = "ac"
        k = 1
        answer = ["abc", "adc"]
        result = self.sol.kDistance(words, target, k)
        self.assertEqual(sorted(answer), sorted(result))


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""

Naive Solution:
A naive solution would be, for each word in the list, calculate the edit distance with the target word. If it is equal 
or less than k, output to the result list. If we assume that the average length of the words is m, and the total number
 of words in the list is n, the total time complexity is O(n * m^2).

Trie tree:
The problem with the previous solution is if the given list of the words is like ab, abc, abcd, each time we need to 
repeatedly calculate the edit distance with the target word. If we can combine the prefix of all words together, we can 
save lots of time.




https://www.jiuzhang.com/solutions/k-edit-distance/

Q: 请问K Edit Distance问题python答案中的dp数组和next数组的含义是什么？
A: 
dp[i]是当前结点对应的单词到target第i位第最小花费
find与dp一个含义，接下来的查找如果还用dp，那么会对上一层有影响，所以需要另一个数组

Q: 想知道这道题按solution解法，时间复杂度是什么。
建立Trie Tree时间复杂度是O(nL)
但是find函数的时间复杂度不太清楚怎么分析？老师可以解答一下吗？
A: 刘助教
target的长度是n，words中最长的长度是m
每个结点内都花费了O(n)的时间，结点最多26 ^ m
所以时间复杂度是O(n * 26 ^ m)


class TrieNode:
    def __init__(self):
        # Initialize your data structure here.
        self.children = [None for i in xrange(26)]
        self.hasWord = False
        self.str = None
    
    @classmethod
    def addWord(cls, root, word):
        node = root
        for letter in word:
            child = node.children[ord(letter) - ord('a')]
            if child is None:
                child = TrieNode()
                node.children[ord(letter) - ord('a')] = child
            node = child
    
        node.hasWord = True
        node.str = word

class Solution:
    # @param {string[]} words a set of strings
    # @param {string} target a target string
    # @param {int} k an integer
    # @return {string[]} output all the stirngs that meet the requirements 
    def kDistance(self, words, target, k):
        # Write your code here
        root = TrieNode()
        for word in words:
            TrieNode.addWord(root, word)

        result = []
        n = len(target)
        dp = [i for i in xrange(n + 1)]

        self.find(root, result, k, target, dp)
        return result

    def find(self, node, result, k, target, dp):
        n = len(target)

        if node.hasWord and dp[n] <= k:
            result.append(node.str)

        next = [0 for i in xrange(n + 1)]

        for i in xrange(26):
            if node.children[i] is not None:
                next[0] = dp[0] + 1
                for j in xrange(1, n + 1):
                    if ord(target[j - 1]) - ord('a') == i:
                        next[j] = min(dp[j - 1], min(next[j - 1] + 1, dp[j] + 1))
                    else:
                        next[j] = min(dp[j - 1] + 1, min(next[j - 1] + 1, dp[j] + 1))

                self.find(node.children[i], result, k, target, next)
 


"""