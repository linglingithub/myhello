"""

61. Rotate List

Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.

Subscribe to see which companies asked this question

Hide Tags Linked List Two Pointers
Hide Similar Problems (E) Rotate Array



"""

import unittest

from util.list_node import ListNode


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k): #45ms, 95%
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or k==0:
            return head
        dummy = ListNode(0)
        dummy.next = head
        fast = head
        full_length = 1
        tag = False
        i = 0
        #for i in range(k):  # can not use range when k is really big, memory error for case2
        while i < k:
            if fast.next:
                fast = fast.next
                full_length += 1
                i += 1
            else:
                # this is for if k is bigger than the link length
                tag = True
                break
        if tag:
            k = k % full_length
            fast = head
            for i in range(k):
                fast = fast.next
        slow = head
        while fast.next:
            fast = fast.next
            slow = slow.next
        fast.next = head
        dummy.next = slow.next
        slow.next = None
        return dummy.next







class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,2,3,4,5]
        k = 2
        answer = [4,5,1,2,3]
        result = self.sol.rotateRight(ListNode.parseArray2List(nums), k)
        self.assertEqual(answer, ListNode.parseList2Array(result))

    def test_case2(self): # ========>
        nums = [1, 2, 3]
        k = 2000000000
        answer = [2, 3, 1]
        result = self.sol.rotateRight(ListNode.parseArray2List(nums), k)
        self.assertEqual(answer, ListNode.parseList2Array(result))


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8