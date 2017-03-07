__author__ = 'linglin'

import unittest

"""
151. Reverse Words in a String

Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.

click to show clarification.

Subscribe to see which companies asked this question.

Hide Tags String
Hide Similar Problems (M) Reverse Words in a String II


Medium

"""

class Solution(object):
    def reverseWords(self, s): #58%
        """
        :type s: str
        :rtype: str
        """
        words = s.split(" ")
        words = [x for x in words if x != '' and x!= " " ] # important here
        if words:
            return " ".join(words[::-1])
        else:
            return ""



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = " "
        answer = ""
        result = self.sol.reverseWords(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8