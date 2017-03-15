#coding=utf-8
"""

126. Word Ladder II

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from
beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
UPDATE (2017/1/20):
The wordList parameter had been changed to a list of strings (instead of a set of strings). Please reload the code
definition to get the latest changes.

Subscribe to see which companies asked this question.

Hide Tags Array Backtracking Breadth-first Search String

Hard

"""

import unittest


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList): #ref, leetcode has problem with this problem
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        results = []

        from collections import defaultdict, deque
        queue = deque([[beginWord, 1]])
        visited = set([beginWord])
        neighbors = defaultdict(list)
        for word in wordList:
            for x in range(len(word)):
                token = word[:x] + '_' + word[x+1:]
                neighbors[token] += word,
        while queue:
            word, length = queue.popleft()
            if self.wordDist(word, endWord) <= 1:
                return length + 1
            for x in range(len(word)):
                token = word[:x] + '_' + word[x+1:]
                for ladder in neighbors[token]:
                    if ladder not in visited:
                        visited.add(ladder)
                        queue += [ladder, length + 1],
        return results

    def wordDist(self, wordA, wordB):
        return sum([wordA[x] != wordB[x] for x in range(len(wordA))])


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        a = 'hit'
        b = 'cog'
        wordList = ["hot","dot","dog","lot","log","cog"]
        answer =  [
            ["hit","hot","dot","dog","cog"],
            ["hit","hot","lot","log","cog"]
        ]
        result = self.sol.findLadders(a, b, wordList)
        self.assertEqual(sorted(answer), sorted(result))


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()


"""
LeetCode中为数不多的考图的难题。尽管题目看上去像字符串匹配题，但从“shortest transformation sequence from start to end”还是能透露出
一点图论中最短路径题的味道。如何转化？

1. 将每个单词看成图的一个节点。
2. 当单词s1改变一个字符可以变成存在于字典的单词s2时，则s1与s2之间有连接。
3. 给定s1和s2，问题I转化成了求在图中从s1->s2的最短路径长度。而问题II转化为了求所有s1->s2的最短路径。

无论是求最短路径长度还是求所有最短路径，都是用BFS。在BFS中有三个关键步骤需要实现:

1. 如何找到与当前节点相邻的所有节点。
这里可以有两个策略：
(1) 遍历整个字典，将其中每个单词与当前单词比较，判断是否只差一个字符。复杂度为：n*w，n为字典中的单词数量，w为单词长度。
(2) 遍历当前单词的每个字符x，将其改变成a~z中除x外的任意一个，形成一个新的单词，在字典中判断是否存在。复杂度为：26*w，w为单词长度。
这里可以和面试官讨论两种策略的取舍。对于通常的英语单词来说，长度大多小于100，而字典中的单词数则往往是成千上万，所以策略2相对较优。

2. 如何标记一个节点已经被访问过，以避免重复访问。
可以将访问过的单词从字典中删除。

3. 一旦BFS找到目标单词，如何backtracking找回路径？

"""
#-*- coding:utf-8 -*-
