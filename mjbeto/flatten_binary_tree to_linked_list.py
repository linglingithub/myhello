#coding=utf-8

import unittest
from util.tree_node import TreeNode

"""
Flatten a binary tree to a fake "linked list" in pre-order traversal.

Here we use the right pointer in TreeNode as the next pointer in ListNode.

 Notice

Don't forget to mark the left child of each node to null. Or you will get Time Limit Exceeded or Memory Limit Exceeded.

Have you met this question in a real interview? Yes
Example
              1
               \
     1          2
    / \          \
   2   5    =>    3
  / \   \          \
 3   4   6          4
                     \
                      5
                       \
                        6
Challenge 
Do it in-place without any extra memory.

Tags 
Binary Tree Depth First Search
Related Problems 
Medium Flatten 2D Vector 46 %
Medium Flatten Nested List Iterator 27 %
Medium Convert Binary Search Tree to Doubly Linked List 29 %
Medium Convert Sorted List to Balanced BST


"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:  # 29% cases passed, locally : RuntimeError: maximum recursion depth exceeded
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def flatten(self, root):
        # write your code here
        if not root:
            return None
        self.pre_dfs(root)

    def pre_dfs(self, root):
        if not root:
            return None, None
        right = root.right
        tail = root
        if root.left:
            lhead, ltail = self.pre_dfs(root.left)
            root.right = lhead
            ltail.right = right
            tail = ltail
            root.left = None
        if right:
            # rhead, rtail = self.pre_dfs(root.right)  # wrong to say root.right here, already modified, should be right
            rhead, rtail = self.pre_dfs(right)
            tail.right = rhead
            tail = rtail
        return root, tail


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case2(self):
        nums = [1,2]
        root = TreeNode.generate_bt_from_list(nums)
        answer = [1,2]
        self.sol.flatten(root)
        result = TreeNode.get_tree_right_list(root)
        self.assertEqual(answer, result)

    def test_case1(self):
        nums = [1,2,5,3,4,None, 6]
        root = TreeNode.generate_bt_from_list(nums)
        answer = [1,2,3,4,5,6]
        self.sol.flatten(root)
        result = TreeNode.get_tree_right_list(root)
        self.assertEqual(answer, result)


    def test_case11(self):  #===>
        nums = "98,97,#,88,#,84,#,79,87,64,#,#,#,63,69,62,#,#,#,30,#,27,59,9,#,#,#,3,#,0,#,-4,#,-16,#,-18,-7,-19,#,#,#,-23,#,-34,#,-42,#,-59,#,-63,#,-64,#,-69,#,-75,#,-81"
        answer = "98,#,97,#,88,#,84,#,79,#,64,#,63,#,62,#,30,#,27,#,9,#,3,#,0,#,-4,#,-16,#,-18,#,-19,#,-23,#,-34,#,-42,#,-59,#,-63,#,-64,#,-69,#,-75,#,-81,#,-7,#,59,#,69,#,87"
        from util.tree_node import TreeNode
        root = TreeNode.generate_bt_from_string_standard(nums)
        answer_tree = TreeNode.generate_bt_from_string_standard(answer)
        self.sol.flatten(root)
        compare = TreeNode.compare_tree(root, answer_tree)
        self.assertTrue(compare)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
