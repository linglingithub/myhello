#coding=utf-8

import unittest

"""

Connected Component in Undirected Graph


Find the number connected component in the undirected graph. Each node in the graph contains a label and a list of its 
neighbors. (a connected component (or just component) of an undirected graph is a subgraph in which any two vertices 
are connected to each other by paths, and which is connected to no additional vertices in the supergraph.)

 Notice

Each connected component should sort by label.

Have you met this question in a real interview? Yes
Clarification
Learn more about representation of graphs

Example
Given graph:

A------B  C
 \     |  | 
  \    |  |
   \   |  |
    \  |  |
      D   E
Return {A,B,D}, {C,E}. Since there are two connected component which is {A,B,D}, {C,E}

Tags 
Breadth First Search Union Find
Related Problems 
Medium Graph Valid Tree 26 %
Medium Find the Weak Connected Component in the Directed Graph

"""


# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    # @return {int[][]} a connected set of a undirected graph
    """
    used bfs / dfs for this one (undirected graph)
    """
    def connectedSet(self, nodes):
        # Write your code here
        result = []
        visited = {}
        for node in nodes:
            group = {}
            self.travel(node, group, visited)
            if group:
                result.append(sorted(group.keys()))
        return result

    def travel(self, node, group, visited):
        if visited.get(node.label):
        #if visited[node.label]: # can directly use this, may cause KeyError
            return
        visited[node.label] = True
        group[node.label] = True
        for nei in node.neighbors:
            self.travel(nei, group, visited)


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = 1
        answer = 1
        result = self.sol.connectedSet(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""

class Solution:
    # @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    # @return {int[][]} a connected set of a undirected graph
    def dfs(self, x, tmp):
        self.v[x.label] = True
        tmp.append(x.label)
        for node in x.neighbors:
            if not self.v[node.label]:
                self.dfs(node, tmp)
            
    def connectedSet(self, nodes):
        # Write your code here
        self.v = {}
        for node in nodes:
            self.v[node.label] = False

        ret = []
        for node in nodes:
            if not self.v[node.label]:
                tmp = []
                self.dfs(node, tmp)
                ret.append(sorted(tmp))
        return ret
            


"""