#coding=utf-8

import unittest

"""
Repeat String 

 Description
 Notes
 Testcase
 Judge
Write a function, give a string A consisting of N characters and a string B consisting of M characters, returns the 
number of times A must be stated such that B is a substring of the repeated string. If B can never be a substring of 
the repeated A, then your function should return -1.

 Notice

Assume that 0 <= N <= 1000, 1 <= M <= 1000

Have you met this question in a real interview? Yes
Example
Given A = abcd, B = cdabcdab

your function should return 3, bcause after stating string A three times we otain the string abcdabcdabcd. String B is 
a substring of this string.

Tags 
Google
Related Problems 
Medium Longest Repeating Subsequence

"""


class Solution:
    """
    @param: : string A to be repeated
    @param: : string B
    @return: the minimum number of times A has to be repeated
    
    abcd,  abcdabcd --> 2   # no pre, no tail
    ba, abab --> 3          # pre and tail
    abcd, cdabcd --> 2      # pre, no tail
    
    abcd, a --> 1  
    
    ab, abc --> -1
    abc, eabc --> -1
    abcd, ad --> -1         # if B not in A when len(B) < len(A)
    abcd, ef --> -1         #if any char not in A
    
    """

    def repeatedString(self, A, B):
        if not A or not B:
            return -1
        m = len(A)
        n = len(B)
        # if B shorter than A
        if n <= m:
            return 1 if B in A else -1

        from collections import Counter
        chars = Counter(A)
        # start searching a in b
        i = j = 0
        start = i
        while i < m:
            if A[i] != B[j]:
                if B[j] not in chars:
                    return -1
                i += 1
                start = i
            else:
                i += 1
                j += 1
        # did not find overlapping in A and B
        print("early part checking: ", start, i, j)
        if start == i:
            return -1
        # check later part of A with following part in B
        early_part = A[start:]
        later_part = A[:start]
        for k in range(len(later_part)):
            if j + k >= n or A[k] != B[j + k]:
                return -1
        print("later part checking: ", early_part, later_part, start, i, j)
        # j = 1+ end of matched early part
        # whole A found in B, now check remaining part of B
        # for easy proces of tailing in B, shift idx to compare as A starts

        # pattern = early_part + later_part
        # print("pattern: ", pattern)
        # res = 0 if start == 0 else 1
        res = 1

        # j = j+len(later_part)
        # j -= len(later_part)

        print("checking remaining: ", i, j, res)
        while j < n:
            res += 1  # should add before checking
            for k in range(m):
                print("Debug: ", k, j + k)
                if j + k >= n:  # need to add this protection
                    break
                if A[k] != B[j + k]:
                    return -1
            j += m  # finish one round, shift j
        return res

    def repeatedString_wrong(self, A, B):
        if not A or not B:
            return -1
        m = len(A)
        n = len(B)
        # if B shorter than A
        if n <= m:
            return 1 if B in A else -1

        from collections import Counter
        chars = Counter(A)
        # start searching a in b
        i = j = 0
        start = i
        while i < m and j < m:
            if A[i] != B[j]:
                if B[j] not in chars:
                    return -1
                i += 1
                start = i
            else:
                i += 1
                j += 1
        # did not find overlapping in A and B
        if start == i:
            return -1
        # check later part of A with following part in B
        early_part = A[start:]
        later_part = A[:start]
        for k in range(len(later_part)):
            if j + k >= n or A[k] != B[j + k]:
                return -1

        # whole A found in B, now check remaining part of B
        pattern = early_part + later_part
        res = 1 if start == 0 else 2
        j = j + k
        while j < n:
            for k in range(m):
                if pattern[k] != B[j + k]:
                    return -1
            j += k
            res += 1
        return res

    def repeatedString_wrong(self, A, B):
        # write your code here
        if not A or not B or len(B) % len(A) != 0:
            return -1
        i = j = 0
        m = len(A)
        n = len(B)
        start = j
        while i < m and j - start < m:
            if A[i] != B[j]:
                j += 1
                start = j
            else:
                i += 1
                j += 1  # don't forget this
        if i == m and j - start == m: # should not be j-start+1==m, j already be increased as i did
            return int(n / m) + (0 if start == 0 else 1)
        return -1


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        a = "abcd"
        b = "cdabcdab"
        answer = 3
        result = self.sol.repeatedString(a, b)
        self.assertEqual(answer, result)

    def test_case2(self): # ===>
        a = "abcd"
        b = "abcdab"
        answer = 2
        result = self.sol.repeatedString(a, b)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
