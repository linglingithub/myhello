#coding=utf-8
__author__ = 'linglin'
"""
133. Clone Graph

Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
Subscribe to see which companies asked this question

Hide Tags Depth-first Search Breadth-first Search Graph
Hide Similar Problems (M) Copy List with Random Pointer

Medium

"""


import unittest
from util.undirected_graph_node import UndirectedGraphNode

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node): #DFS, 95ms, 64%
        self.node_dict = {}
        if not node:
            return None
        return self.dfs_clone(node)

    def dfs_clone(self, node):
        if node in self.node_dict:
            return self.node_dict[node]
        newnode = UndirectedGraphNode(node.label)
        self.node_dict[node] = newnode
        for neighbor in node.neighbors:
            newnode.neighbors.append(self.dfs_clone(neighbor))
        return newnode



    def cloneGraph2(self, node): #BFS, 95ms, 64%
        # compare this with 1, for undirected graph, it's ok to combine two loops??, no connection will be lost
        if not node:
            return None
        node_dict = {}
        newhead = UndirectedGraphNode(node.label)
        node_dict[node] = newhead
        queue = [node]
        while queue:
            old = queue.pop(0)
            for neighbor in old.neighbors:
                if neighbor not in node_dict:
                    queue.append(neighbor)
                    newnei = UndirectedGraphNode(neighbor.label)
                    node_dict[neighbor] = newnei
                node_dict[old].neighbors.append(node_dict[neighbor])
        return newhead


    def cloneGraph1(self, node): #BFS, 99ms, 54%
        if not node:
            return None
        node_dict = {}
        queue = [node]
        while queue:
            old = queue.pop(0)
            current = UndirectedGraphNode(old.label)
            node_dict[old] = current
            for neighbor in old.neighbors:
                if neighbor not in node_dict: # add this to avoid infinite loop when there is loop in graph
                    queue.append(neighbor)
        for old in node_dict.keys():
            for tmp in old.neighbors:
                node_dict[old].neighbors.append(node_dict[tmp])
        return node_dict[node]


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self): #===> how to stop when there is a loop?
        nums = {0,0,0}
        answer = 1
        result = self.sol.cloneGraph(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
