"""
25. Reverse Nodes in k-Group

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Subscribe to see which companies asked this question

Hide Tags Linked List
Hide Similar Problems (E) Swap Nodes in Pairs

Hard

"""

import unittest

from util.list_node import ListNode

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        # Write your code here
        if not head or k < 2:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        start = head
        preHead = dummy
        while True:
            head, tail, postTail = self.get_k_nodes(start, k)
            if not tail:
                break
            head, tail = self.reverse_node_list(head, tail)
            preHead.next = head
            tail.next = postTail
            start = postTail
            preHead = tail
        return dummy.next

    def get_k_nodes(self, start, k):
        head, tail, postTail = start, start, None
        if not head:
            return head, tail, postTail
        cnt = 1
        while cnt < k:
            tail = tail.next
            if not tail:
                break
            cnt += 1
        if not tail:
            return head, None, None
        return head, tail, tail.next

    def reverse_node_list(self, head, tail):
        _newTail = [head]
        left, right = head, head.next
        while right != tail:
            tmp = right.next
            right.next = left
            left = right
            right = tmp
        right.next = left
        return tail, _newTail[0]

class Solution1(object):
    def reverseKGroup(self, head, k): # 85ms, 37%, pay attention to link details, trial and error process
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        if k==1:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        p = dummy
        done_tail = dummy
        cnt = 0
        while True:
            while cnt < k:
                p = p.next
                if p:
                    cnt+=1
                else:
                    break
            if cnt < k or not p:
                return dummy.next
            next_head = p.next
            new_done = done_tail.next
            done_tail.next = self.reverse_link(done_tail.next,next_head)
            done_tail = new_done
            p = next_head
            if not p:
                return dummy.next
            cnt = 1
        return dummy.next


    def reverse_link(self, head, tail):
        dummy = ListNode(-1)
        dummy.next = head
        p = head.next
        while p!=tail:
            new_next = p.next
            head.next = new_next
            p.next = dummy.next
            dummy.next = p
            p = new_next
        return dummy.next


    def reverseKGroup_ref(self, head, k): #89ms, 28%
        if head is None or k < 2:
            return head
        ret = head
        for i in range(k - 1):
            ret = ret.next
            if ret is None:
                return head
        prev, current = None, head
        for i in range(k):
            _next = current.next
            current.next = prev
            prev = current
            current = _next
        head.next = self.reverseKGroup(current, k)
        return ret




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case6(self): # ====>
        nums = [1,2,3,4]
        k = 2
        answer = [2,1,4,3]
        result = self.sol.reverseKGroup(ListNode.parseArray2List(nums), k)
        self.assertEqual(answer, ListNode.parseList2Array(result))

    def test_case5(self): # ====>
        nums = [1,2,3]
        k = 3
        answer = [3,2,1]
        result = self.sol.reverseKGroup(ListNode.parseArray2List(nums), k)
        self.assertEqual(answer, ListNode.parseList2Array(result))

    def test_case1(self):
        nums = [1]
        k = 1
        answer = [1]
        result = self.sol.reverseKGroup(ListNode.parseArray2List(nums), k)
        self.assertEqual(answer, ListNode.parseList2Array(result))

    def test_case2(self):
        nums = [1,2]
        k = 2
        answer = [2,1]
        result = self.sol.reverseKGroup(ListNode.parseArray2List(nums), k)
        self.assertEqual(answer, ListNode.parseList2Array(result))

    def test_case3(self):
        nums = [1,2]
        k = 3
        answer = [1,2]
        result = self.sol.reverseKGroup(ListNode.parseArray2List(nums), k)
        self.assertEqual(answer, ListNode.parseList2Array(result))

    def test_case4(self):
        nums = [1,2]
        k = 1
        answer = [1,2]
        result = self.sol.reverseKGroup(ListNode.parseArray2List(nums), k)
        self.assertEqual(answer, ListNode.parseList2Array(result))


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8