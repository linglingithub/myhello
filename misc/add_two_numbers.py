"""
2. Add Two Numbers

You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

Subscribe to see which companies asked this question

Hide Tags Linked List Math
Hide Similar Problems (M) Multiply Strings (E) Add Binary (E) Sum of Two Integers (E) Add Strings (M) Add Two Numbers II

Difficulty: Medium

"""


import unittest
from list_node import ListNode


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2): #119ms, 95%
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
        head = dummy
        carry = 0
        while l1 and l2:
            tmp = l1.val + l2.val + carry
            carry = tmp / 10
            digit = tmp % 10
            head.next = ListNode(digit)
            head = head.next
            l1 = l1.next
            l2 = l2.next
        if l2:
            l1 = l2
        if l1:
            while l1:
                tmp = l1.val + carry
                carry = tmp / 10
                digit = tmp % 10
                head.next = ListNode(digit)
                head = head.next
                l1 = l1.next
        if carry: # don't forget this one, otherwise wrong for case3
            head.next = ListNode(1)

        return dummy.next


    def addTwoNumbers_ref(self, l1, l2): # code simpler, but runs slower, around 75%-50%
        head = ListNode(0)
        l = head
        carry = 0
        while l1 or l2 or carry:
            sum, carry = carry, 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            if sum > 9:
                carry = 1
                sum -= 10
            l.next = ListNode(sum)
            l = l.next
        return head.next


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        l1 = [2,4,3]
        l2 = [5,6,4]
        answer = [7,0,8]
        result = self.sol.addTwoNumbers(ListNode.parseArray2List(l1),ListNode.parseArray2List(l2))
        self.assertEqual(answer, ListNode.parseList2Array(result))


    def test_case2(self):
        l1 = [2]
        l2 = [8, 6, 4]
        answer = [0, 7, 4]
        result = self.sol.addTwoNumbers(ListNode.parseArray2List(l1), ListNode.parseArray2List(l2))
        self.assertEqual(answer, ListNode.parseList2Array(result))


    def test_case3(self): # ====>
        l1 = [5]
        l2 = [5]
        answer = [0, 1]
        result = self.sol.addTwoNumbers(ListNode.parseArray2List(l1), ListNode.parseArray2List(l2))
        self.assertEqual(answer, ListNode.parseList2Array(result))

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8


################################################

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution_old(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         if l1 is None:
#             return l2
#         if l2 is None:
#             return l1
#
#         dummy = ListNode(0)
#         t = dummy
#         d1 = 0
#         d2 = 0
#
#         while l1 is not None and l2 is not None:
#             d1 = (l1.val + l2.val + d2) % 10
#             tmp = ListNode(d1)
#             t.next = tmp
#             t = t.next
#             d2 = (l1.val+l2.val + d2) / 10
#             l1 = l1.next
#             l2 = l2.next
#         while l1 is not None:
#             d1 = (l1.val + d2) % 10
#             d2 = (l1.val + d2) / 10
#             tmp = ListNode(d1)
#             t.next = tmp
#             t = t.next
#             l1 = l1.next
#         while l2 is not None:
#             d1 = (l2.val + d2) % 10
#             d2 = (l2.val + d2) / 10
#             tmp = ListNode(d1)
#             t.next = tmp
#             t = t.next
#             l2 = l2.next
#         if d2 != 0:
#             tmp = ListNode(d2)
#             d2 = 0
#             t.next = tmp
#             t = t.next
#         return dummy.next
#
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None