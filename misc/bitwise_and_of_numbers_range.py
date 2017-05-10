#coding=utf-8

import unittest

"""
201. Bitwise AND of Numbers Range

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.

Credits:
Special thanks to @amrsaqr for adding this problem and creating all test cases.

Subscribe to see which companies asked this question.

Hide Tags Bit Manipulation

Medium

"""



class Solution(object):
    def rangeBitwiseAnd(self, m, n): #ref
        """
        ?? do m need do add leading zero if m is shorter in n ?, yes
        ** key idea is to find the left most common part of m and n
        :type m: int
        :type n: int
        :rtype: int
        """
        cnt = 0
        while m != n:
            m >>= 1
            n >>= 1
            cnt += 1
        return n << cnt  # or m <<cnt is the same, because after right shift , m and n are the same value


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [5,7] # 101, 110, 111
        answer = 4
        result = self.sol.rangeBitwiseAnd(nums[0], nums[1])
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [0,0]
        answer = 0
        result = self.sol.rangeBitwiseAnd(nums[0], nums[1])
        self.assertEqual(answer, result)

    def test_case3(self):
        nums = [3,4]  # 11, 100, which means need to pad leading zero
        answer = 0
        result = self.sol.rangeBitwiseAnd(nums[0], nums[1])
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
