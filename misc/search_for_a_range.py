"""
34. Search for a Range

Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

Subscribe to see which companies asked this question

Hide Tags Binary Search Array
Hide Similar Problems (E) First Bad Version



"""

import unittest


class Solution(object):
    def searchRange(self, nums, target): # 52ms, 80.97%
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums is None or len(nums) == 0:
            return [-1, -1]
        mid = self.binarySearch(nums, 0, len(nums)-1, target)
        if mid == -1:
            return [-1, -1]
        result = [-1, -1]
        left = mid
        while mid >= left >= 0:
            result[0] = left
            left = self.binarySearch(nums, 0, left-1, target)
        right = mid
        while mid <= right < len(nums):
            result[1] = right
            right = self.binarySearch(nums, right+1, len(nums)-1, target)
        return result


    def binarySearch(self, nums, left, right, target):
        """
        :param nums:
        :param left:
        :param right:
        :param target:
        :return: int: the index of target value found in nums, -1 if not found
        """
        if left > right or left < 0 or right > len(nums) - 1:
            return -1

        while 0 <= left <= right < len(nums):
            mid = (left + right) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 8
        answer = [3, 4]
        result = self.sol.searchRange(nums, target)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 5
        answer = [0, 0]
        result = self.sol.searchRange(nums, target)
        self.assertEqual(answer, result)

    def test_case3(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 11
        answer = [-1, -1]
        result = self.sol.searchRange(nums, target)
        self.assertEqual(answer, result)

    def test_case4(self):
        nums = [5]
        target = 5
        answer = [0, 0]
        result = self.sol.searchRange(nums, target)
        self.assertEqual(answer, result)

    def test_case5(self):
        nums = [5, 5, 5,5,5]
        target = 5
        answer = [0, 4]
        result = self.sol.searchRange(nums, target)
        self.assertEqual(answer, result)

    def test_case6(self):
        nums = []
        target = 11
        answer = [-1, -1]
        result = self.sol.searchRange(nums, target)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()
