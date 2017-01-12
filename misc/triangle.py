#coding=utf-8
__author__ = 'linglin'



"""
120. Triangle

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

Subscribe to see which companies asked this question

Hide Tags Array Dynamic Programming

Medium

"""

import unittest


class Solution(object):
    def minimumTotal(self, triangle): #52ms, 57%
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return -1
        dp = [0 for x in range(len(triangle[-1]))]
        dp[0] = triangle[0][0]
        if len(triangle) >= 2:
            dp[1] = dp[0] + triangle[1][1]
            dp[0] = dp[0] + triangle[1][0]
        for row in triangle[2:]:
            cnt = len(row)
            dp[cnt-1] = dp[cnt-2]+row[cnt-1]
            for i in range(cnt-2,0,-1):
                dp[i] = row[i] + min(dp[i],dp[i-1])
            dp[0] += row[0]

        return min(dp)

    def minimumTotal_ref(self, triangle): # O(1) space, use bottom-up way , use input as storage, 49ms, 71%
        for i in range(len(triangle)-2,-1,-1):
            for j in range(0,i+1):
                triangle[i][j] += min(triangle[i+1][j],triangle[i+1][j+1])
        return triangle[0][0]

    def minimumTotal_ref2(self, triangle): # similar to ref1, 52ms, 58%
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        dp = triangle[-1]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
        return dp[0]


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [
             [2],
            [3,4],
           [6,5,7],
          [4,1,8,3]
        ]
        answer = 11
        result = self.sol.minimumTotal(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""

这题要求我们求出一个三角形中从顶到底最小路径和，并且要求只能使用O(n)的空间。

这题有两种解法，自顶向下以及自底向上。

首先来看自顶向下，根据题目我们知道，每向下一层，我们只能选择邻接数字进行累加，譬如上面第1行的数字3，它的下一行邻接数字就是6和5。

我们假设dp[m][n]保存了第m行第n个节点的最小路径和，我们有如下dp方程

dp[m + 1][n] = min(dp[m][n], dp[m][n - 1]) + triangle[m + 1][n] if n > 0
dp[m + 1][0] = dp[m][0] + triangle[m + 1][0]
因为只能使用O(n)的空间，所以我们需要滚动计算，使用一个一位数组保存每层的最小路径和，参考Pascal's Triangle，我们知道，为了防止计算的时候
不覆盖以前的值，所以我们需要从后往前计算。


区别于自顶向下，另一种更简单的做法就是自底向上了。dp方程为

dp[m][n] = min(dp[m + 1][n], dp[m + 1][n + 1]) + triangle[m][n]

我们仍然可以使用一位数组滚动计算。



"""

#-*- coding:utf-8 -*-
