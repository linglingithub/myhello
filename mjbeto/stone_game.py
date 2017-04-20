#coding=utf-8

import unittest

"""

Stone Game

There is a stone game. At the beginning of the game the player picks n piles of stones in a line.

The goal is to merge the stones in one pile observing the following rules:

At each step of the game,the player can merge two adjacent piles to a new pile.
The score is the number of stones in the new pile.
You are to determine the minimum of the total score.

Have you met this question in a real interview? Yes
Example
For [4, 1, 1, 4], in the best solution, the total score is 18:

1. Merge second and third piles => [4, 2, 4], score +2
2. Merge the first two piles => [6, 4]，score +6
3. Merge the last two piles => [10], score +10
Other two examples:
[1, 1, 1, 1] return 8
[4, 4, 5, 9] return 43

Tags
Dynamic Programming
Related Problems
Medium Stone Game II 42 %
Hard Burst Balloons

"""


class Solution:
    # @param {int[]} A an integer array
    # @return {int} an integer
    def stoneGame(self, nums):  # 2143 ms, 1676 ms
        # Write your code here
        if not nums:
            return 0
        n = len(nums)
        cache = {}

        def helper(start, end):
            if start == end-1: # should be 0 here, not nums[i] because cache is for the mergeed stones , if single, no merge, should return 0
                return 0
            elif (start, end) in cache:
                return cache[(start, end)]
            merge_value = -1
            for i in range(start+1, end):
                value = helper(start, i) + helper(i, end)
                merge_value = value if merge_value == -1 else min(merge_value, value)
            merge_value += sum([ nums[x] for x in range(start,end)])
            cache[(start, end)] = merge_value
            return merge_value

        return helper(0,n)
        #return cache[(0, n)]   # when only one element, no cache, should return directly, see case 5


    def stoneGame_wrong(self, nums):
        # Write your code here
        if not nums:
            return 0
        n = len(nums)
        cache = {}

        def helper(start, end):
            if start == end:
                return nums[start]
            elif start == end - 1: # don't forget about this one, otherwise i in range(start,end-1) will not be executed.
                cache[(start, end)] = nums[start] + nums[end]
                return cache[(start, end)]
            elif (start, end) in cache:
                return cache[(start, end)]
            merge_value = -1
            for i in range(start, end):  # should be end, not end - 1 here, because end is open in range()
                value = helper(start, i) + helper(i+1, end)
                merge_value = value if merge_value == -1 else min(merge_value, value)
            merge_value += sum([ nums[x] for x in range(start,end+1)])
            cache[(start, end)] = merge_value
            return merge_value

        helper(0,n-1)
        return cache[(0, n-1)]


    def stoneGame_ref(self, A): # 1103ms
        # Write your code here
        n = len(A)
        if n < 2:
            return 0
        dp = [[0 for _ in xrange(n)] for _ in xrange(n)]
        sum = [[0 for _ in xrange(n)] for _ in xrange(n)]

        # 0, 1, 2, ... n-2, n-1
        for i in xrange(n):
            dp[i][i] = 0
        for i in xrange(0, n-1):
            dp[i][i+1] = A[i]+A[i+1]

        for i in xrange(n):
            sum[i][i] = A[i]
            for j in xrange(i+1, n):
                sum[i][j] = sum[i][j-1] + A[j]

        for x in xrange(3, n+1):
            i = 0
            while i+x-1 < n:
                j = i+x-1
                k = i
                dp[i][j] = sys.maxint
                while k+1 <= j:
                    t = dp[i][k] + dp[k+1][j] + sum[i][k] + sum[k+1][j]
                    dp[i][j] = min(dp[i][j], t)
                    k += 1
                i += 1
        return dp[0][n-1]



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case0(self):
        nums = [1, 1, 2]
        answer = 6
        result = self.sol.stoneGame(nums)
        self.assertEqual(answer, result)

    def test_case1(self):
        nums = [4, 1, 1, 4]
        answer = 18
        result = self.sol.stoneGame(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [1, 1, 1, 1]
        answer = 8
        result = self.sol.stoneGame(nums)
        self.assertEqual(answer, result)

    def test_case3(self):
        nums = [4, 4, 5, 9]
        answer = 43
        result = self.sol.stoneGame(nums)
        self.assertEqual(answer, result)

    def test_case4(self):
        nums = [6, 4, 4, 6]
        answer = 40
        result = self.sol.stoneGame(nums)
        self.assertEqual(answer, result)

    def test_case5(self): #===>
        nums = [10]
        answer = 0
        result = self.sol.stoneGame(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
