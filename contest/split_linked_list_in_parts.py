"""


725. Split Linked List in Parts My SubmissionsBack to Contest
User Accepted: 0
User Tried: 0
Total Accepted: 0
Total Submissions: 0
Difficulty: Medium
Given a (singly) linked list with head node root, write a function to split the linked list into k consecutive linked list "parts".

The length of each part should be as equal as possible: no two parts should have a size differing by more than 1. This may lead to some parts being null.

The parts should be in order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal parts occurring later.

Return a List of ListNode's representing the linked list parts that are formed.

Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]
Example 1:
Input: 
root = [1, 2, 3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The input and each element of the output are ListNodes, not arrays.
For example, the input root has root.val = 1, root.next.val = 2, \root.next.next.val = 3, and root.next.next.next = null.
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but it's string representation as a ListNode is [].
Example 2:
Input: 
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
Note:

The length of root will be in the range [0, 1000].
Each value of a node in the input will be an integer in the range [0, 999].
k will be an integer in the range [1, 50].

"""

import unittest


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        if not root:
            return [ [] for _ in range(k)]
        list_len = self.find_len(root)
        short_len = list_len / k
        long_cnt = list_len % k
        #long_len = short_len + list_len % k
        long_len = short_len + 1
        dummy = ListNode(-1)
        dummy.next = root
        res = []
        curr = dummy
        tmp = dummy.next
        for i in range(long_cnt):
            res.append(tmp)
            curr = tmp
            for j in range(long_len-1):
                curr = curr.next
            tmp = curr.next
            curr.next = None
        # tmp = curr.next if curr else None
        dummy = ListNode(-1)
        dummy.next = tmp
        curr = dummy
        for i in range(k - long_cnt):
            if not short_len:
                res.append(None)
                continue
            res.append(tmp)
            curr = tmp
            for j in range(short_len-1):
                if not curr:
                    return res
                curr = curr.next
            if curr:
                tmp = curr.next
                curr.next = None
            else:
                tmp = None
        return res

    def find_len(self, root):
        cnt = 1
        while root.next:
            cnt += 1
            root = root.next
        return cnt


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case2(self):
        nums = [1,2,3,4,5,6,7]
        k = 3
        from util.list_node import ListNode
        head = ListNode.parseArray2List(nums)
        answer = [head, head.next, head.next.next, head.next.next.next, None]
        result = self.sol.splitListToParts(head, k)
        pass
        #self.assertEqual(answer, result)

    def test_case1(self):
        nums = [1,2,3,4]
        k = 5
        from util.list_node import ListNode
        head = ListNode.parseArray2List(nums)
        #answer = [head, head.next, head.next.next, head.next.next.next, None]
        result = self.sol.splitListToParts(head, k)
        pass
        #self.assertEqual(answer, result)

    def test_case3(self):
        nums = [0,1]
        k = 2
        from util.list_node import ListNode
        head = ListNode.parseArray2List(nums)
        #answer = [head, head.next, head.next.next, head.next.next.next, None]
        result = self.sol.splitListToParts(head, k)
        pass
        #self.assertEqual(answer, result)

    def test_case04(self):
        nums = [0,1,2]
        k = 3
        from util.list_node import ListNode
        head = ListNode.parseArray2List(nums)
        #answer = [head, head.next, head.next.next, head.next.next.next, None]
        result = self.sol.splitListToParts(head, k)
        pass
        #self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-