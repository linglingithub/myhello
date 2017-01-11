#coding=utf-8
__author__ = 'linglin'
"""

99. Recover Binary Search Tree

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
Subscribe to see which companies asked this question

Hide Tags Tree Depth-first Search

Hard

"""

import unittest
from util.tree_node import TreeNode


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree1(self, root): #132ms, 26%
        """
        (1) Inorder traverse a bst, correct sequence will be an increasing array.
        If two nodes swapped, the array values will be like:

                  /\               //////////////////
                /   \//////////\  /
        ///////                 \/

        Two bumps on the increasing line.
        First bump, you found the smaller value, and the one PREVIOUS to the smaller val is the swapped node.
        Second bump, the smaller value ITSELF, is the swapped node.

        (2) Inorder traverse without stack and with O(1) space, you need to keep a previous node. Normal inorder
        with stack or with recursive way will use O(n) or O(logN) space. Need to know about "Thread Binary Tree".
        Or "Morris Inorder Traverse"

        (3) If two neighboring nodes are swapped, then there are actually only one bump on the increasing line.
         Therefore, when finding the first bump, record the CURRENT node and the PREVIOUS node. Keep searching, if
         there is a next bump, then update the second recorded node. Case 1

        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        self.one = None
        self.two = None
        self.pre = None
        self.find_wrong_nodes(root)
        tmp = self.one.val
        self.one.val = self.two.val
        self.two.val = tmp

    def find_wrong_nodes(self,root):
        if root is None:
            return
        print root.val
        self.find_wrong_nodes(root.left)
        if self.pre and root.val < self.pre.val:
            if self.one is None:
                self.one = self.pre
                self.two = root # this is important, see comments (3) and case 1
            else:
                self.two = root
                return
        self.pre = root
        self.find_wrong_nodes(root.right)


    def recoverTree(self, root): #108ms, 80%
        """
        但是这题要求使用O(1)的空间，如果采用通常的中序遍历（递归或者栈）的方式，都需要O(N)的空间，所以这里我们用Morris Traversal的方式来进行树的中序遍历。

        Morris Traversal中序遍历的原理比较简单：

        如果当前节点的左孩子为空，则输出当前节点并将其有孩子作为当前节点。
        如果当前节点的左孩子不为空，在当前节点的左子树中找到当前节点在中序遍历下的前驱节点，也就是当前节点左子树的最右边的那个节点。
            如果前驱节点的右孩子为空，则将它的右孩子设置为当前节点，当前节点更新为其左孩子。
            如果前驱节点的右孩子为当前节点，则将前驱节点的右孩子设为空，输出当前节点，当前节点更新为其右孩子。
        """
        cur = None
        pre = None
        p1 = None
        p2 = None
        preCur = None

        found = False

        if not root:
            return

        cur = root
        while cur:
            # if no left, visit self, go to right, update preCur
            if not cur.left:
                #记录p1和p2
                if preCur and preCur.val > cur.val:
                    if not found:
                        p1 = preCur
                        found = True
                    p2 = cur


                preCur = cur
                cur = cur.right
            # end of if not left

            # if there is left, process thread, if no thread, create thread and go to left, otherwise ( left already
            # visited), remove thread, visit self, and go to right.
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right

                if not pre.right:
                    pre.right = cur
                    cur = cur.left
                else:
                    #记录p1和p2
                    if preCur.val > cur.val:
                        if not found:
                            p1 = preCur
                            found = True
                        p2 = cur

                    preCur = cur
                    cur = cur.right
                    # left subtree's right most is already visited, remove thread and restore tree structure
                    pre.right = None
            #end of else
        # end of while cur

        if p1 and p2:
            t = p1.val
            p1.val = p2.val
            p2.val = t



    def recoverTree_ref1(self, root):#116ms, 59%
        pre = None
        first = None
        second = None

        # finding the first and second nodes
        tmp = None
        while root:
            # for each node, we compare it with prev node as we did in in-order-traversal
            if pre and root.val < pre.val:
                if first is None:
                    first = pre
                    second = root
                else:
                    second = root

            if root.left: # ---> first left subtree, if not, see else
                # find tmp, which is (the left sub tree's last node) to root (current)
                # we may have visited the left tree before, and connect the rightmost node with curr node (root node)
                tmp = root.left
                while tmp.right is not None and tmp.right != root:
                    tmp = tmp.right
                # the threading already existed
                if tmp.right is None:
                    # if this left tree has not been visited before, then we create a back edge from rightmost node
                    # to curr node, so we can return to the start point after done the left tree
                    # build the threading
                    tmp.right = root
                    # continue to traverse the left sub tree, buiding thread ---> left
                    root = root.left
                else:
                    # thread already there, visit current node, remove threading ---> right
                    # continue to traverse the right sub tree
                    # if this left tree has been visited before, then we are done with it
                    # cut the connection with currNode and start visit curr's right tree
                    tmp.right = None
                    pre = root
                    root = root.right
            else:
                # left child none, means already done with all left subtree, visit current node, traverse right substree
                pre = root
                root = root.right # --> for a node without left child, it's right would be either real child, or parent (thread)

        # swap the value and correct the tree
        if first and second:
            t = first.val
            first.val = second.val
            second.val = t






class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case2(self):
        nums = [0,1]
        answer = [1,0]
        root = TreeNode.generate_bt_from_list(nums)
        self.sol.recoverTree(root)
        compare = TreeNode.compare_tree(root, TreeNode.generate_bt_from_list(answer))
        self.assertTrue(compare)


    def test_case1(self):
        nums = [3,1,2]
        answer = [2,1,3]
        root = TreeNode.generate_bt_from_list(nums)
        self.sol.recoverTree(root)
        compare = TreeNode.compare_tree(root, TreeNode.generate_bt_from_list(answer))
        self.assertTrue(compare)

    def test_case3(self):
        nums = [6,5,8,1,3,7,11,None,None,None,None,None,None,9]
        answer = [6,3,8,1,5,7,11,None,None,None,None,None,None,9]
        root = TreeNode.generate_bt_from_list(nums)
        self.sol.recoverTree(root)
        compare = TreeNode.compare_tree(root, TreeNode.generate_bt_from_list(answer))
        self.assertTrue(compare)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""

Good post for threaded BST.

http://www.cnblogs.com/AnnieKim/archive/2013/06/15/MorrisTraversal.html

=============================================================================

O(n)空间的解法比较直观，中序遍历一遍以后，重新赋值一遍即可，这个解法可以面向n个元素错位的情况。但是对于O(1)空间的解法，最开始的想法是，可以
考虑采用类似最大堆的调正过程的算法，但是这样又可能会破坏树的原有结构。暂未想出来解法。

只能给个O(n)空间的解法。

Updates:  3/16/2013
Searched in the web. Actually, there is a smart solution to travel the tree with two node.
The link is http://discuss.leetcode.com/questions/272/recover-binary-search-tree

Update: 3/21/2013  上一个解法不容易看清楚，添加分析。
O(1)的解法就是
Inorder traverse, keep the previous tree node,
Find first misplaced node by
if ( current.val < prev.val )
   Node first = prev;

Find second by
if ( current.val < prev.val )
   Node second = current;

After traversal, swap the values of first and second node. Only need two pointers, prev and current node. O(1) space.

但是这个解法的前提是Traverse Tree without Stack. 中序遍历如何才能不使用栈。这里就要引入一个概念， Threaded Binary Tree。So, we
first create links to Inorder successor and print the data using these links, and finally revert the changes to restore
original tree.


public class Solution {
    public void recoverTree(TreeNode root) {
	//Morris-traversal

    TreeNode first = null;
    TreeNode second = null;

    TreeNode pred = null; //rightmost node in left tree
    TreeNode prev = null;

    TreeNode curr = root;

    while(curr != null){
        //for each node, we compare it with prev node as we did in in-order-traversal
        if(prev != null && curr.val <= prev.val){
            if(first == null) first = prev;
            second = curr;
        }

        if(curr.left != null){
            //got left tree, then let's locate its rightmost node in left tree
            pred = curr.left;
            //we may have visited the left tree before, and connect the rightmost node with curr node (root node)
            while(pred.right != null && pred.right != curr){
                pred = pred.right;
            }

            if(pred.right == curr){
                //if this left tree has been visited before, then we are done with it
                //cut the connection with currNode and start visit curr's right tree
                pred.right = null;
                prev = curr;
                curr = curr.right;
            }else{
                //if this left tree has not been visited before, then we create a back edge from rightmost node
                // to curr node, so we can return to the start point after done the left tree
                pred.right = curr;
                curr = curr.left;
            }

        }else{
            //no left tree, then just visit its right tree
            prev = curr;
            curr = curr.right;
        }
    }

    int temp = first.val;
    first.val = second.val;
    second.val = temp;
    }
}


"""

#-*- coding:utf-8 -*-
