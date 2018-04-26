#coding=utf-8

import unittest

from util.tree_node import TreeNode
"""

653. Two Sum IV - Input is a BST
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum 
is equal to the given target.

Example 1:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
Example 2:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False


Difficulty:Easy
Total Accepted:21.9K
Total Submissions:43.4K
Contributor: aghanta
Subscribe to see which companies asked this question.

Related Topics 
Tree 
Similar Questions 
Two Sum Two Sum II - Input array is sorted Two Sum III - Data structure design 
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        left_gen = self.get_bigger(root)
        right_gen = self.get_smaller(root)
        left = next(left_gen)
        right = next(right_gen)
        while left != right:
            tmp = left.val + right.val
            if tmp == k:
                return True
            elif tmp < k:
                left = next(left_gen)
            else:
                right = next(right_gen)
        return False

    def get_bigger(self, root):
        """Generator method to return next bigger node in the tree. Traverse inorder.
        Assumptions: root is not None

        """
        stack = deque()
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            if stack:
                node = stack.pop()
                yield node
                node = node.right
        return None

    def get_smaller(self, root):
        """Generator method to return next smaller node in the tree. Reverse traverse inorder.

        """
        stack = deque()
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.right
            if stack:
                node = stack.pop()
                yield node
                node = node.left
        return None


class Solution1(object):
    def findTarget(self, root, n):
        if not root:
            return None
        vals = {}
        return self.helper(root, vals, n)

    def helper(self, root, vals, n):
        if not root:
            return False
        if n - root.val in vals:
            return True
        vals[root.val] = 1
        return self.helper(root.left, vals, n) or self.helper(root.right, vals, n)


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [5, 3, 6, 2, 4, None, 7]
        target = 9
        root = TreeNode.generate_bt_from_list(nums)
        answer = True
        result = self.sol.findTarget(root, target)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [5, 3, 6, 2, 4, None, 7]
        target = 28
        root = TreeNode.generate_bt_from_list(nums)
        answer = False
        result = self.sol.findTarget(root, target)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""
many ways (3) to do it.
check out if have time

https://leetcode.com/problems/two-sum-iv-input-is-a-bst/discuss/

"""