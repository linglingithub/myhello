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
    def flatten_ref(self, root): # ref, use stack, step into and try to understand how it works
        """
        Impression is that the current node 's right will be the stack top element.
        :param root: 
        :return: 
        """
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node.left = None
            if stack:
                node.right = stack[-1]
            else:
                node.right = None


    def flatten2(self, root):   # ref jiuzhang idea
        # write your code here
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        cur = root.left
        if cur:
            # while cur.left:  #wrong, already flatten, should be right
            #     cur = cur.left
            while cur.right:
                cur = cur.right
            cur.right = root.right
            root.right = root.left
            root.left = None


    def flatten1(self, root):
        # write your code here
        if not root:
            return
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

"""

jiuzhang answer: 


class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def flatten(self, root):
        # write your code here
        if root == None:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        p = root
        if p.left == None:
            return
        p = p.left
        while p.right:
            p = p.right
        p.right = root.right
        root.right = root.left
        root.left = None


====================================================================================

jiuzhang Java version

 /**
  * 本代码由九章算法编辑提供。版权所有，转发请注明出处。
  * - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
  * - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，Big Data 项目实战班，
  * - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
  */ 

// Version 1: Traverse
public class Solution {
    private TreeNode lastNode = null;

    public void flatten(TreeNode root) {
        if (root == null) {
            return;
        }

        if (lastNode != null) {
            lastNode.left = null;
            lastNode.right = root;
        }

        lastNode = root;
        TreeNode right = root.right;
        flatten(root.left);
        flatten(right);
    }
}

// version 2: Divide & Conquer
public class Solution {
    /**
     * @param root: a TreeNode, the root of the binary tree
     * @return: nothing
     */
    public void flatten(TreeNode root) {
        helper(root);
    }
    
    // flatten root and return the last node
    private TreeNode helper(TreeNode root) {
        if (root == null) {
            return null;
        }
        
        TreeNode leftLast = helper(root.left);
        TreeNode rightLast = helper(root.right);
        
        // connect leftLast to root.right
        if (leftLast != null) {
            leftLast.right = root.right;
            root.right = root.left;
            root.left = null;
        }
        
        if (rightLast != null) {
            return rightLast;
        }
        
        if (leftLast != null) {
            return leftLast;
        }
        
        return root;
    }
}

// version 3: Non-Recursion
/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */
public class Solution {
    /**
     * @param root: a TreeNode, the root of the binary tree
     * @return: nothing
     */
    public void flatten(TreeNode root) {
        if (root == null) {
            return;
        }
        
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        
        while (!stack.empty()) {
            TreeNode node = stack.pop();
            if (node.right != null) {
                stack.push(node.right);
            }
            if (node.left != null) {
                stack.push(node.left);
            }
            
            // connect 
            node.left = null;
            if (stack.empty()) {
                node.right = null;
            } else {
                node.right = stack.peek();
            }
        }
    }
}




"""




