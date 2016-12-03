#coding=utf-8

"""
81. Search in Rotated Sorted Array II

Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.

Subscribe to see which companies asked this question

Hide Tags Array Binary Search
Hide Similar Problems (H) Search in Rotated Sorted Array

Medium

"""

import unittest


class Solution(object):
    def search(self, nums, target): #75ms, 6.63%
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return -1
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right) / 2
            if nums[mid] == target:
                return True
            if nums[mid]<nums[right]: # starting point in left half
                if nums[mid]<target<=nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[mid]>nums[right]:  # starting point in the right half
                if nums[left]<= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                #left += 1 # wrong for case 2 and 5, because you're using nums[right] to compare with nums[mid],
                # so here you can only move the right.
                # if you are using mid and left for deciding where the starting point is , then you should move left
                right -= 1
        return False


    def search_ref(self, A, target): #36ms, 93.12%, faster for the test cases.
        # very smart here to check if left , mid and right are equal first, if yes, then move both left , right
        # if not three equal values (only two still fine), then you can feel free to cut half, which makes it much faster!!
        left=0; right=len(A)-1
        while left<=right:
            mid=(left+right)/2
            if A[mid]==target: return True
            if A[left]==A[mid]==A[right]:
                left+=1; right-=1
            elif A[left]<=A[mid]:
                if A[left]<=target<A[mid]: right=mid-1
                else: left=mid+1
            else:
                if A[mid]<=target<A[left]: left=mid+1
                else:right=mid-1
        return False


    def search_ref2(self, A, target): # 52ms, 48%
        left, right = 0, len(A) - 1
        while left <= right:
            mid = (left + right) / 2
            if A[mid] == target: return True
            if A[left] < A[mid]: # the right part is rotated
                if A[left] <= target < A[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif A[left] > A[mid]: # the left part is rotated
                if A[mid] < target <= A[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else: # A[left] == A[mid]
                left += 1
        return False


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case5(self): #====>
        nums = [3,1,1]
        target = 3
        answer = True
        result = self.sol.search(nums, target)
        self.assertEqual(answer, result)


    def test_case1(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 1
        answer = True
        result = self.sol.search(nums, target)
        self.assertEqual(answer, result)


    def test_case2(self):
        nums = [3,3,1,2,3,3,3,3,3]
        target = 1
        answer = True
        result = self.sol.search(nums, target)
        self.assertEqual(answer, result)


    def test_case3(self):
        nums = [3,3,3,3,3,3, 1,2,3]
        target = 1
        answer = True
        result = self.sol.search(nums, target)
        self.assertEqual(answer, result)

    def test_case4(self):
        nums = [3,3,3,3,3,3, 1,2,3]
        target = 5
        answer = False
        result = self.sol.search(nums, target)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-


"""

当有重复数字，会存在A[mid] = A[end]的情况。此时右半序列A[mid-1 : end]可能是sorted，也可能并没有sorted，如下例子。

3 1 2 3 3 3 3
3 3 3 3 1 2 3

所以当A[mid] = A[end] != target时，无法排除一半的序列，而只能排除掉A[end]：

A[mid] = A[end] != target时：搜寻A[start : end-1]

正因为这个变化，在最坏情况下，算法的复杂度退化成了O(n)：
序列 2 2 2 2 2 2 2 中寻找target = 1。



=========================================

public class Solution {
    // 这个问题在面试中不会让实现完整程序
    // 只需要举出能够最坏情况的数据是 [1,1,1,1... 1] 里有一个0即可。
    // 在这种情况下是无法使用二分法的，复杂度是O(n)
    // 因此写个for循环最坏也是O(n)，那就写个for循环就好了
    //  如果你觉得，不是每个情况都是最坏情况，你想用二分法解决不是最坏情况的情况，那你就写一个二分吧。
    //  反正面试考的不是你在这个题上会不会用二分法。这个题的考点是你想不想得到最坏情况。
    public boolean search(int[] A, int target) {
        for (int i = 0; i < A.length; i ++) {
            if (A[i] == target) {
                return true;
            }
        }
        return false;
    }
}

"""