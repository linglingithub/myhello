"""
63. Unique Paths II

Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.

Subscribe to see which companies asked this question

Hide Tags Array Dynamic Programming
Hide Similar Problems (M) Unique Paths

Medium

"""


import unittest


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid): #49ms, 49%
        # write your code here
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[1 for _ in range(n)] for _ in range(m)]
        blocked = False
        for i in range(m):
            if blocked or obstacleGrid[i][0]:
                blocked = True
                dp[i][0] = 0
        blocked = False
        for j in range(n):
            if blocked or obstacleGrid[0][j]:
                blocked = True
                dp[0][j] = 0
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

    def uniquePathsWithObstacles1(self, obstacleGrid): #49ms, 59%
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid is None or len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        # dp = [[1] * n] * m, need to watch out here other wise wrong for case 2
        # dp = [ [0 if obstacleGrid[i][j] else 1 for j in range(n)] for i in range(m)], wrong for case 3, first row and column is very different
        # dp = [[1] * n] * m, not ok to init with all 1, better to init with all 0, wrong for case 4
        dp = [[0 for i in range(n)] for j in range(m)] #[[0] * n] * m, can not init in this way, otherwise wrong for case 4, 5, -->
        # <-- (cont') the init in first row and column can be updated as wrong value, all 1 or all 0
        for i in range(m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                break
        for j in range(n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = 1
            else:
                break
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[m-1][n-1]






class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case5(self): # ====>
        nums = [
            [0], [1]
        ]
        answer = 0
        result = self.sol.uniquePathsWithObstacles(nums)
        self.assertEqual(answer, result)

    def test_case4(self): # ====>
        nums = [[0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0],[1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,1],[0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0],[0,0,0,1,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0],[1,0,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0],[0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0],[0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0],[0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0],[0,1,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,1],[1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,1,1,0,1,0,0,0,0,1,1],[0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,1],[1,1,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0]]
        answer = 1637984640 #1662293184
        result = self.sol.uniquePathsWithObstacles(nums)
        self.assertEqual(answer, result)

    def test_case3(self): # ====>
        nums = [
            [1,0]
        ]
        answer = 0
        result = self.sol.uniquePathsWithObstacles(nums)
        self.assertEqual(answer, result)

    def test_case2(self): # ====>
        nums = [
            [1]
        ]
        answer = 0
        result = self.sol.uniquePathsWithObstacles(nums)
        self.assertEqual(answer, result)


    def test_case1(self):
        nums = [
          [0,0,0],
          [0,1,0],
          [0,0,0]
        ]
        answer = 2
        result = self.sol.uniquePathsWithObstacles(nums)
        self.assertEqual(answer, result)

    def test_case0(self):
        nums = [
          [0,1,0],
          [0,1,0],
          [0,0,0]
        ]
        answer = 1
        result = self.sol.uniquePathsWithObstacles(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8

"""
array init tricks:
-- in python console, test the following

a = [[0] * 3] *  2
>>> a
[[0, 0, 0], [0, 0, 0]]
>>> a[1][0] = 1
>>> a
[[1, 0, 0], [1, 0, 0]]


### element-array-multiplication-vs-list-comprehension-initialization

Question: =======>
While working with a two dimentional array, I found that initializing it in a certain way would produce unexpected results.
I would like to understand the difference between initializing an 8x8 grid in these two ways:

a =  [[1]*8]*8
vs.
A =  [[1 for i in range(8)] for j in range(8)]

The unexpected results were that any element accessed with the indeces [0-6][x] would point to the last row in [7][x].
The arrays look identical in the interpreter, hence my confusion. What is wrong with the first approach?


Answer: ======>

In your first version, you're creating a list containing the number 1 and by multiplying it 8 times create a list
containing 8 1s, and using that list 8 times to create a.

So when you change anything in the first version, you'll see that change everywhere else. Your problem being that you're
reusing the same instance, something that doesn't happen in the second version.

Answer 2: ======>

By the way, [[foo]*10 for x in xrange(10)] can be used to get rid of one comprehension. The problem is that
multiplication does a shallow copy, so new = [foo] * 10 new = [new] * 10 will get you a list containing the same list
ten times.



"""