"""
Add Two Numbers

You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

Subscribe to see which companies asked this question

Hide Tags Linked List Math
Hide Similar Problems (M) Multiply Strings (E) Add Binary (E) Sum of Two Integers (E) Add Strings (M) Add Two Numbers II


"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        dummy = ListNode(0)
        t = dummy
        d1 = 0
        d2 = 0

        while l1 is not None and l2 is not None:
            d1 = (l1.val + l2.val + d2) % 10
            tmp = ListNode(d1)
            t.next = tmp
            t = t.next
            d2 = (l1.val+l2.val + d2) / 10
            l1 = l1.next
            l2 = l2.next
        while l1 is not None:
            d1 = (l1.val + d2) % 10
            d2 = (l1.val + d2) / 10
            tmp = ListNode(d1)
            t.next = tmp
            t = t.next
            l1 = l1.next
        while l2 is not None:
            d1 = (l2.val + d2) % 10
            d2 = (l2.val + d2) / 10
            tmp = ListNode(d1)
            t.next = tmp
            t = t.next
            l2 = l2.next
        if d2 != 0:
            tmp = ListNode(d2)
            d2 = 0
            t.next = tmp
            t = t.next
        return dummy.next




class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None