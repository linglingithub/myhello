"""
Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

Subscribe to see which companies asked this question

Hide Tags String
Have you met this question in a real interview? Yes

Next challenges: (H) Regular Expression Matching  (E) Length of Last Word  (H) Distinct Subsequences

"""

import unittest

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        if strs is None or len(strs) == 0:
            return result
        if len(strs) == 1:
            return strs[0]
        for col in range(len(strs[0])):
            for row in range(1, len(strs)):
                if col < len(strs[row]) and col < len(strs[row-1]) and strs[row][col] == strs[row-1][col]:
                    continue
                else:
                    return result
            result += strs[0][col]
        return result


class SolutionTestor(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        strs = ["a", "b", "c"]
        answer = ""
        result = self.sol.longestCommonPrefix(strs)
        self.assertEqual(answer, result)

    def test_case2(self):
        strs = ["abc"]
        answer = "abc"
        result = self.sol.longestCommonPrefix(strs)
        self.assertEqual(answer, result)

    def test_case3(self):
        strs = ["abc","ab","abcdefg"]
        answer = "ab"
        result = self.sol.longestCommonPrefix(strs)
        self.assertEqual(answer, result)

    def test_case4(self): # =======>
        """
        Runtime Error Message:
        Line 11: IndexError: list index out of range
        Last executed input: []
        """
        strs = []
        answer = ""
        result = self.sol.longestCommonPrefix(strs)
        self.assertEqual(answer, result)





def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTestor)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    main()

"""
https://leetcode.com/articles/longest-common-prefix/



"""