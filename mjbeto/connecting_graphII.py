#coding=utf-8

import unittest

"""

 Connecting Graph

 Description
 Notes
 Testcase
 Judge
Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.

You need to support the following method:
1. connect(a, b), add an edge to connect node a and node b.
2. query(a), Returns the number of connected component nodes which include node a.

Have you met this question in a real interview? Yes
Example

5 // n = 5
query(1) return 1
connect(1, 2)
query(1) return 2
connect(2, 4)
query(1) return 3
connect(1, 4)
query(1) return 3


Tags
Union Find
Related Problems
Medium Connecting Graph III 56 %
Medium Connecting Graph II 34 %
Medium Graph Valid Tree 26 %
Medium Surrounded Regions 21 %
Hard Number of Islands II 18 %
Medium Find the Weak Connected Component in the Directed Graph

"""



class ConnectingGraph2(object):

    # @param {int} n
    def __init__(self, n):
        # initialize your data structure here.
        self.parents = [x for x in range(n+1)]
        self.connect_cnts = [1 for _ in range(n+1)]


    # @param {int} a, b
    # return nothing
    def connect(self, a, b):
        # Write your code here
        pa = self.find(a)
        pb = self.find(b)
        if pa != pb:
            self.parents[pa] = pb
            self.connect_cnts[pb] += self.connect_cnts[pa]

    # @param {int} a
    # return {int}  the number of nodes connected component
    # which include a node.
    def query(self, a):
        # Write your code here
        pa = self.find(a)
        return self.connect_cnts[pa]


    def find(self, a):
        if self.parents[a] != a: # can not use while here
            self.parents[a] = self.find(self.parents[a])
        return self.parents[a]


class ConnectingGraph2_TLE(object): #65% test cases passed.

    # @param {int} n
    def __init__(self, n):
        # initialize your data structure here.
        self.parents = [x for x in range(n+1)]
        #self.connect_cnts = [1 for _ in range(n+1)]


    # @param {int} a, b
    # return nothing
    def connect(self, a, b):
        # Write your code here
        pa = self.find(a)
        pb = self.find(b)
        if pa != pb:
            self.parents[pa] = pb




    # @param {int} a
    # return {int}  the number of nodes connected component
    # which include a node.
    def query(self, a):
        # Write your code here
        cnt = 0
        pa = self.find(a)
        for x in range(1,len(self.parents)):
            if self.find(x) == pa:
                cnt += 1
        return cnt


    def find(self, a):
        if self.parents[a] != a: # can not use while here
            self.parents[a] = self.find(self.parents[a])
        return self.parents[a]



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = ConnectingGraph2(5)
        #self.sol = ConnectingGraph2(12)


    def test_case1(self):
        result = []
        result.append(self.sol.query(1)) #return 1
        self.sol.connect(1, 2)
        result.append(self.sol.query(1)) #return 2
        self.sol.connect(2, 4)
        result.append(self.sol.query(1)) #return 3
        self.sol.connect(1, 4)
        result.append(self.sol.query(1)) #return 3
        answer = [1,2,3,3]
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-


