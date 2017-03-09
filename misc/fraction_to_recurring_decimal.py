#coding=utf-8

import unittest

"""
166. Fraction to Recurring Decimal

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
Hint:

No scary math, just apply elementary math knowledge. Still remember how to perform a long division?
Try a long division on 4/9, the repeating part is obvious. Now try 4/333. Do you see a pattern?
Be wary of edge cases! List out as many test cases as you can think of and test your code thoroughly.
Credits:
Special thanks to @Shangrila for adding this problem and creating all test cases.

Subscribe to see which companies asked this question.

Hide Tags Hash Table Math

Medium

"""



class Solution(object):
    def fractionToDecimal(self, numerator, denominator): #48ms, 44%
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if denominator == 0:
            raise ZeroDivisionError
        if numerator == 0: # remember to add this, no '-0' allowed, see case 7
            return '0'
        neg = False
        if numerator < 0:
            numerator *= -1
            neg = not neg
        if denominator < 0:
            denominator *= -1
            neg = not neg

        remain_dict = {}
        quotient = numerator / denominator
        remain = numerator % denominator
        decimal_str = ""
        place = 0
        while remain != 0 and str(remain) not in remain_dict:  #remember to add str(), otherwise dead loop
            remain_dict[str(remain)] = place
            remain *= 10
            if remain >= denominator:
                digit = str(remain/denominator)
                remain = remain % denominator
            else:
                digit = "0"
            decimal_str += digit
            place += 1
        if remain != 0:
            idx = remain_dict[str(remain)]
            decimal_str = decimal_str[:idx]+"("+decimal_str[idx:] + ")"
            result = ".".join([str(quotient), decimal_str])
        else:
            result = ".".join([str(quotient), decimal_str]) if decimal_str else str(quotient)
        if neg:
            result = "-"+result
        return result




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        num = 1
        denom = 2
        answer = "0.5"
        result = self.sol.fractionToDecimal(num, denom)
        self.assertEqual(answer, result)

    def test_case2(self):
        num = 2
        denom = 1
        answer = "2"
        result = self.sol.fractionToDecimal(num, denom)
        self.assertEqual(answer, result)

    def test_case3(self):
        num = 2
        denom = 3
        answer = "0.(6)"
        result = self.sol.fractionToDecimal(num, denom)
        self.assertEqual(answer, result)

    def test_case4(self):
        num = 1
        denom = -2
        answer = "-0.5"
        result = self.sol.fractionToDecimal(num, denom)
        self.assertEqual(answer, result)

    def test_case5(self):
        num = 1
        denom = -20
        answer = "-0.05"
        result = self.sol.fractionToDecimal(num, denom)
        self.assertEqual(answer, result)

    def test_case6(self):
        num = 1
        denom = 0
        answer = ZeroDivisionError
        with self.assertRaises(answer):
            self.sol.fractionToDecimal(num, denom)

    def test_case7(self): #====>
        num = 0
        denom = -5
        answer = '0'
        result = self.sol.fractionToDecimal(num, denom)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
