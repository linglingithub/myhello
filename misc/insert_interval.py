#coding=utf-8

import unittest

"""

57. Insert Interval

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

Hard

===============

Given a non-overlapping interval list which is sorted by start point.

Insert a new interval into it, make sure the list is still in order and non-overlapping (merge intervals if necessary).

Have you met this question in a real interview? Yes
Example
Insert [2, 5] into [[1,2], [5,9]], we get [[1,9]].

Insert [3, 4] into [[1,2], [5,9]], we get [[1,2], [3,4], [5,9]].


Tags 
LinkedIn Basic Implementation Google
Related Problems 
Easy Merge Intervals


"""


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        Important to thinks about corner cases.
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]
        left, right, n = 0, 0, len(intervals)
        while left < n and intervals[left].end < newInterval.start:  # left included
            left += 1
        right = left
        while right < n and intervals[right].start <= newInterval.end: # right excluded
            right += 1
        if left == 0 and intervals[0].start > newInterval.end:  # opposite case for case4 !!!
            return [newInterval] + intervals

        if left == n: # add for case4
            return intervals + [newInterval]

        s = min(intervals[left].start, newInterval.start) # think about case4 !!!
        e = max(intervals[right-1].end, newInterval.end)   # single interval, override by whoe newInterval, other corner cases?
        mergeInterval = Interval(s, e)
        return intervals[:left] + [mergeInterval] + intervals[right:]


class Solution1(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            if not newInterval:
                return []
            else:
                return [[newInterval.start, newInterval.end]]
        result = []
        left, right = 0, 0
        n = len(intervals)
        # find left idx
        left, lwithin = self.search(intervals, newInterval.start, 0)
        # find right idx
        right, rwithin = self.search(intervals, newInterval.end, left)
        # process and insert
        for idx in range(0, left):
            result.append(intervals[idx])

        if lwithin:
            newInterval.start = intervals[left].start
        if rwithin:
            newInterval.end = intervals[right].end
        result.append(newInterval)
        if rwithin:
            right += 1 # should add this, otherwise repeated adding, see case 03

        for idx in range(right, n):
            result.append(intervals[idx])
        return result

    def search(self, intervals, target, start):
        idx = start
        within = False
        while idx < len(intervals):
            tmp = intervals[idx]
            if target < tmp.start:
                return idx, within
            if target >= tmp.start:
                within = True
            if target > tmp.end:
                within = False
            else:
                return idx, within
            idx += 1
        return len(intervals), False

class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case04(self):   # =====> Line 22: IndexError: list index out of range
        nums = [[1,5]]
        newinv = [2,3]
        answer = [[1,5]]
        from util.interval import Interval
        result = self.sol.insert(Interval.generate_intervals(nums), Interval(newinv[0], newinv[1]))
        result = Interval.generate_list(result)
        self.assertEqual(answer, result)


    def test_case3(self):   # =====> wrong output as [[1,5], [1,5]]
        nums = [[1,5]]
        newinv = [2,3]
        answer = [[1,5]]
        from util.interval import Interval
        result = self.sol.insert(Interval.generate_intervals(nums), Interval(newinv[0], newinv[1]))
        result = Interval.generate_list(result)
        self.assertEqual(answer, result)


    def test_case1(self):
        nums = [[1,3],[6,9]]
        newinv = [2,5]
        answer = [[1,5],[6,9]]
        from util.interval import Interval
        result = self.sol.insert(Interval.generate_intervals(nums), Interval(newinv[0], newinv[1]))
        result = Interval.generate_list(result)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [[1,2],[3,5],[6,7],[8,10],[12,16]]
        newinv = [4,9]
        answer = [[1,2],[3,10],[12,16]]
        from util.interval import Interval
        result = self.sol.insert(Interval.generate_intervals(nums), Interval(newinv[0], newinv[1]))
        result = Interval.generate_list(result)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""

# simple and good solution in Java

public List<Interval> insert(List<Interval> intervals, Interval newInterval) {
    List<Interval> result = new LinkedList<>();
    int i = 0;
    // add all the intervals ending before newInterval starts
    while (i < intervals.size() && intervals.get(i).end < newInterval.start)
        result.add(intervals.get(i++));
    // merge all overlapping intervals to one considering newInterval
    while (i < intervals.size() && intervals.get(i).start <= newInterval.end) {
        newInterval = new Interval( // we could mutate newInterval here also
                Math.min(newInterval.start, intervals.get(i).start),
                Math.max(newInterval.end, intervals.get(i).end));
        i++;
    }
    result.add(newInterval); // add the union of intervals we got
    // add all the rest
    while (i < intervals.size()) result.add(intervals.get(i++)); 
    return result;
}


========================================================================================

# good solutions in python


Solution 1: (7 lines, 88 ms)

Collect the intervals strictly left or right of the new interval, then merge the new one with the middle ones (if any) 
before inserting it between left and right ones.

def insert(self, intervals, newInterval):
    s, e = newInterval.start, newInterval.end
    left = [i for i in intervals if i.end < s]
    right = [i for i in intervals if i.start > e]
    if left + right != intervals:
        s = min(s, intervals[len(left)].start)
        e = max(e, intervals[~len(right)].end)
    return left + [Interval(s, e)] + right
Solution 2: (8 lines, 84 ms)

Same algorithm as solution 1, but different implementation with only one pass and explicitly collecting the to-be-merged 
intervals.

def insert(self, intervals, newInterval):
    s, e = newInterval.start, newInterval.end
    parts = merge, left, right = [], [], []
    for i in intervals:
        parts[(i.end < s) - (i.start > e)].append(i)
    if merge:
        s = min(s, merge[0].start)
        e = max(e, merge[-1].end)
    return left + [Interval(s, e)] + right
Solution 3: (11 lines, 80 ms)

Same again, but collect and merge while going over the intervals once.

def insert(self, intervals, newInterval):
    s, e = newInterval.start, newInterval.end
    left, right = [], []
    for i in intervals:
        if i.end < s:
            left += i,
        elif i.start > e:
            right += i,
        else:
            s = min(s, i.start)
            e = max(e, i.end)
    return left + [Interval(s, e)] + right

"""