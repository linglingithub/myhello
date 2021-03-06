#coding=utf-8

import unittest

"""
371. Sum of Two Integers
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.

Credits:
Special thanks to @fujiaozhu for adding this problem and creating all test cases.

Difficulty:Easy
Total Accepted:79K
Total Submissions:154.3K
Contributor: LeetCode
Subscribe to see which companies asked this question.

Related Topics 
Bit Manipulation 
Similar Questions 
Add Two Numbers 

"""



class Solution(object):
    def getSum(self, a, b):
        """
        Obviously bit operation.
        Need to think about negative number's bit representation
        
        :type a: int
        :type b: int
        :rtype: int
        """
        if not a:
            return b
        if not b:
            return a
        res = 0



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1, 2]
        answer = 3
        result = self.sol.getSum(*nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
"""

class Solution(object):
    def getSum(self, a, b):
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)

"""