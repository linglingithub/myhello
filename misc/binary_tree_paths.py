__author__ = 'linglin'


"""

257. Binary Tree Paths

Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

Subscribe to see which companies asked this question

Hide Tags Tree Depth-first Search
Hide Similar Problems (M) Path Sum II

Easy


"""

import unittest
from util.tree_node import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param {TreeNode} root the root of the binary tree
    # @return {List[str]} all root-to-leaf paths
    def binaryTreePaths(self, root):
        # Write your code here
        if not root:
            return []
        result = []
        res = []
        self.dfs(root, res, result)
        return result

    def dfs(self, root, res, result):
        res.append(str(root.val))
        if root.left is None and root.right is None:
            result.append("->".join(res))
            # !!! here also need to pop, otherwise wrong
            res.pop()
            return

        if root.left:
            self.dfs(root.left, res, result)
        if root.right:
            self.dfs(root.right, res, result)
        res.pop()

class Solution1:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root): #62ms, 16%
        if root is None:
            return []
        result = []
        self.dfs_btp(root, result, []) #should use array instead of str, in case one value may be multiple digit, eg 15
        return result

    def dfs_btp(self, root, result, tmp):
        if root.left is None and root.right is None:
            result.append("->".join(tmp+[str(root.val)]))
            return
        if root.left:
            self.dfs_btp(root.left, result, tmp+[str(root.val)])
        if root.right:
            self.dfs_btp(root.right, result, tmp+[str(root.val)])

    def binaryTreePaths_ref_dfs(self, root): # 68%
        self.ans = []
        if root is None:
            return self.ans
        def dfs(root, path):
            if root.left is None and root.right is None:
                self.ans += path,
            if root.left:
                dfs(root.left, path + "->" + str(root.left.val))
            if root.right:
                dfs(root.right, path + "->" + str(root.right.val))
        dfs(root, str(root.val))
        return self.ans

    def binaryTreePaths_ref2(self, root):
        if not root:
            return []
        return [str(root.val) + '->' + path
                for kid in (root.left, root.right) if kid
                for path in self.binaryTreePaths(kid)] or [str(root.val)]


    def binaryTreePaths_ref_bfs(self, root): # 68%
        from collections import deque
        if root is None:
            return []
        queue = deque( [ [root, str(root.val)] ] )
        ans = []
        while queue:
            front, path = queue.popleft()
            if front.left is None and front.right is None:
                ans += path,
                continue
            if front.left:
                queue += [front.left, path + "->" + str(front.left.val)],
            if front.right:
                queue += [front.right, path + "->" + str(front.right.val)],
        return ans






class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,2,3,None, 5]
        answer = ["1->2->5", "1->3"]
        result = self.sol.binaryTreePaths(TreeNode.generate_bt_from_list(nums))
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8