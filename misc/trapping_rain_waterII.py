#coding=utf-8

import unittest

"""
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it
is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue
section) are being trapped. Thanks Marcos for contributing this image!

Subscribe to see which companies asked this question.

Hide Tags Array Stack Two Pointers
Hide Similar Problems (M) Container With Most Water (M) Product of Array Except Self (H) Trapping Rain Water II

Hard

"""



class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = 1
        answer = 1
        result = self.sol.trap(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
