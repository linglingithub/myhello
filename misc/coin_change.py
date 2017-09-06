#coding=utf-8

import unittest

"""

322. Coin Change

You are given coins of different denominations and a total amount of money amount. Write a function to compute the 
fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any 
combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

Difficulty:Medium
Total Accepted:67.6K
Total Submissions:254.3K
Contributor:


Related Topics 
Dynamic Programming 

"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins:
            return -1
        import sys
        dp = [sys.maxsize for _ in range(amount+1)]
        dp[0] = 0
        for val in range(1, amount+1):
            for coin in coins:
                if val-coin >= 0:
                    dp[val] = min(dp[val], dp[val-coin]+1)
        return dp[amount] if dp[amount]!=sys.maxsize else -1


class Solution1(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins or amount <= 0:
            return 0  # test case require 0 , not -1,  input [1], 0, output 0, diff from problem statement
        import sys
        dp = [sys.maxsize for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):  # end point should be +1, not amount itself
            for coin in coins:
                if 0 <= i - coin:  # need to check this, otherwise can inlist index out of range
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        # can't do this, because coin of a vale is not limited, can have multiple one
        # for coin in coins:
        #     if coin <= amount:
        #         dp[coin] = 1
        #     for j in range(coin+1, amount-coin+1):
        #         if dp[j] == -1:
        #             dp[j] = dp[j-coin] + 1 if dp[j-coin]  != -1 else -1
        #         else:
        #             dp[j] = min(dp[j], dp[j-coin] + 1)
        return dp[amount] if dp[amount] != sys.maxsize else -1  # need to add check for if


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1, 2, 5]
        amount = 11
        answer = 3  # 11 = 5 + 5 + 1
        result = self.sol.coinChange(nums, amount)
        self.assertEqual(answer, result)


    def test_case2(self):
        nums = [2]
        amount = 3
        answer = -1
        result = self.sol.coinChange(nums, amount)
        self.assertEqual(answer, result)

    def test_case3(self):   # ====>
        nums = [1]
        amount = 0
        answer = 0
        result = self.sol.coinChange(nums, amount)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
