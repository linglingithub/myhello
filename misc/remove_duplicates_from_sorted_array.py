"""
26. Remove Duplicates from Sorted Array

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't
matter what you leave beyond the new length.

Subscribe to see which companies asked this question

Hide Tags Array Two Pointers
Hide Similar Problems (E) Remove Element

Easy

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
        if n <= 1:
            return n
        fast, idx = 1, 0
        while fast < n:
            while fast < n and A[fast] == A[idx]:
                fast += 1
            if fast >= n:
                break
            if fast == idx + 1:
                fast += 1
                idx += 1
            else:
                idx += 1
                A[idx], A[fast] = A[fast], A[idx]
                fast += 1
        return idx + 1

class Solution_good(object):
    def removeDuplicates(self, nums): #82ms, 83% ==> 79ms, 88%
        """
        Use a pointer to keep the end of 'good' array, another pointer to scan the rest part of the array.
        Key points:
        1. The good pointer is always not faster than the searching pointer.
        2. The searcher pointer will always get a value that is equal or larger than good pointer.
        3. If equal, then ignore and move on
        4. If not equal (greater), put it to the end of good array, update good pointer position.
        5. How to update good array? Better to use swap
        :type nums: List[int]
        :rtype: int
        """
        if not nums: # equal to is None or len(nums)==0
            return 0
        good = 0
        for i in range(1, len(nums)):
            if nums[good] != nums[i]:
                good += 1
                nums[good] = nums[i]
                #nums[good+1], nums[i] = nums[i], nums[good+1]
                #good += 1
        #return good  # good is the index, should +1 and return as the length
        return good+1





    def removeDuplicates_ref(self, A):
        if len(A) == 0:
            return 0
        j = 0
        for i in range(0, len(A)):
            if A[i] != A[j]:
                A[i], A[j + 1] = A[j + 1], A[i]
                j = j + 1
        return j + 1





class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,1,2]
        answer = 2
        nums_answer = [1,2]
        result = self.sol.removeDuplicates(nums)
        self.assertEqual(answer, result)
        self.assertEqual(nums_answer, nums[:result])


    def test_case2(self):
        nums = [1, 1, 2, 2, 2, 3, 3]
        answer = 3
        nums_answer = [1, 2, 3]
        result = self.sol.removeDuplicates(nums)
        self.assertEqual(answer, result)
        self.assertEqual(nums_answer, nums[:result])

    def test_case3(self):
        nums = [1, 2, 3]
        answer = 3
        nums_answer = [1, 2, 3]
        result = self.sol.removeDuplicates(nums)
        self.assertEqual(answer, result)
        self.assertEqual(nums_answer, nums[:result])

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8