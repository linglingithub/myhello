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
    def maxProfit1(self, prices): #ref, 52ms, 49%, 代码1 O(n)空间
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices:
            return 0
        n = len(prices)
        sell = [0 for i in range(n)]
        buy = [0 for i in range(n)]
        sell[0] = 0
        buy[0] = -prices[0]
        for i in range(1,n):
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
            buy[i] = max(buy[i - 1], (sell[i - 2] if i > 1 else 0) - prices[i])
        return sell[-1]


    def maxProfit(self, prices): #ref, 46ms, 75%, 代码2 O(1)空间
        if not prices:
            return 0
        n = len(prices)

        curSell = 0   #sell[i]
        prevSell = 0  #sell[i-2]
        buy = -prices[0]  #buy[i]

        for i in range(1,n):
            tmp = curSell
            curSell = max(curSell, buy + prices[i])
            buy = max(buy, (prevSell if i > 1 else 0) - prices[i])
            prevSell = tmp

        return curSell




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1, 2, 3, 0, 2]
        answer = 3
        result = self.sol.maxProfit(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-


"""

https://soulmachine.gitbooks.io/algorithm-essentials/java/dp/best-time-to-buy-and-sell-stock-with-cooldown.html

这题比Best Time to Buy and Sell Stock II多了一个cooldown的条件，就变得麻烦多了。这题是一个多阶段优化问题，首先范围缩小到广搜，贪心或
者动规。因为每步之间互相牵连，贪心显然不行。广搜固然可以，不过是O(2^n)复杂度，所以我们先考虑用动规。
对于每一天，有三种动作，buy, sell, cooldown, sell 和 cooldown 可以合并成一种状态，因为手里最终没有股票。最终需要的结果是 sell，即手里
股票卖了获得最大利润。我们可以用两个数组来记录当前持股和未持股的状态，令sell[i] 表示第i天未持股时，获得的最大利润，buy[i]表示第i天持有股
票时，获得的最大利润。
对于sell[i]，最大利润有两种可能，一是今天没动作跟昨天未持股状态一样，二是今天卖了股票，所以状态转移方程如下：
sell[i] = max{sell[i - 1], buy[i-1] + prices[i-1]}
对于buy[i]，最大利润有两种可能，一是今天没动作跟昨天持股状态一样，二是前天卖了股票，今天买了股票，因为 cooldown 只能隔天交易，所以今天买
股票要追溯到前天的状态。状态转移方程如下：
buy[i] = max{buy[i-1], sell[i-2] - prices[i]}
最终我们要求的结果是sell[n - 1]，表示最后一天结束时，手里没有股票时的最大利润。
这个算法的空间复杂度是O(n)，不过由于sell[i]仅仅依赖前一项，buy[i]仅仅依赖前两项，所以可以优化到O(1)，具体见第二种代码实现。



========================================================================================================================

设sell[i] 卖出操作的最大利润。它需要考虑的是，第i天是否卖出。（手上有stock在第i天所能获得的最大利润）

buy[i] 买进操作的最大利润。它需要考虑的是，第i天是否买进。（手上没有stock在第i天所能获得的最大利润）

所以，显然有状态转移方程

buy[i] = max(buy[i-1] , sell[i-2] – prices[i])  // 休息一天在买入，所以是sell[i-2]在状态转移
sell[i] = max(sell[i-1], buy[i-1] + prices[i])
最后显然有sell[n-1] > buy[n-1] 所以我们返回sell[n-1]

"""