#coding=utf-8


import unittest

"""

198. House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
money you can rob tonight without alerting the police.

Credits:
Special thanks to @ifanchu for adding this problem and creating all test cases. Also thanks to @ts for adding additional
test cases.

Subscribe to see which companies asked this question.

Hide Tags Dynamic Programming
Hide Similar Problems (M) Maximum Product Subarray (M) House Robber II (E) Paint House (E) Paint Fence
(M) House Robber III


Easy

"""



class Solution(object):
    def rob(self, nums): #49ms, 34%
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [0 for _ in range(3)]
        dp[0] = nums[0]
        if len(nums) < 2: # add check here, otherwise wrong for case 2
            return dp[0]
        dp[1] = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            dp[i%3] = max(dp[(i-2)%3]+nums[i], dp[(i-1)%3])
        return dp[(len(nums)-1)%3]


    def rob1(self, nums): #35ms, 94%
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [0 for _ in nums]
        dp[0] = nums[0]
        if len(nums) < 2: # add check here, otherwise wrong for case 2
            return dp[0]
        dp[1] = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[len(nums)-1]


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [2,1,1,2]
        answer = 4
        result = self.sol.rob(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [0]
        answer = 0
        result = self.sol.rob(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-



"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        max1 = nums[0]
        if len(nums) == 1:
            return max1
        max2 = nums[1]
        for i in range(2,len(nums)):
            maxn = max1 + nums[i]
            if max1 < max2:
                max1 = max2
            max2 = maxn

        return max(max1,max2)

if __name__ == '__main__':
    solu = Solution()
    house = [2,1,1,2]
    print solu.rob(house)

"""