"""
Remove Nth Node From End of List

Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.

Subscribe to see which companies asked this question

 Linked List Two Pointers

"""

import unittest
from list_node import ListNode

class Solution(object):

    # http://www.cnblogs.com/zuoyuan/p/3701971.html
    def removeNthFromEnd(self, head, n): # slower 72ms
        dummy=ListNode(0); dummy.next=head
        p1=p2=dummy
        for i in range(n): p1=p1.next
        while p1.next:
            p1=p1.next; p2=p2.next
        p2.next=p2.next.next
        return dummy.next

    def removeNthFromEnd1(self, head, n): # 65ms
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n==0:
            return head

        slow = head
        fast = head
        for i in range(n):
            fast = fast.next
        if fast is None:
            slow = slow.next
            head = slow
            return head
        while fast.next:
            fast = fast.next
            slow = slow.next
        if slow.next:
            new_tail = slow.next.next
            slow.next = new_tail
        return head





class SolutionTestor(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        head = None
        n = 0
        answer = None
        result = self.sol.removeNthFromEnd(head, n)
        self.assertEqual(answer, result)

    def test_case2(self):
        head = ListNode(0)
        head.next = None
        n = 1
        answer = None
        result = self.sol.removeNthFromEnd(head, n)
        self.assertEqual(answer, result)

    def test_case3(self):
        head = ListNode(0)
        n1 = ListNode(1)
        head.next = n1
        n = 2
        answer = n1
        result = self.sol.removeNthFromEnd(head, n)
        self.assertEqual(answer, result)

    def test_case4(self):
        head = ListNode(0)
        n1 = ListNode(1)
        head.next = n1
        n = 1
        answer = head
        result = self.sol.removeNthFromEnd(head, n)
        self.assertEqual(None, result.next)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTestor)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()