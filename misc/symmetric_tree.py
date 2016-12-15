"""

101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,None,3,None,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

Subscribe to see which companies asked this question

Hide Tags Tree Depth-first Search Breadth-first Search

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
    def isSymmetric(self, root): #recursive way, 49ms, 56%
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.checkSymmetric_recur(root.left, root.right)

    def checkSymmetric_recur(self, left, right):
        if left is None and right is None:
            return True
        if left and right and left.val==right.val:
            return self.checkSymmetric_recur(left.left,right.right) and self.checkSymmetric_recur(left.right,right.left)
        return False



    def isSymmetric_iter(self, root): #iterative way, 59ms, 28%
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        level = [root.left, root.right] # should not start from root
        while level:
            cnt = len(level)
            children = []
            idx=0
            for i in range(cnt/2):
                a = level[i]
                b = level[-(i+1)]
                if a is None and b is None:
                    continue
                if a and b and a.val == b.val:  #can not use 2*i ~ 2*i+3 here, maybe None nodes, see case3
                    children.insert(idx,a.left)
                    children.insert(idx+1, a.right)
                    children.insert(idx+2, b.left)
                    children.insert(idx+3, b.right)
                    idx+=2
                else:
                    return False
            level = children
        return True




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case3(self):
        nums = [9,
                -12, -12,
                32, 10, 10, 32,
                None, -79, 95, 88, 88, 95, -79, None,
                -90, None, 56, None, None, 50, 50, None, None, 56, None, -90]
        answer = True
        result = self.sol.isSymmetric(TreeNode.generate_bt_from_list(nums))
        self.assertEqual(answer, result)



    def test_case1(self):
        nums = [1,2,2,3,4,4,3]
        answer = True
        result = self.sol.isSymmetric(TreeNode.generate_bt_from_list(nums))
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [1,2,2,None,3,None,3]
        answer = False
        result = self.sol.isSymmetric(TreeNode.generate_bt_from_list(nums))
        self.assertEqual(answer, result)




def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8