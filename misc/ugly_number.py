#coding=utf-8

import unittest

"""
263. Ugly Number
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not 
ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

Difficulty:Easy
Total Accepted:104.2K
Total Submissions:265.9K
Contributor: LeetCode
Subscribe to see which companies asked this question.

Related Topics 
Math 
Similar Questions 
Happy Number Count Primes Ugly Number II 

"""


class Solution(object):
    def isUgly(self, num):
        """
        2，3，5，6，8，9，10，
        :type num: int
        :rtype: bool
        """
        for divisor in 2, 3, 5:
            while num % divisor == 0:
                num /= divisor
        return num == 1


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = 1
        answer = 1
        result = self.sol.isUgly(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
