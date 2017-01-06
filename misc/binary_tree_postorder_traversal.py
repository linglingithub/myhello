#coding=utf-8
"""
145. Binary Tree Postorder Traversal

Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?

Subscribe to see which companies asked this question

Hide Tags Tree Stack
Hide Similar Problems (M) Binary Tree Inorder Traversal

Hard

"""


import unittest
from util.tree_node import TreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root): #45ms, 38%
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = []
        result = []
        current = root
        both_dict = {}
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                tmp = stack[-1]
                if tmp not in both_dict:
                    current = tmp.right
                    both_dict[tmp] = True
                else:
                    result.append(tmp.val)
                    stack.pop()
        return result



    def postorderTraversal_recursive(self, root): #42ms, 46%
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        result = []
        self.recur_postorder(root, result)
        return result

    def recur_postorder(self, root, result):
        if root is None:
            return
        self.recur_postorder(root.left, result)
        self.recur_postorder(root.right, result)
        result.append(root.val)


    def postorderTraversal_ref(self, root): #43ms, 45%
        """
        For _ref and _ref1, please see the bottom comments for details.
        :param root:
        :return:
        """
        if root is None:
            return []
        stack = [root]
        ans = []
        while stack:
            top = stack.pop()
            ans.append(top.val)
            if top.left:
                stack.append(top.left)
            if top.right:
                stack.append(top.right)
        return ans[::-1]

    def postorderTraversal_ref2(self, root): #55ms, 17%
        if root is None:
            return []
        stack = [root]
        ans = []
        pre = None
        while stack:
            cur = stack[-1]
            if pre is None or pre.left == cur or pre.right == cur:
                if cur.left:
                    stack.append(cur.left)
                elif cur.right:
                    stack.append(cur.right)
            elif pre == cur.left and cur.right:
                stack.append(cur.right)
            else:
                ans.append(cur.val)
                stack.pop()
            pre = cur
        return ans


    def postorderTraversal_ref3(self, root): #38ms, 73%
        """
        这道题的迭代求解比先序遍历和后序遍历要麻烦一些。假设一棵树是这样的：

　　　　　　　　　　　　　　　　　　　　　　　　1

　　　　　　　　　　　　　　　　　　　　　　　/　　\

　　　　　　　　　　　　　　　　　　　　　　2　　　　3

　　　　　　　　　　　　　　　　　　　　　　　　　　/　\

　　　　　　　　　　　　　　　　　　　　　　　　　 4　　5

　　　　　使用一个栈。分几个步骤：

　　　　　一，将根节点入栈，并将根节点的孩子入栈，入栈顺序为：先入右孩子，再入左孩子，顺序不能错。因为这样在弹栈时的顺序就是后序遍历的顺序了
        。如果左孩子还有左孩子或者右孩子，那么继续按先右后左的顺序入栈。那么上面这棵树开始的入栈顺序是：1，3，2。由于2不存在左右孩子，停止
        入栈。

　　　　   二，由于2没有左右孩子，遍历2并将2弹出，同时使用prev记录下2这个节点。

　　　　   三，2出栈后，栈为{1，3}，此时3在栈顶，由于3存在左右孩子，按顺序入栈，此时栈为{1，3，5，4}。

　　　　   四，将4和5遍历并出栈，此时prev指向5，栈为{1，3}。prev的作用是什么呢？用来判断prev是否为栈顶元素的孩子，如果是，则说明子树的孩
        子已经遍历完成，需要遍历树根了。以上树为例：4和5出栈后，prev指向5，而5是栈顶元素3的孩子，说明孩子已经遍历完毕，则遍历3然后弹出3即
        可，即完成了子树{3，4，5}的后序遍历。

　　　　   五，此时栈为{1}，为树根，而左右子树都遍历完了，最后遍历树根并弹出即可。


        :param root:
        :return:
        """
        list = []
        self.iterative_postorder(root,list)
        return list

    def iterative_postorder(self, root, list):
        stack = []
        pre = None
        if root:
            stack.append(root)
            while stack:
                curr = stack[len(stack) - 1]
                if (curr.left == None and curr.right == None) or (pre and (pre == curr.left or pre == curr.right)):
                    list.append(curr.val)
                    stack.pop()
                    pre = curr
                else:
                    if curr.right: stack.append(curr.right)
                    if curr.left: stack.append(curr.left)
        return list


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case2(self): #====>
        nums = [3,1,2]
        answer = [1,2,3]
        result = self.sol.postorderTraversal(TreeNode.generate_bt_from_list(nums))
        self.assertEqual(answer, result)

    def test_case1(self):
        nums = [1,None, 2,3]
        answer = [3,2,1]
        result = self.sol.postorderTraversal(TreeNode.generate_bt_from_list(nums))
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()


"""
http://bookshadow.com/weblog/2015/01/19/binary-tree-post-order-traversal/

二叉树的后序遍历很容易采用递归方式实现：

void postOrderTraversal(BinaryTree *p) {
  if (!p) return;
  postOrderTraversal(p->left);
  postOrderTraversal(p->right);
  cout << p->data;
}
1
2
3
4
5
6
后序遍历是二叉树三种遍历的非递归算法中最难实现的一种，在做这道题目之前可以首先尝试一下这一题，因为它相对简单一些：Binary Search Tree In-Order Traversal Iterative Solution。

三种遍历的非递归实现中最容易的是先序遍历。

后序遍历是一种非常有用的树操作，例如它可以被用于下面的场景：

树的删除。为了释放树结构的内存，某节点在被释放以前，其左右子树的节点首先应当被释放掉。
后缀表示法（逆波兰表示法）
如果在遍历树时维护一个visited标记，问题可以比较直观地解决。在此不详细讨论该方法，可以参阅Wikipedia的描述：Tree Traversal。

iterativePostorder(node)
  parentStack = empty stack
  lastnodevisited = null
  while (not parentStack.isEmpty() or node ≠ null)
    if (node ≠ null)
      parentStack.push(node)
      node = node.left
    else
      peeknode = parentStack.peek()
      if (peeknode.right ≠ null and lastnodevisited ≠ peeknode.right)
        /* if right child exists AND traversing node from left child, move right */
        node = peeknode.right
      else
        visit(peeknode)
        lastnodevisited = parentStack.pop()
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
在此我们讨论一种不使用visited标记的算法，看起来比较有挑战性。

提示：
通常情况下，如果树节点中没有指向父节点的指针，就必须借助于栈（Stack）实现遍历。试着想象一下二叉树的遍历过程。什么时候应该输出节点的值？留意在什么条件下会向上/向下遍历树。使用一个变量记录上一次访问的节点，这个辅助节点有什么用处？

Post-order traversal sequence

Post-order traversal sequence: A, C, E, D, B, H, I, G, F
解决方案：
我们使用prev变量跟踪上一次访问的节点。假设栈顶元素是curr。当prev是curr的父节点时，我们正在向下遍历树。此时，优先遍历curr的左孩子（将左孩子压入栈）。如果没有左孩子，再看右孩子。如果左右孩子都不存在（curr是叶节点），就输出curr的值并弹出栈顶元素。

如果prev是curr的左孩子，我们正在从左子树向上遍历。我们看一下curr的右孩子。如果可以，就从右孩子向下遍历（将右孩子压入栈），否则打印curr的值并弹出栈顶元素。

如果prev是curr的右孩子，我们正在从右子树向上遍历。打印curr的值并弹出栈顶元素。

void postOrderTraversalIterative(BinaryTree *root) {
  if (!root) return;
  stack<BinaryTree*> s;
  s.push(root);
  BinaryTree *prev = NULL;
  while (!s.empty()) {
    BinaryTree *curr= s.top();
    // we are traversing down the tree
    if (!prev || prev->left == curr|| prev->right == curr) {
      if (curr->left) {
        s.push(curr->left);
      } else if (curr->right) {
        s.push(curr->right);
      } else {
        cout << curr->data << " ";
        s.pop();
      }
    }
    // we are traversing up the tree from the left
    else if (curr->left == prev) {
      if (curr->right) {
        s.push(curr->right);
      } else {
        cout << curr->data << " ";
        s.pop();
      }
    }
    // we are traversing up the tree from the right
    else if (curr->right == prev) {
      cout << curr->data << " ";
      s.pop();
    }
    prev = curr;  // record previously traversed node
  }
}
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
上面的代码比较容易理解，但是包含冗余代码。我们可以对代码进行重构，使之更加简洁。观察一下curr值的打印代码是怎样重构成单个else块的。不用担心迭代时会漏掉curr的打印过程，因为它可以确保在下一次迭代时一定会进入else分支。

void postOrderTraversalIterative(BinaryTree *root) {
  if (!root) return;
  stack<BinaryTree*> s;
  s.push(root);
  BinaryTree *prev = NULL;
  while (!s.empty()) {
    BinaryTree *curr= s.top();
    if (!prev || prev->left == curr|| prev->right == curr) {
      if (curr->left)
        s.push(curr->left);
      else if (curr->right)
        s.push(curr->right);
    } else if (curr->left == prev) {
      if (curr->right)
        s.push(curr->right);
    } else {
      cout << curr->data << " ";
      s.pop();
    }
    prev = curr;
  }
}
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
另一种解法：
另一种解法是使用两个栈。试着在纸上写一下代码。我认为这种解法非常的神奇而优美。你可能觉得这很不可思议，但实际上它做的是反向的先序遍历。亦即遍历的顺序是：节点 -> 右子树 -> 左子树。这生成的是后根遍历的逆序输出。使用第二个栈，再执行一次反向输出即可得到所要的结果。

下面是它的实现步骤：

将根节点压入第一个栈
从第一个栈中弹出一个元素，压入第二个栈
然后分别将该节点的左右孩子压入第一个栈
重复步骤2和步骤3直到第一个栈为空
执行结束，第二个栈中就保存了所有节点的后序遍历输出结果。依次将元素从第二个栈中弹出即可。
void postOrderTraversalIterativeTwoStacks(BinaryTree *root) {
  if (!root) return;
  stack<BinaryTree*> s;
  stack<BinaryTree*> output;
  s.push(root);
  while (!s.empty()) {
    BinaryTree *curr= s.top();
    output.push(curr);
    s.pop();
    if (curr->left)
      s.push(curr->left);
    if (curr->right)
      s.push(curr->right);
  }
  while (!output.empty()) {
    cout << output.top()->data << " ";
    output.pop();
  }
}
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
复杂度分析：
双栈法的空间复杂度高于第一个解法。实际上，第一个解法的空间复杂度是O(h)，其中h是树的最大高度。而双栈法的空间复杂度是O(n)，其中n是节点的总个数。

原文链接：Binary Tree Post-Order Traversal Iterative Solution




"""

#-*- coding:utf-8 -*-
#coding=utf-8