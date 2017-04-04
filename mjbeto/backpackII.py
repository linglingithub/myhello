#coding=utf-8

import unittest

"""
Backpack


Given n items with size Ai, an integer m denotes the size of a backpack. How full you can fill this backpack?

 Notice

You can not divide any item into small pieces.

Have you met this question in a real interview? Yes
Example
If we have 4 items with size [2, 3, 5, 7], the backpack size is 11, we can select [2, 3, 5], so that the max size we
can fill this backpack is 10. If the backpack size is 12. we can select [2, 3, 7] so that we can fulfill the backpack.

You function should return the max size we can fill in the given backpack.

Challenge
O(n x m) time and O(m) memory.

O(n x m) memory is also acceptable if you do not know how to optimize memory.

Tags
LintCode Copyright Dynamic Programming Backpack
Related Problems
Medium Backpack VI 30 %
Medium Backpack V 44 %
Medium Backpack IV 40 %
Hard Backpack III 53 %
Medium Number of Ways to Represent N Cents 27 %
Medium Backpack II

"""



class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def backPack(self, m, nums):
        # write your code here
        if not nums or m <= 0:
            return 0
        dp = [0 for _ in range(m+1)]
        nums.sort()
        for size in range(1,m+1):
            for j in range(len(nums)):
                if size < nums[j]:
                    break
                elif size == nums[j]:
                    dp[size] = size
                else:
                    #dp[size] = max(dp[size], (dp[j] + dp[size-j]))
                    dp[size] = max(dp[size], (dp[nums[j]] + dp[size-nums[j]]))
        return dp[m]





class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [2,4,5,7]
        m = 6
        answer = 6
        result = self.sol.backPack(m, nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [2,4,5,7]
        m = 12
        answer = 12
        result = self.sol.backPack(m, nums)
        self.assertEqual(answer, result)

    def test_case3(self):
        nums = [2,4,5,7]
        m = 10
        answer = 9
        result = self.sol.backPack(m, nums)
        self.assertEqual(answer, result)

    def test_case4(self):
        nums = [2,4,5,7]
        m = 13
        answer = 13
        result = self.sol.backPack(m, nums)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""

动规经典题目，用数组dp[i]表示书包空间为i的时候能装的A物品最大容量。两次循环，外部遍历数组A，内部反向遍历数组dp，若j即背包容量大于等于物品
体积A[i]，则取前i-1次循环求得的最大容量dp[j]，和背包体积为j-A[i]时的最大容量dp[j-A[i]]与第i个物品体积A[i]之和即dp[j-A[i]]+A[i]的较大
值，作为本次循环后的最大容量dp[i]。

注意dp[]的空间要给m+1，因为我们要求的是第m+1个值dp[m]，否则会抛出OutOfBoundException。

"""

#-*- coding:utf-8 -*-
