#coding=utf-8

import unittest

"""

Build Post Office II

Given a 2D grid, each cell is either a wall 2, an house 1 or empty 0 (the number zero, one, two), find a place to build 
a post office so that the sum of the distance from the post office to all the houses is smallest.

Return the smallest sum of distance. Return -1 if it is not possible.

 Notice

You cannot pass through wall and house, but can pass through empty.
You only build post office on an empty.
Have you met this question in a real interview? Yes
Example
Given a grid:

0 1 0 0 0
1 0 0 2 1
0 1 0 0 0
return 8, You can build at (1,1). (Placing a post office at (1,1), the distance that post office to all the house sum 
is smallest.)

Challenge 
Solve this problem within O(n^3) time.

Tags 
Breadth First Search Zenefits Google
Related Problems 
Hard Build Post Office

Hard

"""

import sys
import collections

class Solution:  # ref
    # @param {int[][]} grid a 2D grid
    # @return {int} an integer
    def shortestDistance(self, grid):
        # Write your code here
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])

        # for every empty space, the sum of distances to each house ( if reachable ), init as maxint
        dist = [[sys.maxint for j in range(n)] for i in range(m)]
        # for every empty space, the count of reachable houses, init as 0
        reachable_count = [[0 for j in range(n)] for i in range(m)]
        # the mininum distance sum (of the best post office to all houses), init as maxint
        min_dist = sys.maxint

        # total number of houses, and init as 0
        buildings = 0

        # for every house, use BFS to update the dist and reachable_count, and get the total number of houses
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.bfs(grid, i, j, dist, m, n, reachable_count)
                    buildings += 1


        # for every empty space, check if it is the best office place, if no space is reachable to all houses, return -1
        for i in range(m):
            for j in range(n):
                if reachable_count[i][j] == buildings and dist[i][j] < min_dist:
                    min_dist = dist[i][j]
        return min_dist if min_dist != sys.maxint else -1

    def bfs(self, grid, i, j, dist, m, n, reachable_count):
        """
        use queue to do bfs
        :param grid: the input grid
        :param i: the current house's i
        :param j: the current house's j
        :param dist: the distance matrix for empty spaces
        :param m: 
        :param n: 
        :param reachable_count: the reachable house count matrix for empty spaces
        :return: 
        """
        visited = [[False for y in range(n)] for x in range(m)]
        visited[i][j] = True
        q = collections.deque([(i, j, 0)]) # the deque for BFS, i, j is the position, 0 is the distance to given house

        while q:
            i, j, l = q.popleft()
            if dist[i][j] == sys.maxint:
                dist[i][j] = 0
            dist[i][j] += l  # accumulate the bfs distance to each empty space

            # for all neighboring 4 spots, if valid and not visited and is empty space --> set visit, update bfs distance enque, update reachable
            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = i + x, j + y

                if nx > -1 and nx < m and ny > -1 and ny < n and not visited[nx][ny] and grid[nx][ny] == 0:
                    #visited[nx][ny] = True
                    #if grid[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append((nx, ny, l + 1))
                    reachable_count[nx][ny] += 1





class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [
            [0, 1, 0, 0, 0],
            [1, 0, 0, 2, 1],
            [0, 1, 0, 0, 0]
        ]
        answer = 8  # [1, 1]
        result = self.sol.shortestDistance(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""

作为上一题的变形，在这一题的题设中，这里的网格多了一种类型 - 墙 2，而且房子也被当做障碍物处理，即不能通过。这样的话，我们就不能利用上一题的
解法，而要采用图论中的最短路径解法了，BFS 就是一种常用的选择。

同样，最开始能够想到的也是暴力算法，即穷举每一块空地，然后用 BFS 算一下到所有房子的距离，代码实现起来也不难，就略过了。

但是这里还有另外一个角度来思考这个问题，即从房子的角度来看。也是用 BFS 来遍历所有的空地，不过这里就需要在每个空地中记录房子访问次数和房子距
离之和了。记录访问次数是为了确保所有房子都能访问到该空地，否则就不是可行解。这种解法的优势是在于当房子数目远小于空地数目时比上面从空地出发进
行 BFS 要更快一些。所以这也是一种权衡（trade-off）了，要视数据集的具体情况而定。



========================================================================================================================

这道题和I比较类似，但是因为不能穿过wall和house，所以必须用bfs的方法搜索最近距离，而不能直接计算几何距离。
1. 将数组扫描一遍找到所有房子。
2. 为每一个房子建立一个距离矩阵，计算该房子到所有0点的距离。即distance[i][j][k]为k房子到grid[i][j]上的点的距离。计算距离的时候用bfs搜
索。
3. 然后遍历图上所有为0的点，查询k张距离矩阵，将所有房子到该点的距离加起来即为在该点建邮局的距离总和。若在查询过程中遇到某个点在某张距离矩阵
上的
值为无穷大，则说明该点无法到达该房子，直接停止搜索即可。
4. 选3中距离最小的点即可。+

public class Solution {
    /**
     * @param grid a 2D grid
     * @return an integer
     */
    class Node{
        int x;
        int y;
        int dis;
        public Node(int x, int y, int dis){
            this.x = x;
            this.y = y;
            this.dis = dis;
        }
    }

    public int shortestDistance(int[][] grid) {
        // Write your code here
        if(grid == null || grid.length == 0 || grid[0].length == 0){
            return -1;
        }

        int n = grid.length;
        int m = grid[0].length;
        ArrayList<Node> house = new ArrayList<Node>();
        //find all houses, with pos(i,j) and distance 0
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(grid[i][j] == 1){
                    house.add(new Node(i, j, 0));
                }
            }
        }
        //no empty place, k -- number of houses
        int k = house.size();
        if(k == n * m){
            return -1;
        }
        
        // init all distances as max values
        int[][][] distance = new int[k][n][m];
        for(int i = 0; i < k; i++){
            for(int j = 0; j < n; j++){
                Arrays.fill(distance[i][j], Integer.MAX_VALUE);
            }
        }

        // get all distances for each house to each possible empty places
        for(int i = 0; i < k; i++){
            getDistance(house.get(i), distance, i, grid);
        }

        // for every position in grid, find the distance sum to all k houses
        // outer loop: n, m; inner loop to sum up the distance, k
        int min = Integer.MAX_VALUE;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(grid[i][j] == 0){
                    int sum = 0;
                    for(int l = 0; l < k; l++){
                        if(distance[l][i][j] == Integer.MAX_VALUE){
                            sum = Integer.MAX_VALUE;
                            break;
                        }
                        sum += distance[l][i][j];
                    }
                    min = Math.min(min, sum);
                }
            }
        }

        if(min == Integer.MAX_VALUE){
            return -1;
        }
        return min;
    }

    int[] dx = {-1, 1, 0, 0};
    int[] dy = {0, 0, -1, 1};
    //BFS search to find the distances kth house to all other empty places.
    private void getDistance(Node curt, int[][][] distance, int k, int[][] grid){
        // curt is the house, k means the kth house
        int n = grid.length;
        int m = grid[0].length;
        Queue<Node> queue = new LinkedList<Node>();
        boolean[][] visited = new boolean[n][m];
        // starting point of BFS is the house itself, with curt.dis = 0
        queue.offer(curt);
        // set house's place as visited
        visited[curt.x][curt.y] = true;

        while(!queue.isEmpty()){
            Node now = queue.poll();
            for(int i = 0; i < 4; i++){
                int nextX = now.x + dx[i];
                int nextY = now.y + dy[i];
                // for all 4 neighboring empty places of now, set dis+1, enque, visited
                if(nextX >= 0 && nextX < n && nextY >= 0 && nextY < m && grid[nextX][nextY] == 0 && !visited[nextX][nextY]){
                    distance[k][nextX][nextY] = now.dis + 1;
                    queue.add(new Node(nextX, nextY, now.dis + 1));
                    visited[nextX][nextY] = true;
                }
            }
        }
    }
}

=======================================================

========================================================================================================================

class Solution:
    # @param {int[][]} grid a 2D grid
    # @return {int} an integer
    def shortestDistance(self, grid):
        # Write your code here
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        
        dist = [[sys.maxint for j in range(n)] for i in range(m)]
        reachable_count = [[0 for j in range(n)] for i in range(m)]
        min_dist = sys.maxint
        
        buildings = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.bfs(grid, i, j, dist, m, n, reachable_count)
                    buildings += 1
  
        for i in range(m):
            for j in range(n):
                if reachable_count[i][j] == buildings and dist[i][j] < min_dist:
                    min_dist = dist[i][j]
        return min_dist if min_dist != sys.maxint else -1
        
    def bfs(self, grid, i, j, dist, m, n, reachable_count):
        visited = [[False for y in range(n)] for x in range(m)]
        visited[i][j] = True
        q = collections.deque([(i,j, 0)])
        
        while q:
            i, j, l = q.popleft()
            if dist[i][j] == sys.maxint:
                dist[i][j] = 0
            dist[i][j] += l

            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = i+x, j+y

                if nx > -1 and nx < m and ny > -1 and ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    if grid[nx][ny] == 0:
                        q.append((nx, ny, l+1))
                        reachable_count[nx][ny] += 1 

"""