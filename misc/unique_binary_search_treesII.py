__author__='linglin'

""""
Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.
For example,
Given n = 3, your program should return all 5 unique BST's shown below.
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
confused what "{1,#,2,3}" means?

Subscribe to see which companies asked this question

Hide Tags Tree Dynamic Programming
Hide Similar Problems (M) Unique Binary Search Trees (M) Different Ways to Add Parentheses



"""

from tree_node import TreeNode
import unittest


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        n = 3
        answer = TreeNode("a")
        answer.left = TreeNode("b")
        answer.right = TreeNode("c")
        result = self.sol.generateTrees(n)
        compare = TreeNode.compare_tree(answer, result)
        self.assertTrue(compare)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()

#####################################################

class Solution_Old:
    # @return a list of tree node
    def dfs(self, start, end):
        if start > end: return [None]
        res = []
        for rootval in range(start, end+1):

            LeftTree = self.dfs(start, rootval-1)
            RightTree = self.dfs(rootval+1, end)
            for i in LeftTree:

                for j in RightTree:

                    root = TreeNode(rootval)
                    root.left = i
                    root.right = j
                    res.append(root)
        return res
    def generateTrees(self, n):
        return self.dfs(1, n)


# if __name__ == '__main__':
#     sol = Solution()
#     a = sol.generateTrees(3)
#     print a
