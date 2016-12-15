# Definition for a linked list node.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        self.next_node = self.next


    @staticmethod
    def parseArray2List(nums):
        dummy = ListNode(0)
        tail = dummy
        for num in nums:
            node = ListNode(num)
            tail.next = node
            tail.next_node = tail.next
            tail = tail.next
        return dummy.next

    @staticmethod
    def parseList2Array(head):
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return nums


