
#coding=utf-8

import unittest

"""

218. The Skyline Problem

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a 
distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo 
(Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).

 Buildings  Skyline Contour
The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are 
the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed 
that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles 
grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], 
[19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that 
uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, 
where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. 
Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

The number of buildings in any input list is guaranteed to be in the range [0, 10000].
The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.
There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], 
[7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output 
as such: [...[2 3], [4 5], [12 7], ...]
Credits:
Special thanks to @stellari for adding this problem, creating these two awesome images and all test cases.

Difficulty:Hard
Total Accepted:47K
Total Submissions:170.3K
Contributor: LeetCode
Subscribe to see which companies asked this question.

Related Topics 
Divide and Conquer Heap Binary Indexed Tree Segment Tree 


"""

import functools, heapq


class Solution_REF(object):
    def getSkyline(self, buildings):
        events = sorted(buildings + [[b[1], float("inf"), 0] for b in buildings])
        skyline, curb = [], [(0, float("inf"))]
        for L, R, H in events:
            top = curb[0][0]
            while curb[0][1]<= L:
                heapq.heappop(curb)
            if H > 0:
                heapq.heappush(curb,(-H, R))
            if top != curb[0][0]:
                if skyline and L == skyline[-1][0]:
                    skyline[-1][1] = -curb[0][0]
                else:
                    skyline.append([L, -curb[0][0]])
        return skyline


class Solution(object):  # AC, second time TLE ==> AC, 2.47%, after remove inner class ==> after change remove process, to 40+%,
    def getSkyline(self, buildings):  # TLE on last case, 35/36 cases passed
        """
        Basic idea:
        1. parse input into (x, height, true -- start / false -- close)
        2. sort the converted input according to (x, height)
        3. scan through the inputs, keep current height according to input, when there is changing point, put it to result
        when open: check height with current height, if bigger, append a new start point, else continue
                    -- remember to add to height candidates....
        when clopse: check next height ---> so need to maintain a heap or stack or some structure for potential heights???
        ?? how to store height candidates and keep height order and (quick/or not quickly) remove?

        Time: O(nlogn) + O(n^2)

        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings:
            return []
        # process inputs
        points = self._process_buildings(buildings) # sort points, and merge building when necessary
        # result and status bookkeepoing
        result = []
        heights = [0]  # insert a 0 height for no building case
        for point in points:
            if point[2]:
                if -point[1] > -heights[0]:
                    if result and result[-1][0] == point[0]:      # add if for [-1] here for cases 4
                        result[-1] = [point[0], -point[1]]
                    else:
                        result.append([point[0], -point[1]])
                heapq.heappush(heights, point[1])  # inorder to make a max heap, use -height, and point[1] is already -height,
            else:
                self._remove_point(heights, point) # find and reomve buildingpoint with same height
                if -point[1] > -heights[0]:
                    # result.append([point.x, -heights[0][0]]) # add new interval for new current height
                    if result and result[-1][0] == point[0]:      # add if for [-1] here for cases 4
                        result[-1] = [point[0], -heights[0]]
                    else:
                        result.append([point[0], -heights[0]])

        return result

    def _process_buildings(self, buildings):
        points = []
        for build in buildings:
            a = (build[0], -build[2], True)
            b = (build[1], -build[2], False)
            points.append(a)
            points.append(b)
        points.sort()
        # merge if necessary, only for open and close ones, ignore repeated ones, main method will cover
        merged = []
        i = 0
        while i < len(points) - 1:
            a, b = points[i], points[i + 1]  # !!! miss case 3 because forget i + 1 here
            if a[0] == b[0] and a[1] == b[1] and a[2] == (not b[2]):
                i += 2
                continue
            merged.append(a)
            i += 1
        if i == len(points) - 1:
            merged.append(points[-1])
        return merged

    def _remove_point(self, heights, point):
        for i in range(len(heights)):
            if (point[1]) == (heights[i]):
                heights[i] = heights[-1]
                heights.pop()
                if i < len(heights):
                    heapq._siftup(heights, i)
                    heapq._siftdown(heights, 0, i)
                break

    def _remove_point1(self, heights, point):
        for i in range(len(heights)):
            if (point[1]) == (heights[i]):
                del heights[i]
                break
        heapq.heapify(heights)


class Solution1(object):
    def getSkyline(self, buildings):  # TLE on last case, 35/36 cases passed
        """
        Basic idea:
        1. parse input into (x, height, true -- start / false -- close)
        2. sort the converted input according to (x, height)
        3. scan through the inputs, keep current height according to input, when there is changing point, put it to result
        when open: check height with current height, if bigger, append a new start point, else continue
                    -- remember to add to height candidates....
        when clopse: check next height ---> so need to maintain a heap or stack or some structure for potential heights???
        ?? how to store height candidates and keep height order and (quick/or not quickly) remove?

        Time: O(nlogn) + O(n^2)

        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings:
            return []
        # process inputs
        points = self._process_buildings(buildings) # sort points, and merge building when necessary
        # result and status bookkeepoing
        result = []
        heights = [(0, Solution.BuildingPoint(-1, 0, True))]  # insert a 0 height for no building case
        for point in points:
            if point.open:
                if point.height > -heights[0][0]:
                    if result and result[-1][0] == point.x:      # add if for [-1] here for cases 4
                        result[-1] = [point.x, point.height]
                    else:
                        result.append([point.x, point.height])
                heapq.heappush(heights, (-point.height, point))  # inorder to make a max heap, use -height
            else:
                self._remove_point(heights, point) # find and reomve buildingpoint with same height
                if point.height > -heights[0][0]:
                    # result.append([point.x, -heights[0][0]]) # add new interval for new current height
                    if result and result[-1][0] == point.x:      # add if for [-1] here for cases 4
                        result[-1] = [point.x, -heights[0][0]]
                    else:
                        result.append([point.x, -heights[0][0]])

        return result

    def _process_buildings(self, buildings):
        points = []
        for build in buildings:
            a = Solution.BuildingPoint(build[0], build[2], True)
            b = Solution.BuildingPoint(build[1], build[2], False)
            points.append(a)
            points.append(b)
        points.sort()
        # merge if necessary, only for open and close ones, ignore repeated ones, main method will cover
        merged = []
        i = 0
        while i < len(points) - 1:
            a, b = points[i], points[i + 1]  # !!! miss case 3 because forget i + 1 here
            if a.x == b.x and a.height == b.height and a.open == (not b.open):
                i += 2
                continue
            merged.append(a)
            i += 1
        if i == len(points) - 1:
            merged.append(points[-1])
        return merged

    def _remove_point(self, heights, point):
        for i in range(len(heights)):
            if point.height == -(heights[i][0]):
                del heights[i]
                break
        heapq.heapify(heights)


    @functools.total_ordering
    class BuildingPoint:
        def __init__(self, x, height, open=True):
            self.x = x
            self.height = height
            self.open = open

        def __lt__(self, other):
            return (self.x, -self.height, self.open) < (other.x, -other.height, other.open)  # make open one's first to avoid case 2
            # !!! use -height to make higher ones go first
            #return (self.x, self.height, not self.open) < (other.x, other.height, not other.open)

        def __eq__(self, other):
            return self.x == other.x and self.height == other.height and self.open == other.open






class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ]
        answer = [ [2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0] ]
        result = self.sol.getSkyline(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [ [2, 9, 10], [9, 12, 15]]
        answer = [[2,10],[9,15],[12,0]]  # wrong output as [[2,10],[9,0],[9,15],[12,0]] !!! note there should be cases points are one same x!!!
        result = self.sol.getSkyline(nums)
        self.assertEqual(answer, result)

    def test_case3(self):
        nums = [[0,2,3],[2,5,3]]
        answer = [[0,3],[5,0]]  # wrong output as [[0,3],[2,0],[2,3],[5,0]]  # !!! still should check similar case 2, __lt__ is not enough
        result = self.sol.getSkyline(nums)
        self.assertEqual(answer, result)

    def test_case4(self):
        nums = [[1,2,1],[1,2,2],[1,2,3]]
        answer = [[1,3],[2,0]]   # wrong output as [[1,3],[2,2],[2,1],[2,0]]  !!! when appending to result, always check
        result = self.sol.getSkyline(nums)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""
This is a Python version of my modification of dong.wang.1694's brilliant C++ solution. It sweeps from left to right. 
But it doesn't only keep heights of "alive buildings" in the priority queue and it doesn't remove them as soon as their 
building is left behind. Instead, (height, right) pairs are kept in the priority queue and they stay in there as long 
as there's a larger height in there, not just until their building is left behind.

In each loop, we first check what has the smaller x-coordinate: adding the next building from the input, or removing 
the next building from the queue. In case of a tie, adding buildings wins, as that guarantees correctness 
(think about it :-). We then either add all input buildings starting at that x-coordinate or we remove all 
queued buildings ending at that x-coordinate or earlier (remember we keep buildings in the queue as long as they're 
"under the roof" of a larger actually alive building). And then, if the current maximum height in the queue differs 
from the last in the skyline, we add it to the skyline.


from heapq import *
class Solution:
    #def getSkyline(self, buildings):
    def getSkyline(self, LRH):
        skyline = []
        i, n = 0, len(LRH)
        liveHR = []
        while i < n or liveHR:
            if not liveHR or i < n and LRH[i][0] <= -liveHR[0][1]:
                x = LRH[i][0]
                while i < n and LRH[i][0] == x:
                    heappush(liveHR, (-LRH[i][2], -LRH[i][1]))
                    i += 1
            else:
                x = -liveHR[0][1]
                while liveHR and -liveHR[0][1] <= x:
                    heappop(liveHR)
            height = len(liveHR) and -liveHR[0][0]
            if not skyline or height != skyline[-1][1]:
                skyline += [x, height],
        return skyline
        
        


http://www.cnblogs.com/grandyang/p/4534586.html
这道题一打开又是图又是这么长的题目的，看起来感觉应该是一道相当复杂的题，但是做完之后发现也就那么回事，虽然我不会做，是学习的别人的解法。
这道求天际线的题目应该算是比较新颖的题，要是非要在之前的题目中找一道类似的题，也就只有 Merge Intervals 合并区间了吧，但是与那题不同的是，
这道题不是求被合并成的空间，而是求轮廓线的一些关键的转折点，这就比较复杂了，我们通过仔细观察题目中给的那个例子可以发现，要求的红点都跟每个
小区间的左右区间点有密切的关系，而且进一步发现除了每一个封闭区间的最右边的结束点是楼的右边界点，其余的都是左边界点，而且每个红点的纵坐标都
是当前重合处的最高楼的高度。在网上搜了很多帖子，发现网友百草园的博客上的解法最简洁且易懂，这里完全按照其解法来的。这里用到了multiset数据
结构，其好处在于其中的元素是按堆排好序的，插入新元素进去还是有序的，而且执行删除元素也可方便的将所有相同的元素删掉。这里为了区分左右边界，
将左边界的高度存为负数，这样遇到左边界就存入堆中，遇到右边界就删掉，然后看当前状态有无改变，改变了话就把左边界和当前的高度存入结果中，
具体实现参看代码如下：

 

复制代码
class Solution {
public:
    vector<pair<int, int>> getSkyline(vector<vector<int>>& buildings) {
        vector<pair<int, int> > h, res;
        multiset<int> m;
        int pre = 0, cur = 0;
        for (auto &a : buildings) {
            h.push_back({a[0], -a[2]});
            h.push_back({a[1], a[2]});
        }
        sort(h.begin(), h.end());
        m.insert(0);
        for (auto &a : h) {
            if (a.second < 0) m.insert(-a.second);
            else m.erase(m.find(a.second));
            cur = *m.rbegin();
            if (cur != pre) {
                res.push_back({a.first, cur});
                pre = cur;
            }
        }
        return res;
    }
};

"""

#-*- coding:utf-8 -*-
