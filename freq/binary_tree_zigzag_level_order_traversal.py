"""
103. Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then
right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,None,None,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
Subscribe to see which companies asked this question

Hide Tags Tree Breadth-first Search Stack
Hide Similar Problems (E) Binary Tree Level Order Traversal

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
    def zigzagLevelOrder(self, root):
        """
        use a stack
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stack = [root]
        res = []
        forward = True
        while stack:
            res.append([])
            children = []
            while stack:
                node = stack.pop()
                res[-1].append(node.val)
                if forward:
                    if node.left:
                        children.append(node.left)
                    if node.right:
                        children.append(node.right)
                else:
                    if node.right:
                        children.append(node.right)
                    if node.left:
                        children.append(node.left)

            stack = children
            forward = not forward  # don't forget this
        return res

    def zigzagLevelOrder1(self, root):
        """
        use a queue
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        level = [root]
        res = []
        forward = True
        while level:
            res.append([])
            children = []
            if forward:
                for node in level:
                    res[-1].append(node.val)
                    if node.left:
                        children.append(node.left)
                    if node.right:
                        children.append(node.right)
            else:
                for i in range(len(level)-1, -1, -1):
                    node = level[i]
                    res[-1].append(node.val)
                    if node.right:
                        children.insert(0, node.right)
                    if node.left:
                        children.insert(0, node.left)
            level = children
            forward = not forward  # don't forget this
        return res


class Solution1(object):
    def zigzagLevelOrder(self, root): # 39ms, 86%, change to shuffle the way to insert into level,
        """
        [1,23,45 67]
        1 -- 2,3
        3,2 -- 7,6,5,4

        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        result = []
        left = True
        level = [root]
        while level:
            children = []
            result.append([])
            if left:
                for i in range(len(level)):
                    tmp = level[i]
                    result[-1].append(tmp.val)
                    children.append(tmp.left)
                    children.append(tmp.right)
            else:
                for i in range(len(level)):
                    tmp = level[i]
                    result[-1].insert(0,tmp.val)
                    children.append(tmp.left)  #note, here is the same as left flag, first left child, then right child
                    children.append(tmp.right)
            level = [x for x in children if x is not None]
            left = not left
        return result


    def zigzagLevelOrder2(self, root): #move left or right uppper, 42ms, 73%
        """
        [1,23,45 67]
        1 -- 2,3
        3,2 -- 7,6,5,4

        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        result = []
        left = True
        level = [root]
        while level:
            children = []
            result.append([])
            if left:
                for i in range(len(level)-1, -1, -1):
                    tmp = level[i]
                    if tmp:
                        result[-1].append(tmp.val)
                        children.append(tmp.left)
                        children.append(tmp.right)
            else:
                for i in range(len(level)-1, -1, -1):
                    tmp = level[i]
                    if tmp:
                        result[-1].append(tmp.val)
                        children.append(tmp.right)
                        children.append(tmp.left)

            level = [x for x in children if x is not None]
            left = not left
        return result


    def zigzagLevelOrder1(self, root): #65ms, 17%
        """
        [1,23,45 67]
        1 -- 2,3
        3,2 -- 7,6,5,4

        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        result = []
        left = True
        level = [root]
        while level:
            children = []
            result.append([])
            for i in range(len(level)-1, -1, -1):
                tmp = level[i]
                if tmp:
                    if left:
                        result[-1].append(tmp.val)
                        children.append(tmp.left)
                        children.append(tmp.right)
                    else:
                        result[-1].append(tmp.val)
                        children.append(tmp.right)
                        children.append(tmp.left)
            level = [x for x in children if x is not None]
            left = not left
        return result


    def zigzagLevelOrder_ref(self, root): #recursive way, code is clean, need to think more to understand
        """

        :param root:
        :return:
        """
        self.results = []
        self.preorder(root, 0, self.results)
        return self.results

    def preorder(self, root, level, res):
        if root:
            if len(res) < level+1: res.append([])
            if level % 2 == 0:
                res[level].append(root.val)
            else:
                res[level].insert(0, root.val)
            self.preorder(root.left, level+1, res)
            self.preorder(root.right, level+1, res)


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [3,9,20,None,None,15,7]
        answer = [
          [3],
          [20,9],
          [15,7]
        ]
        result = self.sol.zigzagLevelOrder(TreeNode.generate_bt_from_list(nums))
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8