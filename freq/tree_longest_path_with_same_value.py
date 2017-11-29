#coding=utf-8

import unittest

"""

[check with --> 687. Longest Univalue Path]


717. Tree Longest Path With Same Value 

 Description
 Notes
 Testcase
 Judge
We consider an undirected tree with N nodes, numbered from 1 to N, Additionally, each node also has a label attached to 
it and the label is an integer value. Note that different nodes can have identical labels. You need to write a function , 
that , given a zero-indexed array A of length N, where A[J] is the label value of the (J + 1)-th node in the tree, and 
a zero-indexed array E of length K = (N - 1) * 2 in which the edges of the tree are described (for every 0 <= j <= N -2 
values E[2 * J] and E[2 * J + 1] represents and edge connecting node E[2 * J] with node E[2 * J + 1])， returns the 
length of the longest path such that all the nodes on that path have the same label. Then length of a path if defined 
as the number of edges in that path.

 Notice

Assume that: 1 <= N <= 1000

Have you met this question in a real interview? Yes
Example
Give A = [1, 1, 1 ,2, 2] and E = [1, 2, 1, 3, 2, 4, 2, 5]
described tree appears as follows:

                   1 （value = 1）
                 /   \
    (value = 1) 2     3 (value = 1)
               /  \
 (value = 2)  4     5 (value = 2)
and your function should return 2, because the longest path (in which all nodes have the save value of 1) is 
(2 -> 1 -> 3). The number of edges on this path is 2, thus, that is the answer.

Tags 
Binary Tree Depth First Search Google
Related Problems 
Easy Binary Tree Paths

"""


class Solution1:
    """
    @param: : as indicated in the description
    @param: : as indicated in the description
    @return: Return the number of edges on the longest path with same value.
    """

    def LongestPathWithSameValue(self, A, E):
        if not A or not E:
            return 0
        n = len(A)
        neighbors = [[] for _ in range(n)]
        # process edges, and make the id of node from 1 based to 0 based
        for i in range(n-1):
            pa, pb = E[i*2], E[i*2+1]
            neighbors[pa-1].append(pb-1)
            neighbors[pb-1].append(pa-1)
        self.res = [0]
        visited = [False for _ in range(n)]
        for node in range(n):
            if not visited[node]:
                join_path, single_path = self.helper(A, neighbors, node, visited)
                self.res.append(max(join_path, single_path))
        return max(self.res)

    def helper(self, A, neighbors, node, visited):
        visited[node] = True
        node_paths = []

        for nei in neighbors[node]:
            if visited[nei]:
                continue
            if A[nei] == A[node]:
                node_paths.append(1+ self.helper(A, neighbors, nei, visited)[1])

        node_paths.sort(reverse=True)
        # every node has at most 3 neighbors, and one is as previous, the other two will do dfs and combine if ok -- WRONG
        # actually above thought wrong, description did not say binary tree, may have more than 2 expanding neighbors
        if len(node_paths) >= 2:  # only say a tree,
            join_path = node_paths[0]+node_paths[1]
            single_path = node_paths[0]
        elif len(node_paths) == 1:
            join_path = node_paths[0]
            single_path = node_paths[0]
        else:
            join_path, single_path = 0, 0
        # important, need to add join_path to res, otherwise wrong, see case 5
        if max(self.res) < max(join_path, single_path):
            self.res.append(max(join_path, single_path))
        return join_path, single_path



    def helper_wrong(self, A, neighbors, node, res, visited):
        if node >= len(A) or visited[node]:
            return res
        visited[node] = True
        for nei in neighbors[node]:
            if visited[nei]:
                continue
            if A[nei] == A[node]:
                tmp = self.helper(A, neighbors, nei, res, visited)[-1]
                res.append(1+tmp)
            else:
                self.helper(A, neighbors, nei, res, visited)
        if res:
            res.sort(reverse=True)
        return res




class Solution:
    """
    @param: : as indicated in the description
    @param: : as indicated in the description
    @return: Return the number of edges on the longest path with same value.
    """

    def LongestPathWithSameValue(self, A, E):
        n = len(A)
        neighbors = [[] for _ in range(n + 1)]
        for i in range(n - 1):
            neighbors[E[i * 2]].append(E[i * 2 + 1])
            neighbors[E[i * 2 + 1]].append(E[i * 2])
        A = [0] + A
        self.ans = 0
        tmp = self.dfs(1, 0, A, neighbors)
        self.ans = max(self.ans, tmp)
        return self.ans - 1

    def dfs(self, o, fa, A, neighbors):
        """
        https://www.jiuzhang.com/qa/6700/

        dfs is for getting single-path value recursively ( one path from current node)
        but inside the dfs, the possible join-path case is also compared and recorded with self.ans.
        Thus covering all possible cases.
        :param o:  current node to explore
        :param fa: father node, where previous node is
        :param A:
        :param neighbors:
        :return: the node count of current node's longest same value branch (including self), to the father node for father's case calculation
        """
        v = []  # to save the node counts of current point's connected branches of same value
        for c in neighbors[o]:
            if c != fa:
                if A[c] == A[o]:
                    v.append(self.dfs(c, o, A, neighbors))
                else:
                    self.dfs(c, o, A, neighbors)
        v.append(0)
        v.append(0)
        # for the end point (no more children to expand, or no same value to expand), v is [], and will return 1 to father
        # then adding two 0 here is helpful to save if else condition
        # ( two same value case -- v has 4 elements, one same value case -- v has 3 elements, no same value case -- v has 1 element)
        # then self.ans is always compared to possible longest case, 1 -- current node, v[0] longest children node counts, v[1] second longest
        v = sorted(v, reverse=True)
        self.ans = max(self.ans, v[0] + v[1] + 1)
        return v[0] + 1   # return the current node's longest branches to the father point ( to append to father's v)


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        a = [1, 1, 1 ,2, 2]
        e = [1, 2, 1, 3, 2, 4, 2, 5]
        answer = 2
        result = self.sol.LongestPathWithSameValue(a, e)
        self.assertEqual(answer, result)

    def test_case2(self):  # ====>
        a = [1,1,1,1,1]
        e = [1,2,1,3,2,4,2,5]
        answer = 3
        result = self.sol.LongestPathWithSameValue(a, e)
        self.assertEqual(answer, result)

    def test_case3(self):
        a = [1,1,1,2,2]
        e = [1,2,3,1,2,4,2,5]
        answer = 2
        result = self.sol.LongestPathWithSameValue(a, e)
        self.assertEqual(answer, result)

    def test_case4(self):
        from util.ini_file_util import IniFileUtil
        params = IniFileUtil.read_into_dict("tree_longest_path_with_same_value_case4.ini")
        a = IniFileUtil.string_to_int_list(params.get("a"))
        e = IniFileUtil.string_to_int_list(params.get("e"))
        # nums = IniFileUtil.string_to_int_list_list(params.get("nums"))   # for matrix input
        answer = int(params.get("answer"))  # 35
        result = self.sol.LongestPathWithSameValue(a, e)
        self.assertEqual(answer, result)

    def test_case05(self):
        a = [1,1,1,1,1,1]
        e = [1,2,2,3,2,4,3,5,4,6]
        answer = 4
        result = self.sol.LongestPathWithSameValue(a, e)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""

请助教帮忙看一下这个解法有什么问题？ 在49%过不了。谢谢。

class Solution:

def LongestPathWithSameValue(self, A, E):
    if not A or not E:
        return 0
    n = len(A)
    neighbors = [[] for _ in range(n)]
    for i in range(n-1):
        pa, pb = E[i*2], E[i*2+1]
        neighbors[pa-1].append(pb-1)
        neighbors[pb-1].append(pa-1)
    res = []
    visited = [False for _ in range(n)]
    for node in range(n):
        if not visited[node]:
            join_path, single_path = self.helper(A, neighbors, node, visited)
            res.append(max(join_path, single_path))
    return max(res)

def helper(self, A, neighbors, node, visited):
    visited[node] = True
    node_paths = []

    for nei in neighbors[node]:
        if visited[nei]:
            continue
        if A[nei] == A[node]:
            node_paths.append(1+ self.helper(A, neighbors, nei, visited)[1])

    node_paths.sort(reverse=True)
    if len(node_paths) >= 2:  
        return node_paths[0]+node_paths[1], node_paths[0]
    elif len(node_paths) == 1:
        return node_paths[0], node_paths[0]
    else:
        return 0, 0
添加评论
分享
删除
修改
2个回答

2
施助教
编辑于 11/28/2017, 8:22:46 PM · 2个赞
一个问题是：你没有把下层找到返回的join_path拿来取最大值，导致其丢失，具体来说你可以看看下面这个例子：
[1,1,1,1,1,1]
[1,2,2,3,2,4,3,5,4,6]

收起评论
分享
3 个评论
s同学
11/25/2017, 7:29:06 PM
非常感谢，助教节日周末还能及时回复，赞！在helper里增加把中间结果放入res后代码可以通过，不过感觉不是很简洁。
https://www.jiuzhang.com/solution/binary-tree-longest-path-with-same-value/ 上面给的代码很简洁，不过看的不是很明白，能否请
助教加点注释，指点一二？

赞
删除
回复
马克助教
11/26/2017, 4:42:24 AM
可以给助教的回复点赞啊 哈哈

1
回复
s同学
11/28/2017, 8:22:46 PM
但是没有看到可以给施助教和刘助教点赞的button啊？

赞
删除
回复

写下你的评论...
​
评论
0
刘助教
编辑于 11/28/2017, 9:05:14 PM · 0个赞
答案采取的是dfs的解法
我们可以得到每个点的相邻的点，然后遍历相邻的点，如果这个点和相邻的点的值相同，那么这两个点之间是可以连线的，如果值不相同，那么就
不能连线，然后同理再dfs相邻的结点
可能有多个邻居具有相同的值，所以对于答案应该选择这些邻居中最大的一个和第二大的结果，这两个可以连接起来，更新答案。但是对于该结点
能到达的最大值，应该选择最大的一个

收起评论
分享
1 个评论
s同学
11/28/2017, 9:05:14 PM
对，其实就是一开始对v存值和dfs返回值没有想清楚。一开始以为v存的是answer，其实最多不超过4个值，只是一个当前层的临时存储。第二，
这里头v存的是相同值的节点个数。最后，添加2个0占位可以省掉一些条件判断，代码更简单。

赞
删除
回复



"""