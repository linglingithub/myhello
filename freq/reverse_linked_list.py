"""

206. Reverse Linked List

Reverse a singly linked list.

click to show more hints.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?

Subscribe to see which companies asked this question

Hide Tags Linked List
Hide Similar Problems (M) Reverse Linked List II (M) Binary Tree Upside Down (E) Palindrome Linked List

Easy

"""

import unittest

from util.list_node import ListNode


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        return self.reverse(None, head)

    def reverse(self, left, head):
        if not head:
            return left
        mid = head
        right = mid.next
        mid.next = left
        return self.reverse(mid, right)

    def reverseList_iter(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        left, mid = head, head.next
        left.next = None  # important for the first node, otherwise wrong for TLE
        right = None
        while mid:
            right = mid.next
            mid.next = left
            left = mid
            mid = right
        return left

class Solution2:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list. 
                  Reverse it in-place.
    """

    def reverse(self, head):  # recursive way
        # write your code here
        if not head:
            return None
        if not head.next:
            return head
        return self.reverse_helper(head, None)

    def reverse_helper(self, head, tail):
        if not head:
            return tail
        fast = head.next
        head.next = tail
        return self.reverse_helper(fast, head)

    def reverse1(self, head): # iterative way
        # write your code here
        if not head:
            return None
        if not head.next:
            return head
        slow = head
        mid = slow.next
        fast = mid.next
        while mid:
            fast = mid.next
            mid.next = slow
            slow = mid
            mid = fast
        #remember to deal with ending point, otherwise infinite loop??
        head.next = None
        return slow

class Solution1(object):
    def reverseList_recursive_slower(self, head): # recursive way , 108ms, 1.36% -- 59ms, 40%, iter is still better
        """
        remember to do it in on pass!!!
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        dummy = ListNode(-1)
        self.reverse_list_recur(head, dummy)
        return dummy.next

    def reverse_list_recur(self, head, newhead):
        if head:
            tmp = newhead.next
            newhead.next = head
            next_head = head.next
            head.next = tmp
            self.reverse_list_recur(next_head, newhead)
        else:
            return newhead

    def reverseList_ref_recur(self, head): #78ms, 12%, 62ms, 32%
        return self.doReverse(head, None)

    def doReverse(self, head, newHead): # very smart way to do recursive
        if head is None:
            return newHead
        next = head.next
        head.next = newHead
        return self.doReverse(next, head)





    def reverseList_itera(self, head): # iterative way , 49ms, 67%
        """
        remember to do it in on pass!!!
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        dummy = ListNode(0)

        while head:
            tmp = head
            head = head.next
            tmp.next = dummy.next
            dummy.next = tmp
        return dummy.next



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,2,3,4,5]
        answer = [5,4,3,2,1]
        result = self.sol.reverseList(ListNode.parseArray2List(nums))
        prin( ListNode.parseList2Array(result))
        self.assertEqual(answer, ListNode.parseList2Array(result))


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8