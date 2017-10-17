#coding=utf-8

import unittest

"""

239.

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

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if not nums or k <= 0:
            return []
        from collections import deque
        queue = deque()
        res = []
        n = len(nums)
        for i in range(k):
            #while queue and nums[queue[0]] < nums[i]:  # should be queue[-1] here, otherwise wrong
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
        res.append(nums[queue[0]])
        for i in range(k, n):
            wleft = i-k+1
            if queue and queue[0] < wleft:
                queue.popleft()
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            res.append(nums[queue[0]])
        return res

    def maxSlidingWindow1(self, nums, k):
        """
        can actually go without wmax, cause the deque is saving decreasing numbers, so queue[0] is always current max
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k <= 0:   # protection for case3
            return []
        from collections import deque
        queue = deque()
        res = []
        wmax = nums[0]
        for i in range(k):
            wmax = max(wmax, nums[i])
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
        res.append(wmax)
        n = len(nums)
        for i in range(1, n-k+1):
            if queue[0] < i:
                tmp = queue.popleft()
                if nums[tmp] == wmax:
                    wmax = None if not queue else nums[queue[0]]  # need to add this, otherwise wrong, case2
            while queue and nums[queue[-1]] < nums[i+k-1]:
                queue.pop()
            queue.append(i+k-1)
            wmax = max(wmax, nums[i+k-1]) if wmax is not None else nums[i+k-1]
            res.append(wmax)
        return res


class Solution1:
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

    def test_case02(self):
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

    def test_case3(self):   #=====>
        nums = []
        k = 0
        answer = []
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