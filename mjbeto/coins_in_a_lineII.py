#coding=utf-8

import unittest

"""
Coins in a Line II

There are n coins with different value in a line. Two players take turns to take one or two coins from left side until 
there are no more coins left. The player who take the coins with the most value wins.

Could you please decide the first player will win or lose?

Have you met this question in a real interview? Yes
Example
Given values array A = [1,2,2], return true.

Given A = [1,2,4], return false.

Tags 
Dynamic Programming Array Game Theory
Related Problems 
Hard Coins in a Line III 33 %
Medium Coins in a Line

"""


class Solution:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):  # ref main idea, not exactly the same
        # write your code here
        if not values:
            return False
        n = len(values)
        if n <= 2:
            return True
        dp = [0 for _ in range(n+1)]
        dp[n] = 0
        dp[n-1] = values[n-1]
        dp[n-2] = values[n-1] + values[n-2]
        dp[n-3] = values[n-3] + values[n-2]
        dp[n-4] = max(values[n-4] + min(dp[n-2],dp[n-1]), values[n-4]+values[n-3] + min(dp[n-1], dp[n]))
        for i in range(n-4, -1, -1):
            dp[i] = max(values[i] + min(dp[i+2], dp[i+3]), values[i]+values[i+1] + min(dp[i+3], dp[i+4]))
        all_sum = sum(values)
        first_win = dp[0] > all_sum - dp[0]
        return first_win





class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case4(self):
        A = [10,2,1,1,1,14]
        answer = False
        result = self.sol.firstWillWin(A)
        self.assertEqual(answer, result)

    def test_case3(self):
        A = [10,2,1,1,1,10]
        answer = True
        result = self.sol.firstWillWin(A)
        self.assertEqual(answer, result)


    def test_case2(self):
        A = [1,2,4]
        answer = False
        result = self.sol.firstWillWin(A)
        self.assertEqual(answer, result)

    def test_case1(self):
        A = [1,2,2]
        answer = True
        result = self.sol.firstWillWin(A)
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

动态规划、博弈论

坑死，看了好久

定义dp[i]表示从i到end能取到的最大值

当我们在i处，有两种选择：

1.若取values[i]，对方可以取values[i+1] 或者values[i+1] + values[i+2]

当对方取values[i+1] 后 ，我们只能从 i+2 到end内取，我们所取得最大值是dp[i+2],  注意：对方所选取的结果一定是使得我们以后选取的值最小

当对方取values[i+1] + values[i+2]后，我们只能从i+3到end内取，我们所取得最大值是dp[i+3]。

此时：dp[i] = values[i] + min(dp[i+2],dp[i+3]) , 注意：对方所选取的结果一定是使得我们以后选取的值最小

2.若取values[i] + values[i+1],对方可取values[i+2] 或者values[i+2] + values[i+3]

当对方取values[i+2]后，我们只能从i+3到end内取，我们取得最大值是dp[i+3]

当对方取values[i+2]+values[i+3]后，我们只能从i+4到end内去，我们取得最大值是dp[i+4]

此时：dp[i] = values[i] + values[i+1]+min(dp[i+3],dp[i+4])

这里的取最小值和上面一样的意思，对方选取过之后的值一定是使得我们选取的值最小，对方不傻并且还很聪明

最后我们可以取上面两个dp[i]的最大值，就是答案，这里意思是：对方留得差的方案中，我们选取的最大值。


=====================================================================================================================


DP[i]表示从i到end能取到的最大value
function

当我们走到i时，有两种选择
取values[i]
取values[i] + values[i+1]
1. 我们取了values[i],对手的选择有 values[i+1]或者values[i+1] + values[i+2] 剩下的最大总value分别为DP[i+2]或DP[i+3], 对手也是理性
的所以要让我们得到最小value
所以 value1 = values[i] + min(DP[i+2], DP[i+3])
2. 我们取了values[i]和values[i+1] 同理 value2 = values[i] + values[i+1] + min(DP[i+3], DP[i+4])
最后

DP[I] = max(value1, value2)


======================================================

jiujiang answer:

class Solution:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):
        # write your code here
        n, total = len(values), 0
        sumv, f = [], []
        if n<3: return True
        for i in xrange(n): total += values[i]
        for i in xrange(n):
            sumv.append(total)
            total -= values[i]
        f.append(sumv[n-1])
        f.append(sumv[n-2])
        for i in xrange(n-3, -1, -1):
            f.append(max(values[i]+(sumv[i+1]-f[n-1-i-1]), values[i]+values[i+1]+(sumv[i+2]-f[n-1-i-2])))
        if f[n-1]<sumv[0]-f[n-1]: return False
        else: return True


"""