#coding=utf-8

import unittest

"""
173. Binary Search Tree Iterator

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

Medium

Related Topics 
Tree Stack Design 
Similar Questions 
Binary Tree Inorder Traversal Flatten 2D Vector Zigzag Iterator Peeking Iterator Inorder Successor in BST 

====================================================================================================

Design an iterator over a binary search tree with the following rules:

Elements are visited in ascending order (i.e. an in-order traversal)
next() and hasNext() queries run in O(1) time in average.
Have you met this question in a real interview? Yes
Example
For the following binary search tree, in-order traversal by using iterator is [1, 6, 10, 11, 12]

   10
 /    \
1      11
 \       \
  6       12
Challenge 
Extra memory usage O(h), h is the height of the tree.

Super Star: Extra memory usage O(1)

Tags 
Binary Tree Binary Search Tree LintCode Copyright Non Recursion Google LinkedIn Facebook
Related Problems 
Medium Zigzag Iterator II 31 %
Medium Zigzag Iterator



"""


# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    #@param root: The root of binary tree.
    def __init__(self, root):
        # write your code here
        self._stack = []
        _node = root
        while _node:
            self._stack.append(_node)
            _node = _node.left

    #@return: True if there has next node, or false
    def hasNext(self):
        # write your code here
        return len(self._stack)>0

    #@return: return next node
    def next(self):
        #write your code here
        _result = self._stack.pop()
        _tmp = _result.right
        while _tmp:
            self._stack.append(_tmp)
            _tmp = _tmp.left
        #yield _result  # does not work
        return _result


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
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

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = list()
        self.pushAll(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.stack

    # @return an integer, the next smallest number
    def next(self):
        tmpNode = self.stack.pop()
        self.pushAll(tmpNode.right)
        return tmpNode.val
        
    def pushAll(self, node):
        while node is not None:
            self.stack.append(node)
            node = node.left

"""

#-*- coding:utf-8 -*-
