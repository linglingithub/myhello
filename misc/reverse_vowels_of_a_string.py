#coding=utf-8

import unittest

"""

345. Reverse Vowels of a String
DescriptionHintsSubmissionsDiscussSolution
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".


"""




class Solution:
    def reverseVowels(self, s):
        """
        vowels : a, e, i, o, u
        use two pointers, starting from two ends of the string
        when encounter vowels , swap
        stop until i > j
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        VOWELS = 'aeiouAEIOU'
        i, j = 0, len(s) - 1
        s = list(s)
        while i < j:
            if s[i] not in VOWELS:
                i += 1
                continue
            if s[j] not in VOWELS:
                j -= 1
                continue
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return "".join(s)


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = 1
        answer = 1
        result = self.sol.testm(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""
Python

def reverseVowels(self, s):
    vowels = re.findall('(?i)[aeiou]', s)
    return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)
It's possible in one line, but I don't really like it:

def reverseVowels(self, s):
    return re.sub('(?i)[aeiou]', lambda m, v=re.findall('(?i)[aeiou]', s): v.pop(), s)
Another version, finding replacement vowels on the fly instead of collecting all in advance:

def reverseVowels(self, s):
    vowels = (c for c in reversed(s) if c in 'aeiouAEIOU')
    return re.sub('(?i)[aeiou]', lambda m: next(vowels), s)


"""
#-*- coding:utf-8 -*-
