#coding=utf-8


import unittest

"""

213. House Robber II

Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not
get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the
neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous
street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
 money you can rob tonight without alerting the police.

Credits:
Special thanks to @Freezen for adding this problem and creating all test cases.

Subscribe to see which companies asked this question.

Hide Tags Dynamic Programming
Hide Similar Problems (E) House Robber (E) Paint House (E) Paint Fence (M) House Robber III

Medium

"""



class Solution(object):
    def rob(self, nums): #38ms, 88%
        """
        Take nums as two arrays, nums[0:n-1], nums[1:n] , which means the first house is robbed / not robbed
        then take max of the two cases.

        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        if n < 2: #shoud move before dp init, see case 2
            return nums[0]
        if n < 3:  #shoud move before dp init, see case 3
            return max(nums[0], nums[1])

        dp = [0 for _ in range(n-1)]
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        for i in range(2, n-1): # should be n-1, not n-2 here
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        result = dp[n-2]

        dp[0] = nums[1]
        dp[1] = max(nums[1], nums[2])
        for i in range(2, n-1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i+1])
        result = max(result, dp[n-2])
        return result


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [2,1,1,2]
        answer = 3
        result = self.sol.rob(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [0]
        answer = 0
        result = self.sol.rob(nums)
        self.assertEqual(answer, result)

    def test_case3(self):
        nums = [0,0]
        answer = 0
        result = self.sol.rob(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



