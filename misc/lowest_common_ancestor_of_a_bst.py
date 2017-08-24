#coding=utf-8

import unittest

"""

235. Lowest Common Ancestor of a Binary Search Tree

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and 
w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of
 itself).”

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 
4 is 2, since a node can be a descendant of itself according to the LCA definition.

Seen this question in a real interview before?   Yes  

Related Topics 
Tree 
Similar Questions 
Lowest Common Ancestor of a Binary Tree 

"""



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        Basic way is to dfs the tree and find p and q, then compare the paths of p and q and find out the LCA.
        But in a BST, anything else to exploit to make it more efficient?
        NOTE that given a root, all smaller numbers in left sub-tree and all bigger ones in right-subtree.
        If, for example, p.val < root.val and q.val > root.val, then the paths split, current root will be
        the LCA! If both are smaller or both are bigger, then choose one sub-tree and continue to check.
        Remember to Think about when p may be LCA of p and q.
        
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or not p or not q:
            return None
        while root and (root.val-p.val) * (root.val-q.val) > 0:  # simplified code, exit when < (differnt subtree) or = (LCA is one of them)
            root = root.left if root.val>p.val else root.right
        return root




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



#-*- coding:utf-8 -*-

"""

Just walk down from the whole tree's root as long as both p and q are in the same subtree (meaning their values 
are both smaller or both larger than root's). This walks straight from the root to the LCA, not looking at the 
rest of the tree, so it's pretty much as fast as it gets. A few ways to do it:

Iterative, O(1) space

Python

def lowestCommonAncestor(self, root, p, q):
    while (root.val - p.val) * (root.val - q.val) > 0:
        root = (root.left, root.right)[p.val > root.val]
    return root
Java

public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
    while ((root.val - p.val) * (root.val - q.val) > 0)
        root = p.val < root.val ? root.left : root.right;
    return root;
}
(in case of overflow, I'd do (root.val - (long)p.val) * (root.val - (long)q.val))

Different Python

def lowestCommonAncestor(self, root, p, q):
    a, b = sorted([p.val, q.val])
    while not a <= root.val <= b:
        root = (root.left, root.right)[a > root.val]
    return root
"Long" Python, maybe easiest to understand

def lowestCommonAncestor(self, root, p, q):
    while root:
        if p.val < root.val > q.val:
            root = root.left
        elif p.val > root.val < q.val:
            root = root.right
        else:
            return root
Recursive

Python

def lowestCommonAncestor(self, root, p, q):
    next = p.val < root.val > q.val and root.left or \
           p.val > root.val < q.val and root.right
    return self.lowestCommonAncestor(next, p, q) if next else root
Python One-Liner

def lowestCommonAncestor(self, root, p, q):
    return root if (root.val - p.val) * (root.val - q.val) < 1 else \
           self.lowestCommonAncestor((root.left, root.right)[p.val > root.val], p, q)
Java One-Liner

public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
    return (root.val - p.val) * (root.val - q.val) < 1 ? root :
           lowestCommonAncestor(p.val < root.val ? root.left : root.right, p, q);
}
"Long" Python, maybe easiest to understand

def lowestCommonAncestor(self, root, p, q):
    if p.val < root.val > q.val:
        return self.lowestCommonAncestor(root.left, p, q)
    if p.val > root.val < q.val:
        return self.lowestCommonAncestor(root.right, p, q)
    return root


"""