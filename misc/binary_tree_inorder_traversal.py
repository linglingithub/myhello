"""
94. Binary Tree Inorder Traversal

Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?

Subscribe to see which companies asked this question

Hide Tags Tree Hash Table Stack
Hide Similar Problems (M) Validate Binary Search Tree (M) Binary Tree Preorder Traversal
(H) Binary Tree Postorder Traversal (M) Binary Search Tree Iterator (M) Kth Smallest Element in a BST
(H) Closest Binary Search Tree Value II (M) Inorder Successor in BST


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
    def inorderTraversal(self, root): #iterative way, 59ms, 15% --> 36ms, 73%
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        result = []
        p = root
        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            if not p and stack:
                p = stack.pop()
                result.append(p.val)
                p = p.right
        return result



    def inorderTraversal_recursive(self, root): #38ms, 69%
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.traverse(root,result)
        return result

    def traverse(self, root, result):
        if root is None:
            return
        self.traverse(root.left,result)
        result.append(root.val)
        self.traverse(root.right,result)

#######################################################################


    def iterative_inorder(self, root, list):
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                list.append(root.val)
                root = root.right
        return list

    def recursive_inorder(self, root, list):
        if root:
            self.recursive_inorder(root.left, list)
            list.append(root.val)
            self.recursive_inorder(root.right, list)

    def inorderTraversal_ref2(self, root):
        list = []
        self.iterative_inorder(root, list)
        return list




    def inorderTraversal_ref(self, root): #59ms, 15%
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] \
               + self.inorderTraversal(root.right)




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1, None,2,3]
        answer = [1,3,2]
        result = self.sol.inorderTraversal(TreeNode.generate_bt_from_list(nums))
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [1, 2,None,3]
        answer = [3,2,1]
        result = self.sol.inorderTraversal(TreeNode.generate_bt_from_list(nums))
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8