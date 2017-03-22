#coding=utf-8

import unittest

"""

209. Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of
which the sum ≥ s. If there isn't one, return 0 instead.

Have you met this question in a real interview? Yes
Example
Given the array [2,3,1,2,4,3] and s = 7, the subarray [4,3] has the minimal length under the problem constraint.

Challenge
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

Tags
Two Pointers Array Facebook
Related Problems
Medium Subarray Sum Closest 19 %
Easy Subarray Sum

-----

More practice:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

Credits:
Special thanks to @Freezen for adding this problem and creating all test cases.

Array Two Pointers Binary Search
Hide Similar Problems (H) Minimum Window Substring (M) Maximum Size Subarray Sum Equals k

[1,2,2,3,3,4] 7
"""



class Solution(object):
    def minSubArrayLen_ref(self, s, nums): #78%, O(N)
        # write your code here
        n = len(nums)
        if n==0: return 0
        left = right = total = 0
        ans = n+1
        while right<n:
            while right<n and total<s:
                total += nums[right]
                right += 1
            if total<s: break
            while left<right and total>=s:
                total -= nums[left]
                left += 1
            ans = min(ans, right-left+1)
        if ans==n+1: return 0
        else: return ans


    def minSubArrayLen(self, s, nums): #68%, O(N)
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        i, j, sum = 0,0,0
        #nums.sort()
        result = n + 1 #add this to check if result has been achieved or not, see case4
        while j < n:
            while j < n and sum < s:
                sum += nums[j]
                j += 1
            if sum < s and j>=n:
                #return 0 # case 3
                #return result #case4
                return result if result <= n else 0

            result = min(result, j-i)
            while i<j and sum>=s:
                sum -= nums[i]
                i += 1
                if sum >= s:
                    result = min(result, j-i)
        return result


    def minSubArrayLen_deadloop(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        n = len(nums)
        result = n
        i, j, sum = 0, 0, 0
        while i < n:
            while j < n:
                sum += nums[j]
                if sum >= s:
                    result = min(result, j-i+1)
                    break
                j += 1
            while i<j and sum > s and j<n:
                sum -= nums[i]
                i += 1
                if sum >= s:
                    result = min(result, j-i+1)
                else:
                    break
            j+=1
        return result








class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [2,3,1,2,4,3]
        s = 7
        answer = 2
        result = self.sol.minSubArrayLen( s, nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = []
        s = 100
        answer = 0
        result = self.sol.minSubArrayLen( s, nums)
        self.assertEqual(answer, result)

    def test_case3(self): #====> ??? answer should be 7 ==> CONTINUOUS, which means can't sort array,
        s = 213
        nums = [12,28,83,4,25,26,25,2,25,25,25,12]
        answer = 8
        result = self.sol.minSubArrayLen( s, nums)
        self.assertEqual(answer, result)

    def test_case4(self): #====>
        nums = [1,1]
        s = 3
        answer = 0
        result = self.sol.minSubArrayLen( s, nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-


