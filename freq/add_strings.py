#coding=utf-8

import unittest

"""
415. Add Strings
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

Difficulty:Easy
Total Accepted:46.1K
Total Submissions:111.1K
Contributor: LeetCode
Subscribe to see which companies asked this question.

Related Topics 
Math 
Similar Questions 
Add Two Numbers Multiply Strings 

===================

[lintcode]

655. Big Integer Addition 

 Description
 Notes
 Testcase
 Judge
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

 Notice

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
Have you met this question in a real interview? Yes
Example
Given num1 = "123", num2 = "45"
return "168"

Tags 
Mathematics Airbnb Google
Related Problems 
Hard Factorial 16 %
Medium Add Two Numbers II 24 %
Medium Big Integer multiplication 27 %
Easy Add Two Numbers

"""



class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not num1:
            return num2
        if not num2:
            return num1
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        res = []
        while i >= 0 and j >= 0:
            tmp = carry + int(num1[i]) + int(num2[j])
            carry = tmp / 10
            res.append(str(tmp % 10))
            j -= 1
            i -= 1
        while i >= 0:
            tmp = carry + int(num1[i])
            carry = tmp / 10
            res.append(str(tmp % 10))
            i -= 1
        if carry:
            res.append(str(carry))
        return "".join(res[::-1])


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = 1
        answer = 1
        result = self.sol.testm(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
