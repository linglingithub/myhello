#coding=utf-8

import unittest

"""


"""



class Solution(object):
    def valid_brace(self, strs):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not strs:
            return []
        res = []
        for onestr in strs:
            if self.check_valid(onestr):
                res.append("YES")
            else:
                res.append("NO")
        return res

    def check_valid(self, nums):
        stack = []
        lefts = "{[("
        rights = "}])"
        pairs = {
            "]": "[",
            "}": "{",
            ")": "(",
        }
        for char in nums:
            if char in lefts:
                stack.append(char)
                continue
            if char in rights:
                if not stack:
                    return False
                top_char = stack.pop()
                if pairs[char] != top_char:
                    return False
                continue
            # for not valid char in input
            return False
        return True




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = ["{}[]()", "{[}]}", "({[]})", "{)["]
        answer = ["YES", "NO", "YES", "NO"]
        result = self.sol.valid_brace(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
