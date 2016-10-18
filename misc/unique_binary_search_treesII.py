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
    def generateTrees(self, n): # leetcode does not accept correct python answer, change to java form and accepted.
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n <= 0:
            return [] #[None]
        return self.dfs_gen_tree(1, n)

    def dfs_gen_tree(self, start, end):
        if start > end:
            print "Bigger start: ", start, end
            return [None] # need to be [None], not [] here
        if start == end:
            return [TreeNode(start)]
        result = []
        for i in range(start, end+1):
            left_children = self.dfs_gen_tree(start, i-1)
            right_children = self.dfs_gen_tree(i+1, end)
            for lc in left_children:
                for rc in right_children:
                    root = TreeNode(i)
                    root.left = lc
                    root.right =rc
                    result.append(root)
        return result







class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        n = 3
        answer = [[1,None,2,None,3],[1,None,3,2],[2,1,3],[3,1,None,None,2],[3,2,None,1]]
        result = self.sol.generateTrees(n)
        self.assertEqual(answer,len(result))
        #compare = TreeNode.compare_tree(answer, len(result))
        #self.assertTrue(compare)

    def test_case2(self): # ouput [[]], expected []
        n = 0
        answer = []
        result = self.sol.generateTrees(n)
        self.assertEqual(answer, result)

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


######################################################

"""
-- accepted java code
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public List<TreeNode> generateTrees(int n) {
        if(n<=0){
            return new ArrayList<TreeNode>();
        }
        return dfs_gen_tree(1,n);
    }

    public ArrayList<TreeNode> dfs_gen_tree(int start, int end){
        ArrayList<TreeNode> res = new ArrayList<TreeNode>();
        if(start > end){
            res.add(null);
            return res;
        }
        if(start == end){
            TreeNode node = new TreeNode(start);
            res.add(node);
            return res;
        }
        for(int i=start;i<=end;i++){
            ArrayList<TreeNode> left_children = dfs_gen_tree(start, i-1);
            ArrayList<TreeNode> right_children = dfs_gen_tree(i+1, end);
            for (int j = 0; j < left_children.size(); j++){
                 for (int k = 0; k < right_children.size(); k++){
                     TreeNode root = new TreeNode(i);
                     root.left = left_children.get(j);
                     root.right = right_children.get(k);
                     res.add(root);
                 }
             }
        }

        return res;
    }
}
"""