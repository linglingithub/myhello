#coding=utf-8
"""
92. Reverse Linked List II

Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.

Subscribe to see which companies asked this question

Hide Tags Linked List
Hide Similar Problems (E) Reverse Linked List

Medium

"""


import unittest
from list_node import ListNode


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween1(self, head, m, n): #45ms, 49%
        """
        Pay a lot of attention to the links!!! and how to reserve and connect them.
        Easy to think about it, lots of details that may go wrong when implementation.
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return None
        if m==n:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        p = dummy
        cnt = 0
        while cnt<m-1 and p:
            cnt+=1
            p=p.next
        reverse_head = p
        p=p.next
        cnt+=1
        revers_tail = p
        p = p.next
        cnt += 1

        while m <=cnt<=n and p:
            next = p.next
            p.next = reverse_head.next
            reverse_head.next = p
            p = next
            cnt += 1
            if cnt > n:
                revers_tail.next = next

        return dummy.next


    def reverseBetween_ref(self, head, m, n):
        if head == None or head.next == None:
            return head
        dummy = ListNode(0); dummy.next = head
        head1 = dummy
        for i in range(m - 1):
            head1 = head1.next
        p = head1.next
        for i in range(n - m):
            tmp = head1.next
            head1.next = p.next
            p.next = p.next.next
            head1.next.next = tmp
        return dummy.next









class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,2,3,4,5]
        m =2
        n = 4
        answer = [1,4,3,2,5]
        result = self.sol.reverseBetween(ListNode.parseArray2List(nums),m, n)
        self.assertEqual(answer, ListNode.parseList2Array(result))


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8