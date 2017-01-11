"""

Search a 2D Matrix II


"""

import unittest


class Solution(object):
    def searchMatrix(self, matrix, target): #35ms, 94.5%
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        matrix = [
          [1,   3,  5,  7],
          [10, 11, 16, 20],
          [23, 30, 34, 50]
        ]
        target = 3
        answer = True
        result = self.sol.searchMatrix(matrix, target)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8