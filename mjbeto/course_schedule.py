#coding=utf-8

import unittest
from collections import defaultdict, deque

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
class Solution:
    def canFinish(self, numCourses, prereqs):
        """
        Assuptions: no duplicated edges.
        Model the problem as finding topological ordering of a directed graph.
        Time: O(|E| + |V|)
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not numCourses or not prereqs:
            return True
        indegrees = [0 for _ in range(numCourses)]
        edges = defaultdict(list)  # {node : [neis whoes prereq has node]}
        queue = deque()
        self.preprocess(numCourses, prereqs, indegrees, edges, queue)
        course_taken = 0
        while queue:
            cur = queue.popleft()
            course_taken += 1
            neis = edges[cur]  # list of courses ids like [0, 2, 5...]
            if not neis:
                continue
            for nei in neis:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    queue.append(nei)
        return course_taken == numCourses

    def preprocess(self, numCourses, prereqs, indegrees, edges, queue):
        # traverse all edges (prereqs), init the indegrees, edges, and queue
        for pre, post in prereqs:
            indegrees[post] += 1
            edges[pre].append(post)
        for node in range(len(indegrees)):
            if indegrees[node] == 0:
                queue.append(node)

class Solution_DFS2_notgood_local_online:
    def dfs(self, v, visit, gr):
        if visit[v] == 1:
            return True
        visit[v] = -1
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
            if visit[v] != 1:
                if not self.dfs(v, visit, gr):
                    return False
        return True


class Solution_DFS_TLEonline_maxstacklocal(object):
    def canFinish(self, n, pres):
        # Write your code here
        graph = [[] for _ in range(n)]
        visited = [False for _ in range(n)]
        for edge in pres:
            graph[edge[0]].append(edge[1])

        for i in range(n):
            if not self.dfs(i, graph, visited):
                return False
        return True

    def dfs(self, node, graph, visited):
        if visited[node]:
            return False
        visited[node] = True
        for i in graph[node]:
            if not self.dfs(i, graph, visited):
                return False
        visited[node] = False
        return True



class Solution(object):
    def canFinish(self, numCourses, prerequisites): # BFS idea
        """
        remember: key difference, 
        graph should be (a,b) --> graph[a].append(b), not using n*n matrix
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