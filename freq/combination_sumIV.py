"""

Combination Sum IV

Given an integer array with all positive numbers and no duplicates, find the number of possible combinations

that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.

Subscribe to see which companies asked this question

Hide Tags Dynamic Programming
Hide Similar Problems (M) Combination Sum

*************************

http://blog.csdn.net/qq508618087/article/details/52064134

思路: 一开始想到用DFS来做, 但是有个问题就是这种方式得到的答案各个数字排列是无序的, 也就是1, 3和3, 1这种只是一个答案,

然后又想把数字保存起来, 在得到一个答案的时候对这些数字再求一次总共排列的个数, 这种方式还有问题就是在求总排列个数的时候

比如2, 1, 1三个加一起等于4, 总的排列个数即为(3!/2!), 但是当数字个数很多的时候阶乘太大, 根本无法计算.

然后就想到可以用动态规划来做, 也是一个背包问题, 求出[1, target]之间每个位置有多少种排列方式, 这样将问题分化为子问题.

状态转移方程可以得到为:

dp[i] = sum(dp[i - nums[j]]),  (i-nums[j] > 0);

如果允许有负数的话就必须要限制每个数能用的次数了, 不然的话就会得到无限大的排列方式, 比如1, -1, target = 1;

"""

import unittest


class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or target <= 0:
            return 0
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1  # important, otherwise result will be all 0
        nums.sort()  # important, otherwise can't use if num>i then break in the following
        for i in range(target + 1):
            for num in nums:
                if num > i:
                    break
                if i - num >= 0:
                    dp[i] += dp[i - num]
        return dp[target]

    def combinationSum_wrong(self, nums, target):
        """
        this is actually combination with unlimited cnts for ele in nums
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or target <= 0:
            return 0
        dp = [0 for _ in range(target + 1)]
        # dp[0] = 1 # should add this
        for num in nums:
            if num > target:  # should add this check, otherwise out of index, and more efficient
                break
            # for j in range(target-num, 0, -1):  # can't go reversed order, think about 1+1=2, when [1], dp[2] = 1 too
            #     # if dp[j] > 0:
            #     dp[j+num] += dp[j]
            dp[num] += 1
            for j in range(1, target + 1):
                if j + num > target:
                    break
                dp[j + num] += dp[j]
                print("num, j, dp == ", num, j, dp)


                # dp[num] += 1  # put latest, not to pollute updating other dp[j+num] values
        return dp[target]

class Solution1(object):

    def combinationSum4(self, nums, target): #49ms, 96.54%
        """
        combinationSum4(x): f(x)
        f(target) = f(target - nums[0]) + f(target - nums[1]) + ... + f(target - nums.back())

        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None or len(nums) == 0 or target <=0 :
            return 0
        dp = [0] * (target+1)
        dp[0] = 1 # important
        for i in range(target+1):
            for num in nums:
                if i-num >= 0:
                    dp[i] += dp[i-num]
        return dp[target]


    def combinationSum4_ref(self, nums, target): #65ms, 72%
        # a different way to think about the dp. not as fast though
        dp = [1] + [0] * target
        for i in range(target + 1):
            for x in nums:
                if i + x <= target:
                    dp[i + x] += dp[i]
        return dp[target]





    def combinationSum4_tleForCase2(self, nums, target):
        """
        Not best solution. Runs ok for case1, runs 2m 43s for case2 locally.
        Too slow, need to think of a better way.

        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None or len(nums) == 0 or target <=0 :
            return 0
        result = []
        for i in range(len(nums)):
            self.dfs1(result, [nums[i]], target - nums[i], nums)
        return len(result)

    def dfs1(self, result, combi, target, nums):
        if target == 0:
            result.append(combi)
            return
        if target < 0:
            return
        for num in nums:
            self.dfs1(result, combi+[num], target - num, nums)



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1, 2, 3]
        target = 4
        answer = 7
        result = self.sol.combinationSum4(nums, target)
        self.assertEqual(answer, result)

    def test_case2(self): # =====> TLE
        nums = [4,2,1]
        target = 32
        answer = 39882198
        result = self.sol.combinationSum4(nums, target)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""
http://www.cnblogs.com/grandyang/p/5705750.html

"""