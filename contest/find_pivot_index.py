#coding=utf-8

import unittest

"""

724. Find Pivot Index My SubmissionsBack to Contest
User Accepted: 1259
User Tried: 1428
Total Accepted: 1614
Total Submissions: 3598
Difficulty: Easy
Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

Example 1:
Input: 
nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation: 
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.
Example 2:
Input: 
nums = [1, 2, 3]
Output: -1
Explanation: 
There is no index that satisfies the conditions in the problem statement.
Note:

The length of nums will be in the range [0, 10000].
Each element nums[i] will be an integer in the range [-1000, 1000].
"""



class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        if len(nums) == 1:
            return 0
        dp_left = [nums[i] for i in range(len(nums))]

        n = len(nums)
        for i in range(1,n):
            dp_left[i] += dp_left[i-1]
        #dp_left.insert(0, 0)
        dp_right = [nums[i] for i in range(len(nums))]
        for i in range(n-2, -1, -1):
            dp_right[i] += dp_right[i+1]
        #dp_right.append(0)
        if dp_right[1] == 0:
            return 0

        for i in range(1,n-1):
            if dp_left[i-1] == dp_right[i+1]:
                res = i
                return res
        if n>=2 and dp_left[n-2] == 0:
            return n-1

        return -1


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,2,3]
        answer = -1
        result = self.sol.pivotIndex(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [1, 7, 3, 6, 5, 6]
        answer = 3
        result = self.sol.pivotIndex(nums)
        self.assertEqual(answer, result)

    def test_case3(self):
        nums = [-1,-1,-1,0,1,1]
        answer = 0
        result = self.sol.pivotIndex(nums)
        self.assertEqual(answer, result)

    def test_case04(self):
        nums = [-1,-1,1,1,0,0]
        answer = 4
        result = self.sol.pivotIndex(nums)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
