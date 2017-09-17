#coding=utf-8

import unittest

"""

290. Word Pattern

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

Credits:
Special thanks to @minglotus6 for adding this problem and creating all test cases.

Difficulty:Easy
Total Accepted:84.8K
Total Submissions:256.2K
Contributor: LeetCode
Subscribe to see which companies asked this question.

Related Topics 
Hash Table 
Similar Questions 
Isomorphic Strings Word Pattern II 

"""


class Solution_ref(object):
    def wordPattern(self, pattern, str):  # code clean and nice, used split() to tokenize str
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        mp1 = {}
        mp2 = {}
        words = str.split(' ')
        if len(words) != len(pattern):
            return False
        for word, ch in zip(words, pattern):
            if word not in mp1 and ch not in mp2:
                mp1[word] = ch
                mp2[ch] = word
            elif mp1.get(word) == ch and mp2.get(ch) == word:
                pass
            else:
                return False

        return True

    def wordPattern1(self, pattern, str):
        s = pattern
        t = str.split()
        return map(s.find, s) == map(t.index, t)

    def wordPattern2(self, pattern, str):
        s = pattern
        t = str.split()
        return map(s.find, s) == map(t.index, t)


class Solution(object):
    def wordPattern_wrong(self, pattern, str):  # forget about case 4
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        char_word = {}
        i, j = 0, 0
        while i < len(pattern):
            char = pattern[i]
            i += 1
            word, j = self.get_word(str, j)
            if not word:
                return False
            if char in char_word:
                if word != char_word[char]:
                    return False
            else:
                char_word[char] = word
        if j >= len(str) or not self.get_word(str, j)[0]:  # (1)shoud >= not ==, (2)may have trailing spaces?
            return True
        return False


    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        char_word = {}
        word_char = {}
        i, j = 0, 0
        while i < len(pattern):
            char = pattern[i]
            i += 1
            word, j = self.get_word(str, j)
            if not word:
                return False
            if char in char_word:
                if word not in word_char or word != char_word[char]:
                    return False
            else:
                if word in word_char:
                    return False
                char_word[char] = word
                word_char[word] = char
        if j >= len(str) or not self.get_word(str, j)[0]:  # may have trailing spaces?
            return True
        return False

    def get_word(self, str, idx):
        if idx >= len(str):
            return None, idx
        start = idx
        while idx < len(str) and str[idx] != " ":
            idx += 1
        word = str[start:idx]
        idx += 1  # when it's the end of str and no trailing space, idx will be len+1
        return word, idx


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        pattern = "abba"
        str = "dog cat cat dog"
        answer = True
        result = self.sol.wordPattern(pattern, str)
        self.assertEqual(answer, result)

    def test_case2(self):
        pattern = "abba"
        str = "dog cat cat fish"
        answer = False
        result = self.sol.wordPattern(pattern, str)
        self.assertEqual(answer, result)

    def test_case3(self):
        pattern = "aaaa"
        str = "dog cat cat dog"
        answer = False
        result = self.sol.wordPattern(pattern, str)
        self.assertEqual(answer, result)

    def test_case4(self):    # =====>
        pattern = "abba"
        str = "dog dog dog dog"
        answer = False
        result = self.sol.wordPattern(pattern, str)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
