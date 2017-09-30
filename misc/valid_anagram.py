#coding=utf-8

import unittest

"""

242. Valid Anagram


Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?


Difficulty:Easy
Total Accepted:173.8K
Total Submissions:372.8K
Contributor: LeetCode
Subscribe to see which companies asked this question.

Related Topics 
Hash Table Sort 
Similar Questions 
Group Anagrams Palindrome Permutation Find All Anagrams in a String 

"""


class Solution(object):

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s and not t:
            return True
        char_map = {}
        for char in s:
            char_map[char] = char_map.get(char, 0) + 1
        for char in t:
            if char not in char_map:
                return False
            char_map[char] -= 1
            if char_map[char] == 0:
                del char_map[char]
        return not char_map

    def isAnagram_wrong(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s and not t:
            return True
        s.sort()  #'str' object has no attribute 'sort'
        t.sort()
        return s==t


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        s = "anagram"
        t = "nagaram"
        answer = True
        result = self.sol.isAnagram(s, t)
        self.assertEqual(answer, result)

    def test_case1(self):
        s = "anagram"
        t = "nagaram"
        answer = True
        result = self.sol.isAnagram(s, t)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""
The idea is simple. It creates a size 26 int arrays as buckets for each letter in alphabet. It increments the bucket 
value with String s and decrement with string t. So if they are anagrams, all buckets should remain with initial value 
which is zero. So just checking that and return

public class Solution {
    public boolean isAnagram(String s, String t) {
        int[] alphabet = new int[26];
        for (int i = 0; i < s.length(); i++) alphabet[s.charAt(i) - 'a']++;
        for (int i = 0; i < t.length(); i++) alphabet[t.charAt(i) - 'a']--;
        for (int i : alphabet) if (i != 0) return false;
        return true;
    }
}

"""