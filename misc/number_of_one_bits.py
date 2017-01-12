#coding=utf-8

__author__ = 'linglin'

"""
191. Number of 1 Bits

Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming
weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should
return 3.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

Subscribe to see which companies asked this question

Hide Tags Bit Manipulation
Hide Similar Problems (E) Reverse Bits (E) Power of Two (M) Counting Bits (E) Binary Watch (E) Hamming Distance

Easy

"""


import unittest


class Solution(object):
    def hammingWeight(self, n): #62ms, 14% -- 36ms, 94%
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n>0:
            cnt += n&1
            n = n>>1
        return cnt

    def hammingWeight1(self, n): #49ms, 39%
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n>0:
            cnt += n%2
            n /= 2
        return cnt

    def hammingWeight_ref(self, n): # a very different way, 42ms, 67%
        """
        Each time of "n &= n - 1", we delete one '1' from n.
        O(m) by time, m is the count of 1's
        5 -- 111
        4 -- 110
        3 -- 011
        2 -- 010
        1 -- 001

        :type n: int
        :rtype: int
        """
        ans = 0
        while n:
            n &= n - 1
            ans += 1
        return ans



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = 11
        answer = 3
        result = self.sol.hammingWeight(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
