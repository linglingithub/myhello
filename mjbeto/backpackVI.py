#coding=utf-8

import unittest

"""
Backpack VI

Given an integer array nums with all positive numbers and no duplicates, find the number of possible combinations that 
add up to a positive integer target.

 Notice

A number in the array can be used multiple times in the combination. 
Different orders are counted as different combinations.

Have you met this question in a real interview? Yes
Example
Given nums = [1, 2, 4], target = 4

The possible combination ways are:
[1, 1, 1, 1]
[1, 1, 2]
[1, 2, 1]
[2, 1, 1]
[2, 2]
[4]
return 6

Tags 
Dynamic Programming
Related Problems 
Medium Backpack V 45 %
Medium Backpack IV 41 %
Hard Backpack III 54 %
Medium Backpack II 39 %
Medium Backpack

"""


class Solution:
    # @param {int[]} nums an integer array and all positive numbers, no duplicates
    # @param {int} target an integer
    # @return {int} an integer
    def backPackVI(self, nums, target):
        """
        Compare this with backpack IV
        :param nums: 
        :param target: 
        :return: 
        """
        # Write your code here
        dp = [0 for i in xrange(target + 1)]
        dp[0] = 1
        for i in xrange(1, target + 1):
            for j in nums:
                stone, size = j, i
                if stone <= size:
                    dp[size] += dp[size - stone]
        return dp[target]



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,2,3,]
        target = 3
        answer = 4  #[ [1,1,1], [1,2], [2,1], [3]]
        result = self.sol.backPackVI(nums, target)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [1, 2, 4]
        target = 4
        answer = 6 # [[1,1,1,1], [1,1,2], [1,2,1], [2,1,1], [2,2], [4]]
        result = self.sol.backPackVI(nums, target)
        self.assertEqual(answer, result)



def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""

class Solution:
    # @param {int[]} nums an integer array and all positive numbers, no duplicates
    # @param {int} target an integer
    # @return {int} an integer
    def backPackVI(self, nums, target):
        # Write your code here
        dp = [0 for i in xrange(target + 1)]
        dp[0] = 1
        
        for j in xrange(1, target+1):
            for a in nums:
                if j >= a:
                    dp[j] += dp[j - a]
        return dp[target]

===================================================================================================================

https://zhengyang2015.gitbooks.io/lintcode/backpack_vi_564.html


dp[j]表示背包容量为j时，数组nums能装满j的方法数量。
可以想到的方法是对于当前背包容量j，假设最后加入的元素为当前遍历的元素i，则将i元素最后加入的方法数量为dp[j - nums[i]]（此时要求j - nums[i] >= 0），将数组元素全部遍历当过i为止。其中，初始化dp[0]=1，表示数组元素将容量为0的背包装满的方法数为1（即什么元素都不取这一种方法）。
这道题并不难，但需要注意要和IV，V的区别。IV，V中的方法和元素位置有关系，元素的相对位置不能变化，不能先取后面的元素再取前面的元素，即相同元素组成的方法被视为一种方法（就算排列不同），其dp[j]的含义为前i件物品装满容量j的方法数，因此只和i之前的物品相关，而和i之后的物品无关。这道题则说明不同的顺序被认为是不同的方法，因此和元素位置无关，可以先取后面的元素再取前面的元素，即相同元素的不同排列被视为不同的方法，其dp[j]表示的是数组nums装满容量j的方法数，是和数组中所有元素有关。
之前几题能够用一维dp表示的本质其实是因为当前行的值只和上一行有关，因此用动态数组两行就行，如果直接在上一行更新当前行的状态则只需要一行即可，因此其本质就是还是二维dp。但是这道题真的是一维dp，即当前容量的填装数量只和之前容量填装的结果有关，只不过每次填装都要遍历整个nums数组来寻找相关的之前容量的状态，因此要用两重for循环。

        
"""

#-*- coding:utf-8 -*-
