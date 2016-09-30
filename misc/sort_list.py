"""
Sort List

Sort a linked list in O(n log n) time using constant space complexity.

Subscribe to see which companies asked this question

Hide Tags Linked List Sort
Hide Similar Problems (E) Merge Two Sorted Lists (M) Sort Colors (M) Insertion Sort List
Have you met this question in a real interview? Yes

"""

import unittest
from list_node import ListNode

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head): #http://fisherlei.blogspot.com/2013/12/leetcode-sort-list-solution.html
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        h1, h2 = self.split_list(head)
        while h1:
            h1 = self.sortList(h1)
        while h2:
            h2 = self.sortList(h2)
        head = self.merge_list(h1, h2)
        return head

    def split_list(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return fast, slow

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
        nums = [1,0, -1]
        head = ListNode.parseArray2List(nums)
        answer = [-1,0,1]
        result = self.sol.sortList(head)
        self.assertEqual(answer, ListNode.parseList2Array(result))


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTestor)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()