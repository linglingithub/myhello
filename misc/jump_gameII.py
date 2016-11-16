#coding=utf-8

"""
45. Jump Game II


Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1,

then 3 steps to the last index.)

Note:
You can assume that you can always reach the last index.

Subscribe to see which companies asked this question

Hide Tags Array Greedy

Hard

"""


import unittest


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        input = [2,3,1,1,4]
        answer = 2
        result = self.sol.jump(input)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()


"""
同样可以用greedy解决。与I不同的是，求的不是对每个i，从A[0:i]能跳到的最远距离；而是计算跳了k次后能达到的最远距离，

这里的通项公式为：

d[k] = max(i+A[i])     d[k-2] < i <= d[k-1]

"""


"""

    # @param A, a list of integers
    # @return an integer
    # def jump(self, A):
    #     maxint = 1<<31 - 1
    #     dp = [ maxint for i in range(len(A)) ]
    #     dp[0] = 0
    #     for i in range(1, len(A)):
    #         for j in range(i):
    #             if A[j] >= (i - j):
    #                 dp[i] = min(dp[i], dp[j] + 1)
    #     return dp[len(A) - 1]
    # dp is time limited exceeded!

# We use "last" to keep track of the maximum distance that has been reached
# by using the minimum steps "ret", whereas "curr" is the maximum distance
# that can be reached by using "ret+1" steps. Thus,curr = max(i+A[i]) where 0 <= i <= last.
    def jump(self, A):
        ret = 0
        last = 0
        curr = 0
        for i in range(len(A)):
            if i > last:
                last = curr
                ret += 1
            curr = max(curr, i+A[i])
        return ret

"""

#-*- coding:utf-8 -*-
#coding=utf-8