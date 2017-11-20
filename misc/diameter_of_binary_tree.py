#coding=utf-8

import unittest

"""
543. Diameter of Binary Tree
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the 
length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

Difficulty:Easy
Total Accepted:37.9K
Total Submissions:84.9K
Contributor: nagasupreeth
Subscribe to see which companies asked this question.

Related Topics 
Tree 

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.get_diameter_helper(root)[0]

    def get_diameter_helper(self, root):
        if not root:
            return 0, 0
        left_dia, left_height = self.get_diameter_helper(root.left)
        right_dia, right_height = self.get_diameter_helper(root.right)
        return max(left_dia, right_dia, 2 + left_height + right_height - 2), max(left_height, right_height) + 1

from util.tree_node import TreeNode
class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,2,3,4,5]
        root = TreeNode.generate_bt_from_list(nums)
        answer = 3
        result = self.sol.diameterOfBinaryTree(root)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
