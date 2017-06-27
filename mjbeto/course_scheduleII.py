#coding=utf-8

import unittest

"""

210. Course Schedule II

There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed 
as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to 
finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, 
return an empty array.

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order 
is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]
There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 
and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering 
is[0,2,1,3].

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph 
is represented.
You may assume that there are no duplicate edges in the input prerequisites.


"""


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if numCourses <= 0:
                return []
        if not prerequisites:
            return [ x for x in range(numCourses)]  # see case 3
        # construct graph
        graph = [[] for _ in range(numCourses)]
        ind = [0 for _ in range(numCourses)]
        from collections import deque
        seeds = deque()
        result = []

        for edge in prerequisites:
            #a, b = edge[0], edge[1]
            a, b = edge[1], edge[0]
            if b not in graph[a]:
                graph[a].append(b)
                ind[b] += 1
        for x in range(numCourses):
            if ind[x] == 0:
                seeds.append(x)
        # traverse
        courses = 0
        while seeds:
            next_course = seeds.popleft()
            result.append(next_course)
            courses += 1
            for x in graph[next_course]:
                ind[x] -= 1
                if ind[x] == 0:
                    seeds.append(x)
        # return result  #should check if possible or not, if not then return [] , case 4
        return result if courses == numCourses else []


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()


    def test_case4(self):  #===>
        n = 4
        nums = [[1,0],[2,1],[3,2],[1,3]]
        answer = []
        result = self.sol.findOrder(n, nums)
        self.assertEqual(answer, result)

    def test_case3(self):  #===>
        n = 1
        nums = []
        answer = [0]
        result = self.sol.findOrder(n, nums)
        self.assertEqual(answer, result)

    def test_case1(self):
        n = 2
        nums = [[1,0]]
        answer = [0,1]
        result = self.sol.findOrder(n, nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        n = 4
        nums = [[1,0],[2,0],[3,1],[3,2]]
        answers = [[0, 1,2,3], [0,2,1,3]]
        result = self.sol.findOrder(n, nums)
        print result
        #self.assertEqual(answer, result)
        self.assertTrue(result in answers)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""
some DFS code can be accepted by leetcode, by error on lintcode (probabaly maximum recursive times, n = 100001)
one of the codes is like following

下面我们来看DFS的解法，也需要建立有向图，还是用二维数组来建立，和BFS不同的是，我们像现在需要一个一维数组visit来记录访问状态，大体思路是，
先建立好有向图，然后从第一个门课开始，找其可构成哪门课，暂时将当前课程标记为已访问，然后对新得到的课程调用DFS递归，直到出现新的课程已经访问
过了，则返回false，没有冲突的话返回true，然后把标记为已访问的课程改为未访问。代码如下：

    def dfs(self, v, visit, gr):
        if visit[v] == 1:
            return True
        visit[v] = -1;
        for i in gr[v]:
            if visit[i] == -1 or not self.dfs(i, visit, gr):
                return False
        visit[v] = 1
        return True
     
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        gr = [[] for x in range(numCourses)]
        visit = [0 for x in range(numCourses)]
         
        for p in prerequisites:
            if p[0] not in gr[p[1]]:
                gr[p[1]].append(p[0])
                 
        for v in range(numCourses):
            if visit[v]!=1:
                if not self.dfs(v, visit, gr):
                    return False
        return True

"""