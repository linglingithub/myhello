#coding=utf-8

import unittest

"""

Number of Airplanes in the Sky

Given an interval list which are flying and landing time of the flight. How many airplanes are on the sky at most?

 Notice

If landing and flying happens at the same time, we consider landing should happen at first.

Have you met this question in a real interview? Yes
Example
For interval list

[
  [1,10],
  [2,3],
  [5,8],
  [4,7]
]
Return 3

Tags
LintCode Copyright Array Interval
Related Problems
Easy Merge Intervals

"""



#Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    # @param airplanes, a list of Interval
    # @return an integer
    def countOfAirplanes(self, airplanes):
        if not airplanes:
            return 0
        res = 0
        timeline = []
        for plane in airplanes:
            timeline.append((plane.start, 1))
            timeline.append((plane.end, -1))
        timeline.sort(key=lambda x: (x[0], x[1]))  # sort according to starting time, when one start is same with another end, put ending one first
        cnt = 0
        for point in timeline:
            if point[1] == 1:
                cnt += 1
                res = max(res, cnt)
            else:
                cnt -= 1
        return res


class Solution1:
    # @param airplanes, a list of Interval
    # @return an integer
    def countOfAirplanes(self, airplanes):
        # write your code here
        if not airplanes:
            return 0
        timeline = []
        for plane in airplanes:
            timeline.append((plane.start, 1))
            timeline.append((plane.end, -1))
        timeline.sort(key=lambda tup: tup[0] * 10 + tup[1])
        result = 0
        plane_cnt = 0
        for time, flag in timeline:
            plane_cnt += flag
            result = max(result, plane_cnt)
        return result


    def countOfAirplanes1(self, airplanes):
        # write your code here
        if not airplanes:
            return 0
        timeline = []
        for plane in airplanes:
            timeline.append((plane.start, 1))
            timeline.append((plane.end, 0))
        timeline.sort(key=lambda tup: tup[0] * 100 + tup[1])
        result = 0
        plane_cnt = 0
        for point in timeline:
            if point[1] == 1:
                plane_cnt += 1
                result = max(result, plane_cnt)
            else:
                plane_cnt -= 1
        return result



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [
          [1,10],
          [2,3],
          [5,8],
          [4,7]
        ]
        planes = [Interval(x,y) for x, y in nums]
        answer = 3
        result = self.sol.countOfAirplanes(planes)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
