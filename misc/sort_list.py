"""
Sort List

Sort a linked list in O(n log n) time using constant space complexity.

Subscribe to see which companies asked this question

Hide Tags Linked List Sort
Hide Similar Problems (E) Merge Two Sorted Lists (M) Sort Colors (M) Insertion Sort List
Have you met this question in a real interview? Yes

"""

import unittest

from util.list_node import ListNode


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # http://fisherlei.blogspot.com/2013/12/leetcode-sort-list-solution.html
    # O(nlgn) sorting algos: quick, heap, merge
    # http: // www.cnblogs.com / zuoyuan / p / 3699508.

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        h1, h2 = self.split_list(head)
        #while h1: can't write this here, otherwise dead loop, recursive will be handled by recursively call sortList, not by loop here!!!
        if h1:
            h1 = self.sortList(h1)
        #while h2:
        if h2:
            h2 = self.sortList(h2)
        head = self.merge_list(h1, h2)
        return head

    def split_list(self, head):
        if head is None:
            return None, None
        fast = head.next
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        head2 = slow.next
        slow.next = None
        return head, head2
        #return fast, slow  #wrong way to write this


    def merge_list(self, h1, h2):
        if h1 is None:
            return h2
        if h2 is None:
            return h1
        dummy = ListNode(0)
        tmp = dummy
        while h1 and h2:
            if h1.val <= h2.val:
                tmp.next = h1
                h1 = h1.next
            else:
                tmp.next = h2
                h2 = h2.next
            tmp = tmp.next
        if h1:
            tmp.next = h1
        else:
            tmp.next = h2
        return dummy.next





class SolutionTestor(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1, 0, -1]
        head = ListNode.parseArray2List(nums)
        answer = [-1, 0, 1]
        result = self.sol.sortList(head)
        self.assertEqual(answer, ListNode.parseList2Array(result))

    def test_case2(self):
        nums = [1, 0, -1, -2]
        head = ListNode.parseArray2List(nums)
        answer = [-2, -1, 0, 1]
        result = self.sol.sortList(head)
        self.assertEqual(answer, ListNode.parseList2Array(result))

    def test_case3(self):
        nums = [1]
        head = ListNode.parseArray2List(nums)
        answer = [1]
        result = self.sol.sortList(head)
        self.assertEqual(answer, ListNode.parseList2Array(result))

    def test_case4(self):
        nums = [1,0]
        head = ListNode.parseArray2List(nums)
        answer = [0,1]
        result = self.sol.sortList(head)
        self.assertEqual(answer, ListNode.parseList2Array(result))

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTestor)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()