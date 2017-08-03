#coding=utf-8

import unittest

"""

Paint House II

There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a 
certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is 
the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find 
the minimum cost to paint all houses.

 Notice

All costs are positive integers.

Have you met this question in a real interview? Yes
Example
Given n = 3, k = 3, costs = [[14,2,11],[11,14,5],[14,3,10]] return 10

house 0 is color 2, house 1 is color 3, house 2 is color 2, 2 + 5 + 3 = 10

Challenge 
Could you solve it in O(nk)?

Tags 
Dynamic Programming Facebook
Related Problems 
Hard Sliding Window Median 19 %
Medium Paint House 35 %
Easy Paint Fence 30 %
Super Sliding Window Maximum 27 %
Easy Product of Array Exclude Itself

"""



class Solution:
    # @param {int[][]} costs n x 3 cost matrix
    # @return {int} an integer, the minimum cost to paint all houses
    # Write your code here
    def minCostII(self, costs):
        if not costs or not costs[0]:
            return 0
        # dp init
        m, n = len(costs), len(costs[0])
        dp = [[costs[i][j] for j in range(n)] for i in range(m)]

        pre_row_min = []  # size of 2 should be good, save the idx of min vals

        for j in range(n):
            self.keep_min(pre_row_min, costs[0][j], j)

        # start calc
        for i in range(1, m):
            tmp_min = []
            for j in range(n):
                # minsum = -pre_row_min[0][0] if pre_row_min[0][1] != j else -pre_row_min[1][0]  # wrong , remember it's a max heap!!!
                minsum = -pre_row_min[1][0] if pre_row_min[1][1] != j else -pre_row_min[0][0]
                dp[i][j] = costs[i][j] + minsum
                self.keep_min(tmp_min, dp[i][j], j)
            pre_row_min = tmp_min
        # return min(dp[m-1])
        #return -pre_row_min[0][0] # wrong here , max heap!!!
        return -pre_row_min[1][0]


    def keep_min(self, pre_row_min, val, idx):
        import heapq
        if len(pre_row_min) == 2:
            tmp = pre_row_min[0]
            t1, t2 = -tmp[0], tmp[1]
            if val < t1:
                heapq.heappop(pre_row_min)
                heapq.heappush(pre_row_min, (-val, idx))
        else:
            heapq.heappush(pre_row_min, (-val, idx))






    def minCostII_TLE(self, costs): # TLE with 89% pass,
            # Write your code here
            if not costs or not costs[0]:
                return 0
            # dp init
            m, n = len(costs), len(costs[0])
            if m < 2:
                return min(costs[0])
            # !!! need to check when there is only ONE row, otherwise wrong!!!
            # use rolling array
            dp = [[costs[i][j] for j in range(n)] for i in range(2)]
            for i in range(1, m):
                for j in range(n):
                    dp[i%2][j] = costs[i][j] + min(x for x in dp[(i-1)%2][:j] + dp[(i-1)%2][j+1:])
            return min(dp[(m-1)%2])


    def minCostII1(self, costs):
        # Write your code here
        if not costs or not costs[0]:
            return 0
        # dp init
        m, n = len(costs), len(costs[0])
        dp = [[costs[i][j] for j in range(n)] for i in range(m)]
        for i in range(1, m):
            pre_row_min = dp[i][0]
            for j in range(n):
                dp[i][j] = costs[i][j] + min(x for x in dp[i-1][:j] + dp[i-1][j+1:])
        return min(dp[m-1])


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        costs = [[14,2,11],[11,14,5],[14,3,10]]
        answer = 10  # house 0 is blue, house 1 is green, house 2 is blue, 2 + 5 + 3 = 10
        result = self.sol.minCostII(costs)
        self.assertEqual(answer, result)

    def test_case2(self):  #====>
        costs = [[1,2,3]]
        answer = 1
        result = self.sol.minCostII(costs)
        self.assertEqual(answer, result)

    def test_case3(self):  #====> TLE, local runs wrong for not matching value, but ac online

        from util.ini_file_util import IniFileUtil
        params = IniFileUtil.read_into_dict("paint_houseII_case3.ini")
        nums = IniFileUtil.string_to_int_list_list(params.get("nums"))
        answer = int(params.get("answer"))
        result = self.sol.minCostII(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
"""

这道题是之前那道Paint House的拓展，那道题只让用红绿蓝三种颜色来粉刷房子，而这道题让我们用k种颜色，这道题不能用之前那题的解法，会TLE。这题
的解法的思路还是用DP，但是在找不同颜色的最小值不是遍历所有不同颜色，而是用min1和min2来记录之前房子的最小和第二小的花费的颜色，如果当前房子
颜色和min1相同，那么我们用min2对应的值计算，反之我们用min1对应的值，这种解法实际上也包含了求次小值的方法，感觉也是一种很棒的解题思路，参见
代码如下：

 

解法一：

复制代码
class Solution {
public:
    int minCostII(vector<vector<int>>& costs) {
        if (costs.empty() || costs[0].empty()) return 0;
        vector<vector<int>> dp = costs;
        int min1 = -1, min2 = -1;
        for (int i = 0; i < dp.size(); ++i) {
            int last1 = min1, last2 = min2;
            min1 = -1; min2 = -1;
            for (int j = 0; j < dp[i].size(); ++j) {
                if (j != last1) {
                    dp[i][j] += last1 < 0 ? 0 : dp[i - 1][last1];
                } else {
                    dp[i][j] += last2 < 0 ? 0 : dp[i - 1][last2];
                }
                if (min1 < 0 || dp[i][j] < dp[i][min1]) {
                    min2 = min1; min1 = j;
                } else if (min2 < 0 || dp[i][j] < dp[i][min2]) {
                    min2 = j;
                }
            }
        }
        return dp.back()[min1];
    }
};
复制代码
 

下面这种解法不需要建立二维dp数组，直接用三个变量就可以保存需要的信息即可，参见代码如下：

 

解法二：

复制代码
class Solution {
public:
    int minCostII(vector<vector<int>>& costs) {
        if (costs.empty() || costs[0].empty()) return 0;
        int min1 = 0, min2 = 0, idx1 = -1;
        for (int i = 0; i < costs.size(); ++i) {
            int m1 = INT_MAX, m2 = m1, id1 = -1;
            for (int j = 0; j < costs[i].size(); ++j) {
                int cost = costs[i][j] + (j == idx1 ? min2 : min1);
                if (cost < m1) {
                    m2 = m1; m1 = cost; id1 = j;
                } else if (cost < m2) {
                    m2 = cost;
                }
            }
            min1 = m1; min2 = m2; idx1 = id1;
        }
        return min1;
    }
};



"""