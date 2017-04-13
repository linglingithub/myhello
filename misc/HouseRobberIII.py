#coding=utf-8


import unittest

"""

337. House Robber III

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the
"root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that
"all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses
 were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
     3
    / \
   2   3
    \   \
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
     3
    / \
   4   5
  / \   \
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.
Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.

Subscribe to see which companies asked this question.

Hide Tags Tree Depth-first Search
Hide Similar Problems (E) House Robber (M) House Robber II


Medium

"""



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from util.tree_node import TreeNode

class Solution(object):

    def rob(self, root): # idea same as rob1, rewrite code,  88ms, 55%; 500 + ms on lint
        money = {}
        def solve(root):
            if not root:
                return 0
            if root not in money:
                left, right = root.left, root.right
                ll = lr = rl = rr = None
                if left:
                    ll, lr = left.left, left.right
                if right:
                    rl, rr = right.left, right.right
                skipit = solve(left) + solve(right)
                robit = root.val + solve(ll) + solve(lr) + solve(rl) + solve(rr)
                money[root] = max(robit, skipit)
            return money[root]
        return solve(root)

    def rob1(self, root): #145ms, 6%; 92ms, 42%; 649ms / 510ms / 800+ms on lint
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.money = {}
        self.rob_dp(root)
        return self.money[root]

    def rob_dp(self, root):
        if not root:
            return 0
        if root in self.money:
            return self.money[root]
        rob_this = root.val
        if root.left:
            rob_this += self.rob_dp(root.left.left) + self.rob_dp(root.left.right)
        if root.right:
            rob_this += self.rob_dp(root.right.left) + self.rob_dp(root.right.right)
        skip_this = self.rob_dp(root.left) + self.rob_dp(root.right)
        self.money[root] = max(rob_this, skip_this)
        return self.money[root]




    def rob_TLE(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.rob_helper(root, True), self.rob_helper(root, False))

    def rob_helper(self, root, robThis):
        if not root:
            return 0
        if robThis:
            return root.val + self.rob_helper(root.left, False) + self.rob_helper(root.right, False)
        else:
            #return self.rob_helper(root.left, True) + self.rob_helper(root.right, True) # can't say for sure to rob left or right, case 4, 5
            return max(self.rob_helper(root.left, True), self.rob_helper(root.left, False)) + max(self.rob_helper(root.right, True), self.rob_helper(root.right, False))


    def rob_ref(self, root): #115ms, 19%; 89ms, 49%; 512ms on lint
        rob, not_rob = self.visit(root)
        return max(rob, not_rob)

    def visit(self, root):
        if root is None:
            return 0, 0

        left_rob, left_not_rob = self.visit(root.left)
        right_rob, right_not_rob = self.visit(root.right)

        rob = root.val + left_not_rob + right_not_rob
        not_rob = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)
        return rob, not_rob



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [3,2,3,None,3,None,1]
        root = TreeNode.generate_bt_from_list(nums)
        answer = 7
        result = self.sol.rob(root)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [3,4,5,1,3,None,1]
        root = TreeNode.generate_bt_from_list(nums)
        answer = 9
        result = self.sol.rob(root)
        self.assertEqual(answer, result)

    def test_case3(self):
        nums = [0,0]
        root = TreeNode.generate_bt_from_list(nums)
        answer = 0
        result = self.sol.rob(root)
        self.assertEqual(answer, result)

    def test_case4(self):  # not necessarily rob by level, see this case, can skip the level
        nums = [4,1,None,2,None,None,None,3]
        root = TreeNode.generate_bt_from_list(nums)
        answer = 7
        result = self.sol.rob(root)
        self.assertEqual(answer, result)

    def test_case5(self): # siblings can be one robbed and the other not.
        nums = [1,2,3,5,4]
        root = TreeNode.generate_bt_from_list(nums)
        answer = 12
        result = self.sol.rob(root)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



