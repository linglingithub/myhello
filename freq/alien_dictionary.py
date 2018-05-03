#coding=utf-8

import unittest

"""
269. Alien Dictionary (locked)

There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You 
receive a list of words from the dictionary, where words are sorted lexicographically by the rules of this new language. 
Derive the order of letters in this language.

For example, Given the following words in dictionary,

[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
] 
The correct order is: "wertf".

Note: You may assume all letters are in lowercase. If the order is invalid, return an empty string. There may be multiple 
valid order of letters, return any one of them is fine.


==========================


892. Alien Dictionary
 Description
 Notes
 Testcase
 Judge
Discuss
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

 Notice
You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters,
return the SMALLEST in lexicographical order ??


Example
Given the following words in dictionary,

[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
The correct order is: "wertf"

Given the following words in dictionary,

[
  "z",
  "x"
]
The correct order is: "zx".

Tags
Twitter Pocket Gems Airbnb Facebook Snapchat Topological Sort Directed Graph Google
Related Problems
Medium Course Schedule II 21 %


"""

from collections import deque, defaultdict
import heapq

class Solution:  # change queue to heap
    """
    Assumptions: only consider lowercase letters, a-z
    Main idea:
    1. model as graph, a letter is a node, generate a DAG
    2. BFS on the graph, and generate the topological sorting of the node
    3. if sorted nodes contains the same number of nodes in the graph (all letters)
        return sorted result, otherwise ""

    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        if not words:
            return ""

        # process and generate graph
        hqueue = []
        indegrees = [0 for _ in range(26)]
        pre_posts = defaultdict(set) # {preNode: set(post_nodes)}, eg: {'t': {'f','a'}}
        letter_cnt = self.process(words, hqueue, indegrees, pre_posts)

        # BFS to get topological sort
        result = []
        while hqueue:
            cur = heapq.heappop(hqueue)
            result.append(cur)
            for nei in pre_posts[cur]:
                indegrees[ord(nei) - ord('a')] -= 1
                if indegrees[ord(nei) - ord('a')] == 0:
                    heapq.heappush(hqueue, nei)
        # return result if len(result) == letter_cnt else ""
        return "".join(result) if len(result) == letter_cnt else ""

    def process(self, words, hqueue, indegrees, pre_posts):
        letter_set = set()
        for i in range(len(words) - 1):
            # compare every two words
            one, two = words[i], words[i + 1]
            min_len = min(len(one), len(two))
            j = 0
            while j < min_len:
                # compare every char in two words
                if one[j] == two[j]:
                    letter_set.add(one[j])
                    j += 1
                else:
                    if two[j] not in pre_posts[one[j]]:
                        indegrees[ord(two[j]) - ord('a')] += 1
                        pre_posts[one[j]].add(two[j])
                    letter_set.add(one[j])
                    letter_set.add(two[j])
                    j += 1
                    break  # the break here will skip the all the letters after first different idx
            # !!! should process tailing chars in one and two, though they don't need to compare char after first diff idx
            for tail in range(j, len(one)):
                letter_set.add(one[tail])
            for tail in range(j, len(two)):
                letter_set.add(two[tail])
        for i in range(26):
            char = chr(ord('a') + i)
            if indegrees[i] == 0 and char in letter_set:
                heapq.heappush(hqueue, char)
        return len(letter_set)

    def process_wrong(self, words, hqueue, indegrees, pre_posts):
        letter_set = set()
        for i in range(len(words) - 1):
            # compare every two words
            one, two = words[i], words[i + 1]
            for j in range(max(len(one), len(two))):  # !!!should include the max length
                if j >= len(one):
                    letter_set.add(two[j])
                    continue
                if j >= len(two):
                    letter_set.add(one[j])
                    continue
                # compare every char in two words
                if one[j] == two[j]:
                    letter_set.add(one[j])
                else:
                    if two[j] not in pre_posts[one[j]]:
                        indegrees[ord(two[j]) - ord('a')] += 1
                        pre_posts[one[j]].add(two[j])
                    letter_set.add(one[j])
                    letter_set.add(two[j])
                    break  # the break here will skip the all the letters after first different idx
        for i in range(26):
            char = chr(ord('a') + i)
            if indegrees[i] == 0 and char in letter_set:
                heapq.heappush(hqueue, char)
        return len(letter_set)


class Solution_shouldOKForLeetCodeExceptLintCase2:
    """
    Assumptions: only consider lowercase letters, a-z
    Main idea:
    1. model as graph, a letter is a node, generate a DAG
    2. BFS on the graph, and generate the topological sorting of the node
    3. if sorted nodes contains the same number of nodes in the graph (all letters)
        return sorted result, otherwise ""

    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        if not words:
            return ""

        # process and generate graph
        queue = ()
        indegrees = [0 for _ in range(26)]
        pre_posts = defaultdict(set) # {preNode: set(post_nodes)}, eg: {'t': {'f','a'}}
        letter_cnt = self.process(words, queue, indegrees, pre_posts)

        # BFS to get topological sort
        result = []
        while queue:
            cur = queue.popleft()
            result.append(cur)
            for nei in pre_posts[cur]:
                indegrees[ord(nei) - ord('a')] -= 1
                if indegrees[ord(nei) - ord('a')] == 0:
                    queue.append(nei)
        # return result if len(result) == letter_cnt else ""
        return "".join(result) if len(result) == letter_cnt else ""

    def process(self, words, queue, indegrees, pre_posts):
        letter_set = set()
        for i in range(len(words) - 1):
            # compare every two words
            one, two = words[i], words[i + 1]
            for j in range(max(len(one), len(two))):  # !!!should include the max length
                if j >= len(one):
                    letter_set.add(two[j])
                    continue
                if j >= len(two):
                    letter_set.add(one[j])
                    continue
                # compare every char in two words
                if one[j] == two[j]:
                    letter_set.add(one[j])
                else:
                    if two[j] not in pre_posts[one[j]]:
                        indegrees[ord(two[j]) - ord('a')] += 1
                        pre_posts[one[j]].add(two[j])
                    letter_set.add(one[j])
                    letter_set.add(two[j])
                    break
        for i in range(26):
            char = chr(ord('a') + i)
            if indegrees[i] == 0 and char in letter_set:
                queue.append(char)
        print(letter_set)
        return len(letter_set)

class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        words = [
          "wrt",
          "wrf",
          "er",
          "ett",
          "rftt"
        ]
        answer = "wertf"
        result = self.sol.alienOrder(words)
        self.assertEqual(answer, result)

    def test_case2(self):
        words = [
          "zy",
          "zx"
        ]
        answer = "yxz"
        result = self.sol.alienOrder(words)
        self.assertEqual(answer, result)

    def test_case3(self):
        words = [
          "ab",
          "adc"
        ]
        answer = "abcd"   # wrong output as 'abd', missing the longer word letter
        result = self.sol.alienOrder(words)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
