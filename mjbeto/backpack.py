#coding=utf-8

import unittest
from util.ini_file_util import IniFileUtil

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

    def backPack(self, m, nums): # MLE at case 5, pass case 6
        """
        use dp[i][j] to record whether previous i stones can make a size j (total weight is j), 1 yes, 0 not.
        :param m: 
        :param nums: 
        :return: 
        """
        n = len(nums)
        dp = [0 for _ in range(m+1)]
        for i in range(n):
            for j in range(m, 0, -1):
                size = j
                stone = nums[i]
                if size == stone or size>stone and dp[size-stone] == 1 or dp[j] == 1:
                    # need to add dp[i-1][j] here, otherwise wrong, means if previous stones can mke the way, one more stone also can
                    dp[j] = 1
                else:
                    dp[j] = 0
        for size in range(m, 0, -1):
            if dp[size] == 1:
                return size
        return 0


    def backPack_MLEcase5(self, m, nums): # MLE at case 5, pass case 6
        """
        use dp[i][j] to record whether previous i stones can make a size j (total weight is j), 1 yes, 0 not.
        :param m: 
        :param nums: 
        :return: 
        """
        n = len(nums)
        dp = [ [0 for _ in range(m+1)] for _ in range(n)]
        for i in range(n):
            for j in range(1, m+1):
                size = j
                stone = nums[i]
                if size == stone or size>stone and dp[i-1][size-stone] == 1 or dp[i-1][j] == 1:
                    # need to add dp[i-1][j] here, otherwise wrong, means if previous stones can mke the way, one more stone also can
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0
        for size in range(m, 0, -1):
            if dp[n-1][size] == 1:
                return size
        return 0


    def backPack_TLE1(self, m, nums):  # TLE on case 5
        dp = [0 for _ in range(m+1)]
        for i in range(len(nums)):
            for j in range(m, 0, -1):
                # need to go from m to 1, because supress dp, larger size need to use the previous loop's smaller size value
                size = j
                stone = nums[i]
                if stone <= size:
                    dp[j] = max(dp[j], dp[size-stone] + stone)
        return dp[m]


    def backPack_TLE(self, m, nums): # TLE on case 5, pass MLE case6
        n = len(nums)
        dp = [[0 for _ in range(m+1)] for _ in range(2)]
        for i in range(1, n+1):
            stone = nums[i-1]
            for j in range(1, m+1):
                size = j
                if stone > size:
                    dp[i%2][j] = dp[(i-1)%2][j]
                else:
                    a = stone+dp[(i-1)%2][size-stone]
                    b = dp[(i-1)%2][size]
                    dp[i%2][j] = max(a, b)
        return dp[n%2][m]


    def backPack_MLE2(self, m, nums):  # use stone as row, and size as column, similar to _MLE
        n = len(nums)
        dp = [ [0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            stone = nums[i-1]
            for j in range(1, m+1):
                size = j
                if stone > size:
                    dp[i][size] = dp[i-1][size]
                else:
                    a = stone+dp[i-1][size-stone]
                    b = dp[i-1][size]
                    dp[i][j] = max(a, b)
        return dp[n][m]

    def backPack_WRONG(self, m, nums):
        n = len(nums)
        dp = [0 for _ in range(m + 1)]
        for i in range(1, m + 1):
            size = i
            for j in range(n, 0, -1):
                stone = nums[j - 1]
                if stone > size:
                    continue
                else:
                    dp[i] = max(stone + dp[size - stone], dp[size])
        return dp[m]


    def backPack_MLE(self, m, nums):  # correct, and MLE on case6
        """
        0-1背包问题是个典型举办子结构的问题，但是只能采用动态规划来解决，而不能采用贪心算法。因为在0-1背包问题中，在选择是否要把一个物品
        加到背包中，必须把该物品加进去的子问题的解与不取该物品的子问题的解进行比较。这种方式形成的问题导致了许多重叠子问题，满足动态规划的
        特征。动态规划解决0-1背包问题步骤如下：

        0-1背包问题子结构：选择一个给定物品i，则需要比较选择i的形成的子问题的最优解与不选择i的子问题的最优解。分成两个子问题，进行选择比
        较，选择最优的。
        
        0-1背包问题递归过程：设有n个物品，背包的重量为w，C[i][w]为最优解。即：
        
        C[i][w] = 
        
        (1) 0   if i=0 or w = 0
        (2) C[i-1][w]    if w_i > w
        (3) max(C[i-1][w - w_i] + w_i, C[i-1][w])
        
        :param m: 
        :param nums: 
        :return: 
        """
        n = len(nums)
        dp = [ [0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(1, m+1):
            size = i
            for j in range(1, n+1):
                stone = nums[j-1]
                if stone > size:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = max(stone+dp[size-stone][j-1], dp[size][j-1])
        return dp[m][n]


    def backPack_wrong(self, m, nums):
        dp = [ [0 for _ in range(m+1)] for _ in range(len(nums)+1)]
        for i in range(1, len(nums)):
            for j in range(1,m+1):
                stone = nums[i-1]
                for smaller in range(0, i):
                    if stone <= j - dp[smaller][j]:
                        dp[i][j] = max(stone + dp[smaller][j], dp[i][j])
                    else:
                        dp[i][j] = max(dp[smaller][j], dp[i][j])
        return dp[len(nums)][m]



    def backPack1(self, m, nums): #ref
        dp = [0 for _ in range(m+1)]
        dp[0] = 1
        ans = 0
        for stone in nums:
            for size in range(m, -1, -1):
                if size >= stone and dp[size-stone]>0:
                    ans = max(ans, size)
                    dp[size] = 1
        return ans


    def backPack_ref(self, m, A):
        # write your code here
        n = len(A)
        dp = [0 for x in range(m+1)]
        dp[0] = 1
        ans = 0
        for item in A:
            for bag in range(m,-1,-1):
                if bag-item >=0 and dp[bag-item] > 0:
                    ans = max(ans,bag)
                    dp[bag] = 1
        return ans

    def backPack_TLE(self, m, nums):
        dp = [0 for _ in range(m+1)]
        for stone in range(len(nums)):
            #for size in range(1, m+1):
            for size in range(m, 0, -1):
            # need to use smaller dp[size] calced before (one less stone loop ),
            # and because used one-d array, the dp[size larger] in current loop should be updated first (size in (m, -1, -1])
            # otherwise, dp[size smaller] will be updated in current loop first, then larger size can not have acces
            # to dp[smaller] for last loop, will cause error.
                if size >= nums[stone]:
                    dp[size] = max(dp[size], dp[size-nums[stone]] + nums[stone])
        return dp[m]


    def backPack_wrong(self, m, nums):
        # write your code here
        # can't put rocks in the inner loop, because every rock can only be use once.
        # if in inner loop, you would not know if the old dp[i] already use the rock or not !!!!
        if not nums or m <= 0:
            return 0
        dp = [0 for _ in range(m+1)]
        nums.sort()
        for size in range(1,m+1):
            for j in range(len(nums)-1, -1, -1):
                if size < nums[j]:
                    continue
                elif size == nums[j]:
                    dp[size] = size
                else:
                    dp[size] = max(dp[size], (nums[j] + dp[size-nums[j]])) #when size-nums[j] == nums[j], this can be wrong, see case3
                    # when m = 8, nums[j] =4
        return dp[m]


    def backPack_wrong(self, m, nums):
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
                    #dp[size] = max(dp[size], (dp[nums[j]] + dp[size-nums[j]]))
                    dp[size] = max(dp[size], (nums[j] + dp[size-nums[j]])) #when size-nums[j] == nums[j], this can be wrong, see case3
                    # when m = 4, nums[j] =2
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

    def test_case3(self): # ====>
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

    def test_case5(self): # ====> TLE, local 2.874s
        nums = [81,112,609,341,164,601,97,709,944,828,627,730,460,523,643,901,602,508,401,442,738,443,555,471,97,644,184,964,418,492,920,897,99,711,916,178,189,202,72,692,86,716,588,297,512,605,209,100,107,938,246,251,921,767,825,133,465,224,807,455,179,436,201,842,325,694,132,891,973,107,284,203,272,538,137,248,329,234,175,108,745,708,453,101,823,937,639,485,524,660,873,367,153,191,756,162,50,267,166,996,552,675,383,615,985,339,868,393,178,932]
        m = 80000
        answer = 52741
        result = self.sol.backPack(m, nums)
        self.assertEqual(answer, result)

    def test_case6(self):  #=======> MLE
        params = IniFileUtil.read_into_dict("backpack_case6.ini")
        nums = IniFileUtil.string_to_int_list(params.get("nums"))
        m = int(params.get("m"))
        answer = 5678
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


public class Solution {
    public int backPack(int m, int[] A) {
        int[] dp = new int[m+1];
        for (int i = 0; i < A.length; i++) {
            for (int j = m; j > 0; j--) {
                if (j >= A[i]) {
                    dp[j] = Math.max(dp[j], dp[j-A[i]] + A[i]);
                }
            }
        }
        return dp[m];
    }
}


========================================================================================================================

jiuzhang ref

class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    def backPack(self, m, A):
        # write your code here
        n = len(A)
        dp = [0 for x in range(m+1)]
        dp[0] = 1
        ans = 0
        for item in A:
            for i in range(m,-1,-1):
                if i-item >=0 and dp[i-item] > 0:
                    ans = max(ans,i)
                    dp[i] = 1
        return ans 

"""

#-*- coding:utf-8 -*-
