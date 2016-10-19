"""
Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
Subscribe to see which companies asked this question

Hide Tags Tree Depth-first Search
Hide Similar Problems (E) Path Sum (E) Binary Tree Paths


"""

import unittest
from tree_node import TreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        result = []
        path = []
        self.dfs_path_sum(root, sum, path, result)
        return result

    def dfs_path_sum(self, root, sum, path, res):
        if root.left is None and root.right is None:
            if sum == root.val:
                res.append(path+[root.val])
                #print "===> ", res
            return
        if root.left:
            self.dfs_path_sum(root.left, sum - root.val, path + [root.val], res)
        if root.right:
            self.dfs_path_sum(root.right, sum - root.val, path + [root.val], res)

    def dfs_path_sum_wrong(self, root, sum, path, res):
        if root is None:
            # do result here, will cause duplicate path in res, because leaf node will come to null children twice
            # need to revise this part
            if sum == 0:
                res.append(path)
                print "===> ", res
            return
        print "=== ", root.val, sum, path, res
        # path.append(root.val)
        # self.dfs_path_sum(root.left, sum-root.val, path.append(root.val), res)
        # self.dfs_path_sum(root.right, sum-root.val, path.append(root.val), res)
        ## append will change the path , and when do the right rcursive will lead to wrong answer
        self.dfs_path_sum(root.left, sum - root.val, path+[root.val], res)
        self.dfs_path_sum(root.right, sum - root.val, path+[root.val], res)







class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        n = 22
        root = TreeNode.generate_binary_tree("5,#,4,8,#,11,null,13,4,#,7,2,null,null,5,1,#")
        answer = [
           [5,4,11,2],
           [5,8,4,5]
        ]
        result = self.sol.pathSum(root, n)
        self.assertEqual(answer, result)






def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()


################################
"""
saw this code after solving the problem,
code is simpler
http://www.cnblogs.com/zuoyuan/p/3752503.html


class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        def dfs(root, currsum, valuelist):
            if root.left==None and root.right==None:
                if currsum==sum: res.append(valuelist)
            if root.left:
                dfs(root.left, currsum+root.left.val, valuelist+[root.left.val])
            if root.right:
                dfs(root.right, currsum+root.right.val, valuelist+[root.right.val])

        res=[]
        if root==None: return []
        dfs(root, root.val, [root.val])
        return res

"""
