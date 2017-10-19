from util.list_node import ListNode


def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    dummy = ListNode(-1)
    dummy.next = head
    p1 = head
    for i in range(n-1):
        p1 = p1.next
    p2 = dummy
    while p1.next:
        p1 = p1.next
        p2 = p2.next
    target = p2.next
    p2.next = target.next
    return dummy.next

# http://www.cnblogs.com/zuoyuan/p/3701971.html