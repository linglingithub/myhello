"""

82. Remove Duplicates from Sorted List II

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.

Subscribe to see which companies asked this question

Hide Tags Linked List

Medium

"""

import unittest

from util.list_node import ListNode


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head): #58ms, 65%
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        good = dummy
        first = head
        faster = head.next
        while first:
            if faster is None or first.val != faster.val:
                good.next = first
                good = good.next
                first = faster
                if faster:
                    faster = faster.next
            else:
                while faster and faster.val == first.val:
                    faster = faster.next
                first = faster
                faster = first.next if first else None
        good.next = None # need to add ending to good, otherwise wrong for case 2
        return dummy.next


    def deleteDuplicates_ref(self, head): #69ms, 35%
        if head == None or head.next == None:
            return head
        dummy = ListNode(0); dummy.next = head
        p = dummy
        tmp = dummy.next
        while p.next:
            while tmp.next and tmp.next.val == p.next.val:
                tmp = tmp.next
            if tmp == p.next:
                p = p.next
                tmp = p.next
            else:
                p.next = tmp.next
        return dummy.next


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,1,2]
        answer = [2]
        result = self.sol.deleteDuplicates(ListNode.parseArray2List(nums))
        self.assertEqual(answer, ListNode.parseList2Array(result))

    def test_case2(self):
        nums = [1,1,2,3,3]
        answer = [2]
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