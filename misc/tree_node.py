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


    @staticmethod
    def generate_binary_tree(bfs_str):
        """
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1

        :param bfs_str: string like this '5,#,4,8,#,11,null,13,4,#,7,2,null,null,5,1,#',
                        null for no child place, # for tree level seperator
        :return: root of the tree like above
        """
        vals = bfs_str.split(",")
        root = TreeNode(int(vals[0]))
        if len(vals) <= 2:
            return root
        parent_ref = [root]
        level_ref = []
        left = True
        for i in range(2, len(vals)):
            tmp = vals[i]
            if tmp == '#':
                parent_ref = level_ref
                level_ref = []
                left = True
                continue
            if tmp == 'null' or tmp == 'None':
                node = None
            else:
                node = TreeNode(int(tmp))
            level_ref.append(node)

            # start to assign the current node as child to parent node
            while parent_ref[0] is None:
                del parent_ref[0]
            if left:
                parent_ref[0].left = node
                left = False
            else:
                parent_ref[0].right = node
                left = True
                del parent_ref[0]
        return root


if __name__ == '__main__':
    bfs_str = '5,#,4,8,#,11,null,13,4,#,7,2,null,null,5,1,#'
    root = TreeNode.generate_binary_tree(bfs_str)
    print root










