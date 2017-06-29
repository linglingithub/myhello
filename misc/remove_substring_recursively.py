#coding=utf-8

import unittest

"""


Remove Substring Recursively

Given two strings s and t. Find the maximum number of times that one can recursively remove t from s.

Example 1:
s = "aabcbc"
t="abc"
Return 2.
We can first remove s[1:3] and s becomes "abc". We can then remove it all.

Example 2:
s = "abababaaba"
t="ababa"
Return 2.

"""



class Solution(object):
    def remove(self, s, t):
        res = 0
        i = 0
        while i < (len(s) - len(t) + 1):
            if s[i:i + len(t)] == t:
                l = self.remove(s[:i], t)
                r = self.remove(s[i + len(t):], t)
                m = self.remove(s[:i] + s[i + len(t):], t)
                curr_max = max(l, max(r, m)) + 1
                if curr_max > res:
                    res = curr_max
            i += 1
        return res


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = 1
        answer = 1
        result = self.sol.searchInsert(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
