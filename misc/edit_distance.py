#coding=utf-8

"""

72. Edit Distance

Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2.

(each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
Subscribe to see which companies asked this question

Hide Tags Dynamic Programming String
Hide Similar Problems (M) One Edit Distance

Hard

"""


import unittest


class Solution(object):
    def minDistance(self, word1, word2): #272ms, 45.13%
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1) if word1 else 0
        n = len(word2) if word2 else 0
        if m==0 or n==0:
            return abs(m-n) # remember to add abs(), otherwise wrong fro case2
        dp=[ [0 for i in range(n+1)] for j in range(m+1)] # should be m+1 and n+1 and rethink the ind of dp and word, case4
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        for i in range(1,m+1): # remember to start from 1, otehrwise wrong for case3
            for j in range(1,n+1):
                increase = dp[i-1][j] + 1
                remove = dp[i][j-1] + 1
                # replace_or_not = dp[i-1][j-1] + (1 if word1[i]!=word2[j] else 0), rethink idx, case4
                replace_or_not = dp[i - 1][j - 1] + (1 if word1[i-1] != word2[j-1] else 0)
                dp[i][j] = min(increase, remove, replace_or_not)
        return dp[m][n] #dp[m-1][n-1]

    def minDistance_ref_better(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1 = len(word1)
        len2 = len(word2)
        f = [[0] * (len2 + 1) for i in range(len1 + 1)]
        for i in range(len1 + 1):
            f[i][0] = i
        for j in range(len2 + 1):
            f[0][j] = j

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if word2[j - 1] == word1[i - 1]:  # good here, seperate the last letter equal case
                    f[i][j] = f[i - 1][j - 1]
                else:
                    f[i][j] = min(f[i - 1][j - 1], f[i - 1][j], f[i][j - 1]) + 1

        return f[len1][len2]


    def minDistance_ref1(self, word1, word2):
        """
        解题思路：这道题是很有名的编辑距离问题。用动态规划来解决。状态转移方程是这样的：dp[i][j]表示word1[0...i-1]到word2[0...j-1]
        的编辑距离。而dp[i][0]显然等于i，因为只需要做i次删除操作就可以了。同理dp[0][i]也是如此，等于i，因为只需做i次插入操作就可以了。
        dp[i-1][j]变到dp[i][j]需要加1，因为word1[0...i-2]到word2[0...j-1]的距离是dp[i-1][j]，而word1[0...i-1]到
        word1[0...i-2]需要执行一次删除，所以dp[i][j]=dp[i-1][j]+1；同理dp[i][j]=dp[i][j-1]+1，因为还需要加一次word2的插入操作。
        如果word[i-1]==word[j-1]，则dp[i][j]=dp[i-1][j-1]，如果word[i-1]!=word[j-1]，那么需要执行一次替换replace操作，所以
        dp[i][j]=dp[i-1][j-1]+1，以上就是状态转移方程的推导。

        :param word1:
        :param word2:
        :return:
        """
        m = len(word1) + 1
        n = len(word2) + 1
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(n):
            dp[0][i] = i
        for i in range(m):
            dp[i][0] = i
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1,
                               dp[i - 1][j - 1] + (0 if word1[i - 1] == word2[j - 1] else 1))
        return dp[m - 1][n - 1]


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case4(self):  # ====>
        a = "a"
        b = "b"
        answer = 1
        result = self.sol.minDistance(a, b)
        self.assertEqual(answer, result)

    def test_case3(self): #====>
        a = "a"
        b = "ab"
        answer = 1
        result = self.sol.minDistance(a, b)
        self.assertEqual(answer, result)

    def test_case2(self): #====>
        a = ""
        b = "aa"
        answer = 2
        result = self.sol.minDistance(a, b)
        self.assertEqual(answer, result)

    def test_case1(self):
        a = "abc"
        b = "aab"
        answer = 2
        result = self.sol.minDistance(a,b)
        self.assertEqual(answer, result)




def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8