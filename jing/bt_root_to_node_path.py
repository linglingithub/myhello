from util.tree_node import TreeNode

def find_path(root, target_val):
    result = []
    helper(root, target_val, result)
    return result

def helper(root, target_val, result):
    if not root:
        return False
    result.append(root)  # should be ahead of check val
    if root.val == target_val:
        return True
    if helper(root.left, target_val, result) or helper(root.right, target_val, result):
        return True
    else:
        result.pop()
        return False


        """
                5
               / \
              4   8
             /   / \
            11  13  14
           /  \    /
          7    2  15

        :param list: list like this [5,4,8,11,None,13,14,7,2,None,None,None,None,15]
        """
vals = [5,4,8,11,None,13,14,7,2,None,None,None,None,15]
root = TreeNode.generate_bt_from_list(vals)
path = find_path(root, 2)
for node in path:
    print(node.val)
