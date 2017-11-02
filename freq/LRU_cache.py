#coding=utf-8

import unittest

"""
146. LRU Cache
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: 
get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it 
should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

Difficulty:Hard
Total Accepted:131K
Total Submissions:742K
Contributor: LeetCode
Subscribe to see which companies asked this question.

Related Topics 
Design 
Similar Questions 
LFU Cache Design In-Memory File System Design Compressed String Iterator

"""


class DoubleLinkedNode(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None


class DoubledLinkedList(object):
    def __init__(self, head):
        self.head = head
        self.tail = head

    def move_to_head(self, node):
        old_pre = node.pre
        old_next = node.next
        old_pre.next = old_next
        if old_next:
            old_next.pre = old_pre
        else:
            self.tail = old_pre
        self.insert(node)

    def remove_tail(self):
        tmp = self.tail
        old_pre = self.tail.pre
        old_pre.next = None
        self.tail.pre = None
        self.tail = old_pre
        return tmp.key

    def insert(self, node):
        tmp = self.head.next
        self.head.next = node
        node.pre = self.head
        node.next = tmp
        if tmp:
            tmp.pre = node
        else:
            self.tail = node


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.max_cnt = capacity
        self.cnt = 0
        self.vals = {}
        dummy = DoubleLinkedNode('dummy', -1)
        self.linked_list = DoubledLinkedList(dummy)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.vals.get(key, None)
        if node:
            self.linked_list.move_to_head(node)
            return node.val  # don't forget this
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        node = self.vals.get(key, None)
        if node:
            # should update the key, val here, old same key might have new val!!!
            node.val = value  # !!!important
            self.linked_list.move_to_head(node)
            return  # no need to return, but should return to quit !!!!
            # return node.val    # no need to return
        node = DoubleLinkedNode(key, value)
        if self.cnt >= self.max_cnt:
            old_key = self.linked_list.remove_tail()
            #print("old_key", old_key)
            del self.vals[old_key]
            self.cnt -= 1
        self.vals[key] = node
        self.linked_list.insert(node)
        self.cnt += 1

####################################################################################

class LRUCache1(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        if capacity <= 0:
            raise ValueError("Capacity should be positive integer.")
        self.vals = {}
        self.cnt = 0
        self.capacity = capacity
        self.visit_list = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.vals:
            target = self.vals[key]
            # update the list
            self.visit_list.remove(target)
            self.visit_list.add_head(target)
            return target.val
        else:
            return -1

    def put(self, key, value):
        """
        need to think about 
        1) when key already existes in dict, maybe need to update value, maybe not
        2) adjust the node to head
        3) if not exist, create new node and update, a) capcity not full, b) capacity full, then need to delete tail
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.vals:
            node = self.vals[key]
            self.visit_list.remove(node)
            self.visit_list.add_head(node)
            node.val = value
        else:
            node = ListNode(key, value)
            self.vals[key] = node
            # self.visit_list.add_head(node) # when empty list, AttributeError: 'NoneType' object has no attribute 'add_head'
            if not self.visit_list:
                self.visit_list = DoubleList(node)
            else:
                self.visit_list.add_head(node)
            self.cnt += 1
            if self.cnt > self.capacity: # should not have >=, only use > here
                old_key = self.visit_list.tail.key
                self.visit_list.remove_tail()
                del self.vals[old_key]
                self.cnt -= 1


class ListNode(object):
    def __init__(self, key, val):
        self.key = key  # looks like key is also necessary, when need to remove tail node and del key in cache
        self.val = val
        self.pre = None
        self.post = None


class DoubleList(object):
    def __init__(self, head):
        self.head = head
        self.tail = head

    def remove(self, node):
        if self.head == self.tail:
            self.head, self.tail = None, None
            node.next, node.pre = None, None
            return
        if node == self.head:
            self.head = node.next
            self.head.pre = None
            node.next, node.pre = None, None
            return
        if node == self.tail:
            self.tail = node.pre
            self.tail.next = None
            node.next, node.pre = None, None
            return
        pre, post = node.pre, node.next
        pre.next = post
        post.pre = pre
        node.next, node.pre = None, None

    def add_head(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            return
        node.next = self.head
        self.head.pre = node
        self.head = node

    def remove_tail(self):
        node = self.tail
        self.remove(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.cache = LRUCache(2)
        self.cache.put(1,1)
        self.cache.put(2,2)

    def test_case1(self):
        answer = 1
        result = self.cache.get(1)
        self.assertEqual(answer, result)

    def test_case2(self):
        self.cache.get(1)
        self.cache.put(3,3)  # evict 2
        result = self.cache.get(2)
        answer = -1
        self.assertEqual(answer, result)

    def test_case3(self):
        self.cache.get(1)
        self.cache.put(3,3)  # evict 2
        self.cache.get(2)
        self.cache.put(4, 4) # evicts 1
        result = self.cache.get(1)
        answer = -1
        self.assertEqual(answer, result)

    def test_case4(self):
        self.cache.get(1)
        self.cache.put(3,3)  # evict 2
        self.cache.get(2)
        self.cache.put(4, 4) # evicts 1
        self.cache.get(1)
        result = [self.cache.get(3), self.cache.get(4)]
        answer = [3,4]
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""

http://www.cnblogs.com/zuoyuan/p/3701572.html


原题地址：http://oj.leetcode.com/problems/lru-cache/

题意：设计LRU Cache

参考文献：http://blog.csdn.net/hexinuaa/article/details/6630384 这篇博文总结的很到位。

　　　　   https://github.com/Linzertorte/LeetCode-in-Python/blob/master/LRUCache.py 代码参考的github人写的，思路非常清晰，
写的也很好。

Cache简介：

Cache(高速缓存)， 一个在计算机中几乎随时接触的概念。CPU中Cache能极大提高存取数据和指令的时间，让整个存储器(Cache+内存)既有Cache的高速度，
又能有内存的大容量；操作系统中的内存page中使用的Cache能使得频繁读取的内存磁盘文件较少的被置换出内存，从而提高访问速度；数据库中数据查询也
用到Cache来提高效率；即便是Powerbuilder的DataWindow数据处理也用到了Cache的类似设计。Cache的算法设计常见的有FIFO(first in first out)
和LRU(least recently used)。根据题目的要求，显然是要设计一个LRU的Cache。

解题思路：

Cache中的存储空间往往是有限的，当Cache中的存储块被用完，而需要把新的数据Load进Cache的时候，我们就需要设计一种良好的算法来完成数据块的替
换。LRU的思想是基于“最近用到的数据被重用的概率比较早用到的大的多”这个设计规则来实现的。

为了能够快速删除最久没有访问的数据项和插入最新的数据项，我们双向链表连接Cache中的数据项，并且保证链表维持数据项从最近访问到最旧访问的顺序。
每次数据项被查询到时，都将此数据项移动到链表头部（O(1)的时间复杂度）。这样，在进行过多次查找操作后，最近被使用过的内容就向链表的头移动，而
没有被使用的内容就向链表的后面移动。当需要替换时，链表最后的位置就是最近最少被使用的数据项，我们只需要将最新的数据项放在链表头部，当Cache满
时，淘汰链表最后的位置就是了。

  注： 对于双向链表的使用，基于两个考虑。首先是Cache中块的命中可能是随机的，和Load进来的顺序无关。其次，双向链表插入、删除很快，可以灵活的
  调整相互间的次序，时间复杂度为O(1)。

    查找一个链表中元素的时间复杂度是O(n)，每次命中的时候，我们就需要花费O(n)的时间来进行查找，如果不添加其他的数据结构，这个就是我们能实
    现的最高效率了。目前看来，整个算法的瓶颈就是在查找这里了，怎么样才能提高查找的效率呢？Hash表，对，就是它，数据结构中之所以有它，就是因
    为它的查找时间复杂度是O(1)。

梳理一下思路：对于Cache的每个数据块，我们设计一个数据结构来储存Cache块的内容，并实现一个双向链表，其中属性next和prev是双向链表的两个指针，
key用于存储对象的键值，value用于存储cache块对象本身。

Cache的接口：

查询：

根据键值查询hashmap，若命中，则返回节点key值对应的value，否则返回-1。
从双向链表中删除命中的节点，将其重新插入到表头。
所有操作的复杂度均为O(1)。
插入：

将新的节点关联到Hashmap
如果Cache满了，删除双向链表的尾节点，同时删除Hashmap对应的记录
将新的节点插入到双向链表中头部
更新：

和查询相似
删除：

从双向链表和Hashmap中同时删除对应的记录。
双向链表示意图：



代码：

复制代码
class Node:　　　　　　　　　　　　　　　　　　　　　　　　　　#双向链表中节点的定义
    def __init__(self,k,x):
        self.key=k
        self.val=x
        self.prev=None
        self.next=None

class DoubleLinkedList:　　　　　　　　　　　　　　　　　　　#双向链表是一个表头，head指向第一个节点，tail指向最后一个节点
    def __init__(self):
        self.tail=None
        self.head=None
        
    def isEmpty():　　　　　　　　　　　　　　　　　　　　　　#如果self.tail==None，那么说明双向链表为空
        return not self.tail
    def removeLast(self):　　　　　　　　　　　　　　　　　　#删除tail指向的节点
        self.remove(self.tail)
        
    def remove(self,node):　　　　　　　　　　　　　　　　　 #具体双向链表节点删除操作的实现
        if self.head==self.tail:
            self.head,self.tail=None,None
            return
        if node == self.head:
            node.next.prev=None
            self.head=node.next
            return
        if node ==self.tail:
            node.prev.next=None
            self.tail=node.prev
            return
        node.prev.next=node.next
        node.next.prev=node.prev
        
    def addFirst(self,node):　　　　　　　　　　　　　　　　  #在双向链表的第一个节点前面再插入一个节点　　
        if not self.head:
            self.head=self.tail=node
            node.prev=node.next=None
            return
        node.next=self.head
        self.head.prev=node
        self.head=node
        node.prev=None

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):　　　　　　　　　　　　　　#初始化LRU Cache
        self.capacity=capacity　　　　　　　　　　　　　　　 #LRU Cache的容量大小　　　　　　　　　　　　　
        self.size=0　　　　　　　　　　　　　　　　　　　　　　#LRU Cache目前占用的容量
        self.P=dict()　　　　　　　　　　　　　　　　　　　　　#dict为文章中提到的hashmap，加快搜索速度，{key：对应节点的地址}
        self.cache=DoubleLinkedList()
    # @return an integer
    def get(self, key):　　　　　　　　　　　　　　　　　　　　#查询操作
        if (key in self.P) and self.P[key]:　　　　　　　　#如果key在字典中
            self.cache.remove(self.P[key])　　　　　　　　　#将key对应的指针指向的节点删除
            self.cache.addFirst(self.P[key])　　　　　　　　#然后将这个节点添加到双向链表头部
            return self.P[key].val　　　　　　　　　　　　　　#并返回节点的value
        else: return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):　　　　　　　　　　　　　　　　#设置key对应的节点的值为给定的value值
        if key in self.P:　　　　　　　　　　　　　　　　　　　#如果key在字典中
            self.cache.remove(self.P[key])　　　　　　　　  #先删掉key对应的节点
            self.cache.addFirst(self.P[key])　　　　　　　　#然后将这个节点插入到表的头部
            self.P[key].val=value　　　　　　　　　　　　　　 #将这个节点的值val改写为value
        else:　　　　　　　　　　　　　　　　　　　　　　　　　　#如果key不在字典中
            node=Node(key,value)　　　　　　　　　　　　　　　#新建一个Node节点，val值为value
            self.P[key]=node　　　　　　　　　　　　　　　　　 #将key和node的对应关系添加到字典中
            self.cache.addFirst(node)　　　　　　　　　　　　#将这个节点添加到链表表头
            self.size +=1　　　　　　　　　　　　　　　　　　　#容量加1
            if self.size > self.capacity:　　　　　　　　   #如果链表的大小超过了缓存的大小，删掉最末尾的节点，
                self.size -=1　　　　　　　　　　　　　　　　 #并同时删除最末尾节点key值和末节点在字典中的对应关系
                del self.P[self.cache.tail.key]
                self.cache.removeLast()
复制代码


"""