#coding=utf-8

import unittest

"""

387. First Unique Character in a String


First Position Unique Character

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Have you met this question in a real interview? Yes
Example
Given s = "lintcode", return 0.

Given s = "lovelintcode", return 2.

Tags 
Amazon Microsoft Bloomberg

"""


class Solution:
    # @param {string} s a string
    # @return {int} it's index
    def firstUniqChar(self, s):
        # Write your code here
        if not s:
            return -1
        from collections import Counter
        map = Counter(s)
        for i in range(len(s)):
            if map[s[i]] == 1:
                return i
        return -1


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case2(self):
        nums = "lovelintcode"
        answer = 2
        result = self.sol.firstUniqChar(nums)
        self.assertEqual(answer, result)


    def test_case1(self):
        nums = "lintcode"
        answer = 0
        result = self.sol.firstUniqChar(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
