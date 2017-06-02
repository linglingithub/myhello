#coding=utf-8

import unittest

"""

Sliding Window Maximum

Given an array of n integer with duplicate number, and a moving window(size k), move the window at each iteration from 
the start of the array, find the maximum number inside the window at each moving.

Have you met this question in a real interview? Yes

Example
For array [1, 2, 7, 7, 8], moving window size k = 3. return [7, 7, 8]

At first the window is at the start of the array like this

[|1, 2, 7| ,7, 8] , return the maximum 7;

then the window move one step forward.

[1, |2, 7 ,7|, 8], return the maximum 7;

then the window move one step forward again.

[1, 2, |7, 7, 8|], return the maximum 8;

Challenge 
o(n) time and O(k) memory

Tags 
LintCode Copyright Two Pointers Zenefits
Related Problems 
Hard Sliding Window Median 19 %
Hard Sliding Window Matrix Maximum 36 %
Hard Paint House II

"""


class Solution:
    """
    Key idea is that when a big number comes into the window, the smaller nums before it 
    does not need to be save, can be removed from the stack. So the deque is keeping a 
    decreasing window. When window moves forward, first move the window left, then add in the 
    new number. if the previous max is out of window now, since the deque is keeping a decreasing 
    items, the new max is always at deque[0] ( the index ) -- either the second max from previous
    window, or the new number in the current window.
    @param nums: A list of integers.
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        # write your code here
        if not nums or len(nums) < k or k <1:
            return []
        from collections import deque
        q = deque()
        result = []
        for i in range(0, k):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
        result.append(nums[q[0]])
        for i in range(k, len(nums)):
            left = i - k + 1
            if q[0] < left:
                q.popleft()
            while q and nums[q[-1]] < nums[i]: # not q[-1], carefull
                q.pop()
            q.append(i)
            result.append(nums[q[0]])
        return result




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case2(self):
        nums = [1,2,7,7,2,10,3,4,5]
        k = 2
        answer = [2,7,7,7,10,10,4,5]  # wrong output [2,7,7,7,10,10,3,4]
        result = self.sol.maxSlidingWindow(nums, k)
        self.assertEqual(answer, result)


    def test_case1(self):
        nums = [1,2,7,7,8]
        k = 3
        answer = [7,7, 8]
        result = self.sol.maxSlidingWindow(nums, k)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        # write your code here
        q = deque()
        result = []
        if len(nums) < k or k == 0:
            return []

        n = len(nums)
        for i in xrange(n):
            while len(q) and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)

            if i < k - 1:                        
                continue

            while len(q) and q[0] <= i - k:
                q.popleft()
            
            result.append(nums[q[0]])

        return result;


"""