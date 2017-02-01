__author__ = 'linglin'
"""
150. Evaluate Reverse Polish Notation

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
Subscribe to see which companies asked this question

Hide Tags Stack
Hide Similar Problems (H) Basic Calculator (H) Expression Add Operators

Medium


"""

import unittest


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return None
        stack = []
        operators = ["+", "-", "*", "/"]
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if token == "+":
                    result = a+b
                elif token == "-":
                    result = a-b
                elif token == "*":
                    result = a * b
                else:
                    #result = a/b
                    # here take care of the case like "1/-22",
                    # in Python 2.x, it returns -1, while in
                    # Leetcode it should return 0
                    # see case 4
                    if a*b < 0 and a % b != 0:
                        result = a/b+1
                    else:
                        result = a/b

                stack.append(result)
        if stack: #remember to pop the result, otherwise wrong for case 3
            result = int(stack.pop())
        return result





class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = ["2", "1", "+", "3", "*"]
        answer = 9
        result = self.sol.evalRPN(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = ["4", "13", "5", "/", "+"]
        answer = 6
        result = self.sol.evalRPN(nums)
        self.assertEqual(answer, result)

    def test_case3(self): #======>
        nums = ["18"]
        answer = 18
        result = self.sol.evalRPN(nums)
        self.assertEqual(answer, result)

    def test_case4(self): #======>
        nums = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        answer = 22
        result = self.sol.evalRPN(nums)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8