#coding=utf-8
__author__ = 'linglin'

"""
161. One Edit Distance

Given two strings S and T, determine if they are both one edit distance apart.


locked

"""



import unittest


class Solution:
    # @return an integer
    def isOneEditDistance(self, s, t):
        diff = abs(len(s)-len(t))
        if diff > 1:
            return False
        elif diff == 0:
            cnt = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    cnt += 1
                    if cnt > 1:
                        return False
            return cnt==1
        else:
            i = 0
            end = min(len(s), len(t))
            cnt = 0
            while i < end:
                if s[i] == t[i]:
                    i += 1
                else:
                    if len(s)>len(t):
                        return s[i+1:] == t[i:]
                    else:
                        return s[i:] == t[i+1:]
            return True


    def isOneEditDistance_ref(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m, n = len(s), len(t)
        if m > n:
            return self.isOneEditDistance(t, s)
        if n - m > 1:
            return False

        i, shift = 0, n - m
        while i < m and s[i] == t[i]:
            i += 1
        if shift == 0:
            i += 1
        while i < m and s[i] == t[i + shift]:
            i += 1

        return i == m





class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        s, t = "", " "
        answer = True
        result = self.sol.isOneEditDistance(s, t)
        self.assertEqual(answer, result)

    def test_case2(self):
        s, t = "12", "123"
        answer = True
        result = self.sol.isOneEditDistance(s, t)
        self.assertEqual(answer, result)

    def test_case3(self):
        s, t = "124", "123"
        answer = True
        result = self.sol.isOneEditDistance(s, t)
        self.assertEqual(answer, result)

    def test_case4(self):
        s, t = "14", "123"
        answer = False
        result = self.sol.isOneEditDistance(s, t)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-


"""

复杂度
时间 O(N) 空间 O(1)

思路
虽然我们可以用Edit Distance的解法，看distance是否为1，但Leetcode中会超时。这里我们可以利用只有一个不同的特点在O(N)时间内完成。如果两个
字符串只有一个编辑距离，则只有两种情况：

两个字符串一样长的时候，说明有一个替换操作，我们只要看对应位置是不是只有一个字符不一样就行了

一个字符串比另一个长1，说明有个增加或删除操作，我们就找到第一个对应位置不一样的那个字符，如果较长字符串在那个字符之后的部分和较短字符串那个
字符及之后的部分是一样的，则符合要求
如果两个字符串长度差距大于1，肯定不对


"""