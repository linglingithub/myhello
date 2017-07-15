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


"""

Python 140ms beats 100%, and works for N-sum (N>=2)

57
Z zhuyinghua1203 
Reputation:  244
The core is to implement a fast 2-pointer to solve 2-sum, and recursion to reduce the N-sum to 2-sum. Some optimization was be made knowing the list is sorted.

def fourSum(self, nums, target):
    nums.sort()
    results = []
    self.findNsum(nums, target, 4, [], results)
    return results

def findNsum(self, nums, target, N, result, results):
    if len(nums) < N or N < 2: return

    # solve 2-sum
    if N == 2:
        l,r = 0,len(nums)-1
        while l < r:
            if nums[l] + nums[r] == target:
                results.append(result + [nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while r > l and nums[r] == nums[r + 1]:
                    r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
    else:
        for i in range(0, len(nums)-N+1):   # careful about range
            if target < nums[i]*N or target > nums[-1]*N:  # take advantages of sorted list
                break
            if i == 0 or i > 0 and nums[i-1] != nums[i]:  # recursively reduce N
                self.findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
    return
Just revisited and clean the code

def fourSum(self, nums, target):
    def findNsum(nums, target, N, result, results):
        if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:  # early termination
            return
        if N == 2: # two pointers solve sorted 2-sum problem
            l,r = 0,len(nums)-1
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        else: # recursively reduce N
            for i in range(len(nums)-N+1):
                if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                    findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)

    results = []
    findNsum(sorted(nums), target, 4, [], results)
    return results

"""