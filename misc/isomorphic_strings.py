#coding=utf-8

import unittest

"""

205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.

Subscribe to see which companies asked this question.

Hide Tags Hash Table
Hide Similar Problems (E) Word Pattern

Easy

"""



class Solution(object):
    def isIsomorphic(self, s, t): #55ms, 92%
        words = {}
        for i in range(len(s)):
            if s[i] in words:
                if words[s[i]] != t[i]:
                    return False
            else:

                for val in words.values():
                    if t[i] == val:
                        return False
                words[s[i]] = t[i]
        return True

    def isIsomorphic_wrong(self, s, t): # NOTE: no two char mapped to the same char, wrong for case 5
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #if not s or not t or len(s) != len(t):
        if len(s) != len(t):
            return False
        words = {}
        for i in range(len(s)):
            if s[i] in words:
                if t[i] != words[s[i]]:
                    return False
            elif t[i] in words:  # this is important, see case 4
                if s[i] != words[t[i]]:
                    return False
            else:
                words[s[i]] = t[i]
                words[t[i]] = s[i] # this is important, see case 2, "interchangable"
        return True



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        s, t = "egg", "add"
        answer = True
        result = self.sol.isIsomorphic(s, t)
        self.assertEqual(answer, result)

    def test_case2(self):
        s, t = "egd", "add"
        answer = False
        result = self.sol.isIsomorphic(s, t)
        self.assertEqual(answer, result)

    def test_case3(self):
        s, t = "", ""
        answer = True
        result = self.sol.isIsomorphic(s, t)
        self.assertEqual(answer, result)

    def test_case4(self): #===>
        s, t = "ab", "aa"
        answer = False
        result = self.sol.isIsomorphic(s, t)
        self.assertEqual(answer, result)

    def test_case5(self): #===>
        s, t = "ab", "ca"
        answer = True
        result = self.sol.isIsomorphic(s, t)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
