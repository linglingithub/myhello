"""

83. Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

Subscribe to see which companies asked this question

Hide Tags Linked List

Easy

"""

import unittest

from util.list_node import ListNode


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head): #58ms, 68%
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        good = head
        faster = head.next
        while faster:
            if faster.val != good.val:
                good.next = faster
                good = good.next
            faster = faster.next
        good.next = None
        return head

    def deleteDuplicates_ref(self, head): #52ms, 81%, or 90+%
        if head == None or head.next == None:
            return head
        p = head
        while p.next:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,1,2]
        answer = [1,2]
        result = self.sol.deleteDuplicates(ListNode.parseArray2List(nums))
        self.assertEqual(answer, ListNode.parseList2Array(result))

    def test_case2(self):
        nums = [1,1,2,3,3]
        answer = [1,2,3]
        result = self.sol.deleteDuplicates(ListNode.parseArray2List(nums))
        self.assertEqual(answer, ListNode.parseList2Array(result))

    def test_case3(self):
        nums = [1]
        answer = [1]
        result = self.sol.deleteDuplicates(ListNode.parseArray2List(nums))
        self.assertEqual(answer, ListNode.parseList2Array(result))



def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8