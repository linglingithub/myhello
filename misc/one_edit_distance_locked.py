#coding=utf-8
"""
161. One Edit Distance -- locked

Given two strings S and T, determine if they are both one edit distance apart.

Medium

"""


import unittest


class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m, n = len(s), len(t)
        if abs(m-n) > 1:
            return False
        if m==n:
            skipped = False
            for i in range(m):
                if s[i] != t[i]:
                    if skipped:
                        return False
                    else:
                        skipped = True
            return True  # should add ending return here

        # for case lengths differ by 1
        # check and make s the shorter one
        if m > n:
            s, t = t, s
        shifted = False
        for i in range(len(s)):
            if shifted:
                if s[i] != t[i+1]:
                    return False
            else:
                if s[i] != t[i]:
                    if s[i] != t[i+1]:
                        return False
                    else:
                        shifted = True
        return True





class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        s = "a"
        t = ""
        answer = True
        result = self.sol.isOneEditDistance(s, t)
        self.assertEqual(answer, result)

    def test_case2(self):
        s = "a"
        t = "b"
        answer = True
        result = self.sol.isOneEditDistance(s, t)
        self.assertEqual(answer, result)


    def test_case3(self):
        s = "a"
        t = "a"
        answer = True
        result = self.sol.isOneEditDistance(s, t)
        self.assertEqual(answer, result)

    def test_case4(self):
        s = "b"
        t = "b"
        answer = True
        result = self.sol.isOneEditDistance(s, t)
        self.assertEqual(answer, result)

    def test_case5(self):
        s = "ab"
        t = "ba"
        answer = False
        result = self.sol.isOneEditDistance(s, t)
        self.assertEqual(answer, result)

    def test_case6(self):
        s = ""
        t = "ab"
        answer = False
        result = self.sol.isOneEditDistance(s, t)
        self.assertEqual(answer, result)

    def test_case7(self):
        s = "aabbc"
        t = "aabc"
        answer = True
        result = self.sol.isOneEditDistance(s, t)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()


"""
虽然我们可以用Edit Distance的解法，看distance是否为1，但Leetcode中会超时。这里我们可以利用只有一个不同的特点在O(N)时间内完成。
如果两个字符串只有一个编辑距离，则只有两种情况：

(1)两个字符串一样长的时候，说明有一个替换操作，我们只要看对应位置是不是只有一个字符不一样就行了
(1)一个字符串比另一个长1，说明有个增加或删除操作，我们就找到第一个对应位置不一样的那个字符，如果较长字符串在那个字符之后的部分和较短字符串那个
字符及之后的部分是一样的，则符合要求

如果两个字符串长度差距大于1，肯定不对

"""

#-*- coding:utf-8 -*-
