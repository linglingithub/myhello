

#coding=utf-8
__author__ = 'linglin'

"""

122. Best Time to Buy and Sell Stock II


Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell
one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you
must sell the stock before you buy again).

Subscribe to see which companies asked this question

Hide Tags Array Greedy
Hide Similar Problems (E) Best Time to Buy and Sell Stock (H) Best Time to Buy and Sell Stock III (H) Best Time to Buy
and Sell Stock IV (M) Best Time to Buy and Sell Stock with Cooldown


Medium

"""


import unittest


class Solution(object):
    def maxProfit(self, prices):#52ms, 45%
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        profit = 0
        for i in range(0, len(prices)-1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]
        return profit





class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [7, 1, 5, 3, 6, 4]
        answer = 7
        result = self.sol.maxProfit(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [7, 6, 4, 3, 1]
        answer = 0
        result = self.sol.maxProfit(nums)
        self.assertEqual(answer, result)

    def test_case3(self):
        nums = [7, 3, 5, 1, 6, 4]
        answer = 7
        result = self.sol.maxProfit(nums)
        self.assertEqual(answer, result)

    def test_case4(self):
        nums = [1, 0, 3, 5, 6, 4]
        answer = 6
        result = self.sol.maxProfit(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8