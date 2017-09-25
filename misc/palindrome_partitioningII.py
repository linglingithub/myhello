#coding=utf-8

import unittest

"""
131. Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]

Difficulty:Medium
Total Accepted:103.3K
Total Submissions:306.2K
Contributor: LeetCode
Subscribe to see which companies asked this question.

Related Topics 
Backtracking 
Similar Questions 
Palindrome Partitioning II 

"""


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        palindrome_dict = {}
        self.helper(s, 0, [], palindrome_dict, result)
        return result

    def helper(self, s, start, path, palindrome_dict, result):
        if start >= len(s):  # start, not s here
            result.append(path)   # append, not add here
            return
        self.helper(s, start + 1, path + [s[start]], palindrome_dict, result)
        for i in range(start + 1, len(s)):  # not start + 1 here, the cut ends ON i, new interval starts on i+1
            if (start, i) not in palindrome_dict:
                if self.is_palindrome(s, start, i):
                    palindrome_dict[(start, i)] = True
                else:
                    palindrome_dict[(start, i)] = False
            if palindrome_dict[(start, i)]:
                self.helper(s, i+1, path + [s[start:i+1]], palindrome_dict, result)  # path+[s[start:i+1]]

    def is_palindrome(self, s, l, r):  # r not included here
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = "aab"
        answer = [
          ["aa","b"],
          ["a","a","b"]
        ]
        result = self.sol.partition(nums)
        self.assertEqual(sorted(answer), sorted(result))

    def test_case02(self):   # ====>
        nums = "bb"
        answer = [
          ["b","b"],
          ["bb"]
        ]
        result = self.sol.partition(nums)
        self.assertEqual(sorted(answer), sorted(result))


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
