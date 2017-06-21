#coding=utf-8

import unittest

"""
Scramble String

Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

Have you met this question in a real interview? Yes
Example
Challenge 
O(n3) time

Tags 
String Dynamic Programming

"""


class Solution:
    # @param {string} s1 A string
    # @param {string} s2 Another string
    # @return {boolean} whether s2 is a scrambled string of s1
    def isScramble(self, s1, s2):  # ref, from jiuzhang
        # Write your code here
        if len(s1)!=len(s2): return False
        if s1==s2: return True
        l1=list(s1); l2=list(s2)
        l1.sort();l2.sort()
        if l1!=l2: return False
        length=len(s1)
        for i in range(1,length):
            if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]): return True
            if self.isScramble(s1[:i],s2[length-i:]) and self.isScramble(s1[i:],s2[:length-i]): return True
        return False

class Solution_wrong_understanding_case4:
    # @param {string} s1 A string
    # @param {string} s2 Another string
    # @return {boolean} whether s2 is a scrambled string of s1
    def isScramble(self, s1, s2):
        # Write your code here
        if not s1 or not s2:
            return False
        if len(s1) != len(s2):
            return False
        n = len(s1)
        dp = {}

        result = self.check_scramble(s1, s2, 0, n - 1, 0, n - 1, dp)
        return result

    def check_scramble(self, s1, s2, l1, r1, l2, r2, dp):
        if l1 > r1 or l2 > r2:
            return False
        if l1 == r1:
            if s1[l1] == s2[l2]:
                return True
            else:
                return False
        else:
            if (l1, r1, l2, r2) in dp:
                return dp[(l1, r1, l2, r2)]
            elif s1[l1:r1 + 1] == s2[l2:r2 + 1]:
                dp[(l1, r1, l2, r2)] = True
                return True
            #mid = (l1 + r1) / 2 - 1
            len = (r1-l1+1)/2
            mid = l1 + len - 1
            n = mid - l1
            tmp1 = self.check_scramble(s1, s2, l1, mid, l2, l2 - l1 + mid, dp) and self.check_scramble(s1, s2, mid + 1,
                                                                                                       r1,
                                                                                                       l2 - l1 + mid + 1,
                                                                                                       r2, dp)
            if tmp1:
                dp[(l1, r1, l2, r2)] = tmp1
                return tmp1
            tmp2 = self.check_scramble(s1, s2, l1, mid, r2 - n, r2, dp) and self.check_scramble(s1, s2, mid + 1, r1, l2,
                                                                                                l2 + r1 - mid - 1, dp)
            tmp = tmp1 or tmp2
            dp[(l1, r1, l2, r2)] = tmp
            return tmp






class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()


    def test_case4(self): #=======> ?? what does this mean, scramble can cut anywhere? not only in the middle?
        s1 = "abb"
        s2 = "bab"
        answer = True
        result = self.sol.isScramble(s1, s2)
        self.assertEqual(answer, result)

    def test_case3(self): #=======>
        s1 = "abb"
        s2 = "bba"
        answer = True
        result = self.sol.isScramble(s1, s2)
        self.assertEqual(answer, result)

    def test_case2(self):
        s1 = "great"
        s2 = "rgeat"
        answer = True
        result = self.sol.isScramble(s1, s2)
        self.assertEqual(answer, result)

    def test_case1(self):
        s1 = "great"
        s2 = "rgtae"
        answer = True
        result = self.sol.isScramble(s1, s2)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
