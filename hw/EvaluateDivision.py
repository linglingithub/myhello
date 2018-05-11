#coding=utf-8

import unittest

"""
399. Evaluate Division
DescriptionHintsSubmissionsDiscussSolution
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number 
(floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0. 
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? . 
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , 
where equations.size() == values.size(), and the values are positive. This represents the equations. 
Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is 
no contradiction.


Difficulty:Medium
Total Accepted:30.2K
Total Submissions:71K
Contributor:LeetCode
Subscribe to see which companies asked this question.

Related Topics 
Graph

"""

from collections import defaultdict
class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        if not queries:
            return []
        if not equations or not values or len(equations) != len(values):
            return [-1.0 for _ in range(len(queries))]

        # build a graph of dict: {node: {nei_node: value}}
        graph = self.build_graph(equations, values)
        result = []
        for query in queries:
            val = self.check_value(graph, query)
            result.append(val)
        return result

    def build_graph(self, equations, values):
        graph = defaultdict(dict)
        for (s, t), v in zip(equations, values):
            graph[s][t] = v
            graph[t][s] = 1.0 / v
            graph[s][s] = 1.0
            graph[t][t] = 1.0
        return graph

    def check_value(self, graph, query):
        s, t = query
        if s not in graph or t not in graph:
            return -1.0
        result = [-1.0]  #!!! init as -1.0, not 1.-
        visited = {s} # !!! init as starting point
        self.dfs(graph, s, t, 1.0, visited, result)
        return result[0]

    def dfs(self, graph, s, t, val, visited, result):
        if s == t:
            result[0] = val
            return
        for nei, neival in graph[s].items():
            if nei in visited:
                continue
            visited.add(nei)
            self.dfs(graph, nei, t, val * neival, visited, result)
            visited.remove(nei)


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        equations = [["a", "b"], ["b", "c"]]
        values = [2.0, 3.0]
        queries = [["a", "c"], ["b", "c"], ["a", "e"], ["a", "a"], ["x", "x"]]
        answer = [6.0,3.0,-1.0,1.0,-1.0]
        result = self.sol.calcEquation(equations, values, queries)
        self.assertEqual(answer, result)

    def test_case02(self):
        equations = [["a","b"],["c","d"]]
        values = [1.0,1.0]
        queries = [["a","c"],["b","d"],["b","a"],["d","c"]]
        answer = [-1.0, -1.0, 1.0, 1.0]
        result = self.sol.calcEquation(equations, values, queries)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""

    def calcEquation(self, equations, values, queries):
        g = collections.defaultdict(lambda: collections.defaultdict(int))
        for (s, t), v in zip(equations, values):
            g[s][t] = v
            g[t][s] = 1.0 / v
        for k in g:
            g[k][k] = 1.0
            for s in g:
                for t in g:
                    if g[s][k] and g[k][t]:
                        g[s][t] = g[s][k] * g[k][t]
        ans = []
        for s, t in queries:
            ans.append(g[s][t] if g[s][t] else -1.0)
        return ans
        
  def calcEquation(self, equations, values, queries):
    def divide(x, y, visited):
      if x == y: return 1.0
      visited.add(x)
      for n in g[x]:
        if n in visited: continue
        visited.add(n)
        d = divide(n, y, visited)
        if d > 0: return d * g[x][n]
      return -1.0
    
    g = collections.defaultdict(dict)
    for (x, y), v in zip(equations, values):      
      g[x][y] = v
      g[y][x] = 1.0 / v
    
    ans = [divide(x, y, set()) if x in g and y in g else -1 for x, y in queries]
    return ans        
        
        

"""

#-*- coding:utf-8 -*-
