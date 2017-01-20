__author__ = 'linglin'

"""

Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Subscribe to see which companies asked this question

Hide Tags Tree Depth-first Search Breadth-first Search
Hide Similar Problems (E) Binary Tree Level Order Traversal (E) Maximum Depth of Binary Tree

Easy

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
    def minDepth(self, root): #DFS, 14% --> 68%
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.result = None
        self.find_min(root, 0)
        return self.result

    def find_min(self, root, height):
        if root is None:
            return
        elif root.left is None and root.right is None:
            self.result = min(self.result, height+1) if self.result is not None else height+1
            return
        else:
            self.find_min(root.left, height+1)
            self.find_min(root.right,height+1)







    def minDepth_bfs(self, root): #BFS, 5.15 --> 93%
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        result = 0
        queue = [root]
        while queue:
            result += 1
            next_level = []
            while queue:
                tmp = queue.pop(0)
                if tmp.left is None and tmp.right is None:
                    return result
                else:
                    if tmp.left:
                        next_level.append(tmp.left)
                    if tmp.right:
                        next_level.append(tmp.right)
            queue = next_level


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,2,3]
        answer = 2
        result = self.sol.minDepth(TreeNode.generate_bt_from_list(nums))
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [1,2,3,4,None]
        answer = 2
        result = self.sol.minDepth(TreeNode.generate_bt_from_list(nums))
        self.assertEqual(answer, result)

    def test_case3(self): #===> wrong for dfs
        nums = [1,2]
        answer = 2
        result = self.sol.minDepth(TreeNode.generate_bt_from_list(nums))
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8