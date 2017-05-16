#coding=utf-8

import unittest

"""
Backpack IV

Given n items with size nums[i] which an integer array and all positive numbers, no duplicates. An integer target 
denotes the size of a backpack. Find the number of possible fill the backpack.

Each item may be chosen unlimited number of times

Have you met this question in a real interview? Yes
Example
Given candidate items [2,3,6,7] and target 7,

A solution set is: 
[7]
[2, 2, 3]
return 2

Tags 
Dynamic Programming
Related Problems 
Medium Partition Equal Subset Sum 29 %
Medium Backpack VI 30 %
Medium Backpack V 45 %
Hard Backpack III 54 %
Medium Backpack II 39 %
Medium Backpack


"""


class Solution:
    # @param {int[]} nums an integer array and all positive numbers, no duplicates
    # @param {int} target an integer
    # @return {int} an integer

    def backPackIV(self, nums, target): #ref
        m = target
        n = len(nums)
        dp = [ [0 for _ in range(m+1)] for _ in range(n+1)]
        dp[0][0] = 1

        for i in range(1, n+1):
            for j in range(m+1):
                k = 0
                stone = nums[i-1]
                while k*stone <= j:
                    dp[i][j] += dp[i-1][j-stone* k]
                    k += 1
        return dp[n][m]

    def backPackIV_ref(self, nums, target):
        # Write your code here
        dp = [0 for i in xrange(target + 1)]
        dp[0] = 1
        for i in nums:
            for j in xrange(i, target + 1):
                stone, size = i, j
                dp[size] += dp[size - stone]

        return dp[target]


    def backPackIV_wrong(self, nums, target):
        # Write your code here
        dp = [0 for _ in range(target+1)]
        for i in range(1, target + 1):
            size = i
            checked = [False for _ in range(size + 1)]
            for j in range(len(nums)):
                stone = nums[j]
                if stone == i:
                    dp[stone] += 1
                elif stone < i and not checked[stone] and not checked[i-stone]:
                    # still has repeated combination, 7 = 2+5(2+3), 3+4(2+2)
                    dp[i] += dp[i-stone]
                    checked[stone], checked[i-stone] = True, True
        return dp[target]


    def backPackIV_wrong(self, nums, target):
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        self.fill(nums, target, dp)
        return dp[target]

    def fill(self, nums, size, dp):
        if dp[size] != 0:
            return dp[size]
        checked = [False for _ in range(size+1)]
        for stone in nums:
            if stone <= size:
                dp[size] += dp[size-stone] if not checked[size-stone] else 0
                checked[stone] = True
                checked[size-stone] = True
        return dp[size]


    def backPackIV_wrong(self, nums, target):
        # Write your code here
        dp = [0 for _ in range(target+1)]
        for i in range(1, target + 1):
            for j in range(len(nums)):
                size = i
                stone = nums[j]
                if stone == i:
                    dp[stone] += 1
                elif stone < i:
                    dp[i] += dp[i-stone]  # check when size = 5, here 2+3 and 3+ 2 will be double counted, need to avoid
        return dp[target]





class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [2,3,6,7]
        target = 7
        answer = 2  #[[2,2,3], [7]]
        result = self.sol.backPackIV(nums, target)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [1, 2, 4]
        target = 4
        answer = 4 # [ [1,1,1,1], [1,1,2], [2,2], [4]]
        result = self.sol.backPackIV(nums, target)
        self.assertEqual(answer, result)



def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""

https://zhengyang2015.gitbooks.io/lintcode/backpack_iv_562.html

这道题思路和III几乎一样，dp[j]表示背包容量为j时，对前i中物品来说能填满背包的方法数。当前元素为i时，背包容量大于等于nums[i]的才有可能被更
新。此时，对于j容量的背包，其新的方法数为前i－1件物品能装满j容量背包的方法数（即不装第i件物品的方法数）＋前i-1件物品能装满j-nums[i]容量的
背包的方法数（即装第i件物品的方法数）。这里状态方程只是把III中的max改成了+。所有求总共有多少种方法的题都可以从最大值问题变换max为+得到。
因此，状态函数为：
dp[j] = dp[j] + dp[j - nums[i]] (右边的dp[j]表示上一行中（即i－1件物品）能装满j容量的方法数)

==============================================================================================================================


class Solution:
    # @param {int[]} nums an integer array and all positive numbers, no duplicates
    # @param {int} target an integer
    # @return {int} an integer
    def backPackIV(self, nums, target):
        # Write your code here
        dp = [0 for i in xrange(target + 1)]
        dp[0] = 1
        
        for a in nums:
            for j in xrange(a, target+1):
                dp[j] += dp[j - a]

        return dp[target]
        
==============================================================================================================================
        

// 方法一
public class Solution {
    /**
     * @param nums an integer array and all positive numbers, no duplicates
     * @param target an integer
     * @return an integer
     */
    public int backPackIV(int[] nums, int target) {
        // Write your code here
        int m = target;
        int []A = nums;
        int f[][] = new int[A.length + 1][m + 1];
        
        f[0][0] = 1;
        for (int i = 1; i <= A.length; i++) {
            for (int j = 0; j <= m; j++) {
                int k = 0; 
                while(k * A[i-1] <= j) {
                    f[i][j] += f[i-1][j-A[i-1]*k];
                    k+=1;
                }
            } // for j
        } // for i    
        return f[A.length][target];
    }
}


// 方法二

public class Solution {
    /**
     * @param nums an integer array and all positive numbers, no duplicates
     * @param target an integer
     * @return an integer
     */
    public int backPackIV(int[] nums, int target) {
        // Write your code here
        int[] f = new int[target + 1];
        f[0] = 1;
        for (int i = 0; i < nums.length; ++i)
            for (int  j = nums[i]; j <= target; ++j)
                f[j] += f[j - nums[i]];

        return f[target];
    }
}        
        
"""

#-*- coding:utf-8 -*-
