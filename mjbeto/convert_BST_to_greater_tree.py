# coding=utf-8

"""

Convert BST to Greater Tree


Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to 
the original key plus sum of all keys greater than the original key in BST.

Have you met this question in a real interview? Yes
Example
Given a binary search Tree ｀{5,2,3}｀:

              5
            /   \
           2     13
Return the root of new tree

             18
            /   \
          20     13
Tags 
Binary Search Tree Binary Tree Amazon

"""

import unittest

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the new root
    def convertBST(self, root):
        # accepted online, some answer shows that can actually modify the tree in place
        # originally thinks that it requires to construct and return a 'new' tree
        # Write your code here
        if not root:
            return None
        new_root = self.convert(root, [0])
        return new_root

    def convert(self, root, gsum):
        if root.left is None and root.right is None:
            gsum[0] += root.val
            node = TreeNode(gsum[0])  # don't forget to add gsum here
            return node
        new_right = None
        if root.right:
            new_right = self.convert(root.right, gsum)
        gsum[0] += root.val
        node = TreeNode(gsum[0])
        node.right = new_right
        if root.left:
            new_left = self.convert(root.left, gsum)
            node.left = new_left
        return node


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1, 2, 3, 4]
        answer = [24, 12, 8, 6]
        result = self.sol.productExceptSelf(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner.run(suite)


if __name__ == '__main__':
    main()

"""

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the new root
    def convertBST(self, root):
        # Write your code here
        self.sum = 0
        self.helper(root)
        return root

    def helper(self, root):
        if root is None:
            return
        if root.right:
            self.helper(root.right)
        
        self.sum += root.val
        root.val = self.sum
        if root.left:
            self.helper(root.left)

"""