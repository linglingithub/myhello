#coding=utf-8

import unittest

"""

Stone Game II

There is a stone game. At the beginning of the game the player picks n piles of stones in a circle.

The goal is to merge the stones in one pile observing the following rules:

At each step of the game,the player can merge two adjacent piles to a new pile.
The score is the number of stones in the new pile.
You are to determine the minimum of the total score.

Example
For [1, 4, 4, 1], in the best solution, the total score is 18:

1. Merge second and third piles => [2, 4, 4], score +2
2. Merge the first two piles => [6, 4]，score +6
3. Merge the last two piles => [10], score +10
Other two examples:
[1, 1, 1, 1] return 8
[4, 4, 5, 9] return 43

Tags
Dynamic Programming
Related Problems
Medium Stone Game

"""


class Solution:
    # @param {int[]} A an integer array
    # @return {int} an integer
    def stoneGame2(self, nums):  #1742ms
        # Write your code here
        if not nums or len(nums) < 2:
            return 0
        #vals = [x for x in nums]
        n = len(nums)
        #vals[n] = nums[0] #can't assign value like this
        #vals.append(nums[0])
        nums.append(nums[0])
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

        min1 = helper(0, n)
        min2 = helper(1,n+1)
        return min(min1, min2)


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case0(self):
        nums = [1, 1, 2]
        answer = 6
        result = self.sol.stoneGame2(nums)
        self.assertEqual(answer, result)

    def test_case1(self):
        nums = [4, 1, 1, 4]
        answer = 18
        result = self.sol.stoneGame2(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [1, 1, 1, 1]
        answer = 8
        result = self.sol.stoneGame2(nums)
        self.assertEqual(answer, result)

    def test_case3(self):
        nums = [4, 4, 5, 9]
        answer = 43
        result = self.sol.stoneGame2(nums)
        self.assertEqual(answer, result)

    def test_case4(self):
        nums = [6, 4, 4, 6]
        answer = 40
        result = self.sol.stoneGame2(nums)
        self.assertEqual(answer, result)

    def test_case5(self): #===>
        nums = [10]
        answer = 0
        result = self.sol.stoneGame2(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
