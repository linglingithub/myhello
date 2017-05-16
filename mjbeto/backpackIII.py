#coding=utf-8

import unittest

"""
Backpack III

Given n kind of items with size Ai and value Vi( each item has an infinite number available) and a backpack with size m. 
What's the maximum value can you put into the backpack?

 Notice

You cannot divide item into small pieces and the total size of items you choose should smaller or equal to m.

Have you met this question in a real interview? Yes
Example
Given 4 items with size [2, 3, 5, 7] and value [1, 5, 2, 4], and a backpack with size 10. The maximum value is 15.

Tags 
Dynamic Programming
Related Problems 
Medium Partition Equal Subset Sum 29 %
Medium Backpack VI 30 %
Medium Backpack V 45 %
Medium Backpack IV 41 %
Medium Backpack II 39 %
Medium Backpack
"""



class Solution:
    # @param {int[]} A an integer array
    # @param {int[]} V an integer array
    # @param {int} m an integer
    # @return {int} an array
    def backPackIII(self, nums, vals, m): #1105ms, 758ms
        # Write your code here
        dp = [0 for _ in range(m+1)]
        self.fill(nums, vals, m, dp)
        return dp[m]

    def fill(self, nums, vals, size, dp):
        if size == 0 or size>0 and dp[size] != 0:
            return dp[size]
        for i in range(len(nums)):
            weight = nums[i]
            val = vals[i]
            if size >= weight:
                dp[size] = max(self.fill(nums, vals, size-weight, dp) + val, dp[size])
        return dp[size]  # don't forget to return value here






class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [2, 3, 5, 7]
        vals = [1, 5, 2, 4]
        m = 10
        answer = 15
        result = self.sol.backPackIII(nums, vals, m)
        self.assertEqual(answer, result)



def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""

Following is a very simple and smart way

class Solution:
    # @param {int[]} A an integer array
    # @param {int[]} V an integer array
    # @param {int} m an integer
    # @return {int} an array
    def backPackIII(self, A, V, m):  #590ms
        # Write your code here
        f = [0 for i in xrange(m+1)]
        for (a, v) in zip(A, V):
            for j in xrange(a, m+1):
                if f[j - a] + v > f[j]:
                    f[j] = f[j - a] + v
        return f[m]
        

===================================================================================================================

https://zhengyang2015.gitbooks.io/lintcode/backpack_iii_440.html

这道题和II的思想一样，f[j]表示容量为j的背包对前i件物品能取的最大值，其中物品可以重复选取。对物品从0遍历到n－1，每次只有比A[i]大的背包容量
才有可能被更新。
和II不同的是，这道题物品可以重复选择，所以内层遍历j的时候从小到大遍历，这样物品可以重复选取。比如一开始在j的时候取了i，然后随着j的增大，在
j'的时候又取了i，而恰好j = j' - A[i]，在这种情况下i就被重复选取。如果从大往小遍历则所有物品只能取一次，所以II中是从大往小遍历。
因此可以重复取元素则背包容量从小到大遍历，反之从大到小遍历。

        
"""

#-*- coding:utf-8 -*-
