#coding=utf-8

import unittest

"""

518. Coin Change 2

ou are given coins of different denominations and a total amount of money. Write a function to compute the number of 
combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

Note: You can assume that

0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer
Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10] 
Output: 1


Difficulty:Medium
Total Accepted:6.2K
Total Submissions:19.1K
Contributor: vchernoy


"""

class Solution(object):
    def change(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        if amount == 0:
            return 1    # note this case, require to return 1
        if not coins:
            return 0
        dp = [0 for _ in range(amount+1)]
        dp[0] = 1   #!!! should be 1 here, otherwise wrong
        for coin in coins:
            for val in range(1, amount+1):
                if val - coin >= 0:
                    dp[val] += dp[val-coin]
        return dp[amount]





class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1, 2, 5]
        amount = 5
        answer = 4  # 5; 2+2+1; 2+1+1+1; 1*5
        result = self.sol.change(nums, amount)
        self.assertEqual(answer, result)


    def test_case2(self):
        nums = [2]
        amount = 3
        answer = 0
        result = self.sol.change(nums, amount)
        self.assertEqual(answer, result)

    def test_case3(self):
        nums = [10]
        amount = 10
        answer = 1
        result = self.sol.change(nums, amount)
        self.assertEqual(answer, result)

    def test_case4(self):   # ====>
        nums = []
        amount = 0
        answer = 1
        result = self.sol.change(nums, amount)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
