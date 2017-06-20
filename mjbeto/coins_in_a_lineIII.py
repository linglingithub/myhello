#coding=utf-8

import unittest

"""
There are n coins in a line. Two players take turns to take a coin from one of the ends of the line until there are 
no more coins left. The player with the larger amount of money wins.

Could you please decide the first player will win or lose?

Have you met this question in a real interview? Yes
Example
Given array A = [3,2,2], return true.

Given array A = [1,2,4], return true.

Given array A = [1,20,4], return false.

Challenge 
Follow Up Question:

If n is even. Is there any hacky algorithm that can decide whether first player will win or lose in O(1) memory and 
O(n) time?

Tags 
Dynamic Programming Array Game Theory
Related Problems 
Medium Coins in a Line II 32 %
Medium Coins in a Line

"""


class Solution:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):  # ref, passed

        n = len(values)
        if n <= 2:
            return True
        store = [[0 for _ in range(n)] for _ in range(n)]
        ssum = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                ssum[i][j] = values[j] if i == j else ssum[i][j-1] + values[j]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:
                    store[i][j] = values[i]
                else:
                    cur = min(store[i+1][j], store[i][j-1])
                    store[i][j] = ssum[i][j] - cur



        return store[0][n - 1] > ssum[0][n-1] - store[0][n - 1]




class Solution_TLE3:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):  #modification upon TLE2, which is similar to online way in java (accepted), still TLE for python
        # write your code here
        if not values:
            return 0
        n = len(values)
        if n <= 2:
            return True
        dp = [ [0 for _ in range(n)] for _ in range(n)]
        sum_cache = [[values for _ in range(n)] for _ in range(n)]
        visited = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                sum_cache[i][j] = values[j] if i==j else values[j] + sum_cache[i][j-1]

        total = sum(values)
        self.values = values
        first_sum = self.find_sum(0, n-1, dp, sum_cache, visited)
        return first_sum > total-first_sum

    def find_sum(self, left, right, dp, sum_cache, visited): #RuntimeError: maximum recursion depth exceeded in cmp in local
        if left > right:
            return 0
        if visited[left][right]:
            return dp[left][right]
        if left == right:
            visited[left][right] = True
            dp[left][right] = self.values[left]
            return self.values[left]
        if left + 1 == right:
            dp[left][right] = max(self.values[left], self.values[right])
            visited[left][right] = True
            return dp[left][right]
        else:

            dp[left][right] = sum_cache[left][right] - min(self.find_sum(left+1, right, dp, sum_cache, visited), self.find_sum(left, right-1, dp, sum_cache, visited))
            visited[left][right] = True
            return dp[left][right]


class Solution_TLE2:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):
        # write your code here
        if not values:
            return 0
        n = len(values)
        if n <= 2:
            return True
        dp = {}
        sum_cache = {}
        total = sum(values)
        self.values = values
        first_sum = self.find_sum(0, n-1, dp, sum_cache)
        return first_sum > total-first_sum

    def find_sum(self, left, right, dp, sum_cache):  #RuntimeError: maximum recursion depth exceeded in cmp in local
        if left > right:
            return 0
        if left == right:
            return self.values[left]
        if left + 1 == right:
           return max(self.values[left], self.values[right])
        if (left, right) in dp:
            return dp[(left, right)]
        if (left, right) in sum_cache:
            tmp_sum = sum_cache[(left, right)]
        else:
            sum_cache[(left,right)] = sum(self.values[left: right+1])
            tmp_sum = sum_cache[(left, right)]
        dp[(left, right)] = tmp_sum - min(self.find_sum(left+1, right, dp, sum_cache), self.find_sum(left, right-1, dp, sum_cache))
        return dp[(left, right)]



class Solution_TLE:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):
        # write your code here
        if not values:
            return 0
        n = len(values)
        if n <= 2:
            return True
        dp = {}
        total = sum(values)
        self.values = values
        first_sum = self.find_sum(0, n - 1, dp)
        return first_sum > total - first_sum

    def find_sum_TLE(self, left, right, dp): # state transfer has too many recursive call? try to write in a different way
        if left > right:
            return 0
        if left == right:
            return self.values[left]
        if left + 1 == right:
            return max(self.values[left], self.values[right])
        if (left, right) in dp:
            return dp[(left, right)]
        dp[(left, right)] = max(
            self.values[left] + min(self.find_sum(left + 2, right, dp), self.find_sum(left + 1, right - 1, dp)),
            self.values[right] + min(self.find_sum(left, right - 2, dp), self.find_sum(left + 1, right - 1, dp)))
        return dp[(left, right)]


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()


    def test_case4(self):  # ====> TLE with 73% cases passed, locally correct and takes nearly 3.5s
        from util.ini_file_util import IniFileUtil
        params = IniFileUtil.read_into_dict("coins_in_a_lineIII_case4.ini")
        A = IniFileUtil.string_to_int_list(params.get("values"))
        answer = True
        result = self.sol.firstWillWin(A)
        self.assertEqual(answer, result)


    def test_case3(self):
        A = [1,20,4]
        answer = False
        result = self.sol.firstWillWin(A)
        self.assertEqual(answer, result)


    def test_case2(self):
        A = [1,2,4]
        answer = True
        result = self.sol.firstWillWin(A)
        self.assertEqual(answer, result)

    def test_case1(self):
        A = [3,2,2]
        answer = True
        result = self.sol.firstWillWin(A)
        self.assertEqual(answer, result)



def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()
    # sol = Solution()
    # import sys
    # sys.setrecursionlimit(10000)
    # print sol.firstWillWin(9999)


#-*- coding:utf-8 -*-

"""

# a java version that can be accepted but not working in python

public class Solution {
    /**
     * @param values: an array of integers
     * @return: a boolean which equals to true if the first player will win
     */
    public boolean firstWillWin(int[] values) {
        // write your code here
        if(values == null || values.length == 0){
            return false;
        }

        int n = values.length;
        int[] sum = new int[n + 1];
        sum[0] = 0;
        for(int i = 1; i <= n; i++){
            sum[i] = sum[i - 1] + values[i - 1];
        }
        int[][] dp = new int[n + 1][n + 1];
        boolean[][] visit = new boolean[n + 1][n + 1];

        return search(1, n, sum, dp, visit) > sum[n] / 2;
    }

    private int search(int start, int end, int[] sum, int[][] dp, boolean[][] visit){
        if(visit[start][end]){
            return dp[start][end];
        }

        if(start == end){
            visit[start][end] = true;
            return dp[start][end] = sum[end] - sum[start - 1];
        }

        int max = (sum[end] - sum[start - 1]) - Math.min(search(start, end - 1, sum, dp, visit), search(start + 1, end, sum, dp, visit));

        visit[start][end] = true;
        dp[start][end] = max;
        return dp[start][end];
    }
}


========================================================================================================================

这道题的follow up 如果n是even的做法应该是什么？

是greedy, 每次都选两边最大的数么？

 (0)
2 个回复 


2016-01-26 九章管理员
是贪心法，不过不是你说的那种贪心法。（一般只顾眼前利益的贪心法都是错的，正如Triangle那题每次都挑小的一边走）

如果N是偶数的时候，把在奇数位置上的coin相加得到OddSum，把在偶数位置上的coin相加EvenSum。如果OddSum>EvenSum，那么从左边开始取，反之从右边。因为你取走一个奇数位置的coin之后，留给对手的两头都是原来的偶数位置的coin。反之亦然。

 (0)

2016-01-26 九章管理员
所以结论是，只要OddSum != EvenSum，那么先手必胜。如果OddSum == EvenSum，先手至少不输。


========================================================================================================================


public class Solution {
    public boolean firstWillWin(int[] values) {
        int len = values.length;
        if (len <= 1) {
            return true;
        }
        int[][] store = new int[len][len];
        int[][] sum = new int[len][len];
        for (int i = 0; i < len; i++) {
            for (int j = i; j < len; j++) {
                sum[i][j] = i == j ? values[j] : sum[i][j-1] + values[j];
            }
        }
        for (int i = len - 1; i >= 0; i--) {
            for (int j = i; j < len; j++) {
                if (i == j) {
                    store[i][j] = values[i];
                } else {
                    int cur = Math.min(store[i+1][j], store[i][j-1]);
                    store[i][j] = sum[i][j] - cur;
                }
            }
        }
        return store[0][len - 1] > sum[0][len-1] - store[0][len - 1];
    }
}



"""