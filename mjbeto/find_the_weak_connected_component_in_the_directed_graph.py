#coding=utf-8

import unittest

"""
Find the Weak Connected Component in the Directed Graph

Find the number Weak Connected Component in the directed graph. Each node in the graph contains a label and a list of 
its neighbors. (a connected set of a directed graph is a subgraph in which any two vertices are connected by direct 
edge path.)

 Notice

Sort the element in the set in increasing order

Have you met this question in a real interview? Yes
Example
Given graph:

A----->B  C
 \     |  | 
  \    |  |
   \   |  |
    \  v  v
     ->D  E <- F
Return {A,B,D}, {C,E,F}. Since there are two connected component which are {A,B,D} and {C,E,F}

Tags 
Union Find
Related Problems 
Medium Connecting Graph 40 %
Hard Number of Islands II 18 %
Medium Find the Weak Connected Component in the Directed Graph 25 %
Medium Connected Component in Undirected Graph


"""



# Definition for a directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param {DirectedGraphNode[]} nodes a array of directed graph node
    # @return {int[][]} a connected set of a directed graph
    def connectedSet2(self, nodes):
        # Write your code here
        roots = {}
        for node in nodes:
            if node.label not in roots:
                roots[node.label] = node.label
            parent = self.find(node.label, roots)
            for neighbor in node.neighbors:
                bparent = self.find(neighbor.label, roots)
                if parent != bparent:
                    roots[bparent] = parent
                    roots[neighbor.label] = parent  # should be neighbor.label, not neighbor here
        result = {}
        for nodelabel in roots:  # should be nodelabel ( not a node object in roots)
            parent = self.find(nodelabel, roots)
            if parent in result:
                result[parent].append(nodelabel)
            else:
                result[parent] = [nodelabel]
        #return list(result.values)
        #return list(result.values())
        rev = [sorted(x) for x in result.values() ]
        return rev

    def find(self, nodelabel, roots):
        if nodelabel not in roots:
            roots[nodelabel] = nodelabel
            return nodelabel
        else:
            if roots[nodelabel] == nodelabel:
                return nodelabel
            else:
                roots[nodelabel] = self.find(roots[nodelabel], roots)
                return roots[nodelabel]

class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

    @classmethod
    def generate_graph(cls, nodes):
        """
        nodes is a list of list, in which first ele is the node label, and remaining eles(if any) are the neighbors
        :param nodes: 
        :return: 
        """
        result = {}
        for node in nodes:
            label = node[0]
            if label in result:
                one = result[label]
            else:
                one = DirectedGraphNode(node[0])
            for neighbor in node[1:]:
                if neighbor in result:
                    neinode = result[neighbor]
                else:
                    neinode = DirectedGraphNode(neighbor)
                    result[neighbor] = neinode
                one.neighbors.append(neinode)
            result[one.label] = one
        return result.values()



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):  #===> output [[1],[2],[3],[4],[5],[6]]
        nums = DirectedGraphNode.generate_graph([[1,2,4],[2,4],[3,5],[4],[5],[6,5]])
        answer = [[1,2,4],[3,5,6]]
        result = self.sol.connectedSet2(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""
这道题如果是无向图的话，我们可以用宽度优先搜索直接扫一遍就可以。但是如果是有向图的话，就不能用宽度优先搜索了。因为边是有向的。 那么怎么才能
更好的解决这个问题呢？

那么就只有并查集了。 最开始可以认为图中每个点都是自成一个集合。然后一次遍历每一条边，如果这条边所连的两个点在不同的集合中，那么就用并查集把
这两个集合中所有的元素合并起来。 然后最后扫描完整个边后，统计有多少个集合，那么最后就是弱联通分量的数目。

class Solution:
    # @param {DirectedGraphNode[]} nodes a array of directed graph node
    # @return {int[][]} a connected set of a directed graph
    def __init__(self):
        self.f = {}

    def merge(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            self.f[x] = y

    def find(self, x):
        if self.f[x] == x:
            return x
        
        self.f[x] = self.find(self.f[x])
        return self.f[x]

    def connectedSet2(self, nodes):
        # Write your code here
        for node in nodes:
            self.f[node.label] = node.label

        for node in nodes:
            for nei in node.neighbors:
                self.merge(node.label, nei.label)

        result = []
        g = {}
        cnt = 0

        for node in nodes:
            x = self.find(node.label)
            if not x in g:
                cnt += 1
                g[x] = cnt
            
            if len(result) < cnt:
                result.append([])
        
            result[g[x] - 1].append(node.label)

        return result

"""