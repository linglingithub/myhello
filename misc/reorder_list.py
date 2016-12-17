#coding=utf-8

"""

143. Reorder List

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.

Subscribe to see which companies asked this question

Hide Tags Linked List

Medium

"""

import unittest
from util.list_node import ListNode

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head): #228ms, 14%, 212ms, 23%, 179ms, 63%
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        # find half list
        fast = head
        slow = head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        # reverse right half
        dummy = slow
        tail = dummy.next
        while tail and tail.next:  # should add checking for tail here, otherwise wrong for case2, same for next while
            tmp = tail.next
            new_tail = tmp.next
            tail.next = new_tail
            tmp.next = dummy.next
            dummy.next = tmp
        # merge left half and right half
        left = head
        right = dummy.next
        while left != dummy: #should use left as the judge, otherwise wrong for case3. right has more complicated
            # situation ( when more than one node, last node no need to do, when only one node, still need to operate
            next_left = left.next
            next_right = right.next
            left.next = right
            right.next = next_left
            left = next_left
            right = next_right
            dummy.next = next_right  # important, otherwise wrong link

        # while right and right.next:  # last node no need to operate, otherwise wrong, so not right, should be right.next
        #     next_left = left.next
        #     next_right = right.next
        #     left.next = right
        #     right.next = next_left
        #     left = next_left
        #     right = next_right
        #     dummy.next = next_right  # important, otherwise wrong link


    def reorderList_ref(self, head): #202ms, 31%
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None or head.next.next == None: return

        # break linked list into two equal length
        slow = fast = head  # 快慢指针技巧
        while fast and fast.next:  # 需要熟练掌握
            slow = slow.next  # 链表操作中常用
            fast = fast.next.next
        head1 = head
        head2 = slow.next
        slow.next = None

        # reverse linked list head2
        dummy = ListNode(0);
        dummy.next = head2  # 翻转前加一个头结点
        p = head2.next;
        head2.next = None  # 将p指向的节点一个一个插入到dummy后面
        while p:  # 就完成了链表的翻转
            tmp = p;
            p = p.next  # 运行时注意去掉中文注释
            tmp.next = dummy.next
            dummy.next = tmp
        head2 = dummy.next

        # merge two linked list head1 and head2
        p1 = head1;
        p2 = head2
        while p2:
            tmp1 = p1.next;
            tmp2 = p2.next
            p1.next = p2;
            p2.next = tmp1
            p1 = tmp1;
            p2 = tmp2

    def reorderList_ref2(self, head): #179, 62%
        # write your code here
        if None == head or None == head.next:
            return

        pfast = head
        pslow = head

        while pfast.next and pfast.next.next:
            pfast = pfast.next.next
            pslow = pslow.next
        pfast = pslow.next
        pslow.next = None

        pnext = pfast.next
        pfast.next = None
        while pnext:
            q = pnext.next
            pnext.next = pfast
            pfast = pnext
            pnext = q

        tail = head
        while pfast:
            pnext = pfast.next
            pfast.next = tail.next
            tail.next = pfast
            tail = tail.next.next
            pfast = pnext
        return


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case3(self): #====>
        nums = [1,2,3]
        answer = [1,3,2]
        root = ListNode.parseArray2List(nums)
        self.sol.reorderList(root)
        self.assertEqual(answer, ListNode.parseList2Array(root))

    def test_case2(self): #====>
        nums = [1]
        answer = [1]
        root = ListNode.parseArray2List(nums)
        self.sol.reorderList(root)
        self.assertEqual(answer, ListNode.parseList2Array(root))

    def test_case1(self):
        nums = [1,2,3,4]
        answer = [1,4,2,3]
        root = ListNode.parseArray2List(nums)
        self.sol.reorderList(root)
        self.assertEqual(answer, ListNode.parseList2Array(root))


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8