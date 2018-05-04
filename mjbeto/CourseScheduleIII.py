# coding=utf-8

import unittest
from collections import defaultdict, deque

"""

630. Course Schedule III
DescriptionHintsSubmissionsDiscussSolution
There are n different online courses numbered from 1 to n. Each course has some duration(course length) t and closed on dth day. A course should be taken continuously for t days and must be finished before or on the dth day. You will start at the 1st day.

Given n online courses represented by pairs (t,d), your task is to find the maximal number of courses that can be taken.

Example:
Input: [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
Output: 3
Explanation: 
There're totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day. 
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day. 
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.
Note:
The integer 1 <= d, t, n <= 10,000.
You can't take two courses simultaneously.

Difficulty:Hard
Total Accepted:6K
Total Submissions:20.3K
Contributor:Stomach_ache
Subscribe to see which companies asked this question.

Related Topics 

Similar Questions 
Course ScheduleCourse Schedule II

"""
import heapq
class Solution:
    def scheduleCourse(self, courses):  # ref
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        pq = []
        start = 0
        for t, end in sorted(courses, key = lambda x: x[1]):  # sort courses in end time ascending order
            start += t   # add all courses' duration
            heapq.heappush(pq, -t)  # put to heap in duration's descending order
            while start > end:  #  If time exceeds, drop the previous course which costs the most time. (That must be the best choice!)
                start += heapq.heappop(pq)  # course was pushed with -t , so here means start -= some time.
        return len(pq)


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()



    def test_case1(self):
        n = 2
        nums = [[1, 0]]
        answer = True
        result = self.sol.scheduleCourse(n, nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        n = 2
        nums = [[1, 0], [0, 1]]
        answer = False
        result = self.sol.scheduleCourse(n, nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

# -*- coding:utf-8 -*-

"""

Sort all the courses by their ending time. When considering the first K courses, they all end before end. 
A necessary and sufficient condition for our schedule to be valid, is that (for all K), the courses we choose to take
 within the first K of them, have total duration less than end.

For each K, we will greedily remove the largest-length course until the total duration start is <= end. 
To select these largest-length courses, we will use a max heap. start will maintain the loop invariant that it is the 
sum of the lengths of the courses we have currently taken.

Clearly, this greedy choice makes the number of courses used maximal for each K. When considering potential future K, 
there's never a case where we preferred having a longer course to a shorter one, so indeed our greedy choice dominates 
all other candidates.

def scheduleCourse(self, A):
    pq = []
    start = 0
    for t, end in sorted(A, key = lambda (t, end): end):
        start += t
        heapq.heappush(pq, -t)
        while start > end:
            start += heapq.heappop(pq)
    return len(pq)
(With thanks to @uwi - see his solution here)

========================================================================================

First, we sort courses by the end date, this way, when we're iterating through the courses, we can switch out any 
previous course with the current one without worrying about end date.

Next, we iterate through each course, if we have enough days, we'll add it to our multiset. If we don't have enough days, 
then we can either ignore this course, or we can use it to replace a longer course we added earlier.



"""