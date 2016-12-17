"""
224. Basic Calculator

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers
and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
Note: Do not use the eval built-in library function.

Subscribe to see which companies asked this question

Hide Tags Stack Math
Hide Similar Problems (M) Evaluate Reverse Polish Notation (M) Basic Calculator II (M) Different Ways to Add Parentheses
 (H) Expression Add Operators

Hard

"""

import unittest


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.s = s
        result = 0
        stack = []
        slen = len(s)
        idx = 0
        plus = True
        while stack or idx < len(s):
            char = s[idx]
            ########
            if '0'<=char<='9':
                num, idx = self.get_number(idx)
                if plus:
                    result += num
                else:
                    result -= num
            elif char== "(":
                pass





class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = "1 + 1"
        answer = 2
        result = self.sol.calculate(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = " 2-1 + 2 "
        answer = 3
        result = self.sol.calculate(nums)
        self.assertEqual(answer, result)

    def test_case3(self):
        nums = "(1+(4+5+2)-3)+(6+8)"
        answer = 23
        result = self.sol.calculate(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8