#coding=utf-8

import unittest

"""
215. Kth Largest Element in an Array


Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the
kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.

Subscribe to see which companies asked this question.

Hide Tags Heap Divide and Conquer
Hide Similar Problems (M) Wiggle Sort II (M) Top K Frequent Elements (E) Third Maximum Number


Medium

===================================================================================================================


Find K-th largest element in an array.

 Notice

You can swap elements in the array

Have you met this question in a real interview? Yes
Example
In array [9,3,2,4,8], the 3rd largest element is 4.

In array [1,2,3,4,5], the 1st largest element is 5, 2nd largest element is 4, 3rd largest element is 3 and etc.

Challenge
O(n) time, O(1) extra memory.

Tags
Quick Sort Sort

Related Problems
Medium Wiggle Sort II 25 %
Medium Kth Smallest Numbers in Unsorted Array 33 %
Medium Kth Smallest Number in Sorted Matrix 23 %
Easy Median

"""



class Solution(object):
    def findKthLargest(self, nums, k): #quick select
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or k > len(nums):
            return None
        left, right = 0, len(nums)-1
        while left < right: # ---
            pivot = nums[right]
            i = left-1
            j = left
            while j < right:
                if nums[j] > pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
                j += 1 # don't forget this
            i += 1
            nums[i], nums[right] = nums[right], nums[i]
            if i == k - 1:
                return nums[i]
            elif i > k - 1:
                right = i - 1
            else:
                left = i + 1
        return nums[left]





    def findKthLargest2(self, nums, k): #use sorted first, #52ms, 80%
        return sorted(nums, reverse=True)[k-1]


    def findKthLargest1(self, nums, k): #66ms, 65%, heapq n largest, --> 77% , return heapq.nlargest(k, nums)[-1]
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return None
        import heapq
        tmp = heapq.nlargest(k, nums)
        return tmp[-1]

    def findKthLargest3(self, nums, k): # kth largest is n-k+1 -th smallest, 142ms, 39%
        import heapq
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        for _ in xrange(len(nums)-k):
            heapq.heappop(heap)
        return heapq.heappop(heap)

    def findKthLargest4(self, nums, k):   # quick selection, 3475ms, 5.77%
    # convert the kth largest to smallest
        return self.findKthSmallest(nums, len(nums)+1-k)

    def findKthSmallest(self, nums, k):
        if nums:
            pos = self.partition(nums, 0, len(nums)-1)
            if k > pos+1:
                return self.findKthSmallest(nums[pos+1:], k-pos-1)
            elif k < pos+1:
                return self.findKthSmallest(nums[:pos], k)
            else:
                return nums[pos]

    # choose the right-most element as pivot
    def partition(self, nums, l, r):
        low = l
        while l < r:
            if nums[l] < nums[r]:
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [3,2,1,5,6,4]
        k = 2
        answer = 5
        result = self.sol.findKthLargest(nums, k)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [9,3,2,4,8]
        k = 3
        answer = 4
        result = self.sol.findKthLargest(nums, k)
        self.assertEqual(answer, result)

    def test_case3(self):
        nums = [1,2,3,4,5]
        k = 5
        answer = 1
        result = self.sol.findKthLargest(nums, k)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
"""
378. Kth Smallest Element in a Sorted Matrix
230. Kth Smallest Element in a BST

# O(nlgn) time
def findKthLargest1(self, nums, k):
    return sorted(nums, reverse=True)[k-1]

# O(nk) time, bubble sort idea, TLE
def findKthLargest2(self, nums, k):
    for i in xrange(k):
        for j in xrange(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                # exchange elements, time consuming
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums[len(nums)-k]

# O(nk) time, selection sort idea
def findKthLargest3(self, nums, k):
    for i in xrange(len(nums), len(nums)-k, -1):
        tmp = 0
        for j in xrange(i):
            if nums[j] > nums[tmp]:
                tmp = j
        nums[tmp], nums[i-1] = nums[i-1], nums[tmp]
    return nums[len(nums)-k]

# O(k+(n-k)lgk) time, min-heap
def findKthLargest4(self, nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
    for _ in xrange(len(nums)-k):
        heapq.heappop(heap)
    return heapq.heappop(heap)

# O(k+(n-k)lgk) time, min-heap
def findKthLargest5(self, nums, k):
    return heapq.nlargest(k, nums)[k-1]

# O(n) time, quick selection
def findKthLargest(self, nums, k):
    # convert the kth largest to smallest
    return self.findKthSmallest(nums, len(nums)+1-k)

def findKthSmallest(self, nums, k):
    if nums:
        pos = self.partition(nums, 0, len(nums)-1)
        if k > pos+1:
            return self.findKthSmallest(nums[pos+1:], k-pos-1)
        elif k < pos+1:
            return self.findKthSmallest(nums[:pos], k)
        else:
            return nums[pos]

# choose the right-most element as pivot
def partition(self, nums, l, r):
    low = l
    while l < r:
        if nums[l] < nums[r]:
            nums[l], nums[low] = nums[low], nums[l]
            low += 1
        l += 1
    nums[low], nums[r] = nums[r], nums[low]
    return low



=======

In computer science, quickselect is a selection algorithm to find the kth smallest element in an unordered list. It is
related to the quicksort sorting algorithm. Like quicksort, it was developed by Tony Hoare, and thus is also known as
Hoare's selection algorithm.[1] Like quicksort, it is efficient in practice and has good average-case performance, but
has poor worst-case performance. Quickselect and its variants are the selection algorithms most often used in efficient
real-world implementations.

Quickselect uses the same overall approach as quicksort, choosing one element as a pivot and partitioning the data in
two based on the pivot, accordingly as less than or greater than the pivot. However, instead of recursing into both
sides, as in quicksort, quickselect only recurses into one side – the side with the element it is searching for. This
reduces the average complexity from O(n log n) to O(n), with a worst case of O(n2).


"""