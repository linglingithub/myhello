#coding=utf-8

import unittest

"""
K Closest Points

Given some points and a point origin in two dimensional space, find k points out of the some points which are nearest to origin.
Return these points sorted by distance, if they are same with distance, sorted by x-axis, otherwise sorted by y-axis.

Have you met this question in a real interview? Yes
Example
Given points = [[4,6],[4,7],[4,4],[2,5],[1,1]], origin = [0, 0], k = 3
return [[1,1],[2,5],[4,4]]

Tags 
LinkedIn Heap Amazon
Related Problems 

"""



# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param {Pint[]} points a list of points
    # @param {Point} origin a point
    # @param {int} k an integer
    # @return {Pint[]} the k closest points
    def kClosest(self, points, origin, k):  # accepted by Lintcode
    def kClosest(self, points, origin, k):  # accepted by Lintcode
        # Write your code here
        import heapq
        if not points or not k:
            return []
        result = []
        for point in points:
            dist = (point.x-origin.x)**2 + (point.y-origin.y)**2
            if len(result) < k:
                heapq.heappush(result, (-dist, -point.x, -point.y, point))
            else:
                far_dist, px, py, far_point = result[0]
                if dist < -far_dist:
                   heapq.heappop(result)
                   heapq.heappush(result, (-dist, -point.x, -point.y, point))
        res = []
        while result:
            dist, x, y, point = heapq.heappop(result)
            res.insert(0, point)
        return res


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [[4,6],[4,7],[4,4],[2,5],[1,1]]
        origin = [0,0]
        k = 3
        answer = [[1,1],[2,5],[4,4]]
        result = self.sol.kClosest(nums, origin, k)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
