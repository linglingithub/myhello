"""

91. Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

Subscribe to see which companies asked this question

Hide Tags Dynamic Programming String

Medium

"""

import unittest


class Solution(object):
    def numDecodings(self, s): #49ms, 63%
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        cnt = len(s)
        dp = [ 0 for i in range(cnt+1)]
        dp[0] = 1 # # this is important, not 0, need to be 1 here, not 0, for case1
        dp[1] = 1 if '1' <= s[0] <= '9' else 0 # important, not always 1, see case2
        for i in range(2, cnt+1):
            if '1' <= s[i-1] <= '9': #pay attention to the index here, i means length, so need to -1 for s[i-1]
                dp[i] += dp[i-1]
            if '10' <= s[i-2:i] <= '26':
                dp[i] += dp[i-2]
        return dp[cnt]


    def numDecodings_ref(self, s): #82ms, 8.34%
        if s=="" or s[0]=='0': return 0
        dp=[1,1]
        for i in range(2,len(s)+1):
            if 10 <=int(s[i-2:i]) <=26 and s[i-1]!='0':
                dp.append(dp[i-1]+dp[i-2])
            elif int(s[i-2:i])==10 or int(s[i-2:i])==20:
                dp.append(dp[i-2])
            elif s[i-1]!='0':
                dp.append(dp[i-1])
            else:
                return 0
        return dp[len(s)]







class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case2(self): #=====>
        s = "0"
        answer = 0
        result = self.sol.numDecodings(s)
        self.assertEqual(answer, result)

    def test_case1(self):
        s = "12"
        answer = 2
        result = self.sol.numDecodings(s)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8