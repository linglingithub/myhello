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
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return []
        l, r = 0, len(nums) - 1
        pos = self.quick_select(nums, l, r)
        while pos != k - 1:
            print("pos: ", pos, nums)
            if pos < k - 1:
                pos = self.quick_select(nums, pos + 1, r)
            else:
                pos = self.quick_select(nums, l, pos - 1)
        return nums[k - 1]

    def quick_select(self, nums, l, r):
        """
        bigger -> smaller
        """
        if l == r:
            return l
        i, j = l - 1, r - 1  # i for the end of good parts ( bigger vals)
        pivot = nums[r]
        # if i == j:
        #     if nums[i] < nums[r]:
        #         nums[i], nums[r] = nums[r], nums[j]
        #     return r
        while i < r:
            while i + 1 <= j and nums[i + 1] > pivot:
                i += 1
            while j > i and nums[j] < pivot:
                # can't put <= here, otherwise wrong for case4, infinite loop because
                # duplicated values are not sorted, checkout stdout
                # hint -==> when looking for max kth value, do NOT miss out the bigger or equal values,
                # therefore, for nums[j] that == pivot should be moved to left good part too
                j -= 1
            # print("l, r, == i, j ==: ", l, r, i, j)
            if i >= j:
                break
            nums[i + 1], nums[j] = nums[j], nums[i + 1]
            # print("nums: ", nums)
            i += 1
        if i + 1 <= r:  # should include =
            nums[i + 1], nums[r] = nums[r], nums[i + 1]
            i += 1  # don't forget this
        # print("sorted nums: ", nums)
        return i

    def findKthLargest1(self, nums, k):
        """
        using min- heap
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        heap = []
        for num in nums:
            #print("status... ", heap)
            if len(heap) < k:
                heapq.heappush(heap, num)
                continue   # important !!!
            if num > heap[0]:
                tmp = heapq.heappop(heap)
                heapq.heappush(heap, num)
                #print("poping... ", tmp, heap)
        return heap[0]


class Solution1(object):
    def findKthLargest(self, nums, k): #quick select
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or k > len(nums):
            return None
        left, right = 0, len(nums)-1 # current partition range [left, right]
        while left < right: # while partition range >1, if only one, then return result
            pivot = nums[right]    # last num of current partition range as pivot
            i = left-1    # 'good' array's ending pos ( good means eles bigger than pivot ) ,starting as -1 cause not found yet
            j = left      # the current num to be compared with pivot, start from left and ends on right-1
            while j < right:
                if nums[j] > pivot:   # if bigger, than swap to good array end+1
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
                j += 1 # don't forget this
            i += 1      # all good eles bigger than pivot found, now put pivot to where it should be, which is i + 1
            nums[i], nums[right] = nums[right], nums[i]
            if i == k - 1:       # after partition, i is the pos of pivot, compare with k, then adjust the partition range
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
        for _ in range(len(nums)-k):
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

    def test_case4(self):
        nums = [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6]
        k = 20
        answer = 2
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



===================

https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/

This problem is well known and quite often can be found in various text books.

You can take a couple of approaches to actually solve it:

O(N lg N) running time + O(1) memory
The simplest approach is to sort the entire input array and then access the element by it's index (which is O(1)) operation:

public int findKthLargest(int[] nums, int k) {
        final int N = nums.length;
        Arrays.sort(nums);
        return nums[N - k];
}
O(N lg K) running time + O(K) memory
Other possibility is to use a min oriented priority queue that will store the K-th largest values. The algorithm iterates over the whole input and maintains the size of priority queue.

public int findKthLargest(int[] nums, int k) {

    final PriorityQueue<Integer> pq = new PriorityQueue<>();
    for(int val : nums) {
        pq.offer(val);

        if(pq.size() > k) {
            pq.poll();
        }
    }
    return pq.peek();
}
O(N) best case / O(N^2) worst case running time + O(1) memory
The smart approach for this problem is to use the selection algorithm (based on the partion method - the same one as used in quicksort).

public int findKthLargest(int[] nums, int k) {

        k = nums.length - k;
        int lo = 0;
        int hi = nums.length - 1;
        while (lo < hi) {
            final int j = partition(nums, lo, hi);
            if(j < k) {
                lo = j + 1;
            } else if (j > k) {
                hi = j - 1;
            } else {
                break;
            }
        }
        return nums[k];
    }

    private int partition(int[] a, int lo, int hi) {

        int i = lo;
        int j = hi + 1;
        while(true) {
            while(i < hi && less(a[++i], a[lo]));
            while(j > lo && less(a[lo], a[--j]));
            if(i >= j) {
                break;
            }
            exch(a, i, j);
        }
        exch(a, lo, j);
        return j;
    }

    private void exch(int[] a, int i, int j) {
        final int tmp = a[i];
        a[i] = a[j];
        a[j] = tmp;
    }

    private boolean less(int v, int w) {
        return v < w;
    }
O(N) guaranteed running time + O(1) space

So how can we improve the above solution and make it O(N) guaranteed? The answer is quite simple, we can randomize the input, so that even when the worst case input would be provided the algorithm wouldn't be affected. So all what it is needed to be done is to shuffle the input.

public int findKthLargest(int[] nums, int k) {

        shuffle(nums);
        k = nums.length - k;
        int lo = 0;
        int hi = nums.length - 1;
        while (lo < hi) {
            final int j = partition(nums, lo, hi);
            if(j < k) {
                lo = j + 1;
            } else if (j > k) {
                hi = j - 1;
            } else {
                break;
            }
        }
        return nums[k];
    }

private void shuffle(int a[]) {

        final Random random = new Random();
        for(int ind = 1; ind < a.length; ind++) {
            final int r = random.nextInt(ind + 1);
            exch(a, ind, r);
        }
    }
There is also worth mentioning the Blum-Floyd-Pratt-Rivest-Tarjan algorithm that has a guaranteed O(N) running time.

"""