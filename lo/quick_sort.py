#coding=utf-8

import unittest

"""


"""

import random


class Solution(object):
    def quickSort(self, array):
        """
        array: int[]
        return: int[]
        """
        # write your solution here
        if not array:
            return []
        return self.sort(array, 0, len(array) - 1)

    def sort(self, arr, left, right):
        if left >= right:
            return arr
        if right - left >= 3:
            self.init_pivot(arr, left, right)
        idx = self.partition(arr, left, right)
        self.sort(arr, left, idx - 1)
        self.sort(arr, idx + 1, right)
        return arr

    def init_pivot(self, arr, left, right):
        idx = random.randint(left, right)
        arr[idx], arr[right] = arr[right], arr[left]

    def partition(self, arr, left, right):
        pivot = arr[right]
        i, j = left, right - 1
        while i <= j:
            while i <= j and arr[i] < pivot:
                i += 1
            while i <= j and arr[j] > pivot:
                j -= 1
            if i >= j:
                arr[i], arr[right] = arr[right], arr[i]
                break
            else:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        return i


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()


    def test_case1(self):
        nums = [3,2,5]
        answer = [2,3,5]
        result = self.sol.quickSort(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [3]
        answer = [3]
        result = self.sol.quickSort(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [3]
        answer = [3]
        result = self.sol.quickSort(nums)
        self.assertEqual(answer, result)

    def test_case3(self):
        nums = []
        answer = []
        result = self.sol.quickSort(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
