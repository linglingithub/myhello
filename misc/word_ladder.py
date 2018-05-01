#coding=utf-8
"""

127. Word Ladder

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation
sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
UPDATE (2017/1/20):
The wordList parameter had been changed to a list of strings (instead of a set of strings). Please reload the code
definition to get the latest changes.

Subscribe to see which companies asked this question

Medium

"""

import unittest
from collections import deque, defaultdict

class Solution:

    def ladderLength(self, beginWord, endWord, wordList):  # 124ms
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def make_p2w(word_list, w_idxs):
            """Creates a map of all combinations of words with missing letters mapped
            to all words in the list that match that pattern.
            E.g. hot -> {'_ot': ['hot'], 'h_t': ['hot'], 'ho_': ['hot']}
            """
            p2w = defaultdict(list)

            for word in word_list:
                # for i in range(len(word)):
                for i, j in w_idxs:
                    p = word[:i] + "_" + word[i + 1:]
                    p2w[p].append(word)
            return p2w

        def bfs_words(begin, end,  w_idxs, p2w):
            queue = deque([(begin, 1)])
            visited = set([begin])
            while queue:
                # Get the next node to explore from the top of the queue
                word, depth = queue.popleft()

                # Get the node's children
                # By recreating all possible patterns for that string
                # for i in range(len(word)):
                for i, j in w_idxs:
                    p = word[:i] + "_" + word[i + 1:]
                    neighbor_words = p2w[p]
                    # Iterate through children
                    for nw in neighbor_words:
                        # Goal check (before adding to the queue)
                        if nw == end:
                            return depth+1
                        if nw not in visited:
                            # Add to visited
                            # These is no reason to wait to mark nodes as visited. Because this is
                            # a BFS, once a node has been seen that is the earliest it could have
                            # possibly been seen so any other path to that node would either be
                            # longer or the same length as what we've already observed.
                            visited.add(nw)
                            # Add to the end of the queue
                            queue.append((nw, depth+1))
            return 0

        if endWord not in wordList:
            return 0
        if beginWord == endWord:
            return 1
        # Get word length and character indexes
        wl = len(beginWord)
        w_indexes = [x for x in zip(range(wl), range(1, wl+1))]
        # Preprocess words into a map
        patterns2words = make_p2w(wordList + [beginWord], w_indexes)
        # Do the search
        return bfs_words(beginWord, endWord, w_indexes, patterns2words)

    def ladderLength1(self, beginWord, endWord, wordList):  # ref

        def make_p2w(word_list, w_idxs):
            """Creates a map of all combinations of words with missing letters mapped
            to all words in the list that match that pattern.
            E.g. hot -> {'_ot': ['hot'], 'h_t': ['hot'], 'ho_': ['hot']}
            """
            p2w = defaultdict(word_list)

            for word in word_list:
                for i, j in w_idxs:
                    p = word[:i] + "_" + word[j:]
                    p2w[p].append(word)
            return p2w

        def bfs_words(begin, end, w_idxs, p2w):
            queue = deque([(begin, 1)])
            visited = set([begin])

            while queue:
                # Get the next node to explore from the top of the queue
                word, depth = queue.popleft()

                # Get the node's children
                # By recreating all possible patterns for that string
                for i,j in w_idxs:
                    p = word[:i] + "_" + word[j:]
                    neighbor_words = p2w[p]
                    # Iterate through children
                    for nw in neighbor_words:
                        if nw not in visited:
                            # Goal check (before adding to the queue)
                            if nw == end:
                                return depth+1
                            # Add to visited
                            # These is no reason to wait to mark nodes as visited. Because this is
                            # a BFS, once a node has been seen that is the earliest it could have
                            # possibly been seen so any other path to that node would either be
                            # longer or the same length as what we've already observed.
                            visited.add(nw)
                            # Add to the end of the queue
                            queue.append((nw, depth+1))
            return 0

        # Get word length and character indexes
        wl = len(beginWord)
        w_indexes = zip(range(wl), range(1, wl+1))
        # Preprocess words into a map
        patterns2words = make_p2w(wordList | set([beginWord, endWord]), w_indexes)
        # Do the search
        return bfs_words(beginWord, endWord, w_indexes, patterns2words)

    def ladderLength1(self, beginWord, endWord, wordList): # 144ms
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def construct_dict(word_list):
            d = {}
            for word in word_list:
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i+1:]
                    d[s] = d.get(s, []) + [word]
            return d

        def bfs_words(begin, end, dict_words):
            queue, visited = deque([(begin, 1)]), set()
            while queue:
                word, steps = queue.popleft()
                if word == endWord:
                    return steps
                if word not in visited:
                    visited.add(word)
                    for i in range(len(word)):
                        s = word[:i] + "_" + word[i+1:]
                        neigh_words = dict_words.get(s, [])
                        for neigh in neigh_words:
                            if neigh not in visited:
                                queue.append((neigh, steps + 1))
            return 0

        d = construct_dict(wordList)
        return bfs_words(beginWord, endWord, d)

    def ladderLength_self(self, beginWord, endWord, wordList):  # 468ms
        """
        Assumptions:
            1) all words in lower case
            2) all words have same length
            3) all words have only letters a-z
        :param beginWord:
        :param endWord:
        :param wordList:
        :return:
        """
        if endWord not in wordList:
            return 0
        cost = 0
        queue = deque([beginWord])
        wordList = set(wordList)
        while queue:
            level_size = len(queue)
            cost += 1
            for _ in range(level_size):
                cur = queue.popleft()
                if cur == endWord:
                    return cost
                for i in range(len(cur)):
                    for nch in "abcdefghijklmnopqrstuvwxy":
                        nword = cur[: i] + nch + cur[i + 1:]
                        if nword in wordList:
                            wordList.remove(nword)
                            queue.append(nword)
        return 0


    def ladderLength_TLE(self, beginWord, endWord, wordList):  # local runs 60+s for case 2
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # sanity check
        if not wordList or endWord not in wordList:
            return 0
        # corner case for beginWord already in wordList:
        if beginWord == endWord and beginWord in wordList:
            return -1 # or what ?
        # queue for BFS
        queue = deque()
        # visited for check visited word in wordList
        visited = set()
        # init queue and visited
        queue.append(beginWord)
        visited.add(beginWord)
        cost = 1
        # check level by level the char change
        while queue:
            level_size = len(queue)
            cost += 1
            for _ in range(level_size):
                cur = queue.popleft()
                for i in range(len(cur)):
                    for nch in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = cur[: i] + nch + cur[i + 1 :]
                        # if candidate is the endWord
                        if candidate == endWord:
                            return cost
                        if candidate in wordList and candidate not in visited:
                            visited.add(candidate)
                            queue.append(candidate)
        return 0

class Solution1(object):
    def ladderLength(self, beginWord, endWord, wordList): #ref, 488ms
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        queue = deque([[beginWord, 1]])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0

    def ladderLength1(self, beginWord, endWord, wordList): #ref, leetcode has problem with this problem
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        from collections import defaultdict, deque
        queue = deque( [ [beginWord, 1] ] )
        visited = set( [ beginWord ] )
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
        return 0

    def wordDist(self, wordA, wordB):
        return sum([wordA[x] != wordB[x] for x in range(len(wordA))])


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        a = 'hit'
        b = 'cog'
        wordList = ["hot","dot","dog","lot","log","cog"]
        answer = 5
        result = self.sol.ladderLength(a, b, wordList)
        self.assertEqual(answer, result)

    def test_case2(self):
        a = 'sand'
        b = 'acne'
        from util.ini_file_util import IniFileUtil
        params = IniFileUtil.read_into_dict("word_ladder_case2.ini")
        wordList = IniFileUtil.string_to_string_list(params.get("wordlist"))
        answer = 11
        result = self.sol.ladderLength(a, b, wordList)
        self.assertEqual(answer, result)


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
