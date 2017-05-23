#coding=utf-8

import unittest

"""

Graph Valid Tree

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function 
to check whether these edges make up a valid tree.

 Notice

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [
1, 0] and thus will not appear together in edges.

Have you met this question in a real interview? Yes
Example
Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

Tags 
Depth First Search Facebook Zenefits Union Find Breadth First Search Google
Related Problems 
Medium Connecting Graph 40 %
Medium Connected Component in Undirected Graph

"""



class Solution:
    # @param {int} n an integer
    # @param {int[][]} edges a list of undirected edges
    # @return {boolean} true if it's a valid tree, or false
    """
    There are two key points:
    1. can use union find
    2. the standard of a valid tree (using union find): 
        a. single root(all share one root), 
        b. no cycle in the graph 
    How to check 2? 2a: after adding all edges, all roots should be the same. 2b: while adding edges, no shared parents 
        ( if new edge is between two nodes that already in same tree, it is creating a cycle)    
    ----- according to ref, a good property of undirected graph that is a tree is that : len(edges) = n-1, check the ref    
    """
    def validTree(self, n, edges):
        # Write your code here
        if not edges:
            return True if n == 1 else False
        if n < 1:
            return False    #True, should be careful and distinguish cases, check case 3 and case 4
        self.roots = [x for x in range(n)]
        for edge in edges:
            a, b = edge[0], edge[1]
            ar = self.find(a)
            br = self.find(b)
            if ar == br:
                return False
            else:
                self.roots[br] = ar
        parent = self.find(0) #self.roots[0], check case6, case5
        for i in range(1,n):
            if self.find(i) != parent:
                return False
        return True

    def find(self, x):
        if self.roots[x] == x:
            return x
        else:
            self.roots[x] = self.find(self.roots[x])
        return self.roots[x]




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        n = 5
        edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
        answer = True
        result = self.sol.validTree(n, edges)
        self.assertEqual(answer, result)

    def test_case2(self):
        n = 5
        edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
        answer = False
        result = self.sol.validTree(n, edges)
        self.assertEqual(answer, result)


    def test_case3(self): #====>
        n = 2
        edges = []
        answer = False
        result = self.sol.validTree(n, edges)
        self.assertEqual(answer, result)

    def test_case4(self): #====>
        n = 1
        edges = []
        answer = True
        result = self.sol.validTree(n, edges)
        self.assertEqual(answer, result)

    def test_case5(self): #====>
        n = 3
        edges = [[0,1]]
        answer = False
        result = self.sol.validTree(n, edges)
        self.assertEqual(answer, result)

    def test_case6(self): #====>
        n = 8
        edges = [[0,1],[1,2],[3,2],[4,3],[4,5],[5,6],[6,7]]
        answer = True
        result = self.sol.validTree(n, edges)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""

class Solution:
    # @param {int} n an integer
    # @param {int[][]} edges a list of undirected edges
    # @return {boolean} true if it's a valid tree, or false
    def validTree(self, n, edges):
        # Write your code here
        root = [i for i in range(n)]
        for i in edges:
            root1 = self.find(root, i[0])
            root2 = self.find(root, i[1])
            if root1 == root2:
                return False
            else:
                root[root1] = root2
        return len(edges) == n - 1
        
    def find(self, root, e):
        if root[e] == e:
            return e
        else:
            root[e] = self.find(root, root[e])
            return root[e]



"""