import unittest


class Solution(object):
    def searchInsert(self, nums):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        input = 1
        answer = 1
        result = self.sol.searchInsert(input)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8