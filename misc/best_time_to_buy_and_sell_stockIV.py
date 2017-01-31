#coding=utf-8
__author__ = 'linglin'

"""

188. Best Time to Buy and Sell Stock IV


Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Credits:
Special thanks to @Freezen for adding this problem and creating all test cases.

Subscribe to see which companies asked this question

Hide Tags Dynamic Programming
Hide Similar Problems (E) Best Time to Buy and Sell Stock (M) Best Time to Buy and Sell Stock II (H) Best Time to Buy
and Sell Stock III


Hard

"""


import unittest


class Solution(object):
    def maxProfit_ref3(self, k, prices): #159ms, 18%, 1d-dp
        n = len(prices)
        if n < 2 or k <= 0:
            return 0
        if k >= n/2:
            return self.quickSolve(n,prices)
        local = [ 0 for i in range(k + 1)]
        dp = [ 0 for i in range(k + 1)]
        for i in range(n-1):
            diff = prices[i + 1] - prices[i]
            for j in range(k, 0, -1):
                local[j] = max(dp[j - 1] + max(diff, 0), local[j] + diff)
                dp[j] = max(local[j], dp[j])
        return dp[k]

    def maxProfit_ref2(self, k, prices): #159ms, 18%, 2d-dp
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2 or k <= 0:
            return 0
        if k >= n/2:
            return self.quickSolve(n, prices)
        local = [[0 for y in range(k+1)] for x in range(n)] # where the last (not necessary j-th) sell is done on i-th day
        dp = [[0 for y in range(k+1)] for x in range(n)] # where the max profit is
        for i in range(1, n):
            diff = prices[i] - prices[i - 1]
            for j in range(1, k+1):
                local[i][j] = max(dp[i - 1][j - 1] + max(diff, 0), local[i - 1][j] + diff)
                dp[i][j] = max(dp[i - 1][j], local[i][j])
        return dp[n - 1][k]


    def maxProfit_ref1(self, k, prices): #25ms, 39%, 1d-dp ??
        size = len(prices)
        if k >= size / 2:
            return self.quickSolve(size, prices)
        dp = [None] * (2 * k + 1)
        dp[0] = 0
        for i in range(size):
            for j in range(min(2 * k, i + 1), 0, -1):
                dp[j] = max(dp[j], dp[j - 1] + prices[i] * [1, -1][j % 2])
        return max(dp)

    def quickSolve(self, size, prices):
        sum = 0
        for x in range(size - 1):
            if prices[x + 1] > prices[x]:
                sum += prices[x + 1] - prices[x]
        return sum




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [7, 1, 5, 3, 6, 4]
        k = 2
        answer = 7
        result = self.sol.maxProfit(k,nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [7, 6, 4, 3, 1]
        k = 2
        answer = 0
        result = self.sol.maxProfit(k,nums)
        self.assertEqual(answer, result)

    def test_case3(self):
        nums = [7, 3, 8, 1, 3, 4]
        k = 2
        answer = 8
        result = self.sol.maxProfit(k,nums)
        self.assertEqual(answer, result)

    def test_case4(self):
        nums = [7, 1, 5, 3, 6, 4]
        answer = 5
        result = self.sol.maxProfit(1,nums)
        self.assertEqual(answer, result)

    def test_case5(self):
        nums = [7, 6, 4, 3, 1]
        answer = 0
        result = self.sol.maxProfit(1,nums)
        self.assertEqual(answer, result)

    def test_case6(self):
        nums = [7, 3, 5, 1, 6, 4]
        answer = 5
        result = self.sol.maxProfit(1,nums)
        self.assertEqual(answer, result)

    def test_case7(self):
        nums = [7, 1, 5, 3, 6, 4]
        answer = 7
        result = self.sol.maxProfit(2,nums)
        self.assertEqual(answer, result)

    def test_case8(self):
        nums = [7, 1, 5, 3, 6, 4]
        answer = 5
        result = self.sol.maxProfit(1,nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()


"""


这道题是Best Time to Buy and Sell Stock的扩展，现在我们最多可以进行两次交易。我们仍然使用动态规划来完成，事实上可以解决非常通用的情况，
也就是最多进行k次交易的情况。
这里我们先解释最多可以进行k次交易的算法，然后最多进行两次我们只需要把k取成2即可。我们还是使用“局部最优和全局最优解法”。我们维护两种量，
一个是当前到达第i天可以最多进行j次交易，最好的利润是多少（global[i][j]），
另一个是当前到达第i天，最多可进行j次交易，并且最后一次交易在当天卖出的最好的利润是多少（local[i][j]）。

下面我们来看递推式，全局的比较简单，
global[i][j]=max(local[i][j],global[i-1][j])，

也就是去当前局部最好的，和过往全局最好的中大的那个（因为最后一次交易如果包含当前天一定在局部最好的里面，否则一定在过往全局最优的里面）。
全局（到达第i天进行j次交易的最大收益） = max{局部（在第i天交易后，恰好满足j次交易），全局（到达第i-1天时已经满足j次交易）}

对于局部变量的维护，递推式是
local[i][j]=max(global[i-1][j-1]+max(diff,0),local[i-1][j]+diff)，

也就是看两个量，
第一个是全局到i-1天进行j-1次交易，然后加上今天的交易，如果今天是赚钱的话（也就是前面只要j-1次交易，最后一次交易取当前天），
第二个量则是取local第i-1天j次交易，然后加上今天的差值（这里因为local[i-1][j]比如包含第i-1天卖出的交易，所以现在变成第i天卖出，并不会增加
交易次数，而且这里无论diff是不是大于0都一定要加上，因为否则就不满足local[i][j]必须在最后一天卖出的条件了）。

局部（在第i天交易后，总共交易了j次） =  max{情况2，情况1}
情况1：在第i-1天时，恰好已经交易了j次（local[i-1][j]），那么如果i-1天到i天再交易一次：即在第i-1天买入，第i天卖出（diff），则这不并不会
增加交易次数！【例如我在第一天买入，第二天卖出；然后第二天又买入，第三天再卖出的行为  和   第一天买入，第三天卖出  的效果是一样的，其实只进
行了一次交易！因为有连续性】
情况2：第i-1天后，共交易了j-1次（global[i-1][j-1]），因此为了满足“第i天过后共进行了j次交易，且第i天必须进行交易”的条件：我们可以选择1：
在第i-1天买入，然后再第i天卖出（diff），或者选择在第i天买入，然后同样在第i天卖出（收益为0）。


上面的算法中对于天数需要一次扫描，而每次要对交易次数进行递推式求解，所以时间复杂度是O(n*k)，如果是最多进行两次交易，那么复杂度还是O(n)。空
间上只需要维护当天数据皆可以，所以是O(k)，当k=2，则是O(1)。
http://blog.csdn.NET/linhuanmars/article/details/23236995


========================================================================================================================


这道题实际上是之前那道 Best Time to Buy and Sell Stock III 买股票的最佳时间之三的一般情况的推广，还是需要用动态规划
Dynamic programming来解决，具体思路如下：

这里我们需要两个递推公式来分别更新两个变量local和global，参见网友Code Ganker的博客，我们其实可以求至少k次交易的最大利润。我们定义
local[i][j]为在到达第i天时最多可进行j次交易并且最后一次交易在最后一天卖出的最大利润，此为局部最优。然后我们定义global[i][j]为在到达第i天
时最多可进行j次交易的最大利润，此为全局最优。它们的递推式为：

local[i][j] = max(global[i - 1][j - 1] + max(diff, 0), local[i - 1][j] + diff)

global[i][j] = max(local[i][j], global[i - 1][j])，

其中局部最优值是比较前一天并少交易一次的全局最优加上大于0的差值，和前一天的局部最优加上差值后相比，两者之中取较大值，而全局最优比较局部最优
和前一天的全局最优。

但这道题还有个坑，就是如果k的值远大于prices的天数，比如k是好几百万，而prices的天数就为若干天的话，上面的DP解法就非常的没有效率，应该直接
用Best Time to Buy and Sell Stock II 买股票的最佳时间之二的方法来求解，所以实际上这道题是之前的二和三的综合体，代码如下：

class Solution {
public:
    int maxProfit(int k, vector<int> &prices) {
        if (prices.empty()) return 0;
        if (k >= prices.size()) return solveMaxProfit(prices);
        int g[k + 1] = {0};
        int l[k + 1] = {0};
        for (int i = 0; i < prices.size() - 1; ++i) {
            int diff = prices[i + 1] - prices[i];
            for (int j = k; j >= 1; --j) {
                l[j] = max(g[j - 1] + max(diff, 0), l[j] + diff);
                g[j] = max(g[j], l[j]);
            }
        }
        return g[k];
    }
    int solveMaxProfit(vector<int> &prices) {
        int res = 0;
        for (int i = 1; i < prices.size(); ++i) {
            if (prices[i] - prices[i - 1] > 0) {
                res += prices[i] - prices[i - 1];
            }
        }
        return res;
    }
};

========================================================================================================================

from Code_Ganker:


这道题是Best Time to Buy and Sell Stock的扩展，现在我们最多可以进行两次交易。我们仍然使用动态规划来完成，事实上可以解决非常通用的情况，
也就是最多进行k次交易的情况。
这里我们先解释最多可以进行k次交易的算法，然后最多进行两次我们只需要把k取成2即可。我们还是使用“局部最优和全局最优解法”。我们维护两种量，一个
是当前到达第i天可以最多进行j次交易，最好的利润是多少（global[i][j]），另一个是当前到达第i天，最多可进行j次交易，并且最后一次交易在当天卖
出的最好的利润是多少（local[i][j]）。下面我们来看递推式，全局的比较简单，
global[i][j]=max(local[i][j],global[i-1][j])，
也就是去当前局部最好的，和过往全局最好的中大的那个（因为最后一次交易如果包含当前天一定在局部最好的里面，否则一定在过往全局最优的里面）。对于
局部变量的维护，递推式是
local[i][j]=max(global[i-1][j-1]+max(diff,0),local[i-1][j]+diff)，
也就是看两个量，第一个是全局到i-1天进行j-1次交易，然后加上今天的交易，如果今天是赚钱的话（也就是前面只要j-1次交易，最后一次交易取当前天），
第二个量则是取local第i-1天j次交易，然后加上今天的差值（这里因为local[i-1][j]比如包含第i-1天卖出的交易，所以现在变成第i天卖出，并不会增加
交易次数，而且这里无论diff是不是大于0都一定要加上，因为否则就不满足local[i][j]必须在最后一天卖出的条件了）。
上面的算法中对于天数需要一次扫描，而每次要对交易次数进行递推式求解，所以时间复杂度是O(n*k)，如果是最多进行两次交易，那么复杂度还是O(n)。空
间上只需要维护当天数据皆可以，所以是O(k)，当k=2，则是O(1)。代码如下：

[java] view plain copy 在CODE上查看代码片派生到我的代码片
public int maxProfit(int[] prices) {
    if(prices==null || prices.length==0)
        return 0;
    int[] local = new int[3];
    int[] global = new int[3];
    for(int i=0;i<prices.length-1;i++)
    {
        int diff = prices[i+1]-prices[i];
        for(int j=2;j>=1;j--)
        {
            local[j] = Math.max(global[j-1]+(diff>0?diff:0), local[j]+diff);
            global[j] = Math.max(local[j],global[j]);
        }
    }
    return global[2];
}
可以看到，这里的模型是比较复杂的，主要是在递推式中，local和global是交替求解的。不过理清思路之后，代码是非常简练的，不禁感叹算法真是牛逼哈，
这么个复杂生活问题几行代码就解决了。


"""


#-*- coding:utf-8 -*-
#coding=utf-8