"""
116. Populating Next Right Pointers in Each Node

Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
Subscribe to see which companies asked this question

Hide Tags Tree Depth-first Search
Hide Similar Problems (H) Populating Next Right Pointers in Each Node II (M) Binary Tree Right Side View

Medium

"""


import unittest
from util.tree_link_node import TreeLinkNode

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        next_head = root.left
        while root:
            if root.left:
                root.left.next = root.right
                if root.next:
                    root.right.next = root.next.left
            root = root.next
        self.connect(next_head)


class Solution1:
    # @param root, a tree link nodeprojected_score
    # @return nothing
    def connect(self, root): #155ms, 6%, 85ms, 74%
        if root is None:
            return
        level_head = root
        while level_head:
            next_level = level_head.left
            tmp = level_head
            while tmp:
                if tmp.left:
                    tmp.left.next = tmp.right
                if tmp.right and tmp.next:
                    tmp.right.next = tmp.next.left
                tmp = tmp.next
            level_head = next_level


    def connect_ref(self, root): #92ms, 54%, 105ms, 32% use the recursive way, may or may not be "CONSTANT SPACE"??
        if root == None or root.left == None:
            return
        root.left.next = root.right
        if root.next != None:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)

    def connect_ref2(self, root): #89ms, 625, very simple code, O(1)space
        while root and root.left:
            next = root.left
            while root:
                root.left.next = root.right
                root.right.next = root.next and root.next.left
                root = root.next
            root = next

class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        #nums = [-1,None, 0,1,None, 2,3,4,5,None, 6,7,8,9,10,11,12,13]
        nums = [-1, 0,1, 2,3,4,5, 6,7,8,9,10,11,12,13]
        root = TreeLinkNode.generate_bt_from_list(nums)
        self.sol.connect(root)
        answer = [-1,None,0,1,None,2,3,4,5,None,6,7,8,9,10,11,12,13,None]
        result = TreeLinkNode.bfs_node_by_next(root)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8
