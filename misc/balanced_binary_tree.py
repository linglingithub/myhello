"""
110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of
every node never differ by more than 1.

Subscribe to see which companies asked this question

Hide Tags Tree Depth-first Search
Hide Similar Problems (E) Maximum Depth of Binary Tree

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
    def isBalanced(self, root): #79ms, 72%
        if not root:
            return True
        return self.get_height(root) != -1
    
    def get_height(self, root):
        if root is None:
            return 0
        lh = self.get_height(root.left)
        if lh == -1:
            return -1
        rh = self.get_height(root.right)
        if rh == -1:
            return -1
        if abs(lh-rh)>1:
            return -1
        else:
            return max(lh, rh) + 1
    
    
    def isBalanced2(self, root): #68ms, 93%
        if not root:
            return True
        return self.check_balanced(root)[0]
    
    def check_balanced(self, root):
        if root is None:
            return True, 0
        lb, lh = self.check_balanced(root.left)
        if not lb:
            return False, 0
        rb, rh = self.check_balanced(root.right)
        if not rb:
            return False, 0
        return abs(lh-rh)<=1, max(lh,rh)+1
        
    
    
    def isBalanced1(self, root): #125ms, 14%
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        left = self.dfs_helper(root.left, 1)
        right = self.dfs_helper(root.right, 1)
        if abs(left-right) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
    
    def dfs_helper(self, root, depth):
        if root is None:
            return depth
        else:
            return max(self.dfs_helper(root.left, depth+1), self.dfs_helper(root.right, depth+1))
            


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,2,3,4]
        answer = True
        result = self.sol.isBalanced(TreeNode.generate_bt_from_list(nums))
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [1,2,3,4, None, None, None, 8]
        answer = False
        result = self.sol.isBalanced(TreeNode.generate_bt_from_list(nums))
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8