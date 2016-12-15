#-*- coding:utf-8 -*-
#coding=utf-8

"""
124. Binary Tree Maximum Path Sum

Given a binary tree, find the maximum path sum.
The path may start and end at any node in the tree.
For example, given the below binary tree

       1
      / \
     2   3
the result is 6.

Subscribe to see which companies asked this question

Hide Tags Tree Depth-first Search
Hide Similar Problems (E) Path Sum (M) Sum Root to Leaf Numbers
Difficulty: Hard

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
    def maxPathSum(self, root): # 142ms, 93.03%
        """
        :type root: TreeNode
        :rtype: int
        """
        result = [None]#result = [0]
        self.dfs_path_sum(result, root)
        return result[0]

    def dfs_path_sum(self, result, root):
        if root is None:
            return 0
        left_sum = self.dfs_path_sum(result, root.left)
        right_sum = self.dfs_path_sum(result, root.right)
        # max_sum = max(left_sum + root.val, right_sum + root.val, root.val + left_sum + right_sum, root.val)
        sub_max = max(left_sum+root.val, right_sum+root.val, root.val)
        result[0] = max(result[0], sub_max, left_sum+right_sum+root.val)
        # return max_sum  # don't forget to return this for the recursive call, but should not be max_sum, because if you
        # want to call recursively, then it should not contain case of root.val+left_sum+right_sum as the sub_sum
        # otherwise wrong for case3
        return sub_max





    def maxPathSum_ref(self, root): #152ms, 89.55%
        self.ans = None
        def search(root):
            if root is None:
                return 0
            leftMax = search(root.left)
            rightMax = search(root.right)
            self.ans = max(max(leftMax, 0) + max(rightMax, 0) + root.val, self.ans)
            return max(leftMax, rightMax, 0) + root.val
        search(root)
        return self.ans




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        root = TreeNode.generate_bt_from_string('1,#,2,3,#')
        answer = 6
        result = self.sol.maxPathSum(root)
        self.assertEqual(answer, result)

    def test_case2(self): # ===> this case means that node value can be negative, and the purpose is to search a single path
        root = TreeNode.generate_bt_from_string('2,#,-1,null,#')
        answer = 2
        result = self.sol.maxPathSum(root)
        self.assertEqual(answer, result)

    def test_case3(self):  # ===>
        root = TreeNode.generate_bt_from_list([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
        answer = 49
        result = self.sol.maxPathSum(root)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""
For each node there can be four ways that the max path goes through the node:
1 Node only
2 Max path through Left Child + Node
3 Max path through Right Child + Node
4 Max path through Left Child + Node + Max path through Right Child

The idea is to keep trace of four paths and pick up the max one in the end. An important thing to note is, root of
every subtree need to return maximum path sum such that at most one child of root is involved. This is needed for
parent function call. In below code, this sum is stored in 'max_single' and returned by the recursive function.
"""

"""
解题思路：这道题是在树中寻找一条路径，这条路径上的节点的和为最大，起点和终点只要是树里面的节点就可以了。这里需要注意的一点是：节点值有可能为
负值。
解决这道二叉树的题目还是来使用递归。例如下面这棵树：

　　　　　　　　　　　　   1

　　　　　　　 　　　   /     \

　　　　　　　　  　　 2        3

    　　　　　　　　/    \    /    \

　　　　　　　　　  4     5   6     7

对于这棵树而言，和为最大的路径为：5->2->1->3->7。

那么这条路径是怎么求出来的呢？这里需要用到一个全局变量Solution.max，可以随时被更大的路径和替换掉。
在函数递归到左子树时：最大的路径为：4->2->5。但此时函数的返回值应当为4->2和5->2这两条路径中和最大的一条。右子树同理。
而Solution.max用来监控每个子树中的最大路径和。那么思路就是：（左子树中的最大路径和，右子树中的最大路径和，以及左子树中以root.left为起点
的最大路径（需要大于零）+右子树中以root.right为起点的最大路径（需要大于零）+root.val），这三者中的最大值就是最大的路径和。

"""