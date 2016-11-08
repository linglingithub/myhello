"""

49. Group Anagrams

Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.

Subscribe to see which companies asked this question

Hide Tags Hash Table String
Hide Similar Problems (E) Valid Anagram (E) Group Shifted Strings


"""


import unittest


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if strs is None or len(strs)==0:
            return []
        word_map = {}
        for word in strs:
            sortedword = "".join(sorted(word))
            if sortedword in word_map:
                word_map[sortedword].append(word)
            else:
                word_map[sortedword] = [word]
        return word_map.values()


    def anagrams_ref(self, strs):
        dict = {}
        for word in strs:
            sortedword = ''.join(sorted(word))
            dict[sortedword] = [word] if sortedword not in dict else dict[sortedword] + [word]
        res = []
        for item in dict:
            if len(dict[item]) >= 2:
                res += dict[item]
        return res


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        input = ["eat", "tea", "tan", "ate", "nat", "bat"]
        answer = [
          ["ate", "eat","tea"],
          ["nat","tan"],
          ["bat"]
        ]
        result = self.sol.groupAnagrams(input)
        self.assertEqual(answer.sort(), result.sort())


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8