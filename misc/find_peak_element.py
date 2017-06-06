#coding=utf-8
"""

Find Peak Element

A peak element is an element that is greater than its neighbors.

Given an input array where num[i] <> num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -infinite.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

click to show spoilers.

Note:
Your solution should be in logarithmic complexity.

=======


Next challenges: (M) Summary Ranges  (M) Kth Smallest Element in a BST  (E) Closest Binary Search Tree Value

Medium

================================================================================================================

There is an integer array which has the following features:

The numbers in adjacent positions are different.
A[0] < A[1] && A[A.length - 2] > A[A.length - 1].
We define a position P is a peek if:

A[P] > A[P-1] && A[P] > A[P+1]
Find a peak element in this array. Return the index of the peak.

"""

import unittest

class Solution(object):
    """
    This is an important assumption: You may imagine that num[-1] = num[n] = -infinite.
    Which means that two ends are half - qualified as the candidates
    """


    def findPeak(self, A):
        # write your code here
        if not A:
            return -1
        left, right = 1, len(A)-2
        while left <= right:
            mid = (left+right)/2
            if A[mid-1]<A[mid] and A[mid]>A[mid+1]:
                return mid
            elif A[mid-1] > A[mid]:
                right = mid-1
            else:
                left = mid + 1
        return left if A[left] > A[right] else right
        # return left  -- this is better

    def findPeakElement(self, nums): #55ms, 23%
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        l = 0
        r = len(nums)-1
        while l < r:
            mid = (l+r)/2
            if mid==l:
                return mid if nums[mid]>nums[r] else r
            if nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid-1]<nums[mid]:
                l = mid+1
            else:
                r = mid - 1
        return l





    def findPeakElement2(self, nums):
        if nums is None or len(nums) == 0:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            if left == right:
                return left
            mid = (left+right)/2
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid

    def findPeakElement1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        mid = (left + right) / 2
        while mid <= len(nums) - 1 and mid >= 0:
            # for array
            if left == right:
                return left
            if left == mid:
                return [left, right][0 if nums[left] > nums[right] else 1]
            if mid == 0 or mid == len(nums) - 1:
                return mid
            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid - 1] < nums[mid]:
                left = mid
            else:
                right = mid
            mid = (right + left) / 2
            #print "mid = ", mid, "left = ", left, "right = ", right
        return mid





class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case3(self):
        result = self.sol.findPeakElement([5, 4])
        #print result
        self.assertEqual(result, 0)

    def test_case1(self):
        result = self.sol.findPeakElement([1, 2, 3, 1])
        #print result
        self.assertEqual(result, 2)

    def test_case2(self):
        result = self.sol.findPeakElement([1, 2, 3, 4])
        #print result
        self.assertEqual(result, 3)

    def test_case4(self):
        result = self.sol.findPeakElement([1])
        # print result
        self.assertEqual(result, 0)

    def test_case5(self):
        result = self.sol.findPeakElement([])
        # print result
        self.assertEqual(result, -1)



            # def testcase1(self):
    #     s = "hello world"
    #     self.assertEqual(s.split(), ['hello', 'world'])


if __name__ == '__main__':
    # arr = [1,2,3,1]
    # arr = [1,2,3,4]
    # arr = [1,2]
    arr = [3, 1]
    sol = Solution()
    # print sol.findPeakElement(arr)
    # print "LLLLLLLLLLL ========="
    # unittest.main()

    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

    # solTestSuite = unittest.TestSuite()
    # solTestSuite.addTest(SolutionTest('test_case1'))
    # solTestSuite.addTest(SolutionTest('test_case2'))
    # unittest.TextTestRunner(verbosity=2).run(solTestSuite)

"""


最简单地解法就是遍历数组复杂度为O(N)，只要找到第一个元素，大于两边就可以了，但这题还可以用更优化的二分搜索来做。

首先我们的目标是找到中间节点mid， 1.如果大于两边的数字那么就是找到了答案，直接返回找到的答案。  2. 如果左边的节点比mid大，那么我们可以继续
在左半区间查找，因为左边可以证明一定存在一个peak element， 为什么呢？因为题目告诉了我们区间[0, mid - 1] 中num[0] < num[1]，我们刚才又
知道num[mid - 1]>num[mid]了，所以[0, mid - 1] 之间肯定有一个peak element。  3. 如果num[mid - 2] > num[mid - 1]，那么我们就继续
在[0, mid - 2]区间查找，那么同理可以在右边的区间找到一个peak element。所以继续这个二分搜索的方式最后我们就能找到一个peak element。


"""