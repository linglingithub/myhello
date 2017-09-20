#coding=utf-8

import unittest

"""

From Discussion, no problem found -- 20170920

Count inversion

https://discuss.leetcode.com/topic/218/count-inversion/2
http://www.geeksforgeeks.org/counting-inversions/

Inversion Count for an array indicates – how far (or close) the array is from being sorted. If array is already sorted 
then inversion count is 0. If array is sorted in reverse order that inversion count is the maximum. 
Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j

Example:
The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).


"""



class Solution(object):
    def countInversion(self, nums):
        """
        Divide into halves and merge sort, while merge count the inversions.
        O(nlogn) time, O(n) space
        
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) <= 1:
            return 0
        self.result = 0
        n = len(nums)
        self.merge_sort(nums, 0, n)
        return self.result

    def merge_sort(self, nums, left, right):
        if left >= right - 1:
            return nums[left:right]   # should not be nums here,
        mid = int(left + (right-left)/2)
        half1 = self.merge_sort(nums, left, mid)
        half2 = self.merge_sort(nums, mid, right)
        i, j = 0, 0
        arr = []
        while i < len(half1) and j < len(half2):
            if half1[i] <= half2[j]:
                arr.append(half1[i])
                i += 1
            else:
                self.result += len(half1) - i
                arr.append(half2[j])
                j += 1
        if i < len(half1):
            arr.extend(half1[i:])
        if j < len(half2):
            arr.extend(half2[j:])
        return arr

    def countInversion1(self, nums):
        """
        Basic way, O(n^2) time, O(1) space
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        result = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] > nums[j]:
                    result += 1
        return result


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [2, 4, 1, 3, 5]
        answer = 3
        result = self.sol.countInversion(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [2, 4, 1]
        answer = 2
        result = self.sol.countInversion(nums)
        self.assertEqual(answer, result)

    def test_case3(self):
        nums = [1,2,3,4]
        answer = 0
        result = self.sol.countInversion(nums)
        self.assertEqual(answer, result)

    def test_case4(self):
        nums = [1,2,2,3]
        answer = 0
        result = self.sol.countInversion(nums)
        self.assertEqual(answer, result)

    def test_case5(self):
        nums = [3,2,2,1]
        answer = 5
        result = self.sol.countInversion(nums)
        self.assertEqual(answer, result)

    def test_case6(self):
        nums = [4,3,2,1]
        answer = 6
        result = self.sol.countInversion(nums)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
