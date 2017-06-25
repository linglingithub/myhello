#coding=utf-8

import unittest

"""

Course Schedule

There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed 
as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Have you met this question in a real interview? Yes
Example
Given n = 2, prerequisites = [[1,0]]
Return true

Given n = 2, prerequisites = [[1,0],[0,1]]
Return false

Tags 
Amazon Apple Topological Sort Breadth First Search Zenefits
Related Problems 
Medium Course Schedule II 22 %
Medium Topological Sorting


"""


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        remember: key difference, graph should be (a,b) --> graph[a].append(b), not graph[b].append[a]
        :param numCourses: 
        :param prerequisites: 
        :return: 
        """
        # Write your code here
        if numCourses <= 0 or not prerequisites:
            return True
        # construct graph
        graph = [[] for _ in range(numCourses)]
        ind = [0 for _ in range(numCourses)]
        from collections import deque
        seeds = deque()

        for edge in prerequisites:
            a, b = edge[0], edge[1]
            if b not in graph[a]:
                graph[a].append(b)
                ind[b] += 1
        for x in range(numCourses):
            if ind[x] == 0:
                seeds.append(x)
        # traverse
        courses = 0
        while seeds:
            next_course = seeds.pop()
            courses += 1
            for x in graph[next_course]:
                ind[x] -= 1
                if ind[x] == 0:
                    seeds.append(x)
        return courses == numCourses


class Solution_TLEcase5(object): # TLE on case 5, local around 1s --> deque then 941ms, still TLE
    def canFinish(self, numCourses, prerequisites):
        # Write your code here
        if numCourses <= 0 or not prerequisites:
            return True
        # construct graph

        graph = [[0 for _ in range(numCourses)] for _ in range(numCourses)]
        in_cnts = [0 for _ in range(numCourses)]
        from collections import deque
        seeds = deque()
        # seeds = []
        for edge in prerequisites:
            a, b = edge[0], edge[1]
            if graph[a][b] == 0:
                in_cnts[b] += 1
            graph[a][b] = 1
        for x in range(numCourses):
            if in_cnts[x] == 0:
                seeds.append(x)
        # traverse
        # courses = []
        courses = 0
        while seeds:
            # next_course = self.get_next(graph, in_cnts, courses)  # -->
            #   while next_course != -1:
            next_course = seeds.pop()
            # courses.append(next_course)
            courses += 1
            for x in range(numCourses):
                if graph[next_course][x] == 1:
                    graph[next_course][x] = 0
                    in_cnts[x] -= 1
                    # if in_cnts[x] == 0 and x not in courses:
                    if in_cnts[x] == 0:
                        seeds.append(x)
                        # next_course = self.get_next(graph, in_cnts, courses)
        # return len(courses) == numCourses
        return courses == numCourses

    # def get_next(self, graph, int_cnts, courses): # the cause of TLE maybe??
    #     for x in range(len(int_cnts)):
    #         if int_cnts[x] == 0:
    #             int_cnts[x] = -1
    #             return x
    #     return -1


class Solution_TLEcase4: # TLE on case4, 62% cases passed and then TLE; also TLE on leetcode
    # @param {int} numCourses a total of n courses
    # @param {int[][]} prerequisites a list of prerequisite pairs
    # @return {boolean} true if can finish all courses or false
    def canFinish(self, numCourses, prerequisites):
        """
        store graph simlilar to linked list (dict actually), not very fast
        :param numCourses: 
        :param prerequisites: 
        :return: 
        """
        # Write your code here
        if numCourses <= 0 or not prerequisites:
            return True
        # construct graph -->
        graph, in_cnts = self.make_graph(numCourses, prerequisites)

        # search the possible path
        path = []
        self.search(graph, in_cnts, path)

        if len(path) < numCourses:
            return False
        else:
            return True

    def make_graph(self, numCourses, edges):
        graph = {}
        in_cnts = [0 for _ in range(numCourses)]
        for edge in edges:
            pre, post = edge[0], edge[1]
            if post in graph:
                graph[post][pre] = True
            else:
                graph[post] = {pre: True}
            #in_cnts[post] += 1 # can't use +=1 here, edges maybe repeatedly given, case3
            in_cnts[post] = len(graph[post])
        return graph, in_cnts

    def search(self, graph, in_cnts, path):
        # get a zero in node -->
        tmp = self.get_next(graph, in_cnts, path)
        while tmp>=0: # think about node 0, should say >=0 ,not while tmp
            path.append(tmp)
            for node in graph:
                if tmp in graph[node]:
                    del graph[node][tmp]
                    in_cnts[node] -= 1
            tmp = self.get_next(graph, in_cnts, path)
        return

    def get_next(self, graph, in_cnts, path):
        for i in range(len(in_cnts)):
            # if_cnts[i] == 0 and i in graph:  # should add check that i still in graph --> wrong, should check visited or not
            # some node will automaticly have no in-edge, then not in graph dict
            if in_cnts[i] == 0 and i not in path:
                if i in graph:  # need to check this, otherwise may cause key error
                    del graph[i]
                return i
        return -1    # should deal with no node left to pick


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()


    def test_case05(self):  #=== TLE, local runs about 11s
        from util.ini_file_util import IniFileUtil
        params = IniFileUtil.read_into_dict("course_schedule_case5.ini")
        n = int(params.get("n"))
        nums = IniFileUtil.string_to_int_list_list(params.get("nums"))
        answer = True
        result = self.sol.canFinish(n, nums)
        self.assertEqual(answer, result)


    def test_case4(self):  #=== TLE, local runs about 11s
        from util.ini_file_util import IniFileUtil
        params = IniFileUtil.read_into_dict("course_schedule_case4.ini")
        n = int(params.get("n"))
        nums = IniFileUtil.string_to_int_list_list(params.get("nums"))
        answer = True
        result = self.sol.canFinish(n, nums)
        self.assertEqual(answer, result)





    def test_case3(self):  #===>
        n = 10
        nums = [[5,8],[3,5],[1,9],[4,5],[0,2],[1,9],[7,8],[4,9]]
        answer = True
        result = self.sol.canFinish(n, nums)
        self.assertEqual(answer, result)



    def test_case1(self):
        n = 2
        nums = [[1,0]]
        answer = True
        result = self.sol.canFinish(n, nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        n = 2
        nums = [[1,0],[0,1]]
        answer = False
        result = self.sol.canFinish(n, nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""


"""