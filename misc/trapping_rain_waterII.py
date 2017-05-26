#coding=utf-8

import unittest

"""
407. Trapping Rain Water II

Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the
volume of water it is able to trap after raining.

Note:
Both m and n are less than 110. The height of each unit cell is greater than 0 and is less than 20,000.

Example:

Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.

The above image represents the elevation map [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] before the rain.


After the rain, water are trapped between the blocks. The total volume of water trapped is 4.

Subscribe to see which companies asked this question.

Hide Tags Breadth-first Search Heap
Hide Similar Problems (H) Trapping Rain Water


Hard

"""



class Solution(object):
    def trapRainWater(self, heights):
        if not heights or not heights[0]:
            return 0
        result = 0
        import heapq
        bars = []
        m, n = len(heights), len(heights[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            heapq.heappush(bars, (heights[i][0], i,0))
            heapq.heappush(bars, (heights[i][n-1], i,n-1))
            visited[i][0], visited[i][n-1] = True, True
        for j in range(1,n-1):  # careful , don't repeatedly adding [0][0] and alike points
            heapq.heappush(bars, (heights[0][j], 0,j))
            heapq.heappush(bars, (heights[m-1][j], m-1,j))
            visited[0][j], visited[m-1][j] = True, True
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        while bars:
            tmp = heapq.heappop(bars)
            height, x, y = tmp[0], tmp[1], tmp[2]
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0<=nx<m and 0<=ny<n and not visited[nx][ny]:
                    if heights[nx][ny] < height:
                        result += height - heights[nx][ny]
                        heapq.heappush(bars, (height, nx, ny))
                    else:
                        heapq.heappush(bars, (heights[nx][ny], nx, ny))
                    visited[nx][ny] = True
        return result

    def trapRainWater_wrong(self, heights):
        """
        Can't use the logic "to add result only when current bar is lower than 4 neighbors". As long as the bar is not the
        outer boarder bar, it will accumulate water when it is lower than outer bars, and if the neighboring bars are lower,
        they will also reserve water. Think of a big basin shape matrix.
        :param heights: 
        :return: 
        """
        if not heights or not heights[0]:
            return 0
        result = 0
        import heapq
        bars = []
        m, n = len(heights), len(heights[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            heapq.heappush(bars, (heights[i][0], i,0))
            heapq.heappush(bars, (heights[i][n-1], i,n-1))
            visited[i][0], visited[i][n-1] = True, True
        for j in range(1,n-1):  # careful , don't repeatedly adding [0][0] and alike points
            heapq.heappush(bars, (heights[0][j], 0,j))
            heapq.heappush(bars, (heights[m-1][j], m-1,j))
            visited[0][j], visited[m-1][j] = True, True
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        while bars:
            tmp = heapq.heappop(bars)
            height, x, y = tmp[0], tmp[1], tmp[2]
            neighbors = []
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0<=nx<m and 0<=ny<n:
                    neighbors.append(heights[nx][ny])
                    if not visited[nx][ny]:
                        heapq.heappush(bars, (heights[nx][ny], nx, ny))
                        visited[nx][ny] = True
            if len(neighbors) == 4:
                top = min(neighbors)
                if top > height:
                    result += top - height
                    heights[x][y] = top
        return result

    def trapRainWater_wrong(self, heights):
        if not heights or not heights[0]:
            return 0
        result = 0
        import heapq
        bars = []
        m, n = len(heights), len(heights[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            heapq.heappush(bars, (i,0,heights[i][0]))  # wrong here, heights should be the first one for the  heap to work
            heapq.heappush(bars, (i,n-1,heights[i][n-1]))
            visited[i][0], visited[i][n-1] = True, True
        for j in range(1,n-1):  # careful , don't repeatedly adding [0][0] and alike points
            heapq.heappush(bars, (0,j,heights[0][j]))
            heapq.heappush(bars, (m-1,j,heights[m-1][j]))
            visited[0][j], visited[m-1][j] = True, True
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        while bars:
            tmp = heapq.heappop(bars)
            x, y, height = tmp[0], tmp[1], tmp[2]
            neighbors = []
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0<=nx<m and 0<=ny<n:
                    neighbors.append(heights[nx][ny])
                    if not visited[nx][ny]:
                        heapq.heappush(bars, (nx, ny,heights[nx][ny]))
                        visited[nx][ny] = True
            if len(neighbors) == 4:
                top = min(neighbors)
                if top > height:
                    result += top - height
                    heights[x][y] = top
        return result

    def trapRainWater1(self, heights): #252ms, 60%
        """
        Use the min-heap and init with outer layer, the lowest one will always be found first, process and then expand
        to the 'connected' new neighbors, similar to find the new outer layer for the remaining (inside nodes).
        1) lowest bar in heap will always be popped first, guarantee that water level is decided by lowest bar
           ( won't be higher, because water can't be kept higher than the outer lowest bar; won't be lower, because
            the bar is got from min-heap, guarantee that lowest ba will be reached first)
        2) one by one, all the bars will finally be pushed to queue, which means whole area was covered.

        :type heightMap: List[List[int]]
        :rtype: int
        """
        import heapq
        if not heights or not heights[0]:
            return 0  # don't return 0, should return 0
        walls = []
        m, n = len(heights), len(heights[0])
        visited = [ [False for j in range(n)] for i in range(m)]
        water = 0
        for i in range(m):
            heapq.heappush(walls, (heights[i][0], i, 0))
            visited[i][0] = True
            heapq.heappush(walls, (heights[i][n-1], i, n-1))
            visited[i][n-1] = True
        for j in range(1,n-1):
            heapq.heappush(walls, (heights[0][j], 0, j))
            visited[0][j] = True
            heapq.heappush(walls, (heights[m-1][j], m-1, j))
            visited[m-1][j] = True

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        while walls:
            cur = heapq.heappop(walls)
            height, x, y = cur[0], cur[1], cur[2]
            for next in range(4):
                nx = x + dx[next]
                ny = y + dy[next]
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    nheight = heights[nx][ny]
                    if nheight < height:
                        water += height - nheight
                    heapq.heappush(walls, (max(nheight, height),nx, ny))
                    visited[nx][ny] = True # DO NOT forget this one
        return water














    def trapRainWater_ref(self, heights): #219ms, 88%
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        from heapq import heappush, heappop
        if heights == []:
            return 0

        m, n = len(heights), len(heights[0])
        visited = [ [ 0 for _ in range(n) ] for _ in range(m) ]
        offsets = [ (-1, 0), (0, -1), (1, 0), (0, 1) ]

        # Get the boundary.
        min_heap = [] # A priority queue
        for i in range(m):
            heappush(min_heap, (heights[i][0], i, 0))
            visited[i][0] = 1
            heappush(min_heap, (heights[i][n-1], i, n-1))
            visited[i][n-1] = 1
        for i in range(n):
            heappush(min_heap, (heights[0][i], 0, i))
            visited[0][i] = 1
            heappush(min_heap, (heights[m-1][i], m-1, i))
            visited[m-1][i] = 1

        # Start from the current shortest among the ones in the queue.
        # This ensures that a point would be explored from the LOWEST point around it!
        total_water = 0
        while min_heap:
            h, x, y = heappop(min_heap)
            for dx, dy in offsets:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < m and 0 <= new_y < n and not visited[new_x][new_y]:
                    visited[new_x][new_y] = 1
                    new_h = max(h, heights[new_x][new_y])
                    heappush(min_heap, (new_h, new_x, new_y))
                    if h > heights[new_x][new_y]:
                        total_water += h - heights[new_x][new_y]
        return total_water


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [
          [1,4,3,1,3,2],
          [3,2,1,3,2,4],
          [2,3,3,2,3,1]
        ]
        answer = 4
        result = self.sol.trapRainWater(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [
            [12,13,0,12],
            [13,4,13,12],
            [13,8,10,12],
            [12,13,12,12],
            [13,13,13,13]

        ]
        answer = 14
        result = self.sol.trapRainWater(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""

九章管理员
由于水是往低处流的， 所以对于这一类trapping water 问题，我们只用从最外层开始往内接雨水就可以。

首先对矩阵外层需要找到最小的柱子，那么就想到用堆，每次堆帮助我们在外层的所有柱子里面找到最小的那根表示可以接的雨水的高度至少是多少，然后进行
BSF遍历，如果值相等，继续往下走，如果遇到比当前值小的，或者边境，说明该水流会流出去（遇到这种情况对遍历的数据置为-1）说明往后连通该区域的水
都会流出去，如果BFS一遍发现没有到边界和遇到比起小的点，则将遍历过的点的值设为遇到的最小的点，并更新水的流量，继续进行遍历。直至所有点都为-1
为止，输出结果。

参考代码：http://www.jiuzhang.com/solutions/trapping-rain-water-ii/

"""

#-*- coding:utf-8 -*-
