"""
141. Linked List Cycle

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

Subscribe to see which companies asked this question

Hide Tags Linked List Two Pointers
Hide Similar Problems (M) Linked List Cycle II

Easy

"""

import unittest


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head): #89ms, 45%
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        fast = head
        slow = head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if slow==fast:
                return True
        return False





class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1_not(self):
        nums = 1
        answer = 1
        result = self.sol.hasCycle(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8
