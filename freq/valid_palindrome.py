#coding=utf-8
__author__ = 'linglin'
"""

125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

Subscribe to see which companies asked this question

Hide Tags Two Pointers String
Hide Similar Problems (E) Palindrome Linked List

Easy

"""

import unittest


class Solution(object):

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        i, j = 0, len(s)-1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if i < j and s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

    def isPalindrome1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        i, j = 0, len(s) - 1
        while i < j:
            while i < len(s) and not self.is_letter_num(s[i]):  # don't forget to check i, j boundary
                i += 1
            while j >= 0 and not self.is_letter_num(s[j]):
                j -= 1
            if i < j and s[i].lower() != s[j].lower():  # check i, j valid here
                return False
            i += 1  # don't forget to move i, j
            j -= 1
        return True

    def is_letter_num(self, char):
        if '0' <= char <= '9' or 'a' <= char <= 'z' or 'A' <= char <= "Z":
            return True
        return False

class Solution1:
    # @param {string} s A string
    # @return {boolean} Whether the string is a valid palindrome
    def isPalindrome(self, s):
        # Write your code here
        if not s:
            return True
        l, r = 0, len(s) - 1
        while l <= r:
            # while not self.is_letter(s[l]):
            while l <= r and not self.is_letter_number(s[l]):
                l += 1
            # while not self.is_letter(s[r]):
            while l <= r and not self.is_letter_number(s[r]):
                r -= 1
            if l >= r:
                return True
            if self.is_same_letter(s[l], s[r]):
                l += 1
                r -= 1
            else:
                return False
        return True

    def is_letter_number(self, char):
        return char.isalnum()

    def is_same_letter(self, char1, char2):
        return char1.lower() == char2.lower()


        # " " --> True
        # ".," --> True
        # "1a2" --> require to be false, note problem says "alphanumeric"

class Solution1(object):
    def isPalindrome(self, s): #79ms, 73%, use the built-in sialnum() method
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        l, r = 0, len(s)-1
        while l<=r:
            while l<r and not s[l].isalnum():
                l += 1
            while l<r and not s[r].isalnum():
                r -= 1
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True

    def isPalindrome1(self, s): #135ms, 13%
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        l, r = 0, len(s)-1
        while l <= r:
            # while not ('A' <= s[l] <= 'z' or '0' <= s[l] <= '9') and l < r: # wrong for case 5
            # looks like in python , 'Z' is not directly followeed by 'a'
            while not ('A' <= s[l] <= 'Z' or 'a' <= s[l] <= 'z' or '0' <= s[l] <= '9') and l < r:
                l += 1
            while not ('A' <= s[r] <= 'Z' or 'a' <= s[r] <= 'z'  or '0' <= s[r] <= '9') and l < r:
                r -= 1
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case4(self): #====>, alphanumeric means including numbers
        s = "0P"
        answer = False
        result = self.sol.isPalindrome(s)
        self.assertEqual(answer, result)

    def test_case5(self): #====>
        s = "`l;`` 1o1 ??;l`"
        answer = True
        result = self.sol.isPalindrome(s)
        self.assertEqual(answer, result)

    def test_case1(self):
        s = ""
        answer = True
        result = self.sol.isPalindrome(s)
        self.assertEqual(answer, result)

    def test_case2(self):
        s = "A man, a plan, a canal: Panama"
        answer = True
        result = self.sol.isPalindrome(s)
        self.assertEqual(answer, result)

    def test_case3(self):
        s = "race a car"
        answer = False
        result = self.sol.isPalindrome(s)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
