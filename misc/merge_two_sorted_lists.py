"""
Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Subscribe to see which companies asked this question

Hide Tags Linked List
Hide Similar Problems (H) Merge k Sorted Lists (E) Merge Sorted Array (M) Sort List (M) Shortest Word Distance II


"""

import unittest
from list_node import ListNode

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next # important, don't forget this
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next






class SolutionTestor(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        l1 = ListNode(0)
        l2 = ListNode(1)
        answer = [0, 1]
        result = self.sol.mergeTwoLists(l1, l2)
        self.assertEqual(answer, ListNode.parseList2Array(result))


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTestor)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()