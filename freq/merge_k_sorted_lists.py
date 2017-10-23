#coding=utf-8

"""

23. Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Subscribe to see which companies asked this question

Hide Tags Divide and Conquer Linked List Heap
Hide Similar Problems (E) Merge Two Sorted Lists (M) Ugly Number II

Hard

"""

import unittest
import heapq
from util.list_node import ListNode

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # if have time, comeback and implement the two-two way.
        pass


    def mergeKLists_heapq(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        pq = []
        for node in lists:
            if node: #need to add this protection, otherwise wrong for emapty list input, like case1
                pq.append((node.val, node))
        heapq.heapify(pq)
        dummy = ListNode(0)
        p = dummy
        while pq:
            tmp = heapq.heappop(pq)[1] # don't forget to extract node from tuple, [1]here
            p.next = tmp
            p = p.next
            if tmp.next:
                heapq.heappush(pq, (tmp.next.val,tmp.next))
        return dummy.next
        
        
        

    def mergeKLists_ref(self, lists): #139ms, 67%
        """
        解题思路：归并k个已经排好序的链表。使用堆这一数据结构，首先将每条链表的头节点进入堆中，然后将最小的弹出，并将最小的节点这条链表的
        下一个节点入堆，依次类推，最终形成的链表就是归并好的链表。
        :param lists:
        :return:
        """
        heap = []
        for node in lists:
            if node:
                heap.append((node.val, node))
        heapq.heapify(heap)
        head = ListNode(0); curr = head
        while heap:
            pop = heapq.heappop(heap)
            curr.next = ListNode(pop[0])
            curr = curr.next
            if pop[1].next:
                heapq.heappush(heap, (pop[1].next.val, pop[1].next))
        return head.next


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [[]]
        answer = None
        result = self.sol.mergeKLists(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()


"""

思路1：priority queue

将每个list的最小节点放入一个priority queue (min heap)中。之后每从queue中取出一个节点，则将该节点在其list中的下一个节点插入，以此类推
直到全部节点都经过priority queue。由于priority queue的大小为始终为k，而每次插入的复杂度是log k，一共插入过nk个节点。时间复杂度为
O(nk logk)，空间复杂度为O(k)。

思路2：Merge two lists

利用合并两个list的方法，依次将每个list合并到结果的list中。这个方法的空间复杂度为O(1)，时间复杂度为：
2n + 3n + ... + kn = [(k+1)*k/2-1]*n = O(nk^2)
由于时间复杂度较大，大数据测试会超时。

思路3：二分法

类似merge sort，每次将所有的list两两之间合并，直到所有list合并成一个。如果用迭代而非递归，则空间复杂度为O(1)。时间复杂度：
2n * k/2 + 4n * k/4 + ... + (2^x)n * k/(2^x) = nk * x
k/(2^x) = 1 -> 2^x = k -> x = log2(k)
所以时间复杂度为O(nk log(k))，与方法一相同。


=======================


My simple java Solution use recursion
public static ListNode mergeKLists(ListNode[] lists){
    return partion(lists,0,lists.length-1);
}

public static ListNode partion(ListNode[] lists,int s,int e){
    if(s==e)  return lists[s];
    if(s<e){
        int q=(s+e)/2;
        ListNode l1=partion(lists,s,q);
        ListNode l2=partion(lists,q+1,e);
        return merge(l1,l2);
    }else
        return null;
}

//This function is from Merge Two Sorted Lists.
public static ListNode merge(ListNode l1,ListNode l2){
    if(l1==null) return l2;
    if(l2==null) return l1;
    if(l1.val<l2.val){
        l1.next=merge(l1.next,l2);
        return l1;
    }else{
        l2.next=merge(l1,l2.next);
        return l2;
    }
}


"""


"""
这题需要合并k个排好序的链表，我们采用divide and conquer的方法，首先两两合并，然后再将先前合并的继续两两合并。时间复杂度为O(NlgN)。

代码如下：

class Solution {
public:
     ListNode *mergeKLists(vector<ListNode *> &lists) {
        if(lists.empty()) {
            return NULL;
        }

        int n = lists.size();
        while(n > 1) {
            int k = (n + 1) / 2;
            for(int i = 0; i < n / 2; i++) {
                //合并i和i + k的链表，并放到i位置
                lists[i] = merge2List(lists[i], lists[i + k]);
            }
            //下个循环只需要处理前k个链表了
            n = k;
        }
        return lists[0];
    }

    ListNode* merge2List(ListNode* n1, ListNode* n2) {
        ListNode dummy(0);
        ListNode* p = &dummy;
        while(n1 && n2) {
            if(n1->val < n2->val) {
                p->next = n1;
                n1 = n1->next;
            } else {
                p->next = n2;
                n2 = n2->next;
            }
            p = p->next;
        }

        if(n1) {
            p->next = n1;
        } else if(n2) {
            p->next = n2;
        }

        return dummy.next;
    }
};


"""

"""
# a self implemented way for buidling a heap. # 365ms, 5.09%

    def mergeKLists(self, lists):
        # write your code here
        self.heap = [[i, lists[i].val] for i in range(len(lists)) if lists[i] != None]
        self.hsize = len(self.heap)
        for i in range(self.hsize - 1, -1, -1):
            self.adjustdown(i)
        nHead = ListNode(0)
        head = nHead
        while self.hsize > 0:
            ind, val = self.heap[0][0], self.heap[0][1]
            head.next = lists[ind]
            head = head.next
            lists[ind] = lists[ind].next
            if lists[ind] is None:
                self.heap[0] = self.heap[self.hsize-1]
                self.hsize = self.hsize - 1
            else:
                self.heap[0] = [ind, lists[ind].val]
            self.adjustdown(0)
        return nHead.next

    def adjustdown(self, p):
        lc = lambda x: (x + 1) * 2 - 1
        rc = lambda x: (x + 1) * 2
        while True:
            np, pv = p, self.heap[p][1]
            if lc(p) < self.hsize and self.heap[lc(p)][1] < pv:
                np, pv = lc(p), self.heap[lc(p)][1]
            if rc(p) < self.hsize and self.heap[rc(p)][1] < pv:
                np = rc(p)
            if np == p:
                break
            else:
                self.heap[np], self.heap[p] = self.heap[p], self.heap[np]
                p = np

"""

#-*- coding:utf-8 -*-
