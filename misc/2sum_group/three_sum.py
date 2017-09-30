__author__ = 'linglin'

"""
3Sum

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?

Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

Array Two Pointers
Hide Similar Problems (E) Two Sum (M) 3Sum Closest (M) 4Sum (M) 3Sum Smaller

"""

import unittest


class Solution(object):
    def threeSum(self, nums):
        # write your code here
        if not nums:
            return []
        n = len(nums)
        nums.sort()
        result = []
        for i in range(n - 2):
            v1 = nums[i]
            vals_dict = {}

            for j in range(i + 1, n):
                v2 = nums[j]
                if -v1 - v2 in vals_dict:
                    tmp = sorted([v1, v2, -v1 - v2])
                    tmp = (tmp[0], tmp[1], tmp[2])
                    if tmp not in result:
                        result.append(tmp)
                else:
                    # vals_dict[v1 + v2] = 1, wrong , should be v2
                    vals_dict[v2] = 1
        return result

    def threeSum1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        i = 0
        while i < (len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                    while nums[k] == nums[k + 1] and j < k:
                        k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                else:
                    k -= 1
                    while nums[k] == nums[k+1] and j < k:
                        k -= 1
            # this is the important part
            i += 1
            while 0 < i < len(nums) - 2 and nums[i] == nums[i-1]:
                # 0<1 is kind of important here because the first one need to have a chance
                i += 1

        return result


    def threeSum_1(self, num):
        num.sort()
        res = []
        for i in range(len(num)-2):
            if i == 0 or num[i] > num[i-1]:
                left = i + 1; right = len(num) - 1
                while left < right:
                    if num[left] + num[right] == -num[i]:
                        res.append([num[i], num[left], num[right]])
                        left += 1; right -= 1
                        while left < right and num[left] == num[left-1]: left +=1
                        while left < right and num[right] == num[right+1]: right -= 1
                    elif num[left] + num[right] < -num[i]:
                        while left < right:
                            left += 1
                            if num[left] > num[left-1]: break
                    else:
                        while left < right:
                            right -= 1
                            if num[right] < num[right+1]: break
        return res

    def threeSum_3(self, nums):
        nums.sort()
        res = []
        length = len(nums)
        for i in range(0, length - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            target = nums[i] * -1
            left, right = i + 1, length - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    res.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
        return res


class ThreeSumTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # def test_case01(self):
    #     s = [-1, 0, 1]
    #     result = self.sol.threeSum(s)
    #     answer = [[-1, 0, 1]]
    #     self.assertEqual(result, answer)

    def test_case1(self):
        s = [-1, 0, 1, 2, -1, -4]
        result = self.sol.threeSum(s)
        answer = [[-1, -1, 2], [-1, 0, 1]]
        self.assertEqual(result, answer)

    def test_case2(self):
        s = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
        result = self.sol.threeSum(s)
        answer = [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]
        self.assertEqual(result, answer)

def main():
    test_suite = unittest.TestLoader().loadTestsFromTestCase(ThreeSumTester)
    unittest.TextTestRunner(verbosity=2).run(test_suite)


if __name__ == "__main__":
    # main()
    for i in range(5):
        print(i)
        if i < 2:
            i += 1
