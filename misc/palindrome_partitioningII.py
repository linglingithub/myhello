#coding=utf-8

import unittest
import sys

"""
132. Palindrome Partitioning II

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.


Difficulty:Hard
Total Accepted:73.5K
Total Submissions:302.2K
Contributor: LeetCode
Subscribe to see which companies asked this question.

Related Topics 
Dynamic Programming 
Similar Questions 
Palindrome Partitioning 


"""


class Solution(object):
    def minCut(self, s): # ref idea, 25%
        if not s:
            return 0
        n = len(s)
        palindrome_dict = [[False for _ in range(n)] for _ in range(n)]
        dp = [i for i in range(n)]

        for i in range(1, n):
            for j in range(i, -1, -1):
                palindrome_dict[j][i] = self.is_palindrome(s, j, i, palindrome_dict)
                if palindrome_dict[j][i]:
                    dp[i] = min(dp[i], dp[j-1]+1) if j > 0 else 0  # need to add if j > 0 else 0, otherwise wrong

        return dp[n-1]


    def minCut1(self, s):  #_TLE_case5
        """
        local runs for case 5, most time on calculating the palindrome_dict == > local 1s30ms
        online 22%
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        n = len(s)
        palindrome_dict = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i, -1, -1):  # going this way so (j, i) can make use of (j+1, i-1), to make calc faster
                #tmp, t2 = s[j: i + 1], palindrome_dict[j][i]
                palindrome_dict[j][i] = self.is_palindrome(s, j, i, palindrome_dict)
                #tmp, t2 = s[j: i + 1], palindrome_dict[j][i]
                #print(s[j: i+1], " === ", palindrome_dict[j][i])
        dp = [-1 for _ in range(n)]
        dp[0] = 0
        for i in range(1, n):
            if palindrome_dict[0][i]:
                dp[i] = 0
                continue
            dp[i] = 1 + dp[i-1]
            for j in range(i-1, 0, -1):   # should be i-1, not i-2 here
                if palindrome_dict[j][i]:
                    dp[i] = min(dp[i], dp[j-1] + 1)  # should be j-1 here
        return dp[n-1]

    def is_palindrome(self, s, l, r, palindrome_dict):
        #tmp = s[l: r + 1]
        if l == r:
            return True
        if s[l] == s[r]:
            if l+1<r and palindrome_dict[l+1][r-1] or l+1==r:
                return True
            else:
                return False
        else:
            return False


    def minCut_TLE_case5(self, s):  #_TLE_case5
        """
        local runs for case 5, most time on calculating the palindrome_dict, local runs around 1m 21s == > change to 
        palindrome_dict, still TLE, local runs around 42s
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        n = len(s)
        palindrome_dict = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                palindrome_dict[i][j] = self.is_palindrome(s, i, j)
        dp = [-1 for _ in range(n)]
        dp[0] = 0
        for i in range(1, n):
            if palindrome_dict[0][i]:
                dp[i] = 0
                continue
            dp[i] = 1 + dp[i-1]
            for j in range(i-1, 0, -1):   # should be i-1, not i-2 here
                if palindrome_dict[j][i]:   # should not us is_palindrome, use the dict
                    dp[i] = min(dp[i], dp[j-1] + 1)  # should be j-1 here

        return dp[n-1]



    def minCut_TLE(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        all_paths = self.partition(s)
        return min([len(x)-1 for x in all_paths])

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        palindrome_dict = {}
        self.helper(s, 0, [], palindrome_dict, result)
        return result

    def helper(self, s, start, path, palindrome_dict, result):
        if start >= len(s):  # start, not s here
            result.append(path)   # append, not add here
            return
        self.helper(s, start + 1, path + [s[start]], palindrome_dict, result)
        for i in range(start + 1, len(s)):  # not start + 1 here, the cut ends ON i, new interval starts on i+1
            if (start, i) not in palindrome_dict:
                if self.is_palindrome(s, start, i):
                    palindrome_dict[(start, i)] = True
                else:
                    palindrome_dict[(start, i)] = False
            if palindrome_dict[(start, i)]:
                self.helper(s, i+1, path + [s[start:i+1]], palindrome_dict, result)  # path+[s[start:i+1]]

    def is_palindrome1(self, s, l, r):
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = "aab"
        answer = 1
        result = self.sol.minCut(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = "bb"
        answer = 0
        result = self.sol.minCut(nums)
        self.assertEqual(answer, result)

    def test_case3(self):  # ===> TLE
        nums = "ababababababababababababcbabababababababababababa"
        answer = 0
        result = self.sol.minCut(nums)
        self.assertEqual(answer, result)

    def test_case4(self):  # ===>
        nums = "cdd"
        answer = 1
        result = self.sol.minCut(nums)
        self.assertEqual(answer, result)

    def test_case5(self):  # ===> TLE
        nums = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        answer = 1
        result = self.sol.minCut(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""

 这道题需要用动态规划做，如果用I的DFS的方法做会TLE。

 

 首先设置dp变量 cuts[len+1]。cuts[i]表示从第i位置到第len位置（包含，即[i, len])的切割数（第len位置为空）。

 初始时，是len-i。比如给的例子aab，cuts[0]=3，就是最坏情况每一个字符都得切割：a|a|b|' '。cuts[1] = 2, 即从i=1位置开始，a|b|' '。

 cuts[2] = 1 b|' '。cuts[3]=0,即第len位置，为空字符，不需要切割。

 

 上面的这个cuts数组是用来帮助算最小cuts的。

 

 还需要一个dp二维数组matrixs[i][j]表示字符串[i,j]从第i个位置（包含）到第j个位置（包含） 是否是回文。

 如何判断字符串[i,j]是不是回文？

 1. matrixs[i+1][j-1]是回文且 s.charAt(i) == s.charAt(j)。

 2. i==j（i，j是用一个字符）

 3. j=i+1（i，j相邻）且s.charAt(i) == s.charAt(j)

 

 当字符串[i,j]是回文后，说明从第i个位置到字符串第len位置的最小cut数可以被更新了，

 那么就是从j+1位置开始到第len位置的最小cut数加上[i,j]|[j+1,len - 1]中间的这一cut。

 即，Math.min(cuts[i], cuts[j+1]+1) 

 最后返回cuts[0]-1。把多余加的那个对于第len位置的切割去掉，即为最终结果。
 
 ==============================


思路：Palindrome Partitioning II

整体的思路是一维DP。DP[i]表示长度为i的prefix：s[0: i-1]的min cut数量。
DP[i] = min (DP[j] + 1) ，对所有 0<=j<i，且s[j: i-1]为palindrome。
和I同样的技巧，用DP先计算存储一个palindrome判断矩阵isPal[i][j]，便于后面一维DP计算中能迅速判断s[j: i-1]是否为palindrome。


有一个更优的解法参考：
https://oj.leetcode.com/discuss/9476/solution-does-not-need-table-palindrome-right-uses-only-space



"""


#-*- coding:utf-8 -*-
