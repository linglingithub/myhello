#coding=utf-8

import unittest

"""

44. Wildcard Matching

Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
Subscribe to see which companies asked this question.

Hide Tags Dynamic Programming Backtracking Greedy String
Hide Similar Problems (H) Regular Expression Matching

Hard

"""



class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not s:
            return not p or p == "*"
        if p == "*":
            return True
        m, n = len(s), len(p)
        # init dp
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] = True
        # init for '' to 'lll*lll' case
        for i in range(1, n + 1):
            if p[i - 1] == "*":
                dp[0][i] = dp[0][i - 1]
        # propagate dp
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    dp[i][j] = dp[i - 1][j - 1] or dp[i][j-1] or dp[i-1][j]   # * make 1 or 0, or any sequence
                    # if not dp[i][j]:
                    #     for k in range(i):
                    #         dp[i][j] |= dp[k][j-1]
                else:  # different letters
                    dp[i][j] = False
        return dp[m][n]


    def isMatch_TLE(self, s, p): # AC on lint, TLE on leet for case 9, local runs 1s 412ms
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not s:
            return not p or p == "*"
        if p == "*":
            return True
        m, n = len(s), len(p)
        # init dp
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] = True
        # init for '' to 'lll*lll' case
        for i in range(1, n + 1):
            if p[i - 1] == "*":
                dp[0][i] = dp[0][i - 1]

        # propagate dp
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    dp[i][j] = dp[i - 1][j - 1] or dp[i][j-1]
                    if not dp[i][j]:                         # here means dp[i-1][j] ( don't lookback so many steps!!!)
                        for k in range(i):                   # think about when i is smaller, these are alreay covered,
                            dp[i][j] |= dp[k][j-1]           # therefore, only need to lookback at dp[i-1][j]
                else:  # different letters
                    dp[i][j] = False
        return dp[m][n]

    def isMatch_ref(self, s, p): #145ms, 73%
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        pPointer=sPointer=ss=0; star=-1
        while sPointer<len(s):
            if pPointer<len(p) and (s[sPointer]==p[pPointer] or p[pPointer]=='?'):
                sPointer+=1; pPointer+=1
                continue
            if pPointer<len(p) and p[pPointer]=='*':
                star=pPointer; pPointer+=1; ss=sPointer;
                continue
            if star!=-1:
                pPointer=star+1; ss+=1; sPointer=ss
                continue
            return False
        while pPointer<len(p) and p[pPointer]=='*':
            pPointer+=1
        if pPointer==len(p): return True
        return False

    def isMatch_ref_TLE(self, s, p): #2805ms, 0.76%, sometimes TLE for case8 / not TLE 20170821
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n = len(s)
        m = len(p)
        f = [[False] * (m + 1) for i in range(n + 1)]
        f[0][0] = True

        if n == 0 and p.count('*') == m:
            return True

        for i in range(0, n + 1):
            for j in range(0, m + 1):
                if i > 0 and j > 0:
                    f[i][j] |= f[i-1][j-1] and (s[i-1] == p[j-1] or p[j - 1] in ['?', '*'])

                if i > 0 and j > 0:
                    f[i][j] |= f[i - 1][j] and p[j - 1] == '*'

                if j > 0:
                    f[i][j] |= f[i][j - 1] and p[j - 1] == '*'


        return f[n][m]


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        s, p = "aa","a"
        answer = False
        result = self.sol.isMatch(s, p)
        self.assertEqual(answer, result)

    def test_case2(self):
        s, p = "aa","aa"
        answer = True
        result = self.sol.isMatch(s, p)
        self.assertEqual(answer, result)

    def test_case3(self):
        s, p = "aaa","aa"
        answer = False
        result = self.sol.isMatch(s, p)
        self.assertEqual(answer, result)

    def test_case4(self):
        s, p = "aa", "*"
        answer = True
        result = self.sol.isMatch(s, p)
        self.assertEqual(answer, result)

    def test_case5(self):
        s, p = "aa", "a*"
        answer = True
        result = self.sol.isMatch(s, p)
        self.assertEqual(answer, result)

    def test_case6(self):
        s, p = "ab", "?*"
        answer = True
        result = self.sol.isMatch(s, p)
        self.assertEqual(answer, result)

    def test_case7(self):
        s, p = "aab", "c*a*b"
        answer = False
        result = self.sol.isMatch(s, p)
        self.assertEqual(answer, result)

    def test_case8(self):
        s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        p = "*aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa*"
        answer = False
        result = self.sol.isMatch(s, p)
        self.assertEqual(answer, result)

    def test_case9(self):
        s = "aabbabbaabbbbaabaabaaabaaaabbabaabbaaaaaababaaaaaaaaabaaaaababbbaabbbabbbbabbbbbbabbbbbbabbababbbbaabababbabababbaabbaabbbaaababaabbaaaabababbbbbaabaaabaaaaaabaaaabaabbaabbbbabbaabbaabbabbaabbabaabbbb"
        p = "bbb***bba*ab**a*b***b*a**a*****a***b*a**a***b*b***b****b*ba*a***bbb******ba*bbb*a***aba**ab*****b****ab"
        answer = False
        result = self.sol.isMatch(s, p)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""

Leetcode中最难的题之一，不过很多人onsite还是遇到了这道题，所以还是有必要掌握的。
一个比较好的算法是贪心算法（greedy）: whenever encounter ‘*’ in p, keep record of the current position of ‘*’ in p and the
current index in s. Try to match the stuff behind this ‘*’ in p with s, if not matched, just s++ and then try to match
again.

# 64ms, 82%
public class WildcardMatching {
    public boolean isMatch(String s, String p) {
        int i = 0;
        int j = 0;
        int star = -1;
        int mark = -1;
        while (i < s.length()) {
            if (j < p.length()
                    && (p.charAt(j) == '?' || p.charAt(j) == s.charAt(i))) {
                ++i;
                ++j;
            } else if (j < p.length() && p.charAt(j) == '*') {
                star = j;
                j++;
                mark = i;
           //这一步是关键，匹配s中当前字符与p中‘＊’后面的字符，如果匹配，则在第一个if中处理，如果不匹配，则继续比较s中的下一个字符。
            } else if (star != -1) {
                j = star + 1;
                i = ++mark;
            } else {
                return false;
            }
        }
       //最后在此处处理多余的‘＊’，因为多个‘＊’和一个‘＊’意义相同。
        while (j < p.length() && p.charAt(j) == '*') {
            ++j;
        }
        return j == p.length();
    }
}
此题如果写成递归会因为循环而超时，以下是一个C＋＋代码，用来展示其思路：


class Solution {
public:
    bool isMatch(const char *s, const char *p) {
        char cs = *s;
        char cp = *p;
        if(cp == '\0') {
            return cs == cp;
        } else if (cp == '?') {
            if (cs == '\0') return false;
            return isMatch(s + 1,p + 1);
        } else if (cp == '*') {
            const char *st = s;
            for(; *st != '\0'; ++st) {
                if (isMatch(st, p+1)) return true;
            }
            return isMatch(st,p+1);
        } else if (cp != cs)
            return false;
        return isMatch(s + 1,p + 1);
    }
};


"""

#-*- coding:utf-8 -*-
