"""

104. Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Subscribe to see which companies asked this question

Hide Tags Tree Depth-first Search
Hide Similar Problems (E) Balanced Binary Tree (E) Minimum Depth of Binary Tree

Easy

"""

import unittest
from tree_node import TreeNode


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root): #iterative way, 72ms, 38%
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        depth = 0
        level = [root]
        while level:
            depth += 1
            children = []
            for tmp in level:
                if tmp.left:
                    children.append(tmp.left)
                if tmp.right:
                    children.append(tmp.right)
            level = children
        return depth


    def maxDepth_recursive(self, root): # recursive, 75ms, 33%
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,2,3,None, None, None, 4]
        answer = 3
        result = self.sol.maxDepth(TreeNode.generate_bt_from_list(nums))
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8