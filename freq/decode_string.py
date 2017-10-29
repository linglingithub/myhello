#coding=utf-8

import unittest

"""
394. Decode String
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

Difficulty:Medium
Total Accepted:39.4K
Total Submissions:94.8K
Contributor: LeetCode
Subscribe to see which companies asked this question.

Related Topics 
Stack Depth-first Search 
Similar Questions 
Encode String with Shortest Length 

"""



class Solution(object):

    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = []
        res = [""]
        k = 0
        str_buff = []
        for char in s:
            if '0' <= char <= '9':
                k = k * 10 + int(char)
            elif char == "[":
                cnt.append(k)
                res.append("")
                k = 0
            elif char == "]":
                times = cnt.pop()
                tmp = res.pop()
                if res:
                    res.append(res.pop() + tmp * times)
                else:
                    res.append(tmp * times)
            else:
                res.append(res.pop() + char)
        return "".join(res)


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = "3[a]2[bc]"
        answer = 'aaabcbc'
        result = self.sol.decodeString(nums)
        self.assertEqual(answer, result)


    def test_case2(self):
        nums = "3[a2[c]]"
        answer = 'accaccacc'
        result = self.sol.decodeString(nums)
        self.assertEqual(answer, result)

    def test_case3(self):
        nums = "3[a]2[bc]"
        answer = 'aaabcbc'
        result = self.sol.decodeString(nums)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
