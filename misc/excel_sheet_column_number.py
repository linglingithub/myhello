#coding=utf-8

import unittest

"""
171. Excel Sheet Column Number

Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
Credits:
Special thanks to @ts for adding this problem and creating all test cases.

Subscribe to see which companies asked this question.

Hide Tags Math
Hide Similar Problems (E) Excel Sheet Column Title

Easy

"""



class Solution(object):
    def titleToNumber1(self, s): #62ms, 32%
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        letters = '0ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        result = 0
        for i in range(len(s)):
            result *= 26
            idx = letters.index(s[i])
            result += idx
        return result

    def titleToNumber_ref(self, s): #46ms, 91%
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        #letters = '0ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        result = 0
        for char in s:
            result = result * 26 + ord(char) - ord('A') + 1
        return result




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        answer = 1
        num = 'A'
        result = self.sol.titleToNumber(num)
        self.assertEqual(answer, result)

    def test_case2(self):
        answer = 28
        num = 'AB'
        result = self.sol.titleToNumber(num)
        self.assertEqual(answer, result)

    def test_case3(self):
        answer = 0
        num = ''
        result = self.sol.titleToNumber(num)
        self.assertEqual(answer, result)

    def test_case4(self): #====>
        answer = 26
        num = 'Z'
        result = self.sol.titleToNumber(num)
        self.assertEqual(answer, result)

    def test_case5(self): #====> OUTPUT 'BZ'
        answer = 52
        num = 'AZ'
        result = self.sol.titleToNumber(num)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
