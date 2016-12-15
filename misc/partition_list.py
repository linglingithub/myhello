"""

86. Partition List

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.

Subscribe to see which companies asked this question

Hide Tags Linked List Two Pointers

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

    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:   #39ms, 91%
            return None
        left, right = ListNode(-1), ListNode(-1)
        ltail = left
        rtail = right
        tmp = head
        while tmp:
            if tmp.val<x:
                ltail.next = tmp
                ltail = ltail.next
            else:
                rtail.next = tmp
                rtail = rtail.next
            tmp = tmp.next
        ltail.next = right.next
        rtail.next = None
        return left.next


    def partition1(self, head, x): #55ms, 45%
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        left = ListNode(-1)
        ltail = left
        right = ListNode(-1)
        rtail = right
        tmp = head
        while tmp:
            if tmp.val<x:
                ltail.next = tmp
                ltail = ltail.next
            else:
                rtail.next = tmp
                rtail = rtail.next
            tmp = tmp.next
        if left.next:  # need to check if left part is None, otherwise wrong for case2
            dummy.next = left.next
            ltail.next = right.next
        else:
            dummy.next = right.next
        rtail.next = None
        return dummy.next


    def partition_ref(self, head, x): #45ms, 71%
        head1 = ListNode(0)
        head2 = ListNode(0)
        Tmp = head
        phead1 = head1
        phead2 = head2
        while Tmp:
            if Tmp.val < x:
                phead1.next = Tmp
                Tmp = Tmp.next
                phead1 = phead1.next
                phead1.next = None
            else:
                phead2.next = Tmp
                Tmp = Tmp.next
                phead2 = phead2.next
                phead2.next = None
        phead1.next = head2.next
        head = head1.next
        return head

    def partition_ref2(self, head, x): #39ms, 90%
        # write your code here
        if head is None:
            return head
        aHead, bHead = ListNode(0), ListNode(0)
        aTail, bTail = aHead, bHead
        while head is not None:
            if head.val < x:
                aTail.next = head
                aTail = aTail.next
            else:
                bTail.next = head
                bTail = bTail.next
            head = head.next
        bTail.next = None
        aTail.next = bHead.next
        return aHead.next


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case2(self): #====>
        nums = [1]
        x = 0
        answer = [1]
        result = self.sol.partition(ListNode.parseArray2List(nums), x)
        self.assertEqual(answer, ListNode.parseList2Array(result))

    def test_case1(self):
        nums = [1, 4, 3, 2, 5, 2]
        x = 3
        answer = [1, 2, 2, 4, 3, 5]
        result = self.sol.partition(ListNode.parseArray2List(nums), x)
        self.assertEqual(answer, ListNode.parseList2Array(result))


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8