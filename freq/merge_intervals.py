#coding=utf-8

import unittest

"""

56. Merge Intervals
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].

Seen this question in a real interview before?   Yes  

Difficulty:Medium
Total Accepted:137.2K
Total Submissions:455.7K
Contributor: LeetCode
Subscribe to see which companies asked this question.

Related Topics 
Array Sort 
Similar Questions 
Insert Interval Meeting Rooms Meeting Rooms II Teemo Attacking Add Bold Tag in String 

"""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    """
    @param: intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        # write your code here
        if not intervals or len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda x: (x.start, x.end))
        result = [intervals[0]]
        for tmp in intervals[1:]:
            if result[-1].end >= tmp.start:
                result[-1].end = max(result[-1].end, tmp.end)
            else:
                result.append(tmp)
        return result

    def merge1(self, intervals):
        # write your code here
        if not intervals or len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda x: (x.start, x.end))
        start, end = intervals[0].start, intervals[0].end
        result = []
        for i in range(1, len(intervals)):
            tmp = intervals[i]
            if end >= tmp.start:
                end = max(end, tmp.end)
            else:
                result.append([start, end])
                start, end = tmp.start, tmp.end
        # don't forget the last step !!!
        result.append([start, end])
        return result

class Solution1(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []  # expect [] not None
        #intervals.sort(key=lambda x, y: x.end-y.end if x.start==y.start else x.start-y.start)
        intervals.sort(key=lambda x: (x.start, x.end))
        #intervals.sort(key=lambda x: (x[0], x[1]))
        result = []
        for interval in intervals:
            if not result or result[-1].end < interval.start:
            #if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                if result[-1].end < interval.end:   # need to add check of this, otherwise wrong for case2
                    result[-1].end = interval.end
                #result[-1][1] = interval[1]
        return result


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [[1,3],[2,6],[8,10],[15,18]]
        answer = [[1,6],[8,10],[15,18]]
        result = self.sol.merge(nums)
        self.assertEqual(answer, result)


    def test_case2(self):
        nums = [[1,4],[2,3]]
        answer = [[1,4]]
        result = self.sol.merge(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""

1. Sort the intervals based on increasing order of 
    starting time.
2. Push the first interval on to a stack.
3. For each interval do the following
   a. If the current interval does not overlap with the stack 
       top, push it.
   b. If the current interval overlaps with stack top and ending
       time of current interval is more than that of stack top, 
       update stack top with the ending  time of current interval.
4. At the end stack contains the merged intervals. 

Time complexity of the method is O(nLogn) which is for sorting. Once the array of intervals is sorted, merging takes 
linear time.

A O(n Log n) and O(1) Extra Space Solution

A O(n Log n) and O(1) Extra Space Solution
The above solution requires O(n) extra space for stack. We can avoid use of extra space by doing merge operations 
in-place. Below are detailed steps.

1) Sort all intervals in decreasing order of start time.
2) Traverse sorted intervals starting from first interval, 
   do following for every interval.
      a) If current interval is not first interval and it 
         overlaps with previous interval, then merge it with
         previous interval. Keep doing it while the interval
         overlaps with the previous one.         
      b) Else add current interval to output list of intervals.
Note that if intervals are sorted by decreasing order of start times, we can quickly check if intervals overlap or not 
by comparing start time of previous interval with end time of current interval.


    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x: x.start)
        result = []
        for interval in intervals:
            if len(result) == 0 or result[-1].end < interval.start:
                result.append(interval)
            else:
                result[-1].end = max(result[-1].end, interval.end)
        return result


"""