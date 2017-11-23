#coding=utf-8

import unittest

"""

[lintcode]

689. Two Sum - BST edtion 

Given a binary search tree and a number n, find two numbers in the tree that sums up to n.

 Notice

Without any extra space.

Have you met this question in a real interview? Yes
Example
Given a binary search tree:

    4
   / \
  2   5
 / \
1   3
and a number n = 3
return [1, 2] or [2, 1]

Tags 
Binary Search Tree Google
Related Problems 
Medium Two Sum - Input array is sorted 47 %
Medium Two Sum - Less than or equal to target 38 %
Easy Two Sum


"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: : the root of tree
    @param: : the target sum
    @return: two numbers from tree which sum is n
    """

    def twoSum(self, root, n):
        # write your code here
        if not root:
            return None
        vals = {}
        res = []
        self.helper(root, vals, res, n)
        return res if res else None

    def helper(self, root, vals, res, n):
        if not root:
            return False
        if n - root.val in vals:
            res.append(root.val)
            res.append(n - root.val)
            return True
        vals[root.val] = 1
        return self.helper(root.left, vals, res, n) or \
               self.helper(root.right, vals, res, n)

class Solution_wrong:
    """
    @param: : the root of tree
    @param: : the target sum
    @return: two numbers from tree which sum is n
    
    wrong for the following case:
    
    {9,1,10,#,3,#,#,2,8,#,#,6,#,4,7,#,5}
11
Output
you didn't return two numbers from tree which sum is 11.
[2,9,8,3,10,1]
    
    
    """

    def twoSum(self, root, n):
        # write your code here
        if not root:
            return None
        vals = {}
        res = []
        self.helper(root, vals, res, n)
        return res if res else None

    def helper(self, root, vals, res, n):
        if not root:
            return
        if n - root.val in vals:
            res.append(root.val)
            res.append(n - root.val)
            return
        vals[root.val] = 1
        self.helper(root.left, vals, res, n)
        # wrong here if above already append to res and return, outer recursive call will continue the other part of helper call
        # therefore, need to add some flag for return and stop for the following call if first half is already true.
        self.helper(root.right, vals, res, n)


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = 1
        answer = 1
        result = self.sol.testm(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
