#coding=utf-8
__author__ = 'linglin'

"""
114. Flatten Binary Tree to Linked List

Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
click to show hints.

Hints:
If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.

Subscribe to see which companies asked this question

Hide Tags Tree Depth-first Search

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
    def flatten(self, root): #63ms, 27%, actually the helper can return just one result, root can be neglected
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        self.flatten_helper(root)

    def flatten_helper(self, root):
        if root.left is None and root.right is None:
            return root, root
        elif root.left is None:
            a, b = self.flatten_helper(root.right)
            return root, b
        elif root.right is None:
            a, b = self.flatten_helper(root.left)
            root.right = a
            b.right = None
            root.left = None # don't forget to make left None, seems like this is a requirement, otherwise wrong for case2
            return root, b
        else:
            tmp = root.right
            a, b = self.flatten_helper(root.left)
            root.right = a
            c, d = self.flatten_helper(tmp)
            b.right = c
            root. left = None # same as above
            return root, d





class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case2(self):
        nums = [1,2]
        root = TreeNode.generate_bt_from_list(nums)
        answer = [1,2]
        self.sol.flatten(root)
        result = TreeNode.get_tree_right_list(root)
        self.assertEqual(answer, result)

    def test_case1(self):
        nums = [1,2,5,3,4,None, 6]
        root = TreeNode.generate_bt_from_list(nums)
        answer = [1,2,3,4,5,6]
        self.sol.flatten(root)
        result = TreeNode.get_tree_right_list(root)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""

another post with good explanations of different ways.

http://bangbingsyb.blogspot.com/2014/11/leetcode-flatten-binary-tree-to-linked.html

==============================


题目大意：
给定一棵二叉树，将其就地展开成为一个链表。

测试用例如题目描述。

提示：

如果你仔细观察展开后的树，可以发现每一个节点的右孩子都是其先序遍历的下一个节点。

解题思路：
解法I 非递归先序遍历（Non-recursive Preorder Traversal）

Python代码：
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):

        pointer = dummy = TreeNode(None)
        stack = [root]
        while stack:
            top = stack.pop()
            if not top: continue
            stack.append(top.right)
            stack.append(top.left)
            pointer.right = top
            pointer.left = None
            pointer = top

解法II 递归后序遍历（Recursive Postorder Traversal）

这里对标准的递归后序遍历稍作改动，由“左-右-根”变更为“右-左-根”，详见代码。

Python代码：
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        self.pointer = None
        def traverse(root):
            if not root: return
            traverse(root.right)
            traverse(root.left)
            root.right = self.pointer
            root.left = None
            self.pointer = root
        traverse(root)



本文链接：http://bookshadow.com/weblog/2016/09/02/leetcode-flatten-binary-tree-to-linked-list/

"""


#-*- coding:utf-8 -*-
