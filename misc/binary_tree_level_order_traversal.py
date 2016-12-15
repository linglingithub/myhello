"""

102. Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,None,None,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
Subscribe to see which companies asked this question

Hide Tags Tree Breadth-first Search
Hide Similar Problems (M) Binary Tree Zigzag Level Order Traversal (E) Binary Tree Level Order Traversal II
(E) Minimum Depth of Binary Tree (M) Binary Tree Vertical Order Traversal

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

    def levelOrder(self, root): #recursive way
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        result = []
        self.traverse(result, 1, root)
        return result

    def traverse(self, result, level, root):
        if root:
            if len(result) < level:
                result.append([])
            result[level-1].append(root.val)
            self.traverse(result, level+1, root.left)
            self.traverse(result, level + 1, root.right)


    def levelOrder1(self, root): #iterative way, 68ms, 30%
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        result = []
        level=[root]
        while level:
            children = []
            tmp = []
            for i in range(len(level)):
                curr = level[i]
                tmp.append(curr.val)
                if curr.left:
                    children.append(curr.left)
                if curr.right:
                    children.append(curr.right)
            result.append(tmp)
            level = children
        return result




    def levelOrder_ref(self, root): #58ms, 53%, recursive way
        res=[]
        self.preorder(root, 0, res)
        return res

    def preorder(self, root, level, res):
        if root:
            if len(res) < level+1: res.append([])
            res[level].append(root.val)
            self.preorder(root.left, level+1, res)
            self.preorder(root.right, level+1, res)


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [3,9,20,None,None,15,7]
        answer = [
          [3],
          [9,20],
          [15,7]
        ]
        result = self.sol.levelOrder(TreeNode.generate_bt_from_list(nums))
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8