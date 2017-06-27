#coding=utf-8

import unittest

"""
438. Find All Anagrams in a String  (lincode: Substring Anagrams)

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

Easy

"""


class Solution(object):
    def findAnagrams_ref_dontUnderstand(self, s, p):

        ls, lp = len(s), len(p)
        count = lp
        from collections import Counter
        cp = Counter(p)
        ans = []
        for i in range(ls):
            char = s[i]
            if cp[s[i]] >=1 :
                count -= 1
            cp[s[i]] -= 1
            if i >= lp:
                char_l = s[i - lp]
                if cp[s[i - lp]] >= 0:
                    count += 1
                cp[s[i - lp]] += 1
            if count == 0:
                ans.append(i - lp + 1)
        return ans

    def findAnagrams_self_good(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if not p or not s or len(p) > len(s):
            return []
        from collections import Counter
        pattern = Counter(p)
        start, end = 0, 0
        m, n = len(s), len(p)
        count = n
        result = []
        while end < len(s):
            if s[end] not in pattern:
                end += 1
                start = end
                continue
            if start == end:
                pattern = Counter(p)
                count = n

            char = s[end]
            pattern[char] -= 1
            count -= 1
            if pattern[char] >= 0:
                if count == 0:
                    result.append(start)
                if end-start >= n-1:  # should not have chance to be >
                    lchar = s[start]
                    pattern[lchar] += 1
                    count += 1
                    start += 1
            else:
                while start < end and s[start] != char:
                    pattern[s[start]] += 1  # should be before start += 1, otherwise wrong, case5
                    start += 1
                    count += 1

                start += 1
                pattern[char] += 1
                count += 1
                if count == 0:
                    result.append(start)

            end += 1 #don't forget this

        return result









class Solution_AC_butNotGood(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if not p or not s or len(p) > len(s):  # check the length too, case 4
            return []
        from collections import Counter
        self.pattern = Counter(p)
        start, end = 0, 0
        match = {}
        count = 0
        n = len(s)
        result = []
        while end < len(p):
            char = s[end]
            if char in match:
                match[char] += 1
            else:
                match[char] = 1
            end += 1
        end -= 1 # don't forget this, otherwise wrong

        #while end < len(s):
        while True:
            if self.valid_match(match):
                result.append(start)
            if end == n-1:
                break
            a, b = s[start], s[end + 1]
            match[a] -= 1
            if match[a] == 0:
                del match[a]
            if b in match:
                match[b] += 1
            else:
                match[b] = 1
            start += 1
            end += 1
        return result

    def valid_match(self, match):
        if len(self.pattern) != len(match):
            return False
        for k in self.pattern.keys():
            if k in match and match[k] == self.pattern[k]:
                continue
            else:
                return False
        return True


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case5(self):  #====> p can be longer than s
        s = "abaacbabc"
        p = "abc"
        answer = [3,4,6]
        result = self.sol.findAnagrams(s, p)
        self.assertEqual(answer, result)

    def test_case4(self):  #====> p can be longer than s
        s = "aaaaaaaaaa"
        p = "aaaaaaaaaaaaa"
        answer = []
        result = self.sol.findAnagrams(s, p)
        self.assertEqual(answer, result)


    def test_case3(self):  #====> p can have repeated chars
        s = "baa"
        p = "aa"
        answer = [1]
        result = self.sol.findAnagrams(s, p)
        self.assertEqual(answer, result)


    def test_case1(self):
        s = "cbaebabacd"
        p = "abc"
        answer = [0, 6]
        result = self.sol.findAnagrams(s, p)
        self.assertEqual(answer, result)

    def test_case2(self):
        s = "abab"
        p = "ab"
        answer = [0, 1, 2]
        result = self.sol.findAnagrams(s, p)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""
some very simple codes, not easy to write like this


class Solution(object):
    def findAnagrams(self, s, p):

        ls, lp = len(s), len(p)
        count = lp
        cp = collections.Counter(p)
        ans = []
        for i in range(ls):
            if cp[s[i]] >=1 :
                count -= 1
            cp[s[i]] -= 1
            if i >= lp:
                if cp[s[i - lp]] >= 0:
                    count += 1
                cp[s[i - lp]] += 1
            if count == 0:
                ans.append(i - lp + 1)
        return ans

"""