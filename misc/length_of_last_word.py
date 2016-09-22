"""
Length of Last Word

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.

Subscribe to see which companies asked this question

Hide Tags String

"""

import unittest

class Solution(object):

    def lengthOfLastWord(self, s):
        return len(s.split()[-1]) if s.split() != [] else 0


    def lengthOfLastWord2(self, s): # slowest
        return len(s.strip().split(' ')[-1])


    def lengthOfLastWord1(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_start, last_end = -1, -1
        found = False
        for i in range(len(s)-1, -1, -1):
            if 'A' <= s[i] <= 'z':
                last_end = i
                found = True
                break
        if found:
            for j in range(last_end, -1, -1):
                if s[j] == " ":
                    last_start = j+1
                    break
            if last_start == -1:
                last_start = 0
            return last_end + 1 - last_start
        else:
            return 0


class SolutionTestor(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        s = "Hello World"
        answer = 5
        result = self.sol.lengthOfLastWord(s)
        self.assertEqual(answer, result)

    def test_case2(self): # ==========>
        s = "b   a    "
        answer = 1
        result = self.sol.lengthOfLastWord(s)
        self.assertEqual(answer, result)



def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTestor)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    main()