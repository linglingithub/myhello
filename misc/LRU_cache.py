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


class LRUCache(object):
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
