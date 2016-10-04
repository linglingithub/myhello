"""
Implement strStr()


Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Subscribe to see which companies asked this question

Hide Tags Two Pointers String
Hide Similar Problems (H) Shortest Palindrome


"""

import unittest


class Solution(object):
    # user naive way, check the KMP way later
    # you tube, Knuth-Morris-Pratt(KMP) Pattern Matching(Substring search)
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack) == 0 and len(needle) == 0: # they want this input to be 0, not -1
            return 0
        if not needle or len(needle) == 0:
            return 0
        for i in range(0, len(haystack)-len(needle)+1):
            match = True
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    match = False
                    break
            if match:
                return i
        return -1





class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        haystack = "fjdka;jfkd;jfk;djsakf;djsakf;ju94uqrnmvlc"
        needle = "c"
        answer = len(haystack) - 1
        result = self.sol.strStr(haystack, needle)
        self.assertEqual(answer, result)

    def test_case2(self):
        haystack = "fjdka;jfkd;jfk;djsakf;djsakf;ju94uqrnmvlc"
        needle = "@"
        answer = -1
        result = self.sol.strStr(haystack, needle)
        self.assertEqual(answer, result)

    def test_case3(self): # =======>
        haystack = ""
        needle = ""
        answer = 0
        result = self.sol.strStr(haystack, needle)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()