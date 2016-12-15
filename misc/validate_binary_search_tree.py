"""
98. Validate Binary Search Tree

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.
Subscribe to see which companies asked this question

Hide Tags Tree Depth-first Search
Hide Similar Problems (M) Binary Tree Inorder Traversal

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
    def isValidBST(self, root): #76ms, 58%
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.checkValid(root, None, None)

    def checkValid(self, root, left, right):
        if root is None:
            return True
        if left is not None and root.val <= left: # can't only use left, otherwise when left==0 will result in wrong answer as case4
            return False
        if right is not None and root.val >= right:
            return False
        return self.checkValid(root.left, left, root.val) and self.checkValid(root.right, root.val, right)



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case4(self):
        nums = [0, None, -1]
        answer = False
        result = self.sol.isValidBST(TreeNode.generate_bt_from_list(nums))
        self.assertEqual(answer, result)

    def test_case3(self): #=====> need to check that all the vals in subtree also smaller or greater than the ROOT val!!
        nums = [10,5,15,None,None,6,20]
        answer = False
        result = self.sol.isValidBST(TreeNode.generate_bt_from_list(nums))
        self.assertEqual(answer, result)

    def test_case1(self):
        nums = [2,1,3]
        answer = True
        result = self.sol.isValidBST(TreeNode.generate_bt_from_list(nums))
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [1,2,3]
        answer = False
        result = self.sol.isValidBST(TreeNode.generate_bt_from_list(nums))
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8