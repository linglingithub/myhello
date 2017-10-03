#coding=utf-8

import unittest

"""

128. Longest Consecutive Sequence

DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

Difficulty:Hard
Total Accepted:115.4K
Total Submissions:310.5K
Contributor: LeetCode
Subscribe to see which companies asked this question.

Related Topics 
Array Union Find 
Similar Questions 
Binary Tree Longest Consecutive Sequence 

"""



class Solution(object):
    def longestConsecutive(self, nums):  # 79%
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        vals = {}
        for num in nums:
            vals[num] = 1
        res = 0
        while vals:
            tmp, _ = vals.popitem()
            l, r = self.expand_range(tmp, vals)
            res = max(res, r - l + 1)
        return res

    def expand_range(self, target, vals):
        l, r = target, target
        while l - 1 in vals:
            vals.pop(l - 1)
            l -= 1
        while r + 1 in vals:
            vals.pop(r + 1)
            r += 1
        return l, r




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = 1
        answer = 1
        result = self.sol.searchInsert(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()


"""

这道题利用HashSet的唯一性解决，能使时间复杂度达到O(n)。首先先把所有num值放入HashSet，然后遍历整个数组，如果HashSet中存在该值，
就先向下找到边界，找的同时把找到的值一个一个从set中删去，然后再向上找边界，同样要把找到的值都从set中删掉。所以每个元素最多会被遍历两边，
-- insert once, remove once
时间复杂度为O(n)。
"""
#-*- coding:utf-8 -*-
