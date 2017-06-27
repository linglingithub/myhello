#coding=utf-8

"""
 

409. Longest Palindrome

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

"""

import unittest


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        from collections import Counter
        counts = Counter(s)
        single = False
        result = 0
        for cnt in counts.values():
            if cnt % 2 == 0:
                result += cnt
            else:
                result += cnt - 1
                single = True
        if single:
            result += 1
        return result







class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        s = "abccccdd"
        answer = 7
        result = self.sol.longestPalindrome(s)
        self.assertEqual(answer, result)






def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner.run(suite)


if __name__ == '__main__':
    main()

"""
Some one pass method


public int longestPalindrome(String s) {
        boolean[] map = new boolean[128];
        int len = 0;
        for (char c : s.toCharArray()) {
            map[c] = !map[c];         // flip on each occurrence, false when seen n*2 times
            if (!map[c]) len+=2;
        }
        if (len < s.length()) len++; // if more than len, atleast one single is present
        return len;
    }


"""