#coding=utf-8

import unittest

"""

10. Regular Expression Matching

Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") ? false
isMatch("aa","aa") ? true
isMatch("aaa","aa") ? false
isMatch("aa", "a*") ? true
isMatch("aa", ".*") ? true
isMatch("ab", ".*") ? true
isMatch("aab", "c*a*b") ? true

Hard

Tags 
Backtracking Dynamic Programming String Google Facebook
Related Problems 
Hard Wildcard Matching

"""


class Solution(object):
    def isMatch(self, s, p):
        """
        "ab", ".*" is True means *'s preceding element means the element in p before *, if . before *, then * can be any character.
        :type s: str
        :type p: str
        :rtype: bool
        """
        # input check
        # if not p:    # wrong for case 11
        #     return False
        if len(p) > 0 and p[0] == "*":   # need to check len, see case 11
            return False  # or raise ValueError("wrong pattern input!")??
        if p==".*": #and len(s) > 1:
            return True

        # init
        m, n = len(s), len(p)
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = True
        # for i in range(m+1):  # should be false here
        #     dp[i][0] = True
        # for j in range(n+1):
        #     dp[0][j] = True

        # if n >= 2 and p[1] == "*":   # NOTE, need special init here, otherwise wrong for case7
        #     dp[0][2] = True
        for j in range(2, n+1):  #!!!! important, case 10
            if p[j-1] == "*":
                dp[0][j] = dp[0][j-2]

        # propagate dp
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == p[j-1]:   # same letter
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == ".":     # .
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":     # *
                    # # char*
                    # if j>=2 and p[j-2] != ".":   # (1) * as zero , or (2) * as 1 letter, or (3) * as 2 or more letters
                    #     #dp[i][j] = dp[i][j-2] or (dp[i-1][j-1] and p[j-2]==s[i-1])
                    #     #dp[i][j] = dp[i][j - 2] or (p[j-2] == s[i - 1] and dp[i][j-1]) or (p[j-2] == s[i - 1] and dp[i-1][j-1])
                    #     dp[i][j] = dp[i][j - 2] or (dp[i][j - 1]) or (
                    #     dp[i-1 ][j - 1])
                    # # .*
                    # else:
                    #     dp[i][j] = dp[i-1][j-2]   # .#
                    if dp[i][j-1] or dp[i][j-2]:   #match 0 or 1 preceding element
                        dp[i][j] = True
                    elif (p[j - 2] == s[i - 1] or p[j - 2] == '.') and dp[i - 1][j]: #match multiple preceding elements
                        dp[i][j] = True
                # else:  # different letter without . or *  --> # no need to check, false by default
                #     if j>=2 and p[j-2] == "*":    # remember to check j value
                #         dp[i][j] = dp[i][j-2]
                #     else:
                #         dp[i][j] = False
        return dp[m][n]






































    def isMatch1(self, s, p):
        """
        ref
        :param s: 
        :param p: 
        :return: 
        """
        dp=[[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0]=True
        for i in range(1,len(p)+1):
            if p[i-1]=='*':
                if i>=2:
                    dp[0][i]=dp[0][i-2]
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1]=='.':
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=='*':
                    dp[i][j]=dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.'))
                else:
                    dp[i][j]=dp[i-1][j-1] and s[i-1]==p[j-1]
        return dp[len(s)][len(p)]



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        s, p = "aa", "a"
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
        s, p = "aa", "a*"
        answer = True
        result = self.sol.isMatch(s, p)
        self.assertEqual(answer, result)

    def test_case5(self):
        s, p = "aa", ".*"
        answer = True
        result = self.sol.isMatch(s, p)
        self.assertEqual(answer, result)

    def test_case6(self):
        s, p = "ab", ".*"
        answer = True
        result = self.sol.isMatch(s, p)
        self.assertEqual(answer, result)

    def test_case7(self):   # ====>
        s, p = "aab", "c*a*b"
        answer = True
        result = self.sol.isMatch(s, p)
        self.assertEqual(answer, result)

    def test_case8(self):   # ===>
        #s, p = "aba", ".**"  # --> True
        #s, p = "abc", "*"   # --> False
        #s, p = "abc", "*."  # --> False
        #s, p = "abc", "*.."  # --> False, * need to have a preceding number
        #s, p = "abcdefg584903qfdk", ".*"  # --> True, same for ".**"
        #s, p = "", ".*"  # --> False
        inputs = {
            ("aba", ".**"): True,   #===>
            ("abc", "*"):  False,
            ("abc", "*."): False,
            ("abc", "*.."): False,
            ("abcdefg584903qfdk", ".*"): True,
            ("", ".*"): True
        }
        answer = [True, False, False, False, True, False]
        for (s, p) in inputs.keys():
            result = self.sol.isMatch(s, p)
            answer = inputs.get((s,p))
            print "testing case 8: ", (s, p), result, answer
            self.assertEqual(answer, result)

    def test_case9(self):   #===>
        s, p = "aaa", "ab*a*c*a"
        answer = True
        result = self.sol.isMatch(s, p)
        self.assertEqual(answer, result)


    def test_case10(self):   #===>
        s, p = "aaba", "ab*a*c*a"
        answer = False
        result = self.sol.isMatch(s, p)
        self.assertEqual(answer, result)

    def test_case11(self):   #===>
        s, p = "", ""
        answer = True
        result = self.sol.isMatch(s, p)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-


"""

思路1: DP

关键在于如何处理这个'*'号。

状态：和Mininum Edit Distance这类题目一样。
dp[i][j]表示s[0:i-1]是否能和p[0:j-1]匹配。

递推公式：由于只有p中会含有regular expression，所以以p[j-1]来进行分类。
p[j-1] != '.' && p[j-1] != '*'：dp[i][j] = dp[i-1][j-1] && (s[i-1] == p[j-1])
p[j-1] == '.'：dp[i][j] = dp[i-1][j-1]

而关键的难点在于 p[j-1] = '*'。由于星号可以匹配0，1，乃至多个p[j-2]。
1. 匹配0个元素，即消去p[j-2]，此时p[0: j-1] = p[0: j-3]
dp[i][j] = dp[i][j-2]

2. 匹配1个元素，此时p[0: j-1] = p[0: j-2]
dp[i][j] = dp[i][j-1]

3. 匹配多个元素，此时p[0: j-1] = { p[0: j-2], p[j-2], ... , p[j-2] }
dp[i][j] = dp[i-1][j] && (p[j-2]=='.' || s[i-2]==p[j-2])

 
class Solution {
public:
    bool isMatch(const char *s, const char *p) {
        int m = strlen(s), n = strlen(p);
        vector<vector<bool>> dp(m+1, vector<bool>(n+1,false));
        dp[0][0] = true;
        
        for(int i=0; i<=m; i++) {
            for(int j=1; j<=n; j++) {
                if(p[j-1]!='.' && p[j-1]!='*') {
                    if(i>0 && s[i-1]==p[j-1] && dp[i-1][j-1])
                        dp[i][j] = true;
                }
                else if(p[j-1]=='.') {
                    if(i>0 && dp[i-1][j-1])
                        dp[i][j] = true;
                }
                else if(j>1) {  //'*' cannot be the 1st element
                    if(dp[i][j-1] || dp[i][j-2])  // match 0 or 1 preceding element
                        dp[i][j] = true;
                    else if(i>0 && (p[j-2]==s[i-1] || p[j-2]=='.') && dp[i-1][j]) // match multiple preceding elements
                        dp[i][j] = true;
                }
            }
        }
        return dp[m][n];
    }
};




思路2: 双指针扫描

LeetCode作者给的解法，非常巧妙：

http://leetcode.com/2011/09/regular-expression-matching.html

"""