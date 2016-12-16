#coding=utf-8

"""

109. Convert Sorted List to Binary Search Tree

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

Subscribe to see which companies asked this question

Hide Tags Depth-first Search Linked List
Hide Similar Problems (M) Convert Sorted Array to Binary Search Tree


Medium

"""

import unittest

from util.list_node import ListNode
from util.tree_node import TreeNode


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST_ref(self, head): #265ms, 63%
        """
        This is a bottom up way. Not easy to understand.
        Easy to think about the recursive way as sortedListToBST1, or convert to array way
        :type head: ListNode
        :rtype: TreeNode
        """
        p = head
        list_len = 0
        while p:
            list_len += 1
            p = p.next
        result = self.generateBST([head], 0, list_len-1) # note should be a list [head] , not only head, otehrwise wrong
        return result

    def generateBST(self, head, start, end):
        if start>end:
            return None
        mid = start + (end-start)/2
        left = self.generateBST(head, start, mid-1)
        root = TreeNode(head[0].val)
        head[0] = head[0].next
        right = self.generateBST(head, mid+1, end)
        root.left = left
        root.right = right
        return root




    def sortedListToBST1(self, head): #272ms, 54%
        """
        Recursive way , find mid node as root, O(nlogn) time, O(1) space
        If convert list to array, use O(n) time, O(n) space
        :type head: ListNode
        :rtype: TreeNode
        """
        result = self.helper(head, None)
        return result

    def helper(self, head, tail):
        if head==tail:
            return None
        fast = head
        slow = head
        while fast.next != tail and fast.next.next!=tail:
            fast = fast.next.next
            slow = slow.next
        root = TreeNode(slow.val)
        root.left = self.helper(head, slow)
        root.right = self.helper(slow.next, tail)
        return root




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = ListNode.parseArray2List([1,2,3,4,5,6,7])
        answer = TreeNode.generate_bt_from_list([4,2,6,1,3,5,7])
        result = self.sol.sortedListToBST(nums)
        self.assertTrue(TreeNode.compare_tree(answer, result))


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8

"""

# convert linked list to array
def sortedListToBST1(self, head):
    ls = []
    while head:
        ls.append(head.val)
        head = head.next
    return self.helper(ls, 0, len(ls)-1)

def helper(self, ls, start, end):
    if start > end:
        return None
    if start == end:
        return TreeNode(ls[start])
    mid = (start+end) >> 1
    root = TreeNode(ls[mid])
    root.left = self.helper(ls, start, mid-1)
    root.right = self.helper(ls, mid+1, end)
    return root

# top-down approach, O(n*logn)
def sortedListToBST2(self, head):
    if not head:
        return
    if not head.next:
        return TreeNode(head.val)
    dummy = ListNode(0)
    dummy.next = head
    slow, fast = dummy, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    root = TreeNode(slow.next.val)
    root.right = self.sortedListToBST(slow.next.next)
    slow.next = None
    root.left = self.sortedListToBST(head)
    return root

# bottom-up approach, O(n)
def sortedListToBST3(self, head):
    l, p = 0, head
    while p:
        l += 1
        p = p.next
    return self.convert([head], 0, l-1)

def convert(self, head, start, end):
    if start > end:
        return None
    mid = (start + end) >> 1
    l = self.convert(head, start, mid-1)
    root = TreeNode(head[0].val)
    root.left = l
    head[0] = head[0].next
    root.right = self.convert(head, mid+1, end)
    return root

# bottom-up approach, O(n)
def sortedListToBST(self, head):
    l, p = 0, head
    while p:
        l += 1
        p = p.next
    self.node = head
    return self.convert(0, l-1)

def convert(self, start, end):
    if start > end:
        return None
    mid = (start + end) >> 1
    l = self.convert(start, mid-1)
    root = TreeNode(self.node.val)
    root.left = l
    self.node = self.node.next
    root.right = self.convert(mid+1, end)
    return root


######

Using a list allows the function call that creates the left subtree to update node[0] with the next list node that needs
 to be converted into a tree node. Passing a list node directly without the list wrapper would mean the root would be
 the first (i.e smallest value) of the list, which is not what we want. We want to use all the smaller values in the
 left subtree first before using the mid value for the root.

I guess node could equally well be a set containing a single item of head. Any mutable structure will do.
The other version below called "sortedListToBST" achieves the same effect by declaring a class attribute self.node that
can also be updated by other function calls.
Both of which are similar to using a global variable.

I'm not sure what is most pythonic. Using a list purely to contain a variable seems to be slightly cheating. But then
class attributes should ideally be declared in an init method?

"""



"""

http://bangbingsyb.blogspot.com/2014/11/leetcode-convert-sorted-list-to-binary.html

这题和Convert Sorted Array to Binary Search Tree那题看上去很像，但是从array变成了linked list，就不能O(1)寻找中间节
点了。一种直接的修改就是每次遍历一半的节点来找寻中间节点。如何在不知道linked list总长的情况下遍历一半节点？双指针策略，快指
针一次走2个节点，慢指针一次走1个节点，当快指针到尾部时，慢指针对应的即为中间节点。但这种方法的时间复杂度为O(N logN)：每层递
归一共访问N/2个节点，一共log N层递归（对应树的高度）。

对于构建N节点的binary tree来说理论上算法复杂度最少只能到O(N)，因为生成N个节点本身就需要O(N)。要达到O(N)复杂度的算法，就不
能反复遍历来查找中间节点，而只能顺序边访问linked list边构建树。这里的关键是利用构建left subtree的递归，来找寻middle节点。
即构建left subtree的时候需要返回两个值：left subtree的root节点，以及整个left subtree在linked list中的下一个节点，即
middle节点，也是整个left subtree的parent节点。

跑一个例子：
linked list: 0->1->2->NULL

                                                             call (head(0), 0, 2)
                                                                    mid = 1
                                                             node(1), head(2)
                                                /                                               \
                       call (head(0), 0, 0)                                        call (head(2), 2, 2)
                               mid = 0                                                         mid = 2
                       node(0), head(1)                                           node(2), head(NULL)
                        /                    \                                              /                        \
call (head(0), 0, -1)            call (head(0), 1, 0)     call (head(2), 2, 1)          call (head(0), 2, 1)
return NULL                       return NULL               return NULL                    return NULL

最终结果：
    1
  /    \
0      2

"""