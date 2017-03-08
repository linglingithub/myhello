#coding=utf-8

import unittest

"""

168. Excel Sheet Column Title

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
Credits:
Special thanks to @ifanchu for adding this problem and creating all test cases.

Subscribe to see which companies asked this question.

Hide Tags Math
Hide Similar Problems (E) Excel Sheet Column Number

Easy

"""



class Solution(object):
    def convertToTitle(self, n): #39ms, 62%
        """
        :type n: int
        :rtype: str
        """
        if n < 1:
            return ''
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        result = ''
        while 1<=n:
            current = (n-1) % 26
            result = letters[current] + result
            n /= 26
            # if current == 25 and n == 1: #==add this , otherwise wrong for case4
            #     break
            if current == 25: #==add this and modify, otherwise wrong for case5
                n -= 1
        return result


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        num = 1
        answer = 'A'
        result = self.sol.convertToTitle(num)
        self.assertEqual(answer, result)

    def test_case2(self):
        num = 28
        answer = 'AB'
        result = self.sol.convertToTitle(num)
        self.assertEqual(answer, result)

    def test_case3(self):
        num = 0
        answer = ''
        result = self.sol.convertToTitle(num)
        self.assertEqual(answer, result)

    def test_case4(self): #====>
        num = 26
        answer = 'Z'
        result = self.sol.convertToTitle(num)
        self.assertEqual(answer, result)

    def test_case5(self): #====> OUTPUT 'BZ'
        num = 52
        answer = 'AZ'
        result = self.sol.convertToTitle(num)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
