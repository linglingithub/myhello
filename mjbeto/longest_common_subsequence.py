#coding=utf-8

import unittest

"""

Longest Common Subsequence

Given two strings, find the longest common subsequence (LCS).

Your code should return the length of LCS.

Have you met this question in a real interview? Yes
Clarification
What's the definition of Longest Common Subsequence?

https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
http://baike.baidu.com/view/2020307.htm
Example
For "ABCD" and "EDCA", the LCS is "A" (or "D", "C"), return 1.

For "ABCD" and "EACB", the LCS is "AC", return 2.

Tags 
LintCode Copyright Dynamic Programming Longest Common Subsequence
Related Problems 
Medium Longest Repeating Subsequence 36 %
Medium Edit Distance 30 %
Medium Longest Common Substring


"""



class Solution:
    """
    @param A, B: Two strings.
    @return: The length of longest common subsequence of A and B.
    """
    def longestCommonSubsequence(self, word1, word2):
        # write your code here
        if not word1 or not word2:
            return 0
        m, n = len(word1), len(word2)
        dp = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = 0
        for j in range(n + 1):
            dp[0][j] = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                a, b = word1[i-1], word2[j-1]  # index wrong here, should have -1
                if a == b:
                    dp[i][j] = max(1 + dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
                else:
                    dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        #return dp[m + 1][n + 1]   #wrong index
        return dp[m][n]




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = 1
        answer = 1
        result = self.sol.longestCommonSubsequence(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""

jiuzhang answer


class Solution:
    
    @param A, B: Two strings.
    @return: The length of longest common subsequence of A and B.
    
    def longestCommonSubsequence(self, A, B):
        n, m = len(A), len(B)
        f = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(n):
            for j in range(m):
                f[i + 1][j + 1] = max(f[i][j + 1], f[i + 1][j])
                if A[i] == B[j]:
                    f[i + 1][j + 1] = f[i][j] + 1
        return f[n][m]


"""