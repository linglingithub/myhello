"""
Search Insert Position

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 --> 2
[1,3,5,6], 2 --> 1
[1,3,5,6], 7 --> 4
[1,3,5,6], 0 --> 0

Subscribe to see which companies asked this question

Hide Tags Array Binary Search
Hide Similar Problems (E) First Bad Version


"""

import unittest


class Solution(object):
    def searchInsert(self, nums, target): #52ms, 65.72%
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        left = 0
        right = len(nums) - 1
        while 0<=left<=right<len(nums):
            mid = (left+right)/2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        mid = (left+right) / 2 + 1
        return mid



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,3,5,6]
        target = 5
        answer = 2
        result = self.sol.searchInsert(nums, target)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [1, 3, 5, 6]
        target = 2
        answer = 1
        result = self.sol.searchInsert(nums, target)
        self.assertEqual(answer, result)

    def test_case3(self):
        nums = [1,3,5,6]
        target = 7
        answer = 4
        result = self.sol.searchInsert(nums, target)
        self.assertEqual(answer, result)

    def test_case4(self):
        nums = [1,3,5,6]
        target = -1
        answer = 0
        result = self.sol.searchInsert(nums, target)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()