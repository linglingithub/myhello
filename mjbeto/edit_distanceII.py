#coding=utf-8

import unittest

"""
Edit Distance II

Given two strings S and T, determine if they are both one edit distance apart.

Example
Given s = "aDb", t = "adb"
return true

Tags 
String Twitter Uber Snapchat Facebook
Related Problems 
Medium Edit Distance

"""



class Solution:
    # @param {string} s a string
    # @param {string} t a string
    # @return {boolean} true if they are both one edit distance apart or false
    def isOneEditDistance(self, s, t):
        # Write your code here
        if not s:
            return True if t and len(t) == 1 else False
        if not t:
            return True if s and len(s) == 1 else False
        if not(-1 <= len(s) - len(t) <= 1):
            return False
        cnt = 0
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                if cnt >= 1:
                    return False
                else:
                    cnt += 1
                    if len(s) == len(t):
                        i += 1
                        j += 1
                    elif len(s) > len(t):
                        i += 1
                    else:
                        j += 1
        if len(s) -i + len(t) - j + cnt == 1:
            return True
        else:
            return False







class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        s = "aDb"
        t = "adb"
        answer = True
        result = self.sol.isOneEditDistance(s, t)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
