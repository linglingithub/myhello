#coding=utf-8

import unittest

"""

417. Pacific Atlantic Water Flow
DescriptionHintsSubmissionsDiscussSolution
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.
Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
Seen this question in a real interview before?

Difficulty:Medium
Total Accepted:26K
Total Submissions:74.6K
Contributor:LeetCode
Subscribe to see which companies asked this question.

Related Topics


"""

import sys

class Solution:
    def pacificAtlantic(self, matrix):  # ref
        if not matrix or not matrix[0]:
            return []
        res = []
        n, m = len(matrix), len(matrix[0])
        pacific = [[False for _ in range(m)] for _ in range(n)]
        atlantic = [[False for _ in range(m)] for _ in range(n)]
        min_val = - sys.maxsize - 1
        for i in range(n):
            self.dfs(matrix, pacific, min_val, i, 0)
            self.dfs(matrix, atlantic, min_val, i, m - 1)
        for j in range(m):
            self.dfs(matrix, pacific, min_val, 0, j)
            self.dfs(matrix, atlantic, min_val, n - 1, j)
        for i in range(n):
            for j in range(m):
                if pacific[i][j] and atlantic[i][j]:
                   res.append([i, j])
        return res

    def dfs(self, matrix, visited, height, x, y):
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        n, m = len(matrix), len(matrix[0])
        if not (0 <= x < n and 0 <= y < m) or visited[x][y] or matrix[x][y] < height:
            return
        visited[x][y] = True
        for dx, dy in dirs:
            self.dfs(matrix, visited, matrix[x][y], x + dx, y + dy)

class Solution_Self:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        can_pacific = [[False for _ in range(n)] for _ in range(m)]
        visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        self.init_reach_visit(can_pacific, visited, 1)  # set row[0], col[0] to True
        self.helper(can_pacific, matrix, visited, 1)

        can_atlantic = [[False for _ in range(n)] for _ in range(m)]
        visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        self.init_reach_visit(can_atlantic, visited, 2) # set row[m - 1], col[n - 1] to True
        self.helper(can_atlantic, matrix, visited, 2)
        result = []
        for i in range(m):
            for j in range(n):
                if can_pacific[i][j] and can_atlantic[i][j]:
                    result.append([i, j])
        return result

    def helper_wrong(self, can_reach, matrix, visited, direction):
        row_list = []
        col_list = []
        if direction == 1:
            row_list = [i for i in range(0, len(matrix))]
            col_list = [j for j in range(0, len(matrix[0]))]
        if direction == 2:
            row_list = [i for i in range(len(matrix) - 1, -1, -1)]
            col_list = [j for j in range(len(matrix[0]) - 1, -1, -1)]
        # !!! wrong here, can't start dfs from any (x, y), only where it's reachable from boarder!!!
        # or do dfs from a queue where seeds are originated from the boarder
        for i in row_list:
            for j in col_list:
                self.dfs(can_reach, matrix, visited, i, j)

    def helper(self, can_reach, matrix, visited, direction):
        row_list = []
        col_list = []
        start_row, start_col = -1, -1
        if direction == 1:
            row_list = [i for i in range(0, len(matrix))]
            col_list = [j for j in range(0, len(matrix[0]))]
            start_row, start_col = 0, 0
        if direction == 2:
            row_list = [i for i in range(len(matrix) - 1, -1, -1)]
            col_list = [j for j in range(len(matrix[0]) - 1, -1, -1)]
            start_row, start_col = len(can_reach) - 1, len(can_reach[0]) - 1
        for i in row_list:
            self.dfs(can_reach, matrix, visited, i, start_col)
        for j in col_list:
            self.dfs(can_reach, matrix, visited, start_row, j)

    # !!! here can_reach and visited may be merged ?? by using different status code instead of True / False?
    # can't set can_reach to false only because visit one time and height is not bigger, because might be able to reach
    # from another direction in later visit. But if one place is can_reach true, then for sure can set visited to true,
    # no need to calc / visit again.
    def dfs(self, can_reach, matrix, visited, x, y):
        delta = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for i in range(4):
            nx, ny = x + delta[i][0], y + delta[i][1]
            if not (0 <= nx < len(can_reach) and 0 <= ny < len(can_reach[0])) or visited[nx][ny]:
                continue
            if matrix[nx][ny] >= matrix[x][y]:
                visited[nx][ny] = True
                can_reach[nx][ny] = True
                # print(x, y, " ==> ", nx, ny)
                self.dfs(can_reach, matrix, visited, nx, ny)


    def init_reach_visit(self, can_reach, visited, direction):
        if direction == 1:
            row = 0
            col = 0
        else:
            row = len(can_reach) - 1
            col = len(can_reach[0]) - 1
        # init the row here
        for j in range(len(can_reach[0])):
            can_reach[row][j] = True
            visited[row][j] = True
        # init the col here
        for i in range(len(can_reach)):
            can_reach[i][col] = True
            visited[i][col] = True



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
        answer = [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
        result = self.sol.pacificAtlantic(matrix)
        self.assertCountEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
