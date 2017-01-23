__author__ = 'linglin'
"""
4Sum

Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?

Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
Subscribe to see which companies asked this question

Hide Tags Array Hash Table Two Pointers
Hide Similar Problems (E) Two Sum (M) 3Sum


"""

import unittest


class Solution(object):
    def fourSum(self, nums, target): # 222ms
        if nums is None or len(nums) < 4: #important
            return []
        nums.sort()
        result = set()
        vals = {}
        for i in range(0,len(nums)-3):
            for j in range(i+1, len(nums)-2):
                if nums[i] + nums[j] in vals:
                    vals[nums[i] + nums[j]].append([i, j])
                else:
                    vals[nums[i] + nums[j]] = [[i, j]]
        for k in range(2, len(nums)-1):
            for l in range(k+1, len(nums)):
                diff = target - nums[k] - nums[l]
                if diff in vals:
                    for pair in vals[diff]:
                        if pair[1] < k:
                            result.add((nums[pair[0]], nums[pair[1]], nums[k], nums[l]))
        return [list(rl) for rl in result]



    def fourSum_old(self, nums, target): # slower, around 15~16%, 1482ms
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) < 4: #important
            return []
        nums.sort()
        result = []

        for i in range(0, len(nums)-3):
            # while i > 0 and nums[i] == nums[i-1]:
            #     i += 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                # while j > i+1 and nums[j] == nums[j-1]:
                #     j += 1
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                k = j + 1
                l = len(nums) - 1
                while k < l:
                    sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum == target:
                        result.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k-1]:
                            k += 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
                    elif sum < target:
                        k += 1
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                    else:
                        l -= 1
                        while k < l and nums[l] == nums[l+1]:
                            l -= 1
        return result








class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1, 0, -1, 0, -2, 2]
        target = 0
        answer = [
          [-2, -1, 1, 2],
          [-2,  0, 0, 2],
            [-1, 0, 0, 1],
        ]
        result = self.sol.fourSum(nums, target)
        print "result of case 1: ====== ", result
        self.assertEqual(answer.sort(), result.sort())

    def test_case2(self):
        nums = [-1,0,1,2,-1,-4]
        target = -1
        answer = [[-4,0,1,2],[-1,-1,0,1]]
        result = self.sol.fourSum(nums, target)
        print "result of case 2: ====== ", result
        self.assertEqual(answer.sort(), result.sort())


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()

