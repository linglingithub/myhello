#coding=utf-8
__author__ = 'linglin'

"""

121. Best Time to Buy and Sell Stock


Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an
algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
Subscribe to see which companies asked this question

Hide Tags Array Dynamic Programming
Hide Similar Problems (M) Maximum Subarray (M) Best Time to Buy and Sell Stock II (H) Best Time to Buy and Sell Stock III
(H) Best Time to Buy and Sell Stock IV (M) Best Time to Buy and Sell Stock with Cooldown

Easy

"""


import unittest


class Solution(object):
    def maxProfit(self, prices):
        # write your code here
        if not prices or len(prices) < 2:
            return 0
        result = 0
        i, j = 0, 1
        while j < len(prices):
            if prices[i] >= prices[j]:
                i = j
            while j+1 < len(prices) and prices[j+1] >= prices[j]:
                j += 1
            result = max(result, prices[j] - prices[i])
            j += 1
        return result

    def maxProfit1(self, prices): #49ms, 69%
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        low = prices[0]
        high = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            curr = prices[i]
            if curr > high:
                high = curr
                continue
            elif curr < low:
                profit = max(profit, high - low)
                low = high = curr
        return max(profit, high - low)





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
