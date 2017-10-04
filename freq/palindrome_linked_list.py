#coding=utf-8

import unittest

"""

234. Palindrome Linked List
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?


Difficulty:Easy
Total Accepted:122.3K
Total Submissions:371K
Contributor: LeetCode
Subscribe to see which companies asked this question.

Related Topics 
Linked List Two Pointers 
Similar Questions 
Palindrome Number Valid Palindrome Reverse Linked List 

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from util.list_node import ListNode

class Solution(object):
    def isPalindrome(self, head): # 27.3%
        """

        :type head: ListNode
        :rtype: bool
        """
        # None check
        if not head or not head.next:
            return True

        # find mid and check if even / odd
        fast, slow = head, head
        odd = True
        while slow.next and fast.next:
            if slow.next.next:
                # odd nodes, fast is the middle node, no check
                fast = fast.next
                slow = slow.next.next
            else:
                # even case, fast is the end node of first half, need to check
                odd = False
                break
        half_head = fast.next

        # reverse first half --> better to reverse last half, no need to worry about middle node
        head2 = self.reverse_list(half_head)

        # check if palindrome or not
        return self.check_palindrome(head, head2)

    def reverse_list(self, head):
        if not head:
            return
        dummy = ListNode(-1)
        dummy.next = head
        fast, slow = head.next, head
        while fast:
            tmp = fast.next
            fast.next = slow
            slow = fast
            fast = tmp
        dummy.next.next = None
        return slow


    def reverse_list_wrong(self, head):
        dummy = ListNode(-1)
        dummy.next = head
        fast = head.next
        mid = head
        slow = None
        while fast:
            mid.next = slow
            mid = fast
            slow = mid
            fast = fast.next
        # set new tail to None, when only one head node, won't go into fast loop
        dummy.next.next = None
        return mid

    def check_palindrome(self, head1, head2):
        while head2:
            if head2.val != head1.val:
                return False
            head2 = head2.next
            head1 = head1.next
        return True  # !!! don't forget

class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [0,0]
        head = ListNode.parseArray2List(nums)
        answer = True
        result = self.sol.isPalindrome(head)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [1,1,2,1]
        head = ListNode.parseArray2List(nums)
        answer = False
        result = self.sol.isPalindrome(head)
        self.assertEqual(answer, result)



def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""
http://www.cnblogs.com/grandyang/p/4635425.html

这道题让我们判断一个链表是否为回文链表，LeetCode中关于回文串的题共有六道，除了这道，其他的五道为 Palindrome Number 验证回文数字， 
Validate Palindrome 验证回文字符串， Palindrome Partitioning 拆分回文串，Palindrome Partitioning II 拆分回文串之二 和 
Longest Palindromic Substring 最长回文串.链表比字符串难的地方就在于不能通过坐标来直接访问，而只能从头开始遍历到某个位置。那么根据回文
串的特点，我们需要比较对应位置的值是否相等，那么我们首先需要找到链表的中点，这个可以用快慢指针来实现，使用方法可以参见之前的两篇
Convert Sorted List to Binary Search Tree 将有序链表转为二叉搜索树 和 Reorder List 链表重排序，我们使用快慢指针找中点的原理是fast
和slow两个指针，每次快指针走两步，慢指针走一步，等快指针走完时，慢指针的位置就是中点。我们还需要用栈，每次慢指针走一步，都把值存入栈中，
等到达中点时，链表的前半段都存入栈中了，由于栈的后进先出的性质，就可以和后半段链表按照回文对应的顺序比较了。代码如下：


这道题的Follow Up让我们用O(1)的空间，那就是说我们不能使用stack了，那么如果代替stack的作用呢，用stack的目的是为了利用其后进先出的特点，
好倒着取出前半段的元素。那么现在我们不用stack了，如何倒着取元素呢。我们可以在找到中点后，将后半段的链表翻转一下，这样我们就可以按照回文的顺
序比较了，参见代码如下：


"""

#-*- coding:utf-8 -*-
