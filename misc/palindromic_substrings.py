#coding=utf-8

import unittest

"""
647. Palindromic Substrings
DescriptionHintsSubmissionsDiscussSolution
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
Note:
The input string length won't exceed 1000.

"""


class Solution:
    def countSubstrings(self, s):
        """
        basic idea:
        check every possible mid point of s, extend to left and right, and keep count of the string

        :type s: str
        :rtype: int
        """
        result = [0]
        for i in range(len(s)):
            self.check_palindrome(s, i, i, result)
            self.check_palindrome(s, i, i + 1, result)
        return result[0]

    def check_palindrome(self, s, left, right, result):
        if right >= len(s):
            return
        while left >= 0 and right < len(s) and s[left] == s[right]:
            result[0] += 1
            left -= 1
            right += 1

class Solution_DP:
    def countSubstrings(self, s):
        """
        basic idea: check every [i, j] to see if the substring on [i, j] is a palindrome or not.
        at the end, count all [i, j] that is, return the result.
        use a 2d matrix to store boolean value,
        [i, i] -> true ; [i, i + 1] -> s[i] == s[i + 1]
        [i, j] -> [i + 1, j - 1] true and s[i] == s[j]
        keep a global count, increase when found true.
        return the count

        Time: O(n^2)
        Space: O(n^2)

        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        result = 0
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for j in range(n):
            for i in range(j, -1, -1):
                if i == j:
                    dp[i][j] = True
                elif i == j - 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
                if dp[i][j]:
                    result += 1

        return result


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = 1
        answer = 1
        result = self.sol.testm(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
