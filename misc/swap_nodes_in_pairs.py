"""
24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

Subscribe to see which companies asked this question

Hide Tags Linked List
Hide Similar Problems (H) Reverse Nodes in k-Group

Difficulty: Easy

"""


import unittest
from list_node import ListNode


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head): #45ms, 83%
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        zero = dummy
        one = head
        two = head.next
        while one and two:
            three = two.next
            # one.val, two.val = two.val, one.val   # 32ms, 98%, if use the swap value way
            # zero = two
            # one = three
            # two = one.next if one else None
            zero.next = two
            one.next = three
            two.next = one
            zero = one
            one = one.next
            two = one.next if one else None

        return dummy.next





class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        input = [1,2,3,4]
        answer = [2,1,4,3]
        result = self.sol.swapPairs(ListNode.parseArray2List(input))
        self.assertEqual(answer, ListNode.parseList2Array(result))

    def test_case2(self):
        input = [1, 2, 3]
        answer = [2, 1, 3]
        result = self.sol.swapPairs(ListNode.parseArray2List(input))
        self.assertEqual(answer, ListNode.parseList2Array(result))


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8