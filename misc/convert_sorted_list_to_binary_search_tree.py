#coding=utf-8
__author__ = 'linglin'
"""

109. Convert Sorted List to Binary Search Tree

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

Subscribe to see which companies asked this question

Hide Tags Depth-first Search Linked List
Hide Similar Problems (M) Convert Sorted Array to Binary Search Tree

Medium

"""


import unittest
from util.tree_node import TreeNode
from util.list_node import ListNode

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head): #276ms, 47%
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        else:
            return self.to_bst(head, None)

    def to_bst(self, head, tail):
        if head is None or head==tail: # should move head==tail here, because tail is not included, otherwise wrong.
            return None
        elif head.next == tail:
            return TreeNode(head.val)
        fast = slow = head
        while fast != tail and fast.next!=tail:
            fast = fast.next.next
            slow = slow.next
        root = TreeNode(slow.val)
        root.left = self.to_bst(head, slow)
        root.right = self.to_bst(slow.next, tail)
        return root





    def sortedListToBST1(self, head): #272ms, 53%
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        arr = self.list_to_array(head)
        return self.arr_to_tree(arr, 0, len(arr)-1)

    def list_to_array(self, head):
        if not head:
            return []
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    def arr_to_tree(self, arr, left, right):
        if not arr:
            return None
        if left==right:
            return TreeNode(arr[left])
        if left>right:
            return None
        mid = (left+right)/2
        root = TreeNode(arr[mid])
        root.left = self.arr_to_tree(arr,left,mid-1)
        root.right = self.arr_to_tree(arr,mid+1,right)
        return root





class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,2,3,4,5]
        #answer = [3,1,4,None,2, None,5] # -- array way
        answer = [3,2,5,1, None,4] # -- list way
        result = self.sol.sortedListToBST(ListNode.parseArray2List(nums))
        self.assertEqual(True, TreeNode.compare_tree(result,TreeNode.generate_bt_from_list(answer)))


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
