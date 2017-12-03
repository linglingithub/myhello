#coding=utf-8

import unittest

"""
316. Remove Duplicate Letters
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only 
once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.

Difficulty:Hard
Total Accepted:35.3K
Total Submissions:117.6K
Contributor: LeetCode
Subscribe to see which companies asked this question.

Related Topics 
Stack Greedy 

"""

from collections import Counter
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        char_cnt = Counter(s)
        char_dict = {}
        stack = []
        i = 0
        n = len(s)
        while i < n:
            if stack and stack[-1] > s[i] and char_cnt[stack[-1]] > 0 and not char_dict.get(s[i]): # last condi for case4
                char_dict[stack[-1]] = False
                stack.pop()
                continue
            #if s[i] not in char_dict:   # wrong condition
            if not char_dict.get(s[i]):
                stack.append(s[i])
                #char_cnt[s[i]] -= 1    # this should be moved out of if, everytime move i, should update char_cnt, case3
                char_dict[s[i]] = True
            char_cnt[s[i]] -= 1
            i += 1
        return "".join(stack)


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = "bcabc"
        answer = 'abc'
        result = self.sol.removeDuplicateLetters(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = "cbacdcbc"
        answer = "acdb"
        result = self.sol.removeDuplicateLetters(nums)
        self.assertEqual(answer, result)

    def test_case3(self):
        nums = "bbcaac"
        answer = "bac"
        result = self.sol.removeDuplicateLetters(nums)
        self.assertEqual(answer, result)

    def test_case04(self):    #===> wrong output as acb
        nums = "abacb"
        answer = "abc"
        result = self.sol.removeDuplicateLetters(nums)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
