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
    def generate_bt_from_string_standard(bfs_str):
        """
        "20,6,#,#,4"  --> 
        
            20
           /  \
          6   #
         / \
        #  4
        :param bfs_str: 
        :return: 
        """
        if not bfs_str:
            return None
        vals = bfs_str.split(",")
        root = TreeNode(int(vals[0].strip()))
        queue = [root]
        idx, n = 1, len(vals)
        level = []
        left = True
        while queue and idx < n:
            char = vals[idx].strip()
            if char == "#":
                if not left:
                    del queue[0]
            else:       #if vals[idx] != "#":
                tmp = TreeNode(int(char))
                level.append(tmp)
                if left:
                    queue[0].left = tmp
                else:
                    queue[0].right = tmp
                    del queue[0]
            left = not left
            idx += 1
            if not queue:
                queue = level
                level = []
        return root




    @staticmethod
    def generate_bt_from_string(bfs_str):
        """
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1

        :param bfs_str: string like this '5,#,4,8,#,11,null,13,4,#,7,2,null,null,5,1,#',
                        null for no child place, # for tree level separator
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

    @staticmethod
    def generate_bt_from_list(vals):
        """
                5
               / \
              4   8
             /   / \
            11  13  4
           /  \    /
          7    2  5

        :param list: list like this [5,4,8,11,None,13,4,7,2,None,None,None,None,5]
                    Assume all levels are fully listed, None for no child place, unless the last level, can end without
                    completing with trailing None
        :return: root of the tree like above
        """

        if vals is None or len(vals) == 0:
            return None

        root = TreeNode(vals[0])
        parents = [root]
        start = 1
        level = 1
        while start<len(vals):
            # create new level nodes as the children
            end = start + pow(2, level)
            children = []
            for i in range(start, end):
                if i < len(vals):
                    if vals[i] is not None:
                        children.append(TreeNode(vals[i]))
                    else:
                        children.append(None)
            # match the parents and children
            idx = 0
            for p in parents:
                if p is not None:
                    if idx < len(children):
                        p.left = children[idx]
                    else:
                        break
                    if idx+1 < len(children):
                        p.right = children[idx+1]
                else:
                    if idx==0:
                        continue
                idx += 2
            # update for next loop
            parents = children
            level += 1
            start = end
        return root

    @staticmethod
    def get_tree_right_list(root):
        if not root:
            return []
        result = []
        while root:
            result.append(root.val)
            root = root.right
        return result


def test_case1():
    bfs_str = '5,#,4,8,#,11,null,13,4,#,7,2,null,null,5,1,#'
    root = TreeNode.generate_bt_from_string(bfs_str)
    print(root)


def test_case2():
    vals = [5,4,8,11,None,13,4,7,2,None,None,None,None,5]
    root = TreeNode.generate_bt_from_list(vals)
    print(root)

def test1_case3():
    #bfs_str = "20,6,#,#,4"
    #bfs_str = "20,6,1,#,4, 3"
    bfs_str = "20,6,1,#,4, 2,3,41,42,#,#, #, 32"
    root = TreeNode.generate_bt_from_string_standard(bfs_str)
    print(root)


if __name__ == '__main__':
    #test_case1()
    #test_case2()
    test1_case3()











