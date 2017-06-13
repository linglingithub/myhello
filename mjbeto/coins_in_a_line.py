#coding=utf-8

import unittest

"""
Coins in a Line 

There are n coins in a line. Two players take turns to take one or two coins from right side until there are no more 
coins left. The player who take the last coin wins.

Could you please decide the first play will win or lose?

Have you met this question in a real interview? Yes
Example
n = 1, return true.

n = 2, return true.

n = 3, return false.

n = 4, return true.

n = 5, return true.

Challenge 
O(n) time and O(1) memory

Tags 
Dynamic Programming Greedy Array Game Theory
Related Problems 
Hard Coins in a Line III 33 %
Medium Coins in a Line II

"""


class Solution:
    # @param n: an integer
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, n):
        if n == 0:
            return False
        if n <= 2:
            return True
        dp = [False, True, True]
        for i in range(3, n+1):
            dp[i%3] = not dp[(i-1)%3] or not dp[(i-2)%3]
        return dp[n%3]


    def firstWillWin_not_best(self, n):
        """
        Not the best way to solve
        passed online 100% cases, but locally throws "RuntimeError: maximum recursion depth exceeded in cmp" for case7
        locally need to do 

            import sys
            sys.setrecursionlimit(10000)
        
        :param n: 
        :return: 
        """
        if n == 0:
            return False
        if n <= 2:
            return True
        dp = [None for _ in range(n + 1)]
        dp[0], dp[1], dp[2] = False, True, True
        first = True
        result = not self.check_first_win(n - 1, dp) or not self.check_first_win(n - 2, dp)
        return result

    def check_first_win(self, n, dp):
        if dp[n] != None:
            return dp[n]
        else:
            dp[n] = not self.check_first_win(n - 1, dp) or not self.check_first_win(n - 2, dp)
            return dp[n]



    def firstWillWin_wrong4case7(self, n):
        # write your code here
        if n==0 :  # required corner case, see case 6
            return False
        if n <= 2:
            return True
        elif n == 3:
           return False
        dp = [ False for _ in range(n+1)]
        dp[1], dp[2] = True, True
        for i in range(4, n+1):
            dp[i] = dp[i-1] or dp[i-2]
        return dp[n]


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case7(self):  # =====> 87% cases passed and this case is wrong
        n = 9999
        answer = False
        result = self.sol.firstWillWin(n)
        self.assertEqual(answer, result)

    def test_case6(self):
        n = 0
        answer = False
        result = self.sol.firstWillWin(n)
        self.assertEqual(answer, result)

    def test_case5(self):
        n = 5
        answer = True
        result = self.sol.firstWillWin(n)
        self.assertEqual(answer, result)

    def test_case4(self):
        n = 4
        answer = True
        result = self.sol.firstWillWin(n)
        self.assertEqual(answer, result)

    def test_case3(self):
        n = 3
        answer = False
        result = self.sol.firstWillWin(n)
        self.assertEqual(answer, result)

    def test_case2(self):
        n = 2
        answer = True
        result = self.sol.firstWillWin(n)
        self.assertEqual(answer, result)

    def test_case1(self):
        n = 1
        answer = True
        result = self.sol.firstWillWin(n)
        self.assertEqual(answer, result)



def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()
    # sol = Solution()
    # import sys
    # sys.setrecursionlimit(10000)
    # print sol.firstWillWin(9999)


#-*- coding:utf-8 -*-

"""

jiuzhang answer python version:

class Solution:
    # @param n: an integer
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, n):
        # write your code here
        if n%3==0: return False
        else: return True

"""