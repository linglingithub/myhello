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
from collections import defaultdict

class Solution(object):
    def findOrder_BFS(self, numCourses, prerequisites):
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


    def findOrder(self, numCourses, prereqs):  # DFS way, 52ms, 100%!! 0503
        if not prereqs:
            return [x for x in range(numCourses)]
        can_finish = [0 for _ in range(numCourses)]   # 1: yes, 0: unchecked, -1: checked and has dependends
        # process edges
        depends = defaultdict(set)
        for pre, post in prereqs:
            depends[post].add(pre)
        # DFS to check every courses
        result = []
        for course in range(numCourses):
            if not self.helper(course, can_finish, depends, result):
                return []
        return [x for x in reversed(result)]

    def helper(self, course, can_finish, depends, result):
        if can_finish[course] == 1:
            return True
        if can_finish[course] == -1:  # loop dependence, should return false
            return False
        can_finish[course] = -1
        for nei in depends[course]:
            if not self.helper(nei, can_finish, depends, result):
                return False
        # if all dependends can finish, then current course can be finished
        can_finish[course] = 1
        result.append(course)
        return True


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
        print(result)
        #self.assertEqual(answer, result)
        self.assertTrue(result in answers)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""


"""