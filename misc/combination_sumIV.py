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



"""

import unittest


class Solution(object):
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