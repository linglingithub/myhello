#coding=utf-8
__author__ = 'linglin'

"""
231. Power of Two

Given an integer, write a function to determine if it is a power of two.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

Subscribe to see which companies asked this question

Hide Tags Math Bit Manipulation
Hide Similar Problems (E) Number of 1 Bits (E) Power of Three (E) Power of Four

Easy

"""



import unittest


class Solution(object):
    def isPowerOfTwo(self, n): #52ms, 43%
        """
        :type n: int
        :rtype: bool
        """
        if n<1:
            return False
        return (n & (n-1)) == 0

    def isPowerOfTwo_ref(self, n): #68ms, 14%
        """
        O(1)time, O(1) space
        :param n:
        :return:
        """
        return n > 0 and n & (n - 1) == 0

    def isPowerOfTwo_ref2(self, n): #42ms, 82% --> this show the time calc of LeetCode OJ is not really true
        """
        Complexity:
        O(logn) time
        O(1) space
        :param n:
        :return:
        """
        if n <= 0:
            return False

        while n % 2 == 0:
            n >>= 1

        return n == 1




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = 1
        answer = True
        result = self.sol.isPowerOfTwo(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = 3
        answer = False
        result = self.sol.isPowerOfTwo(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8