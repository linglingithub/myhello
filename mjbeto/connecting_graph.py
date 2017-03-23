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
1. connect(a, b), add an edge to connect node a and node b. 2.query(a, b)`, check if two nodes are connected

Have you met this question in a real interview? Yes
Example
5 // n = 5
query(1, 2) return false
connect(1, 2)
query(1, 3) return false
connect(2, 4)
query(1, 4) return true


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



class ConnectingGraph(object):
    """
    # NOTE that notes should be labeled from 1 to n
    """

    # @param {int} n
    def __init__(self, n):
        # initialize your data structure here.
        self.parents = [x for x in range(n+1)]

    # @param {int} a, b
    # return nothing
    def connect(self, a, b):
        # Write your code here
        ap = self.find(a)
        bp = self.find(b)
        if ap != bp:
            #self.parents[a] = b # can't use this
            self.parents[ap] = bp


    # @param {int} a, b
    # return {boolean} true if they are connected or false
    def query(self, a, b):
        # Write your code here
        ap = self.find(a)
        bp = self.find(b)
        return ap == bp

    def find(self, a):
        if self.parents[a] != a:
            self.parents[a] = self.find(self.parents[a])
        return self.parents[a]


class SolutionTester(unittest.TestCase):
    def setUp(self):
        #self.sol = ConnectingGraph(5)
        self.sol = ConnectingGraph(12)


    def test_case1(self):
        answer = False
        result = self.sol.query(1,2)
        self.assertEqual(answer, result)

    def test_case2(self):
        self.sol.connect(1,2)
        result = self.sol.query(1,3)
        answer = False
        self.assertEqual(answer, result)

    def test_case3(self):
        self.sol.connect(1,2)  # connect in previous test case will not be visible for following test cases
        self.sol.connect(4,2)
        result = self.sol.query(1,4)
        answer = True
        self.assertEqual(answer, result)

    def test_case4(self):
        result = []
        self.sol.connect(3,9)
        self.sol.connect(10,9)
        self.sol.connect(5,7)
        result.append(self.sol.query(1,10))
        result.append(self.sol.query(2,11))
        result.append(self.sol.query(8,9))
        self.sol.connect(3,2)
        self.sol.connect(10,11)
        result.append(self.sol.query(11,3))
        self.sol.connect(12,8)
        self.sol.connect(10,3)
        self.sol.connect(10,12)
        result.append(self.sol.query(2,1))
        self.sol.connect(10,5)
        result.append(self.sol.query(12,5))
        result.append(self.sol.query(9,6))
        result.append(self.sol.query(7,2))
        result.append(self.sol.query(1,12))
        result.append(self.sol.query(3,12))
        self.sol.connect(10,8)
        self.sol.connect(12,2)
        result.append(self.sol.query(10,9))
        result.append(self.sol.query(2,7))
        self.sol.connect(7,6)
        self.sol.result = self.sol.query(1,3)
        answer = [False,False,False,True,False,True,False,True,False,True,True,True]
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-


