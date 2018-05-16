#coding=utf-8

import unittest

"""

827. Making A Large Island
DescriptionHintsSubmissionsDiscussSolution
In a 2D grid of 0s and 1s, we change at most one 0 to a 1.

After, what is the size of the largest island? (An island is a 4-directionally connected group of 1s).

Example 1:

Input: [[1, 0], [0, 1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: [[1, 1], [1, 0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 1.
Example 3:

Input: [[1, 1], [1, 1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 1.
 

Notes:

1 <= grid.length = grid[0].length <= 50.
0 <= grid[i][j] <= 1.
 
 Difficulty:Hard
Total Accepted:2.2K
Total Submissions:5.1K
Contributor:awice
Subscribe to see which companies asked this question.

Related Topics 
DFS
"""

from collections import defaultdict


class Solution:
    DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def largestIsland(self, grid):
        """
        Basic idea:
        normal case, the 0 grid next to the biggest island will make the max result
        spaceal cases: if the 0 grid will connect two (or MORE) islands that with max SUM of islands' area, then it's the result

        status: cur_island_id, margin_cells ( in a defaultdict ((x,y), [island_size]))
        1) DFS on all possible island, and output the island's size, the margin cells, mark original grid as the island id
        2) check all the margin_cells to find the target margin_cell with global max of sum(island_size)

        cases:
        1) mepty grid, return 0
        2) when margin_cells are empty, return grid size ( all island cells)
        3) ??anything else?
        4) !!!!! when all 0 grid, margin_cells are also empty as 2), but result = 1, should has a flag to tell !!!

        Time: O(size of grid)
        Space: O(size of grid) -- possible same magnitude as the size of grid

        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        island_id = 2  # current island_id
        margin_cells = defaultdict(list)  # global margin cells
        has_island = False  # !!!

        # traverse and dfs on grid to mark island, and process
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    has_island = True  # !!!
                    cur_margin_cells = set()
                    cur_island_area = [0]
                    self.dfs(grid, i, j, island_id, cur_margin_cells, cur_island_area)
                    self.process_margins(margin_cells, cur_margin_cells, cur_island_area)
                    island_id += 1

        # process all margin_cells and get result
        if not margin_cells:
            return len(grid) * len(grid[0]) if has_island else 1  # !!!!
        result = 0
        for cell, island_area_list in margin_cells.items():
            result = max(result, sum(island_area_list))
        return result + 1  # !!! don't forget + 1

    def dfs(self, grid, x, y, island_id, cur_margin_cells, cur_island_area):
        # boarder check
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return
        if grid[x][y] == 1:
            # island cell
            cur_island_area[0] += 1
            grid[x][y] = island_id
            # expand in 4 DIRS and dfs
            for (dx, dy) in self.DIRS:  # !!! need to use self. here
                self.dfs(grid, x + dx, y + dy, island_id, cur_margin_cells, cur_island_area)
        elif grid[x][y] == 0:
            # margin cell
            cur_margin_cells.add((x, y))
        else:
            # other island cell
            return

    def process_margins(self, margin_cells, cur_margin_cells, cur_island_area):
        for (x, y) in cur_margin_cells:
            margin_cells[(x, y)].append(cur_island_area[0])


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = 1
        answer = 1
        result = self.sol.testm(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
"""
https://leetcode.com/problems/making-a-large-island/discuss/127032/C++JavaPython-Straight-Forward-O(N2)-with-Explanations

README
The solution is long, but in fact it is really straight forward.
I suggest not going into my codes but reading my explanations, which should be enough.

Prepare helpful subfunction:
I have several simple sub function to help me on this kind of problem.

valid(int x, int y), check if (x, y) is valid in the grid.
move(int x, int y), return all possible next position in 4 directions.
Explanation, Only 2 steps

Explore every island using DFS, count its area, give it an island index and save the result to a {index: area} map.
Loop every cell == 0, check its connected islands and calculate total islands area.

Java:

import javafx.util.Pair;
class Solution {
    public int N = 0;
    public int largestIsland(int[][] grid) {
        N = grid.length;
        //DFS every island and give it an index of island
        int index = 3, res = 0;
        HashMap<Integer, Integer> area = new HashMap<>();
        for (int x = 0; x < N; ++x) for (int y = 0; y < N; ++y)
            if (grid[x][y] == 1) {
                area.put(index, dfs(grid, x, y, index));
                res = Math.max(res, area.get(index++));
            }

        //traverse every 0 cell and count biggest island it can conntect
        for (int x = 0; x < N; ++x) for (int y = 0; y < N; ++y)
            if (grid[x][y] == 0) {
                HashSet<Integer> seen = new HashSet<>();
                int cur = 1;
                for (Pair<Integer, Integer> p : move(x, y)) {
                    index = grid[p.getKey()][p.getValue()];
                    if (index > 1 && !seen.contains(index)) {
                        seen.add(index);
                        cur += area.get(index);
                    }
                }
                res = Math.max(res, cur);
            }
        return res;
    }

    public List <Pair<Integer, Integer>> move(int x, int y) {
        ArrayList <Pair<Integer, Integer>> res = new ArrayList<>();
        if (valid(x, y + 1)) res.add(new Pair<Integer, Integer>(x, y + 1));
        if (valid(x, y - 1)) res.add(new Pair<Integer, Integer>(x, y - 1));
        if (valid(x + 1, y)) res.add(new Pair<Integer, Integer>(x + 1, y));
        if (valid(x - 1, y)) res.add(new Pair<Integer, Integer>(x - 1, y));
        return res;
    }

    public boolean valid(int x, int y) {
        return 0 <= x && x < N && 0 <= y && y < N;
    }

    public int dfs(int[][] grid, int x, int y, int index) {
        int area = 0;
        grid[x][y] = index;
        for (Pair<Integer, Integer> p : move(x, y))
            if (grid[p.getKey()][p.getValue()] == 1)
                area += dfs(grid, p.getKey(), p.getValue(), index);
        return area + 1;
    }
}


Python:

    def largestIsland(self, grid):
        N = len(grid)
        def move(x, y):
            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if 0 <= x + i < N and 0 <= y + j < N:
                    yield x + i, y + j

        def dfs(x, y, index):
            area = 0
            grid[x][y] = index
            for i, j in move(x, y):
                if grid[i][j] == 1:
                    area += dfs(i, j, index)
            return area + 1

        # DFS every island and give it an index of island
        index = 2
        area = {}
        for x in range(N):
            for y in range(N):
                if grid[x][y] == 1:
                    area[index] = dfs(x, y, index)
                    index += 1

        # traverse every 0 cell and count biggest island it can conntect
        res = max(area.values() or [0])
        for x in range(N):
            for y in range(N):
                if grid[x][y] == 0:
                    possible = set(grid[i][j] for i, j in move(x, y) if grid[i][j] > 1)
                    res = max(res, sum(area[index] for index in possible) + 1)
        return res



https://leetcode.com/problems/making-a-large-island/discuss/127256/DFS-JAVA-AC-CONCISE-SOLUTION
==> This one shows a brute force idea, and time O((m*n)^2) 


"""