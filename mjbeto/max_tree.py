#coding=utf-8

import unittest

"""
Max Tree

Given an integer array with no duplicates. A max tree building on this array is defined as follow:

The root is the maximum number in the array
The left subtree and right subtree are the max trees of the subarray divided by the root number.
Construct the max tree by the given array.

Have you met this question in a real interview? Yes
Example
Given [2, 5, 6, 0, 3, 1], the max tree constructed by this array is:

    6
   / \
  5   3
 /   / \
2   0   1
Challenge 
O(n) time and memory.

Tags 
LintCode Copyright Stack Cartesian Tree
Related Problems 
Hard Largest Rectangle in Histogram 27 %
Medium Min Stack



"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

from util.tree_node import TreeNode

class Solution:
    # @param A: Given an integer array with no duplicates.
    # @return: The root of max tree.
    def maxTree(self, A): # ref, use stack to track the decreasing part
        if not A:
            return None
        stack = []
        for i in range(len(A)):
            cur = TreeNode(A[i])
            while stack and stack[-1].val < cur.val:  # if use if here, wrong for case 1
                cur.left = stack.pop()
            if stack:
                stack[-1].right = cur
            stack.append(cur)
        return stack[0]




    def maxTree_TLE(self, A): # TLE, 88% cases passed, TLE case check data/max_tree_case1.ini, increasing array as input
        if not A:
            return None
        start, end = 0, len(A) - 1
        root = self.build_max(A, start, end)
        return root

    def build_max(self, A, start, end):
        if start > end:
            return None
        idx = start
        for i in range(start, end+1):
            if A[i] > A[idx]:
                idx = i
        root = TreeNode(A[idx])
        root.left = self.build_max(A, start, idx-1)
        root.right = self.build_max(A, idx+1, end)
        return root







class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        A = [6,4,20]
        answer = "20,6,#,#,4"            # wrong output "6,#,20,4"
        result = self.sol.maxTree(A)
        answer_tree = TreeNode.generate_bt_from_string_standard(answer)
        self.assertTrue(TreeNode.compare_tree(answer_tree, result))
        #self.assertEqual(TreeNode.generate_bt_from_string(answer), result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""


解题思路

通过观察发现规律，对于每个node的父亲节点 = min(左边第一个比它大的，右边第一个比它大的)
维护一个降序数组，可以实现对这个min的快速查找
# stack = [2], push 5 因为 5 > 2, 所以2是5的左儿子, pop 2
# stack = [], push 5
# stack = [5], push 6, 因为 6 > 5，所以5是6的左儿子, pop 5
# stack = [], push 6
# stack = [6], push 0, 因为0 < 6, stack = [6], 所以0是6的右儿子
# stack = [6, 0], push 3, 因为3 > 0, 所以0是3的左儿子， pop 0
# stack = [6], 所以3是6的右儿子， push 3
# stack = [6, 3], push 1, 因为1 < 3，所以1是3的右儿子
完整代码


Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    # @param A: Given an integer array with no duplicates.
    # @return: The root of max tree.
    def maxTree(self, A):
        # write your code here
        stack = []
        for element in A:
            node = TreeNode(element)
            while len(stack) != 0 and element > stack[-1].val:
                node.left = stack.pop()
            if len(stack) != 0:
                stack[-1].right = node
            stack.append(node)
        return stack[0]

=======================================================================================================================


Recursion: use recursion method, in the worst case, the complexity is O(n^2).

Linear method: Refer to the analysis of some other people: http://www.meetqun.com/thread-3335-1-1.html

这个题Leetcode上没有，其实这种树叫做笛卡树（ Cartesian tree）。直接递归建树的话复杂度最差会退化到O(n^2)。经典建树方法，用到的是单调堆
栈。我们堆栈里存放的树，只有左子树，没有有子树，且根节点最大。
（1） 如果新来一个数，比堆栈顶的树根的数小，则把这个数作为一个单独的节点压入堆栈。
（2） 否则，不断从堆栈里弹出树，新弹出的树以旧弹出的树为右子树，连接起来，直到目前堆栈顶的树根的数大于新来的数。然后，弹出的那些数，已经形
成了一个新的树，这个树作为新节点的左子树，把这个新树压入堆栈。

这样的堆栈是单调的，越靠近堆栈顶的数越小。
最后还要按照（2）的方法，把所有树弹出来，每个旧树作为新树的右子树。


=======================================================================================================================



Should memorize MaxTree. 依次类推，会做Min-Tree, Expression Tree

Stack里，最大的值在下面。利用此性质，有这样几个step:

1   
把所有小于curr node的，全Pop出来, while loop, keep it going.    
最后pop出的这个小于Curr的node：它同时也是stack里面pop出来小于curr的最大的一个，最接近curr大小。（因为这个stack最大值靠下面）    
把这个最大的小于curr的node放在curr.left.    

2   
那么，接下去stack里面的一定是大于curr：   
那就变成curr的left parent. set stack.peek().right = curr.

3   
结尾：stack底部一定是最大的那个，也就是max tree的头。


Can't fingure express tree, so look at Max Tree problem first
Good explain here:http://blog.welkinlan.com/2015/06/29/max-tree-lintcode-java/
Iterate from left of array to right. So, every element we take, it will be the current right-most element.
Goal: find left-child, and find its left-parent.
Do for loop on all nodes.Remember to push the stack on every for iteration.
1. Left-child: use while loop to find the very last smaller node(comparing with curr Node), and set that as left-child.
2. Then, of course, the node left in stack (if still existing a node), will be the first larger node. That, will become curr
	node's left parent.
3. At the end, we need to return largest element, which is root. Just by poping off all nodes will give us the bottom-largest-node
Note: Interesting behavior:
Stack: always stores the largest value at bottom. In above example, when 6 gets in stack, it will never come back.
All smaller element (smaller than current point) will be poped out, 
and of course, the last-possible-smaller element will be the largest smaller point on stack, then we attach it to current node.
These behavior keeps larger value on upper level of the tree


========================================================================================================================


class Solution:
    # @param A: Given an integer array with no duplicates.
    # @return: The root of max tree.
    def maxTree(self, A):
        # write your code here
        stk = []
        for ele in A:
            node = TreeNode(ele)
            while stk and ele > stk[-1].val:
                node.left = stk.pop()
            if stk:
                stk[-1].right = node
            stk.append(node)
        return stk[0]


========================================================================================================================


jiuzhang ref:

class Stack:
  def __init__(self):
    self.items = []

  def __getitem__(self, index):
    return self.items[index]

  def isEmpty(self):
    return len(self.items)==0
   
  def push(self, item):
    self.items.append(item)
   
  def pop(self):
    return self.items.pop() 
   
  def peek(self):
    if not self.isEmpty():
      return self.items[len(self.items)-1]
     
  def size(self):
    return len(self.items) 
class Solution:
    # @param A: Given an integer array with no duplicates.
    # @return: The root of max tree.
    def maxTree(self, A):
        # write your code here
        stk = Stack()
        for ele in A:
            node = TreeNode(ele)
            while not stk.isEmpty() and ele > stk.peek().val:
                node.left = stk.pop()
            if not stk.isEmpty():
                stk.peek().right = node
            stk.push(node)
        return stk[0]


"""

#-*- coding:utf-8 -*-
