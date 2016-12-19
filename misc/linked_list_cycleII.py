"""
142. Linked List Cycle II

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?

Subscribe to see which companies asked this question

Hide Tags Linked List Two Pointers
Hide Similar Problems (E) Linked List Cycle (H) Find the Duplicate Number

Medium

"""

import unittest


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head): #92ms, 42%
        """
        More like a math problem. k = n(a+b) - a, where k is the distance from head to where loop starts,
        a is where fast and slow pointers meet on the loop (from start of loop), b is the rest length of the
        loop. n is the integer of how many laps fast pointer goes before two pointers meet.
        Therefore, after pointers meet, let a pointer start from head again, the other pointer start from
         a, when they meet again, is where the round will start.
        :type head: ListNode
        :rtype: ListNode
        """

        fast = head
        slow = head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if not fast or not fast.next or not fast.next.next: # should check all the fast, fast.next, fast.next.next
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast






class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1_not(self):
        nums = 1
        answer = 1
        result = self.sol.detectCycle(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8
