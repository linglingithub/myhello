"""
117. Populating Next Right Pointers in Each Node II

Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
Subscribe to see which companies asked this question

Hide Tags Tree Depth-first Search
Hide Similar Problems (M) Populating Next Right Pointers in Each Node


Hard

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
    # @param root, a tree link nodeprojected_score
    # @return nothing
    def connect3(self, root): # O(1) space, 92ms, 85%
        if root is None:
            return
        head = root
        while head:
            next_head = None
            tmp = head
            pre = None
            while tmp:
                if not next_head:
                    next_head = tmp.left or tmp.right
                if tmp.left:
                    # if not pre:
                    #    pre = tmp.left
                    # else:
                    #     pre.next = tmp.left
                    #     pre = tmp.left
                    # --> can be simplified as :
                    if pre:
                        pre.next = tmp.left
                    pre = tmp.left
                if tmp.right:
                    if pre:
                        pre.next = tmp.right
                    pre = tmp.right
                tmp = tmp.next
            head = next_head


    def connect2(self, root): # O(1) space, 18%, 119ms, 31%, sibs is array, will be slower, can use (pre, post, etc) to make it faster
        if root is None:
            return
        head = root
        while head:
            next_head = None
            tmp = head
            sibs = [] # should be no more than 3
            while tmp:
                if not next_head:
                    next_head = tmp.left or tmp.right
                if tmp.left:
                    sibs.append(tmp.left)
                if tmp.right:
                    sibs.append(tmp.right)
                if len(sibs)>=2:
                    for i in range(len(sibs)-1):
                        sibs[i].next = sibs[i+1]
                    sibs = [sibs[-1]]
                tmp = tmp.next

            head = next_head



    def connect1(self, root): # not O(1) space, 119ms, 31%, 102ms, 60%
        if root is None:
            return
        level = [root]
        while level:
            next_level = []
            for tmp in level:
                if tmp.left:
                    next_level.append(tmp.left)
                if tmp.right:
                    next_level.append(tmp.right)
            for i in range(len(next_level)-1):
                next_level[i].next = next_level[i+1]
            level = next_level

    def connect(self, root): #simple and fast, 99ms, 69%, but not easy to understand, need to debug and step into
        dummy = TreeLinkNode(-1)
        node = dummy
        while root:
            while root:
                node.next = root.left
                node = node.next or node
                node.next = root.right
                node = node.next or node
                root = root.next
            root, node = dummy.next, dummy


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1, 2,3,4,5, None,7]
        root = TreeLinkNode.generate_bt_from_list(nums)
        self.sol.connect(root)
        answer = [1,None,2,3,None, 4,5,7,None]
        result = TreeLinkNode.bfs_node_by_next(root)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8
