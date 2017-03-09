#coding=utf-8

import unittest

"""

228. Summary Ranges

Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

Subscribe to see which companies asked this question.

Hide Tags Array
Hide Similar Problems (M) Missing Ranges (H) Data Stream as Disjoint Intervals

Medium

"""


class Solution(object):
    def summaryRanges(self, nums): #39ms, 64%
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        result = []
        i = 0
        while i < len(nums): #should be len(nums) here, not len()-1
            low = nums[i]
            while i+1 < len(nums) and nums[i] == nums[i+1] - 1:
                i += 1
            high = nums[i]
            result.append("{}->{}".format(low, high) if high-low>=1 else str(low))
            i+=1
        return result

    def get_range_str(self, low, high):
        diff = high - low
        if diff > 1:
            return "{}->{}".format(low, high-1)
        else:
            return str(low)

    def summaryRanges1(self, nums): #62ms, 7.44%
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        result = []
        i = 0
        while i < len(nums): #should be len(nums) here, not len()-1
            low = nums[i]
            while i+1 < len(nums) and nums[i] == nums[i+1] - 1:
                i += 1
            high = nums[i]
            result.append(self.get_range_str(low,high+1))
            i+=1
        return result

    def get_range_str(self, low, high):
        diff = high - low
        if diff > 1:
            return "{}->{}".format(low, high-1)
        else:
            return str(low)



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [0,1,2,4,5,7]
        answer = ["0->2","4->5","7"]
        result = self.sol.summaryRanges(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()


"""
space: O(1)
time: O(n)



"""

#-*- coding:utf-8 -*-
