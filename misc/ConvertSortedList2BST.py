from TreeNode import TreeNode
from list_node import ListNode


class Solution(object):
    h = None

    def __init__(self):
        pass

    def sortedListToBST(self, head):
        if head is None:
            return None
        Solution.h = head
        len = self.getLength(head)
        return self.sortedListToBSTr(0, len-1)

    # get list length
    def getLength(self, head):
        len = 0
        p = head
        while p is not None:
            len += 1
            p = p.next_node
        return len

    # build tree bottom-up
    def sortedListToBSTr(self, start, end):
        if start > end:
            return None

        # mid
        mid = (start + end) / 2

        left = self.sortedListToBSTr(start, mid - 1)
        root = TreeNode(Solution.h.val)
        Solution.h = Solution.h.next_node
        right = self.sortedListToBSTr(mid + 1, end)

        root.left = left
        root.right = right
        return root

if __name__ == '__main__':
    lhead = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    lhead.next_node = l2
    l2.next_node = l3
    l3.next_node = l4
    l4.next_node = l5

    sol = Solution()
    tr = sol.sortedListToBST(lhead)
    print tr