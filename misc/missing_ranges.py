#coding=utf-8

import unittest

"""
163. Missing Ranges

Given a sorted integer array where the range of elements are [lower, upper] inclusive, return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].

Medium

locked

"""



class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        result = []
        if not nums:
            range = "".join([str(lower), "->", str(upper)])
            return [range]
        current = lower
        idx = 0
        while current <= upper:
            if current != nums[idx]:
                missing = self.get_missing(current, nums[idx])
                result.append(missing)
            current = nums[idx] + 1
            idx += 1
            # remember to add idx check here
            if idx == len(nums):
                if current <= upper:
                    result.append(self.get_missing(current, upper+1))
                break
        return result

    def get_missing(self, low, high):
        diff = high - low
        if diff > 1:
            return "{}->{}".format(low, high-1)
        else:
            return str(low)






class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [0, 1, 3, 50, 75]
        lower = 0
        upper = 99
        answer = ["2", "4->49", "51->74", "76->99"]
        result = self.sol.findMissingRanges(nums, lower, upper)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""

# Time:  O(n)
# Space: O(1)


#related:

228. SUMMARY RANGES
41. First Missing Positive

"""


#-*- coding:utf-8 -*-
