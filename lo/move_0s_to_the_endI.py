#coding=utf-8

import unittest

"""
Move 0s To The End I
Given an array of integers, move all the 0s to the right end of the array.

The relative order of the elements in the original array does not need to be maintained.

Assumptions:

The given array is not null.
Examples:

{1} --> {1}
{1, 0, 3, 0, 1} --> {1, 3, 1, 0, 0} or {1, 1, 3, 0, 0} or {3, 1, 1, 0, 0}

"""



class Solution(object):
    def moveZero(self, array):
        arr = array
        if not arr or len(arr) <= 1:
            return arr
        i, j = 0, len(arr)-1
        while i <= j:
            if arr[i] == 0:
                arr[j], arr[i] = arr[i], arr[j]
                j -= 1
            else:
                i += 1
        return arr



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [0]
        answer = [0]
        result = self.sol.moveZero(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [1, 0]
        answer = [1, 0]
        result = self.sol.moveZero(nums)
        self.assertEqual(answer, result)


    def test_case3(self):
        nums = [1, 0, 3, 0, 1]
        answer = [1, 1, 3, 0, 0]
        result = self.sol.moveZero(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
