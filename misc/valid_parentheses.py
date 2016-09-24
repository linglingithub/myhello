"""
Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Subscribe to see which companies asked this question

Hide Tags Stack String
Hide Similar Problems (M) Generate Parentheses (H) Longest Valid Parentheses (H) Remove Invalid Parentheses


"""

import unittest

class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pair_dict = {"(":")", "{": "}", "[": "]"}
        if len(s) == 0:
            return True
        for char in s:
            if char in pair_dict: # original: ["(", "{", "["], original way 65m, changed to check in dict, 46ms, from around 20% to more than 57%
                stack.append(char)
            if char in [")", "}", "]"]:
                if len(stack) > 0 and pair_dict[stack.pop()] == char: # need to check len before pop, otherwise runtime error.
                    continue
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False





    def isValid_wrong(self, s): # wrong for case4
        """
        :type s: str
        :rtype: bool
        """
        open1 = 0
        open2 = 0
        open3 = 0
        for char in s:
            if char == "(":
                open1 += 1
            elif char == ")":
                open1 -= 1
            elif char == "{":
                open2 += 1
            elif char == "}":
                open2 -= 1
            elif char == "[":
                open3 += 1
            else:
                open3 -= 1
            if open1 < 0 or open2<0 or open3<0:
                return False
        if open1 == 0 and open2 == 0 and open3 == 0:
            return True
        else:
            return False





class SolutionTestor(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        s = ""
        answer = True
        result = self.sol.isValid(s)
        self.assertEqual(answer, result)

    def test_case2(self):
        s = "()"
        answer = True
        result = self.sol.isValid(s)
        self.assertEqual(answer, result)

    def test_case3(self):
        s = ")("
        answer = False
        result = self.sol.isValid(s)
        self.assertEqual(answer, result)

    def test_case4(self): #=====>
        s = "([)]"
        answer = False
        result = self.sol.isValid(s)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTestor)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()