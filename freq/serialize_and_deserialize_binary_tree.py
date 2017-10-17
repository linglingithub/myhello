#coding=utf-8

import unittest

"""
297. Serialize and Deserialize Binary Tree
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored 
in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or 
another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your 
serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a 
string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to 
follow this format, so please be creative and come up with different approaches yourself.
Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should 
be stateless.

Credits:
Special thanks to @Louis1992 for adding this problem and creating all test cases.

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    LABEL_NONE = "#"
    SPLITTER = ","

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        self.recur_serialize(root, res)
        return ",".join(res)

    def recur_serialize(self, root, res):
        if not root:
            res.append(self.LABEL_NONE)
            return
        res.append(str(root.val))
        self.recur_serialize(root.left, res)
        self.recur_serialize(root.right, res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(self.SPLITTER)
        root = self.recur_deserialize(vals)
        return root

    def recur_deserialize(self, data):
        if not data:
            return None
        tmp = data.pop(0)
        if tmp == self.LABEL_NONE:
            return None
        node = TreeNode(int(tmp))
        node.left = self.recur_deserialize(data)
        node.right = self.recur_deserialize(data)
        return node


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


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
