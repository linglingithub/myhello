#coding=utf-8

"""
160. Intersection of Two Linked Lists

Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
Credits:
Special thanks to @stellari for adding this problem and creating all test cases.

Subscribe to see which companies asked this question

Hide Tags Linked List

Easy

"""

import unittest


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB): #468ms, 85%
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a = headA
        alen = 0
        while a:
            a = a.next
            alen += 1
        b = headB
        blen = 0
        while b:
            b = b.next
            blen += 1
        a = headA
        b = headB
        if alen>blen:
            for i in range(alen-blen):
                a = a.next
        elif blen>alen:
            for i in range(blen-alen):
                b = b.next
        while a != b:
            a = a.next
            b = b.next
        return a

    def getIntersectionNode_ref(self, headA, headB): #385ms, 99%, good and fast
        """
        If two linked lists have intersection, we can find two observations:

        They must have same nodes after the intersection point.
        L1+L2 must have same tail from the intersection point as L2 + L1. For example,
        L1 = 1,2,3
        L2 = 6,5,2,3

        L1+L2 = 1,2,3,6,5,2,3
        L2+L1 = 6,5,2,3,1,2,3

        To implement L1+L2 as well as L2+L1, we can simply jump to another list's head
        after traveling through certain list.
        But, you need to notice that if the two lists have no intersection at all,
        you should stop after you've already checked L1+L2, so we need a flag jumpToNext to ensure we only traverse
        L1 + L2 once.
        :param headA:
        :param headB:
        :return:
        """
        ptA, ptB, jumpToNext = headA, headB, False
        while ptA and ptB:
            if ptA == ptB:
                return ptA
            ptA, ptB = ptA.next, ptB.next
            if not ptA and not jumpToNext:  # it does not matter where to change jumpToNext( at ptA or ptB ,
                # first or later), everyone will change once, and onlt need to be chnaged once.
                ptA, jumpToNext = headB, True
            if not ptB:
                ptB = headA
        return None

    def getIntersectionNode_notaccepted_solution2_toomanycornercase(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB: #don't forget to check this, otherwise wrong at next line for None input
            return None
        a, b = headA, headB

        while a.next and b.next:
            if a == b:
                return a
            a = a.next
            b = b.next
        if a.next:
            b.next = headA
            tmp = b
        else:
            a.next = headB
            tmp = a
        # while a!=b : # don't forget to check for cases that no intersection and link will end.
        #     a = a.next
        #     b = b.next
        # tmp.next = None
        # return a
        while a.next and b.next:
            if a==b:
                tmp.next = None
                return a
            a = a.next
            b = b.next

        tmp.next = None
        return None




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1_not(self):
        numsa = [1,2,3]
        numsb = [1,2,3]
        answer = [1]
        result = self.sol.getIntersectionNode(numsa, numsb)
        self.assertEqual(answer, result)

    def test_case2_not(self):
        numsa = []
        numsb = [1,2,3]
        answer = []
        result = self.sol.getIntersectionNode(numsa, numsb)
        self.assertEqual(answer, result)

    def test_case3_not(self):
        numsa = [2,3]
        numsb = [3]
        answer = [3]
        result = self.sol.getIntersectionNode(numsa, numsb)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""
SOLUTION 1:

1. 得到2个链条的长度。

2. 将长的链条向前移动差值（len1 - len2）

3. 两个指针一起前进，遇到相同的即是交点，如果没找到，返回null.

相当直观的解法。空间复杂度O(1)， 时间复杂度O(m+n)


SOLUTION 2: ===> not really good, but just another way to think about it.

解完后，打开Leetcode的solution, 找到一个很巧妙的解法。其实与解法1相比应该快不了多少，但是写出来超有B格的。。

Two pointer solution (O(n+m) running time, O(1) memory):
Maintain two pointers pA and pB initialized at the head of A and B, respectively. Then let them both traverse through
the lists, one node at a time.
When pA reaches the end of a list, then redirect it to the head of B (yes, B, that's right.); similarly when pB reaches
 the end of a list, redirect it the head of A.
If at any point pA meets pB, then pA/pB is the intersection node.
To see why the above trick would work, consider the following two lists: A = {1,3,5,7,9,11} and B = {2,4,9,11}, which
are intersected at node '9'. Since B.length (=4) < A.length (=6), pB would reach the end of the merged list first,
because pB traverses exactly 2 nodes less than pA does. By redirecting pB to head A, and pA to head B, we now ask pB to
travel exactly 2 more nodes than pA would. So in the second iteration, they are guaranteed to reach the intersection
node at the same time.
If two lists have intersection, then their last nodes must be the same one. So when pA/pB reaches the end of a list,
record the last element of A/B respectively. If the two last elements are not the same one, then the two lists have no
intersections.

"""

#-*- coding:utf-8 -*-
#coding=utf-8