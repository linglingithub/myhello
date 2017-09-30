#coding=utf-8

import unittest

"""
344. Reverse String

DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".

Difficulty:Easy
Total Accepted:182.7K
Total Submissions:307.7K
Contributor: LeetCode
Subscribe to see which companies asked this question.

Related Topics 
Two Pointers String 
Similar Questions 
Reverse Vowels of a String Reverse String II 

"""



class Solution(object):
    def reverseString(self, s):
        """
        AC, not very good, check the ref
        :type s: str
        :rtype: str
        """
        buff = [s[i] for i in range(len(s)-1, -1, -1)]
        return "".join(buff)


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

"""

Python 3 solutions: Recursive, Classic, Pythonic
class Solution(object):
    def reverseString(self, s):
        l = len(s)
        if l < 2:
            return s
        return self.reverseString(s[l/2:]) + self.reverseString(s[:l/2])


class SolutionClassic(object):
    def reverseString(self, s):
        r = list(s)
        i, j  = 0, len(r) - 1
        while i < j:
            r[i], r[j] = r[j], r[i]
            i += 1
            j -= 1

        return "".join(r)

class SolutionPythonic(object):
    def reverseString(self, s):
        return s[::-1]
        
=======================================================        


Python solution
Python:

   class Solution(object):
        def reverseString(self, s):
            return s[::-1]
"""

#-*- coding:utf-8 -*-
