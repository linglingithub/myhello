#coding=utf-8

import unittest

"""

376. Wiggle Subsequence
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate 
between positive and negative. The first difference (if one exists) may be either positive or negative. 
A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and 
negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences 
are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is 
obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining 
elements in their original order.

Examples:
Input: [1,7,4,9,2,5]
Output: 6
The entire sequence is a wiggle sequence.

Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].

Input: [1,2,3,4,5,6,7,8,9]
Output: 2
Follow up:
Can you do it in O(n) time?

Credits:
Special thanks to @agave and @StefanPochmann for adding this problem and creating all test cases.

Difficulty:Medium
Total Accepted:28.8K
Total Submissions:80K
Contributor: LeetCode
Subscribe to see which companies asked this question.

Related Topics 
Dynamic Programming Greedy 

"""


class Solution(object):
    def wiggleMaxLength(self, nums):  # self, 70% +
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) <= 1:  # can't just assume this, not good for =get_starting_direction case, see case 4
            return len(nums)
        res = []
        # ascending = (nums[1] > nums[0])   # not good for case 5
        direction = self.get_starting_direction(nums)
        if direction == 0:
            return 1
        ascending = True if direction == 1 else False
        res.append(nums[0])
        n = len(nums)
        i = 1
        while i < n:
            if ascending:
                while i + 1 < n and nums[i + 1] >= nums[i]:
                    i += 1
                if nums[i] > res[-1]:    # add for case4
                    res.append(nums[i])
                    ascending = not ascending
            else:
                while i + 1 < n and nums[i + 1] <= nums[i]:
                    i += 1
                if nums[i] < res[-1]:    # add for case4
                    res.append(nums[i])
                    ascending = not ascending
            # res.append(nums[i])       # can't just add without checking = case, see case 4
            # ascending = not ascending
            i += 1
        return len(res)

    def get_starting_direction(self, nums):
        # return 1, 0, -1, which means ascending, equal, and not ascending
        i, n = 1, len(nums)
        while i < n and nums[i] == nums[0]:
            i += 1
        if i == n:
            return 0
        return 1 if nums[i] > nums[0] else -1


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,7,4,9,2,5]
        answer = 6
        result = self.sol.wiggleMaxLength(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [1,17,5,10,13,15,10,5,16,8]
        answer = 7
        result = self.sol.wiggleMaxLength(nums)
        self.assertEqual(answer, result)


    def test_case3(self):
        nums = [1,2,3,4,5,6,7,8,9]
        answer = 2
        result = self.sol.wiggleMaxLength(nums)
        self.assertEqual(answer, result)


    def test_case4(self):   #===>
        nums = [0, 0]
        answer = 1
        result = self.sol.wiggleMaxLength(nums)
        self.assertEqual(answer, result)

    def test_case05(self):   #===>
        nums = [1,1,7,4,9,2,5]
        answer = 6
        result = self.sol.wiggleMaxLength(nums)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
