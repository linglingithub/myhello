#coding=utf-8

import unittest

"""

312. Burst Balloons
DescriptionHintsSubmissionsDiscussSolution
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums.
You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right]
coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:

Input: [3,1,5,8]
Output: 167
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

Difficulty:Hard
Total Accepted:39.9K
Total Submissions:90.9K
Contributor:dietpepsi
Companies

Related Topics


"""


class Solution(object):
    def maxCoins(self, nums):
        """
        Basic idea:
        [a] ==> a
        [a, b] ==> max(a * b + b, a * b + a)
        [a, b, c] ==> max(a*b + dp[b..c], a*b*c + dp[a] + dp[b], dp[a..b] + b*c)
        basic idea:
        find all possible solutions with dp to memorize calculated result
        dp[i][j]: the max coins you can get from ballons ranging [i:j]
        dp[i][j] = max([dp[i][k - 1] + coins[k - 1]*[k]*[k+1] + dp[k + 1][j]] for all i <= k <= j) ==> WRONG??
        !!! should be ==>
        dp[i][j] = max(dp[i][k - 1] + coins[i - 1]*[k]*[j + 1] for all i <= k <= j)
            --- dp[x][y] means [x:y] are bursted, and thus [k] is left as LAST step, NOT the FIRST and then merge
            --- this way, dp[][] physical meaning holds true
        ==> add surrounding [1] to both ends of input array, and i , j work on [1..len(nums)]
        base case: dp[i][i] = balloons[i] ==> THIS is not TRUE, single balloon can have DIFFERENT neighbor, not as single

        Time: O(n^3)
        Space: O(n^2)



        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        nums = [1] + nums + [1]
        # init the dp
        dp = [[0 for j in range(n + 2)] for _ in range(n + 2)]
        self.helper(nums, 1, n, dp)
        return dp[1][n]

    def helper(self, nums, left, right, dp):
        # if left > right:
        #     return 0     # alreay init as 0, not necessary
        if dp[left][right] > 0:
            return dp[left][right]
        # if left == right:
        #     dp[left][right] = nums[left]
        #     return dp[left][right]     # can be covered by the following loop, not necessary
        for k in range(left, right + 1):
            dp[left][right] = max(dp[left][right], nums[left - 1] * nums[k] * nums[right + 1]
                                  + self.helper(nums, left, k - 1, dp)
                                  + self.helper(nums, k + 1, right, dp))
        return dp[left][right]


class Solution_TLE(object):
    """
    choose k as the FIRST balloon to burst and need to handle left and right part merge issue.
    """
    def maxCoins(self, nums):
        if not nums:
            return 0
        n = len(nums)
        nums = [1] + nums + [1]
        # init the dp
        cache = {}
        return self.helper(nums, self._gen_key([x for x in range(1, n + 1)]), cache)

    def helper(self, nums, key, cache):
        if key in cache:
            return cache[key]
        if key == "":
            return 0
        idx_list = self._parse_key(key)
        cur_max = 0
        idx_list = [0] + idx_list + [len(nums) - 1] # add for easy boundary processing
        for k in range(1, len(idx_list) - 1):
            mid = k #idx_list[k]
            tmp = nums[idx_list[mid - 1]] * nums[idx_list[mid]] * nums[idx_list[mid + 1]]
            tmp_key = self._gen_key(idx_list[1 : mid] + idx_list[mid + 1: len(idx_list) - 1])
            tmp += self.helper(nums, tmp_key, cache)
            cur_max = max(cur_max, tmp)
        cache[key] = cur_max
        return cache[key]

    def _gen_key(self, idx_list):
        return ",".join([str(x) for x in idx_list])

    def _parse_key(self, keystr):
        return [int(x) for x in keystr.split(",")]




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [3,1,5,8]
        answer = 167
        result = self.sol.maxCoins(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()


"""

https://www.hrwhisper.me/leetcode-burst-balloons/

class Solution(object):
    def maxCoins(self, nums):

        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0 for j in xrange(n + 2)] for i in xrange(n + 2)]

        def DP(i, j):
            if dp[i][j] > 0: return dp[i][j]
            for x in xrange(i, j + 1):
                dp[i][j] = max(dp[i][j],DP(i, x - 1) + nums[i - 1] * nums[x] * nums[j + 1]+ DP(x + 1, j))
            return dp[i][j]
        return DP(1,n)


public class Solution {
    public int maxCoins(int[] iNums) {
        int n = iNums.length;
        int[] nums = new int[n + 2];
        for (int i = 0; i < n; i++) nums[i + 1] = iNums[i];
        nums[0] = nums[n + 1] = 1;
        int[][] dp = new int[n + 2][n + 2];
        for (int k = 1; k <= n; k++) {
            for (int i = 1; i <= n - k + 1; i++) {
                int j = i + k - 1;
                for (int x = i; x <= j; x++) {
                    dp[i][j] = Math.max(dp[i][j], dp[i][x - 1] + nums[i - 1] * nums[x] * nums[j + 1] + dp[x + 1][j]);
                }
            }
        }
        return dp[1][n];
    }
}


"""


#-*- coding:utf-8 -*-
