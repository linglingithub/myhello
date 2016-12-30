#coding=utf-8
"""
139. Word Break

Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of
one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

Medium

"""

import unittest


class Solution(object):
    def wordBreak1(self, s, wordDict): #48ms, 76%
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if not s or not wordDict:
            return False
        n = len(s)
        dp = [ False for i in range(n)]
        for i in range(n):
            if s[0:i+1] in wordDict:
                dp[i] = True
                continue
            for w in wordDict:
                k = len(w)
                if i-k >= 0 and dp[i-k] and s[i-k+1:i+1] == w: # pay attention to the index here. and should be >=, otherwise wrong for case 3
                    dp[i] = True
                    break
        return dp[n-1]
    

    def wordBreak_ref_dp(self, s, dict): #58ms, 49%
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for k in range(i):
                if dp[k] and s[k:i] in dict:
                    dp[i] = True
        return dp[len(s)]
    
    def wordBreak_ref_diff(self, s, wordDict): #72ms, 20%
        if not s or not wordDict:
            return False
        n = len(s)
        pos = [False for i in range(n+1)]
        pos[0] = True
        for i in range(n):
            if pos[i]:
                for j in range(i+1, n+1):
                    sub = s[i:j]
                    if sub in wordDict:
                        pos[j] = True
        return pos[n]
        

class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case3(self): #======>
        s = "ab"
        wdict = ["a", "b"]
        answer = True
        result = self.sol.wordBreak(s, wdict)
        self.assertEqual(answer, result)
        
    def test_case1(self):
        s = "leetcode"
        wdict = ["leet", "code"]
        answer = True
        result = self.sol.wordBreak(s, wdict)
        self.assertEqual(answer, result)
        
    def test_case2(self):
        s = "leetcode"
        wdict = ["leete", "code"]
        answer = False
        result = self.sol.wordBreak(s, wdict)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
