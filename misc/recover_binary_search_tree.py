__author__ = 'linglin'
"""

99. Recover Binary Search Tree

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
Subscribe to see which companies asked this question

Hide Tags Tree Depth-first Search

Hard

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
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        self.result = []
        self.find_wrong_nodes(root)
        if len(self.result) == 2:
            tmp = self.result[0].val
            self.result[0].val = self.result[1].val
            self.result[1].val = tmp

    def find_wrong_nodes(self,root):
        if root is None:
            return
        if root.left:
            if root.left.val > root.val:
                self.result.append(root.left)
                if len(self.result)==2:
                    return
            else:
                self.find_wrong_nodes(root.left)
        if root.right:
            if root.right.val






class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [3,1,2]
        answer = [2,1,3]
        root = TreeNode.generate_bt_from_list(nums)
        self.sol.recoverTree(root)
        compare = TreeNode.compare_tree(root, TreeNode.generate_bt_from_list(answer))
        self.assertTrue(compare)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8