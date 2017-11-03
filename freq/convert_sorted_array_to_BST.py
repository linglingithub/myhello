"""
108. Convert Sorted Array to Binary Search Tree

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

Subscribe to see which companies asked this question

Hide Tags Tree Depth-first Search
Hide Similar Problems (M) Convert Sorted List to Binary Search Tree

Medium

"""

import unittest

from util.tree_node import TreeNode


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        return self.gen_tree(nums, 0, len(nums) - 1)

    def gen_tree(self, nums, left, right):
        if left > right:
            return None
        if left == right:
            return TreeNode(nums[left])
        mid = left + int((right - left) / 2)
        root = TreeNode(nums[mid])
        root.left = self.gen_tree(nums, left, mid - 1)
        root.right = self.gen_tree(nums, mid + 1, right)
        return root


class Solution1(object):
    def sortedArrayToBST(self, nums): #92ms, 77%
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        self.nums = nums
        return self.helper(0, len(nums)-1)

    def helper(self, left, right):
        if left>right:
            return None
        if left==right:
            return TreeNode(self.nums[left])
        mid = (left+right) / 2
        root = TreeNode(self.nums[mid])
        root.left = self.helper(left, mid-1)
        root.right = self.helper(mid+1, right)
        return root



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,2,3,4,5,6,7]
        answer = TreeNode.generate_bt_from_list([4,2,6,1,3,5,7])
        result = self.sol.sortedArrayToBST(nums)
        self.assertTrue(TreeNode.compare_tree(answer, result))


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8