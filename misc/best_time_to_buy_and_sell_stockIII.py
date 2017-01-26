#coding=utf-8
__author__ = 'linglin'

"""

123. Best Time to Buy and Sell Stock III


Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Subscribe to see which companies asked this question

Hide Tags Array Dynamic Programming
Hide Similar Problems (E) Best Time to Buy and Sell Stock (M) Best Time to Buy and Sell Stock II (H) Best Time to Buy
and Sell Stock IV


Hard

"""


import unittest


class Solution(object):
    def maxProfit(self, prices): #72ms, 56%
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        dpl = [0 for i in range(n)]
        dpr = [0 for i in range(n)]

        min_price = prices[0]
        for i in range(1,n):
            min_price = min(min_price, prices[i])
            dpl[i] = max(dpl[i-1],prices[i]-min_price)

        max_price = prices[n-1]
        for i in range(n-2,-1,-1):
            max_price = max(max_price, prices[i])
            dpr[i] = max(dpr[i+1], max_price - prices[i])

        result = 0
        for i in range(n):
            result = max(result, dpl[i]+dpr[i])
        return result







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
        nums = [7, 3, 8, 1, 3, 4]
        answer = 8
        result = self.sol.maxProfit(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""
只允许做两次交易，这道题就比前两道要难多了。解法很巧妙，有点动态规划的意思：开辟两个数组f1和f2，f1[i]表示在price[i]之前进行一次交易所获得
的最大利润，f2[i]表示在price[i]之后进行一次交易所获得的最大利润。则f1[i]+f2[i]的最大值就是所要求的最大值，而f1[i]和f2[i]的计算就需要动
态规划了，看代码不难理解。


"""

#-*- coding:utf-8 -*-
#coding=utf-8