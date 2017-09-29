#coding=utf-8

import unittest

"""

230. Kth Smallest Element in a BST

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would
 you optimize the kthSmallest routine?

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

Difficulty:Medium
Total Accepted:111K
Total Submissions:251.5K
Contributor: LeetCode
Subscribe to see which companies asked this question.

Related Topics 
Binary Search Tree 
Similar Questions 
Binary Tree Inorder Traversal Second Minimum Node In a Binary Tree 

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.cnt = 0
        self.k = k
        self.result = -1
        self.traverse(root)
        return self.result

    def traverse(self, root):  # compare with the wrong one, only difference is when to update self.result and check k
        if root.left:
            self.traverse(root.left)

        self.cnt += 1
        if self.cnt == self.k:
            self.result = root.val
            return

        if root.right:
            self.traverse(root.right)

    def traverse_wrong(self, root):
        if root.left:
            self.traverse(root.left)

        # can't do this way, should update cnt first, then check. otherwise, left child cnt will be checked twice
        # step into case 1
        if self.cnt == self.k - 1:
            self.result = root.val
            return
        self.cnt += 1  # don't forget this one, otherwise wrong
        if root.right:
            self.traverse(root.right)

    def kthSmallest_3_recursivenotgoodlooking(self, root, k):  # recursive way
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        nodes = []
        self.traverse(root.left, nodes)
        if len(nodes) == k - 1:
            return root.val
        elif len(nodes) < k - 1:
            nodes.append(root)
            self.traverse(root.right, nodes)
            return nodes[k - 1].val   # need this return here, other wise None result error
        else:
            return nodes[k - 1].val

    def traverse1(self, root, nodes):
        if not root:
            return
        self.traverse(root.left, nodes)
        nodes.append(root)
        self.traverse(root.right, nodes)

    def kthSmallest2(self, root, k): # iter way, 13% ~ 81%
        """
        time complexity: 
        
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        p = root
        stack = []
        cnt = 0
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            if stack:
                p = stack.pop()
                cnt += 1
                if cnt == k:
                    return p.val
                p = p.right
        return -1

    def kthSmallest1(self, root, k):  # binary search, 65% ,
        """
        Time complexity:
        if k bigger than (n/2) and suppose this is a balanced tree:
         O(n/2) + O(n/4) +... untile some point it is the kth, so it's O(n)
        
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        lcnt = self.get_count(root.left)
        if lcnt == k - 1:
            return root.val
        elif lcnt > k - 1:   # should be > not < here !!!
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k - lcnt - 1)

    def get_count(self, root):
        if not root:
            return 0
        lcnt = self.get_count(root.left)
        rcnt = self.get_count(root.right)
        return lcnt + rcnt + 1


from util.tree_node import TreeNode
class SolutionTester(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,None,2]
        k = 2
        root = TreeNode.generate_bt_from_list(nums)
        answer = 2
        result = self.sol.kthSmallest(root, k)
        self.assertEqual(answer, result)

    def test_case02(self):
        nums = [2,1]
        k = 1
        root = TreeNode.generate_bt_from_list(nums)
        answer = 1
        result = self.sol.kthSmallest(root, k)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""

https://discuss.leetcode.com/topic/17810/3-ways-implemented-in-java-python-binary-search-in-order-iterative-recursive

====================================

最简单的办法，中序遍历，即可以得到递增序列，从而可以找到第k大的元素。时间复杂度O(k)。
如果能够修改节点的数据结构TreeNode，可以增加一个字段leftCnt，表示左子树的节点个数。设当前节点为root，
若 k == root.leftCnt+1, 则返回root
若 k > node.leftCnt, 则 k -= root.leftCnt+1, root=root.right
否则，node = node.left
算法复杂度为O(height of BST)。

====================================

If we could add a count field in the BST node class, it will take O(n) time when we calculate the count value for the 
whole tree, but after that, it will take O(logn) time when insert/delete a node or calculate the kth smallest element.

====================================

In a BST, the left subtree of node T contains only elements smaller than the value stored in T. If k is smaller than the number of elements in the left subtree, the kth smallest element must belong to the left subtree. Otherwise, if k is larger, then the kth smallest element is in the right subtree.

We can augment the BST to have each node in it store the number of elements in its left subtree (assume that the left subtree of a given node includes that node). With this piece of information, it is simple to traverse the tree by repeatedly asking for the number of elements in the left subtree, to decide whether to do recurse into the left or right subtree.

Now, suppose we are at node T:

If k == num_elements(left subtree of T), then the answer we're looking for is the value in node T.
If k > num_elements(left subtree of T), then obviously we can ignore the left subtree, because those elements will also be smaller than the kth smallest. So, we reduce the problem to finding the k - num_elements(left subtree of T) smallest element of the right subtree.
If k < num_elements(left subtree of T), then the kth smallest is somewhere in the left subtree, so we reduce the problem to finding the kth smallest element in the left subtree.
Complexity analysis:

This takes O(depth of node) time, which is O(log n) in the worst case on a balanced BST, or O(log n) on average for a random BST.

A BST requires O(n) storage, and it takes another O(n) to store the information about the number of elements. All BST operations take O(depth of node) time, and it takes O(depth of node) extra time to maintain the "number of elements" information for insertion, deletion or rotation of nodes. Therefore, storing information about the number of elements in the left subtree keeps the space and time complexity of a BST.
"""

#-*- coding:utf-8 -*-
