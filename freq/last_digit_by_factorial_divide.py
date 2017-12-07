#coding=utf-8

import unittest

"""

729. Last Digit By Factorial Divide 

 Description
 Notes
 Testcase
 Judge
We are given two numbers A and B such that B >= A. We need to compute the last digit of this resulting F such that F = B! / A! where 1 <= A, B <= 10^18 (A and B are very large)

Have you met this question in a real interview? Yes
Example
Given A = 2, B = 4, return 2
A! = 2 and B! = 24, F = 24 / 2 = 12 --> last digit = 2

Given A = 107, B = 109, return 2
Tags 
Mathematics Google
Related Problems 
Hard Factorial


"""


class Solution:
    """
    @param A: the given number
    @param B: another number
    @return: the last digit of B! / A! 

    234300352440211300, 829691773056400707 ==> 0

    """

    def computeLastDigit(self, A, B):
        # write your code here
        k = B - A
        if k < 0:
            return -1
        if k == 0:
            return 1
        if k >= 5:  # this is the KEY!!!
            return 0
        res = B % 10
        for i in range(1, k):
            res = (res * ((B - i) % 10)) % 10
            if res == 0:  # key point!! should add this !!! -- not good enough
                return 0
        return res


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
