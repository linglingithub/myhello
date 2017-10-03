#coding=utf-8

import unittest

"""
237. Delete Node in a Linked List
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list should 
become 1 -> 2 -> 4 after calling your function.

Difficulty:Easy
Total Accepted:170.1K
Total Submissions:363.7K
Contributor: LeetCode
Subscribe to see which companies asked this question.

Related Topics 
Linked List 
Similar Questions 
Remove Linked List Elements 

"""



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        #dummy = ListNode(-1)
        #dummy.next = node
        if not node.next:
            #del node
            node = None  # won't work actually, but looks like no test case for this on leetcode
        tail = node.next
        pre = node
        while tail:
            node.val = tail.val
            pre = node
            node = tail
            tail = tail.next
        # del node
        #node = None
        pre.next = None

    def deleteNode_ref(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

from util.list_node import ListNode
class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [0,1]
        nodes = ListNode.parseArray2List(nums)
        #node at index 0 (node.val = 0)
        answer = [1]
        result = self.sol.deleteNode(nodes)
        self.assertEqual(answer, ListNode.parseList2Array(nodes))


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
