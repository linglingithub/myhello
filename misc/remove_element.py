"""

27. Remove Element

Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.

Show Hint
Subscribe to see which companies asked this question

Hide Tags Array Two Pointers
Hide Similar Problems (E) Remove Duplicates from Sorted Array (E) Remove Linked List Elements (E) Move Zeroes

Easy

"""

import unittest


class Solution(object):
    def removeElement(self, nums, val):  #39ms, 85%
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        good = 0  #the place to check
        for i in range(len(nums)):
            if nums[i] != val:
                nums[good] = nums[i]
                good += 1
        return good





class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [3,2,2,3]
        val = 3
        answer = 2
        answer_nums = [2,2]
        result = self.sol.removeElement(nums, val)
        self.assertEqual(answer, result)
        self.assertEqual(answer_nums, nums[:result])


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8