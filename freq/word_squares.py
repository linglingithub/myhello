#coding=utf-8

import unittest

"""

634. Word Squares 

 Description
 Notes
 Testcase
 Judge
Given a set of words without duplicates, find all word squares you can build from them.

A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.

b a l l
a r e a
l e a d
l a d y
 Notice

There are at least 1 and at most 1000 words.
All words will have the exact same length.
Word length is at least 1 and at most 5.
Each word contains only lowercase English alphabet a-z.
Have you met this question in a real interview? Yes
Example
Given a set ["area","lead","wall","lady","ball"]
return [["wall","area","lead","lady"],["ball","area","lead","lady"]]
Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word 
square matters).

Given a set ["abat","baba","atan","atal"]
return [["baba","abat","baba","atan"],["baba","abat","baba","atal"]]
Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word 
square matters).
Tags 
Trie Backtracking Google
Related Problems 
Hard Boggle Game 18 %
Hard K Edit Distance 26 %
Medium Implement Trie


"""

class Solution:
    """
    @param: words: a set of words without duplicates
    @return: all word squares
    """
    def wordSquares(self, words):
        # write your code here

class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = ["area","lead","wall","lady","ball"]
        answer = [["wall","area","lead","lady"],["ball","area","lead","lady"]]
        result = self.sol.testm(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = ["abat","baba","atan","atal"]
        answer = [["baba","abat","baba","atan"],["baba","abat","baba","atal"]]
        result = self.sol.testm(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
