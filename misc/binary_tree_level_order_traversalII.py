"""

107. Binary Tree Level Order Traversal II

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by
level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
Subscribe to see which companies asked this question

Hide Tags Tree Breadth-first Search
Hide Similar Problems (E) Binary Tree Level Order Traversal


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
    def levelOrderBottom(self, root): #recursive way
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        result = []
        self.traverse(result, 1, root)
        result.reverse()
        return result

    def traverse(self, result, level, root):
        if root:
            if len(result) < level:
                result.append([])
            result[level - 1].append(root.val)
            self.traverse(result, level + 1, root.left)
            self.traverse(result, level + 1, root.right)


    def levelOrderBottom_ref(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.results = []
        if not root:
            return self.results
        q = [root]
        while q:
            new_q = []
            self.results.append([n.val for n in q])
            for node in q:
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            q = new_q
        return list(reversed(self.results))


    def levelOrderBottom1(self, root): #iterative, same as I, just reverse result at the end, 49ms, 71%
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
        return result[::-1]


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [3,9,20,None,None,15,7]
        answer = [
          [15,7],
          [9,20],
          [3]
        ]
        result = self.sol.levelOrderBottom(TreeNode.generate_bt_from_list(nums))
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8