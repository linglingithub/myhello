#coding=utf-8
"""
138. Copy List with Random Pointer

A linked list is given such that each node contains an additional random pointer which could point to any
node in the list or null.

Return a deep copy of the list.

Subscribe to see which companies asked this question

Hide Tags Hash Table Linked List
Hide Similar Problems (M) Clone Graph

Hard

"""



import unittest
from util.random_list_node import RandomListNode


# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head): #139ms, 66%
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        copy_dict = {}
        curr = head
        dummy = RandomListNode(-1)
        pre = dummy
        while curr:
            tmp = RandomListNode(curr.label)
            copy_dict[curr] = tmp
            pre.next = tmp
            pre = tmp
            curr = curr.next
        curr = head
        while curr:
            if curr.random:
                copy_dict[curr].random = copy_dict[curr.random]
            curr = curr.next
        return dummy.next


    def copyRandomList_old(self, head): #165ms, 31%
        """
        This way can be applied to graph cloning, but actually, this problem can be simpler.
        Because it is still a list, the list structure is maintained by .next. The .random is different from .next.
        So this can be simplified to without using seeds list.
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        seeds = [head]
        node_dict = {}
        while seeds:
            tmp = seeds[0]
            del seeds[0]
            if tmp in node_dict:
                continue
            new_node = RandomListNode(tmp.label)
            node_dict[tmp] = new_node
            if tmp.next and not tmp.next in node_dict:
                seeds.append(tmp.next)
            if tmp.random and not tmp.random in node_dict:
                seeds.append(tmp.random)
        for old_node, new_node in node_dict.iteritems(): # check if link is None or not, otherwise wrong
            new_node.next = node_dict[old_node.next] if old_node.next else None
            new_node.random = node_dict[old_node.random] if old_node.random else None
        return node_dict[head]


    def copyRandomList_ref(self, head):
        """
        首先，在原链表的每个节点后面都插入一个新节点，新节点的内容和前面的节点一样。比如上图，1后面插入1，2后面插入2，依次类推。

        其次，原链表中的random指针如何映射呢？比如上图中，1节点的random指针指向3，4节点的random指针指向2。如果有一个tmp指针
        指向1（蓝色），则一条语句：tmp.next.random = tmp.random.next；就可以解决这个问题。

        第三步，将新的链表从上图这样的链表中拆分出来。


        :param head:
        :return:
        """
        if head == None: return None
        tmp = head
        while tmp:
            newNode = RandomListNode(tmp.label)
            newNode.next = tmp.next
            tmp.next = newNode
            tmp = tmp.next.next
        tmp = head
        while tmp:
            if tmp.random:
                tmp.next.random = tmp.random.next
            tmp = tmp.next.next
        newhead = head.next
        pold = head
        pnew = newhead
        while pnew.next:
            pold.next = pnew.next
            pold = pold.next
            pnew.next = pold.next
            pnew = pnew.next
        pold.next = None
        pnew.next = None
        return newhead



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1_not(self):
        nums = 1
        answer = 1
        result = self.sol.searchInsert(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""

解法I：时间复杂度O(n)，空间复杂度O(n)

使用哈希表保存原链表到新链表节点的映射，即可实现对随机指针域的拷贝

Python代码：
class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head): #126ms, 82%
        nodeDict = dict()
        dummy = RandomListNode(0)
        pointer, newHead = head, dummy
        while pointer:
            newNode = RandomListNode(pointer.label)
            nodeDict[pointer] = newHead.next = newNode
            newHead, pointer = newHead.next, pointer.next
        pointer, newHead = head, dummy.next
        while pointer:
            if pointer.random:
                newHead.random = nodeDict[pointer.random]
            pointer, newHead = pointer.next, newHead.next
        return dummy.next


解法II：时间复杂度O(n)，空间复杂度O(1)

在原始链表的每一个节点之后插入其自身的拷贝，通过这种方式，即可避免额外空间的使用。

参考LeetCode Discuss：https://leetcode.com/discuss/22421/solution-constant-space-complexity-linear-time-complexity

算法包含下面三个步骤：

1. 遍历原链表，并复制每一个节点，将新节点插入原节点之后

2. 遍历新链表，为其中的新增节点设置random指针

3. 重建原链表，并提取出拷贝的新节点
C++代码：
public RandomListNode copyRandomList(RandomListNode head) {
    RandomListNode iter = head, next;

    // First round: make copy of each node,
    // and link them together side-by-side in a single list.
    while (iter != null) {
        next = iter.next;

        RandomListNode copy = new RandomListNode(iter.label);
        iter.next = copy;
        copy.next = next;

        iter = next;
    }

    // Second round: assign random pointers for the copy nodes.
    iter = head;
    while (iter != null) {
        if (iter.random != null) {
            iter.next.random = iter.random.next;
        }
        iter = iter.next.next;
    }

    // Third round: restore the original list, and extract the copy list.
    iter = head;
    RandomListNode pseudoHead = new RandomListNode(0);
    RandomListNode copy, copyIter = pseudoHead;

    while (iter != null) {
        next = iter.next.next;

        // extract the copy
        copy = iter.next;
        copyIter.next = copy;
        copyIter = copy;

        // restore the original list
        iter.next = next;

        iter = next;
    }

    return pseudoHead.next;
}



本文链接：http://bookshadow.com/weblog/2015/07/31/leetcode-copy-list-random-pointer/

"""

#-*- coding:utf-8 -*-
#coding=utf-8