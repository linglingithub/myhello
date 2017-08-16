#coding=utf-8

import unittest

"""
Post Office Problem 

 Description
 Notes
 Testcase
 Judge
On one line there are n houses. Give you an array of integer means the the position of each house. Now you need to pick 
k position to build k post office, so that the sum distance of each house to the nearest post office is the smallest. 
Return the least possible sum of all distances between each village and its nearest post office.

Have you met this question in a real interview? Yes
Example
Given array a = [1,2,3,4,5], k = 2.
return 3.

Challenge 
Could you solve this problem in O(n^2) time ?

"""


class Solution:
    """
    @param: A: an integer array
    @param: k: An integer
    @return: an integer
    """
    def postOffice(self, A, k): # ref idea, use dp
        # if no houses, or number of post offices can be bigger than number of houses, return 0
        if not A or k >= len(A):
            return 0
        n = len(A)
        A.sort()
        # for first i houses, build j post offices, the min distance sum
        dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
        # for ith house to jth house, build one post office, the distance sum
        dis = [[0 for _ in range(n+1)] for _ in range(n+1)]
        self.init_dis(A, dis)

        # if only one post office is built, the init status of dp
        for i in range(n+1):
            dp[i][1] = dis[1][i]

        # when 2 or more post offices are built, populate dp
        import sys
        for office_cnt in range(2, k+1):
            for house_cnt in range(office_cnt, n+1):
                dp[house_cnt][office_cnt] = sys.maxint
                for j in range(house_cnt):
                    tmp = dp[j][office_cnt-1] + dis[j+1][house_cnt]
                    dp[house_cnt][office_cnt] = min(tmp, dp[house_cnt][office_cnt])

        # return result
        return dp[n][k]

    def init_dis(self, A, dis):
        n = len(A)
        for i in range(n+1):
            for j in range(i+1, n+1):
                #mid = (A[i] + A[j]) / 2
                mid = (i+j)/2
                tmp = 0
                for k in range(i, j+1):
                    #tmp += abs(A[k]-mid)
                    tmp += abs(A[k-1]-A[mid-1])
                dis[i][j] = tmp






class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,2,3,4,5]
        k = 2
        answer = 3
        result = self.sol.postOffice(nums, k)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()


"""
dp[i][l] 表示在前i個村莊建l間郵局的最小距離和
状态函数：
dp[i][l]＝dp[j][l-1] + dis[j+1][i] (l-1<=j<i)。
其中
dp[i][l]表示在前i个村庄中建l个post的最短距离，
dis[j+1][i] 表示在第j+1個村莊與第i個房子中間造一間郵局的情況下，所有村莊到郵局的距離和
j为分隔点，可以将问题转化为在前j个村庄建l－1个post的最短距离＋在第j＋1到第i个村庄建1个post的最短距离。
其中有个性质，如元素是单调排列的，则在中间位置到各个元素的距离和最小。因此計算dis[i][j]的方式：
先求得i 與 j 的中點 mid = (i + j) / 2
接著把所有i 與 j 中間所有村莊與郵局的距離加總起來即可

1. 初始化dis矩阵，枚举不同开头和结尾的村庄之间建1个post的最小距离，即求出开头和结尾村庄的中间点，然后计算开头到结尾的所有点到中间点的距离。
记得要对原矩阵排序，这样才能用中间点距离最小性质。
2. 初始化dp矩阵，即初始化dp[i][1]，求前i个村庄建1个post的最小距离（可根据dis求出）。
3. post数l从2枚举到k，开始村庄i从l枚举到结尾（因为要建l个post至少需要l个村庄，否则没有意义），然后根据状态函数求dp[i][l]，
分割点j从l－1枚举到i-1（前j个村庄建l－1个post则至少需要l－1个村庄），在这些分隔点的情况下求dp[i][l]的最小值。
4.返回dp[n][k]即可。

from jiuzhang wenda

class Solution {
public:
    int postOffice(vector<int>& A, int k) {
        // Write your code 
        int n  = A.size();
        if (n == 0 || k >= n) {
            return 0;
        }

        sort(A.begin(), A.end());
        vector<vector<int>> costs(n+1, vector<int>(n+1, 0));
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                int mid = A[i + (j - i) / 2 - 1 ];
                for (int l = i; l <= j; l++) {
                    costs[i][j] += abs(A[l - 1] - mid); 
                }
            }
        }

        vector<vector<int>> dp(n+1, vector<int>(k+1, INT_MAX)); // 前i个村子修k个邮局的代价

        for (int j = 0; j <= k; j++) {
            dp[0][j] = 0;
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j < i && j <= k; j++) {
                for (int l = 0; l < i; l++) {
                    if (dp[l][j - 1] != INT_MAX) {
                        dp[i][j] = min(dp[i][j], dp[l][j - 1] + costs[l + 1][i]);
                    }
                }
            }
        }
        return dp[n][k];
    }
};

马克助教
答案中应用了四边形不等式优化，复杂度是O(n^2)， 如果不用四边形不等式优化复杂度是O(kn^2)。
四边形不等式不要求掌握，证明这个题目满足使用四边形不等式的要求就比较难，不推荐。


"""
#-*- coding:utf-8 -*-
