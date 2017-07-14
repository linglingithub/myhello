"""
Merge Sorted Array

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from 
nums2.

The number of elements initialized in nums1 and nums2 are m and n respectively.

Subscribe to see which companies asked this question

Hide Tags nums1rray Two Pointers
Hide Similar Problems (E) Merge Two Sorted Lists


"""

import unittest
import copy


class Solution(object):
    def merge(self, nums1, m, nums2, n): # ref idea, do that from end to start in nums1 array !
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:   # type: should be while, not if here !!!
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[0:n] = nums2[0:n]

class Solution1(object):
    def merge(self, nums1, m, nums2, n):
        i = 0
        j = 0
        k = 0
        tmp = [ 0 for x in range(m+n)]
        while i < m and j < n:
            if nums1[i] > nums2[j]:
                tmp[k] = nums2[j]
                j += 1
            else:
                tmp[k] = nums1[i]
                i += 1
            k += 1
        if i == m and j < n:
            while j < n:
                tmp[k] = nums2[j]
                k += 1
                j += 1
        else:
            while i < m:
                tmp[k] = nums1[i]
                k += 1
                i += 1
        nums1[:] = tmp



    def merge3(self, nums1, m, nums2, n): # accepted and passed local cases with modified assignment to nums1, 65ms, 25.32%
        tmp = [0 for i in range(m + n)]
        i = 0
        j = 0
        k = 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                tmp[k] = nums1[i]
                i += 1
            else:
                tmp[k] = nums2[j]
                j += 1
            k += 1
        if i == m:
            while k < m + n:
                tmp[k] = nums2[j]
                k += 1
                j += 1
        else:
            while k < m + n:
                tmp[k] = nums1[i]
                i += 1
                k += 1
        nums1[:] = [x for x in tmp]
        # for i in range(0, m + n): this would not work for case 1 , 3, and 4, "list assignment index out of range"
        #     nums1[i] = tmp[i]

    def merge2(self, nums1, m, nums2, n): # accepted by leetcode but not passing the test cases. and slower
        for i in range(n):
            nums1[i + m] = nums2[i]
        nums1.sort()

    def merge1(self, nums1, m, nums2, n): # slower, 78ms
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            #return nums1[:m]  Do not return anything, modify nums1 in-place instead.
            while m < len(nums1):
                del nums1[m]
            return
        if m == 0 and n > 0:
            # nums1 = nums2 --- > this would not work !!!, outer scope will still treat nums1 as the old one
            # nums1 = [ x for x in nums2] --> this would not work either
            # nums1 = nums2[:] --> this would not work either
            nums1[:n] = nums2
            while n < len(nums1):
                del nums1[n]
            return
        i = 0
        j = 0
        k = m # should use k to trace current nums1 'length'
        while i < k and j < n:
            if nums1[i]<nums2[j]:
                i += 1
            else:
                nums1.insert(i, nums2[j])
                j += 1
                i += 1
                k += 1  # important, otherwise wrong answer
        if i == k and j < n:
            for k in range(j, n):
                nums1.insert(i, nums2[k])
                i += 1
        # nums1 = list(nums1[:m+n]) this would not work, outer scope still get old value
        # nums1 = copy.copy(nums1[:m+n])
        # if m+n < len(nums1):
        #     # for k in range(m+n, len(nums1)): can't write this way, k will not be -=1, will still have the range() values
        #     #     del nums1[k]
        #     #     k -= 1
        #     k = m+n
        #     while m+n < len(nums1):
        #         del nums1[k]
        while m+n < len(nums1):
            del nums1[m+n]
        #print nums1
        # return nums1


class SolutionTestor(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums1 = [7, 9, 20]
        m = 3
        nums2 = [6, 21]
        n = 2
        self.sol.merge(nums1, m, nums2, n)
        answer = [6, 7, 9, 20, 21]
        self.assertEqual(answer, nums1)

    def test_case2(self): # ====>
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0
        self.sol.merge(nums1, m, nums2, n)
        answer = [1]
        self.assertEqual(answer, nums1)

    def test_case3(self):  # ====>
        nums1 = []
        m = 0
        nums2 = [1]
        n = 1
        result = self.sol.merge(nums1, m, nums2, n)
        answer = [1]
        self.assertEqual(answer, nums1)

    def test_case4(self):  # ====> ?? result is correct a
        nums1 = [0]
        m = 1
        nums2 = [1]
        n = 1
        self.sol.merge(nums1, m, nums2, n)
        answer = [0, 1]
        self.assertEqual(answer, nums1)

    def test_case5(self):  # ====>
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        self.sol.merge(nums1, m, nums2, n)
        answer = [1]
        self.assertEqual(answer, nums1)

    def test_case6(self):  # ====>
        nums1 = [1, 0]
        m = 1
        nums2 = [2]
        n = 1
        self.sol.merge(nums1, m, nums2, n)
        answer = [1, 2]
        self.assertEqual(answer, nums1)

    def test_case7(self):  # ====>
        nums1 = [1,2,3,0,0,0]
        m = 3
        nums2 = [2,5,6]
        n = 3
        self.sol.merge(nums1, m, nums2, n)
        answer = [1,2,2,3,5,6]
        self.assertEqual(answer, nums1)

    def test_case8(self):  # ====>
        nums1 = [2, 0]
        m = 1
        nums2 = [1]
        n = 1
        self.sol.merge(nums1, m, nums2, n)
        answer = [1, 2]
        self.assertEqual(answer, nums1)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTestor)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()
