#coding=utf-8

import unittest

"""

149. Max Points on a Line
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Difficulty:Hard
Total Accepted:83.3K
Total Submissions:545.1K
Contributor: LeetCode
Subscribe to see which companies asked this question.

Related Topics 
Hash Table Math 
Similar Questions 
Line Reflection 

"""


# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):  # 97%
        """
        :type points: List[Point]
        :rtype: int
        """
        if not points:
            return 0
        if len(points) <= 2:
            return len(points)
        res = 0

        for i in range(len(points)):
            pa = points[i]
            vertical_cnt = 0  # vertical points of pa
            same_cnt = 0  # other points are same point as pa
            max_cnt = 0  # max points for pa's perspective
            slopes = {}
            for j in range(i + 1, len(points)):
                pb = points[j]
                if pb.x == pa.x:
                    if pb.y == pa.y:
                        same_cnt += 1
                    else:
                        vertical_cnt += 1
                else:
                    slope = 10* (float)(pb.y - pa.y) / (pb.x - pa.x)
                    # need to apply 10 for case3, need to apply 100 for case4
                    # after add float, only need to apply 10 for case 3
                    slopes[slope] = slopes.get(slope, 0) + 1
                    max_cnt = max(max_cnt, slopes[slope])
            max_cnt = max(max_cnt, vertical_cnt) + same_cnt + 1  # should be at the end of each point i, not point j
            res = max(max_cnt, res)
        return res


    def maxPoints_wrong(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if not points:
            return 0
        if len(points) <= 2:
            return len(points)
        res = 0
        slopes = {}
        for i in range(len(points)):
            pa = points[i]
            for j in range(i+1, len(points)):
                pb = points[j]
                if pb.x == pa.x:
                    if pb.y == pa.y:
                        continue  # to count as one point or two points? --> no, need to take into count
                    slope = 'n/a'  # wrong here, can have different vertical lines
                else:
                    slope = (pb.y-pa.y) / (pb.x - pa.x)
                slopes[slope] = slopes.get(slope, 0) + 1
                res = max(slopes[slope], res)
        return res + 1

    def maxPoints_ref(self, points):
        """
        add *10 myself for the ref to pass case2.
        :type points: List[Point]
        :rtype: int
        """
        len_points = len(points)
        if len_points <= 1:
            return len_points
        max_count = 0
        for index1 in range(0, len_points):
            p1 = points[index1]
            gradients = {}
            infinite_count = 0
            duplicate_count = 0
            for index2 in range(index1, len_points):
                p2 = points[index2]
                dx = p2.x - p1.x
                dy = p2.y - p1.y
                if 0 == dx and 0 == dy:
                    duplicate_count += 1
                if 0 == dx:
                    infinite_count += 1
                else:
                    g = float(dy) * 10 / float(dx)   # need to add *10 to improve the precision, otherwise wrong for case2
                    gradients[g] = (gradients[g] + 1 if gradients.has_key(g) else 1)
            if infinite_count > max_count:
                max_count = infinite_count
            for k, v in gradients.items():
                v += duplicate_count
                if v > max_count:
                    max_count = v
        return max_count

from util.point_2d import Point

class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()


    def test_case1(self):   # ===>
        nums = [[0,0],[-1,-1],[2,2]]
        nums = Point.get_points_from_array(nums)
        answer = 3
        result = self.sol.maxPoints(nums)
        self.assertEqual(answer, result)

    def test_case2(self):   # ===>
        nums = [[0,0],[94911151,94911150],[94911152,94911151]]
        nums = Point.get_points_from_array(nums)
        answer = 2
        result = self.sol.maxPoints(nums)
        self.assertEqual(answer, result)

    def test_case3(self):   # ===>
        nums = [[0,0],[1,1],[1,-1]]
        nums = Point.get_points_from_array(nums)
        answer = 2
        result = self.sol.maxPoints(nums)
        self.assertEqual(answer, result)

    def test_case4(self):   # ===>
        nums = [[40,-23],[9,138],[429,115],[50,-17],[-3,80],[-10,33],[5,-21],[-3,80],[-6,-65],[-18,26],[-6,-65],[5,72],[0,77],[-9,86],[10,-2],[-8,85],[21,130],[18,-6],[-18,26],[-1,-15],[10,-2],[8,69],[-4,63],[0,3],[-4,40],[-7,84],[-8,7],[30,154],[16,-5],[6,90],[18,-6],[5,77],[-4,77],[7,-13],[-1,-45],[16,-5],[-9,86],[-16,11],[-7,84],[1,76],[3,77],[10,67],[1,-37],[-10,-81],[4,-11],[-20,13],[-10,77],[6,-17],[-27,2],[-10,-81],[10,-1],[-9,1],[-8,43],[2,2],[2,-21],[3,82],[8,-1],[10,-1],[-9,1],[-12,42],[16,-5],[-5,-61],[20,-7],[9,-35],[10,6],[12,106],[5,-21],[-5,82],[6,71],[-15,34],[-10,87],[-14,-12],[12,106],[-5,82],[-46,-45],[-4,63],[16,-5],[4,1],[-3,-53],[0,-17],[9,98],[-18,26],[-9,86],[2,77],[-2,-49],[1,76],[-3,-38],[-8,7],[-17,-37],[5,72],[10,-37],[-4,-57],[-3,-53],[3,74],[-3,-11],[-8,7],[1,88],[-12,42],[1,-37],[2,77],[-6,77],[5,72],[-4,-57],[-18,-33],[-12,42],[-9,86],[2,77],[-8,77],[-3,77],[9,-42],[16,41],[-29,-37],[0,-41],[-21,18],[-27,-34],[0,77],[3,74],[-7,-69],[-21,18],[27,146],[-20,13],[21,130],[-6,-65],[14,-4],[0,3],[9,-5],[6,-29],[-2,73],[-1,-15],[1,76],[-4,77],[6,-29]]
        nums = Point.get_points_from_array(nums)
        answer = 25
        result = self.sol.maxPoints(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""
解这个平面几何题有3个要点：

1. 如何判断共线?
两点成一直线，所以两点没有共线不共线之说。对于点p1(x1, y1)，p2(x2, y2)，p3(x3, y3)来说，共线的条件是p1-p2连线的斜率与p1-p3连线的斜率
相同，即
(y2-y1)/(x2-x1) = (y3-y1)/(x3-x1)
所以对共线的n点，其中任意两点连线的斜率相同。

2. 如何判断最多的共线点?
对于每个点p出发，计算该点到所有其他点qi的斜率，对每个斜率统计有多少个点符合。其中最多的个数加1（出发点本身）即为最多的共线点。

3. 特殊情况
当x1 = x2，y1!=y2时，为垂直连线。计算斜率时分母为0会出错。
当x1 = x2，y1 = y2时，两点重合。则(x2, y2)和所有(x1, y1)的连线共线。


"""

#-*- coding:utf-8 -*-
