#coding=utf-8

import unittest
import ConfigParser

"""

Longest Substring with At Most K Distinct Characters

Given a string s, find the length of the longest substring T that contains at most k distinct characters.

Have you met this question in a real interview? Yes
Example
For example, Given s = "eceba", k = 3,

T is "eceb" which its length is 4.


Challenge 
O(n), n is the size of the string s.

Tags 
Hash Table Two Pointers LintCode Copyright String
Related Problems 
Medium Longest Substring Without Repeating Characters


"""


class Solution:
    # @param s : A string
    # @return : An integer
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        if not s:
            return 0
        if k < 1: # should not be 2 here, consider repeated chars, see case 2
            return k
        result = 0
        i, j = 0, 0
        res = {}
        while j < len(s):
            if s[j] not in res:
                cur = s[j]
                res[cur] = 1
                while len(res.keys()) > k:
                    tmp = s[i]
                    res[tmp] -= 1
                    if res[tmp] == 0:
                        del res[tmp]
                    i += 1

            else:
                res[s[j]] += 1
            # should be put here, can't be put under else
            result = max(result, j - i + 1)
            j += 1
        return result


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        s = "eceba"
        k = 3
        answer = 4
        result = self.sol.lengthOfLongestSubstringKDistinct(s, k)
        self.assertEqual(answer, result)

    def test_case2(self):
        config = ConfigParser.RawConfigParser(allow_no_value=True)
        data_file = "../data/longest_substring_with_at_most_k_distinct_characters.ini"
        with open(data_file) as fin:
            config.readfp(fin)
            s = config.get("data", "s")
            k = int(config.get("data", "k"))
            print type(s), s
            print type(k), k

        answer = 4
        result = self.sol.lengthOfLongestSubstringKDistinct(s, k)
        self.assertEqual(answer, result)




def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
