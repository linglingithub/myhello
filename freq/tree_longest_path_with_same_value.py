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


class Solution:
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



    def helper1(self, A, neighbors, node, res, visited):
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




class Solution_jiuzhang:
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
        v = []
        for c in neighbors[o]:
            if c != fa:
                if A[c] == A[o]:
                    v.append(self.dfs(c, o, A, neighbors))
                else:
                    self.dfs(c, o, A, neighbors)
        v.append(0)
        v.append(0)
        v = sorted(v, reverse=True)
        self.ans = max(self.ans, v[0] + v[1] + 1)
        return v[0] + 1


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
