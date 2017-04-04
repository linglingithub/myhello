#coding=utf-8

import unittest

"""
76. Minimum Window Substring

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity
O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

Subscribe to see which companies asked this question.

Hide Tags Hash Table Two Pointers String
Hide Similar Problems (H) Substring with Concatenation of All Words (M) Minimum Size Subarray Sum (H) Sliding Window
Maximum

Hard


Challenge
Can you do it in time complexity O(n) ?

Tags
LinkedIn Hash Table Facebook

"""



class Solution(object):
    def minWindow(self, s, t): # 146ms, 81%
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
        target = {}  # should have letters
        contains = {}
        target_cnt = len(t)
        for i in t:
            if i in target:
                target[i] += 1
            else:
                target[i] = 1
            contains[i] = 0
        l = 0
        contains_cnt = 0 # valid total, use this together with contains[l/r] to check if has enough match
        result = ""
        while l < len(s) and s[l] not in t: #need to add this, see case 3
            l += 1
        r = l

        while r < len(s):
            #cl, cr = s[l], s[r]
            if s[r] in target:
                if contains[s[r]] < target[s[r]]:
                    contains_cnt += 1
                contains[s[r]] += 1
                if contains_cnt == target_cnt:
                    if r+1-l < len(result) or len(result) == 0:
                        result = s[l:r+1]
                    while l < r:
                        if s[l] in target:
                            if contains_cnt < target_cnt: #need to use this as break condition
                                break
                            if contains[s[l]] == target[s[l]]:
                                contains_cnt -= 1
                            contains[s[l]] -= 1

                            # if contains_cnt < target_cnt: #if use this will not remove letters not in target
                            #     l += 1
                            #     break
                        l += 1
                        if contains_cnt == target_cnt and r+1-l < len(result): # for case 4, add len check for case5
                            result = s[l:r+1]
            r += 1
        return result


    def minWindow_wrong_case2(self, s, t):
        """
        did not think about t may have dupilicated letters, see case 2
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
        target = {}
        for i in t:
            target[i] = 0
        l = 0
        r = 0
        result = ""

        while r < len(s):
            #cl, cr = s[l], s[r]
            if s[r] in target:
                target[s[r]] += 1
                if len([x for x in target.values() if x == 0]) == 0:
                    if r+1-l < len(result) or len(result) == 0:
                        result = s[l:r+1]
                    while l < r:
                        if s[l] in target:
                            target[s[l]] -= 1
                            if len([x for x in target.values() if x == 0]) > 1:
                                target[s[l]] = 1
                                break
                        l += 1
            r += 1
        return result


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        s = "ADOBECODEBANC"
        t = "ABC"
        answer = "BANC"
        result = self.sol.minWindow(s,t)
        self.assertEqual(answer, result)

    def test_case2(self): # ===>
        s = "a"
        t = "aa"
        # answer = "a" # thought answer should be this
        answer = ""
        result = self.sol.minWindow(s,t)
        self.assertEqual(answer, result)

    def test_case3(self): # ===>
        s = "ab"
        t = "b"
        answer = "b"
        result = self.sol.minWindow(s,t)
        self.assertEqual(answer, result)

    def test_case4(self): # ===>
        s = "bba"
        t = "ab"
        answer = "ba"
        result = self.sol.minWindow(s,t)
        self.assertEqual(answer, result)

    def test_case5(self): # ===>
        s = "abcabdebac"
        t = "cda"
        answer = "cabd"
        result = self.sol.minWindow(s,t)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
