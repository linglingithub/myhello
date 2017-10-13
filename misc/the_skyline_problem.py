
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


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ]
        answer = [ [2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0] ]
        result = self.sol.getSkyline(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""
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
