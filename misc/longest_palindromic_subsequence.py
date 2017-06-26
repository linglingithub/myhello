#coding=utf-8

"""
516. Longest Palindro

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s 
is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".


"""

import unittest


class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """





class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        s = "bbbab"
        answer = 4
        result = self.sol.longestPalindromeSubseq(s)
        self.assertEqual(answer, result)

    def test_case2(self):
        s = "cbbd"
        answer = 2
        result = self.sol.longestPalindromeSubseq(s)
        self.assertEqual(answer, result)




def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner.run(suite)


if __name__ == '__main__':
    main()