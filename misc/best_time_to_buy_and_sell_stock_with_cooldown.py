


#coding=utf-8
__author__ = 'linglin'

"""

309. Best Time to Buy and Sell Stock with Cooldown


Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell
one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]
Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.

Subscribe to see which companies asked this question

Hide Tags Dynamic Programming
Hide Similar Problems (E) Best Time to Buy and Sell Stock (M) Best Time to Buy and Sell Stock II

Medium

"""


import unittest


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """





class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [7, 1, 5, 3, 6, 4]
        answer = 5
        result = self.sol.maxProfit(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [7, 6, 4, 3, 1]
        answer = 0
        result = self.sol.maxProfit(nums)
        self.assertEqual(answer, result)

    def test_case3(self):
        nums = [7, 3, 5, 1, 6, 4]
        answer = 5
        result = self.sol.maxProfit(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8