#coding=utf-8

import unittest

"""

[check with --> 717. Tree Longest Path With Same Value ]

687. Longest Univalue Path
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may 
or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:

2
Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output:

2
Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.


Difficulty:Easy
Total Accepted:9.7K
Total Submissions:29.1K
Contributor: 1337c0d3r
Subscribe to see which companies asked this question.

Related Topics 
Tree Recursion 
Similar Questions 
Binary Tree Maximum Path Sum Count Univalue Subtrees Path Sum III 

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root)[0]

    def helper(self, root):
        # return two values, first is the longest univalue path, second is the heighest root-leave univalue height
        if not root:
            return 0, 0
        left_path, left_height = self.helper(root.left)
        right_path, right_height = self.helper(root.right)
        root_height = 0
        root_path = 0
        if root.left and root.right and root.val == root.left.val == root.right.val:
            root_path = max(root_path, 2 + left_height + right_height)
        if root.left and root.val == root.left.val:
            root_height = max(root_height, 1 + left_height)
            root_path = max(root_path, 1 + left_height)
        if root.right and root.val == root.right.val:
            root_height = max(root_height, 1 + right_height)
            root_path = max(root_path, 1 + right_height)
        root_path = max(root_path, left_path, right_path, root_height)
        return root_path, root_height


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = 1
        answer = 1
        result = self.sol.testm(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""



"""

#-*- coding:utf-8 -*-
