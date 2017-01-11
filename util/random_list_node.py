# Definition for a linked list node.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
        #self.next_node = self.next


    @staticmethod
    def parseArray2List(nums):
        dummy = RandomListNode(0)
        tail = dummy
        for num in nums:
            node = RandomListNode(num)
            tail.next = node
            #tail.next_node = tail.next
            tail = tail.next
        return dummy.next

    @staticmethod
    def parseList2Array(head):
        nums = []
        while head:
            nums.append(head.label)
            head = head.next
        return nums


