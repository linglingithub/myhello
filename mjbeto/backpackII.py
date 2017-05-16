#coding=utf-8

import unittest

"""
Backpack II

Given n items with size Ai and value Vi, and a backpack with size m. What's the maximum value can you put into the 
backpack?

 Notice

You cannot divide item into small pieces and the total size of items you choose should smaller or equal to m.

Have you met this question in a real interview? Yes
Example
Given 4 items with size [2, 3, 5, 7] and value [1, 5, 2, 4], and a backpack with size 10. The maximum value is 9.

Challenge
O(n x m) memory is acceptable, can you do it in O(m) memory?

Tags
LintCode Copyright Dynamic Programming Backpack
Related Problems
Medium Backpack VI 30 %
Medium Backpack V 44 %
Medium Backpack IV 40 %
Hard Backpack III 53 %
Medium Backpack

"""



class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A & V: Given n items with size A[i] and value V[i]
    # @return: The maximum value
    def backPackII(self, m, nums, vals):
        dp = [0 for _ in range(m+1)]
        for i in range(len(nums)):
            for j in range(m, 0, -1):
                weight = nums[i]
                val = vals[i]
                size = j
                if size >= weight:
                    dp[size] = max(dp[size], dp[size-weight] + val)
        #return max(dp)  # result can directly be dp[m]
        return dp[m]




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        vals = [1, 5, 2, 4]
        sizes = [2, 3, 5, 7]
        m = 10
        answer = 9
        result = self.sol.backPackII(m, sizes, vals)
        self.assertEqual(answer, result)



def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""
class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A & V: Given n items with size A[i] and value V[i]
    def backPackII(self, m, A, V):
        # write your code here
        f = [0 for i in xrange(m+1)]
        n = len(A)
        for i in range(n):
            for j in xrange(m, A[i]-1, -1):
                f[j] = max(f[j] , f[j-A[i]] + V[i])
        return f[m]


===================================================================================================================

https://zhengyang2015.gitbooks.io/lintcode/backpack_ii_125.html

和I类似。 value[i][j]表示容量为i的背包在前j件物品中能取的最大价值。分两种情况考虑：不要第j件物品，则value[i][j] = value[i][j-1]；要
第j件物品，则value[i][j]=value[i－A［j］][j-1]+V[j]，这种情况要求i-A[j]>=0。取两种情况里面较大的作为value[i][j]的值。这种方法空间复
杂度为O(n * m)。
第二种方法可以将空间复杂度优化到O(m)。f[j]表示背包容量为j时在前i件物品中能够选取的最大价值。到第i件物品时，考虑第i件物品装还是不装。背包容
量j从最大的容量m开始依次递减遍历，只考虑更新背包容量大于A[i]的情况，即加上V[i]之后是否结果会更优，背包容量小于A[i]的情况不用考虑因为第i件
物品根本装不进此时容量的背包。若结果更优，则更新此时的f[j]（即装第i件物品时情况更优），否则不变（即不装第i件物品时情况更优）。因为f会记录i
之前所有的最优情况，因此只需要m空间即可。物品从0遍历到n－1，即可求出前n件物品的最优值。
其实第二种方法相当于使用滚动数组。因为状态函数为
value[i][j]=max(value[i－A［j］][j-1]+V[j], value[i][j-1])
可以看出只和j－1有关，因此保存两行信息就足够了。使用滚动数组必须逐行填写，因为在计算下一行的时候需要上一行的信息，像第一种方法中那样逐列填写
就不行。



"""

#-*- coding:utf-8 -*-
