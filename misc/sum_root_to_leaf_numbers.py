__author__ = 'linglin'
"""


129. Sum Root to Leaf Numbers


Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.

Subscribe to see which companies asked this question

Hide Tags Tree Depth-first Search
Hide Similar Problems (E) Path Sum (H) Binary Tree Maximum Path Sum


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
    def sumNumbers(self, root): #46ms, 55%
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.sum = 0
        self.dfs_sn(root, 0)
        return self.sum

    def dfs_sn(self, root, path_sum):
        path_sum = path_sum *10 + root.val
        if root.left is None and root.right is None:
            self.sum += path_sum
            return
        if root.left:
            self.dfs_sn(root.left, path_sum)
        if root.right:
            self.dfs_sn(root.right, path_sum)







class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,2,3]
        answer = 25
        result = self.sol.sumNumbers(TreeNode.generate_bt_from_list(nums))
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8