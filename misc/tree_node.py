# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


    @staticmethod
    def compare_tree(r1, r2):
        if r1 is None and r2 is None:
            return True
        if r1 is not None and r2 is not None and r1.val == r2.val:
            return TreeNode.compare_tree(r1.left, r2.left) and TreeNode.compare_tree(r1.right, r2.right)
        else:
            return False