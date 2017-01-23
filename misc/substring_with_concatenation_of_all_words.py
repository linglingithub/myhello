#coding=utf-8
__author__ = 'linglin'

"""
30. Substring with Concatenation of All Words

You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of
substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).

Subscribe to see which companies asked this question

Hide Tags Hash Table Two Pointers String
Hide Similar Problems (H) Minimum Window Substring

Hard

"""

import unittest


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        for i in range(0, len(s)):
            for j


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        s = "barfoothefoobarman"
        words = ["foo", "bar"]
        answer = [0, 9]
        result = self.sol.findSubstring(s, words)
        self.assertEqual(sorted(answer), sorted(result))


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
