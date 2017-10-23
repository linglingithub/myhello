"""

80. Remove Duplicates from Sorted Array II

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter

what you leave beyond the new length.

Subscribe to see which companies asked this question

Hide Tags Array Two Pointers

Medium

"""

import unittest


class Solution:
    """
    @param A: a list of integers
    @return an integer
    """

    def removeDuplicates(self, A):
        # write your code here
        if not A:
            return 0
        n = len(A)
        if n <= 2:
            return n
        slow = 0
        fast = 1
        cnt = 1
        while fast < n:
            if A[fast] == A[slow]:
                if cnt == 1:
                    slow += 1
                    cnt += 1

            else:
                cnt = 1
                slow += 1
            A[slow] = A[fast]
            fast += 1
        return slow + 1


class Solution1(object):
    def removeDuplicates2(self, nums): #62ms, 79%
        """
        Base on the first implementation, some improvements.
        Starting point can be 1. (But need to check the len(nums) first otherwise wrong for short nums)
        No need to swap, just get the right value in (here it does not require original values in list)

        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) < 3:
            return len(nums)
        good = 1
        cnt = 1 if nums[0] != nums[1] else 2
        allowed = 2
        for i in range(2, len(nums)):
            if nums[i] == nums[good]:
                if cnt < allowed:
                    cnt += 1
                    good += 1
                    nums[good] = nums[i]
            else:
                cnt = 1
                good += 1
                nums[good] = nums[i]
        return good + 1


    def removeDuplicates1(self, nums): #72ms, 57% ==> 52ms, 98% if remove the swap part for only getting the good value
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        good = 0
        cnt = 1
        allowed = 2
        for i in range(1, len(nums)):
            if nums[i] == nums[good]:
                if cnt < allowed:
                    cnt += 1
                    good += 1
                    #nums[good], nums[i] = nums[i], nums[good] # ===> no need to swap
                    nums[good] = nums[i]
            else:
                cnt = 1
                good += 1
                # nums[good], nums[i] = nums[i], nums[good]
                nums[good] = nums[i]
        return good + 1






class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,1,1,2,2,3]
        answer = 5
        result = self.sol.removeDuplicates(nums)
        nums_answer = [1,1,2,2,3]
        self.assertEqual(answer, result)
        self.assertEqual(nums_answer, nums[:result])


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8