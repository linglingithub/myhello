#coding=utf-8

import unittest

"""
Input:
n : size of matrix
zombies: n * n matrix with values 0 or 1,  where [i][j] means zombie i knows zombie j, two way relation, which means [i][j] = [j][i]
[i][i] always 1


Output:
find zombie cluster count

"""



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
        nums = [
            [1,1,0,0],
            [1,1,1,0],
            [0,1,1,0],
            [0,0,0,1],
        ]
        answer = 2
        result = self.sol.searchInsert(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [
            [1,0,0,0],
            [0,1,0,0],
            [0,0,1,0],
            [0,0,0,1],
        ]
        answer = 4
        result = self.sol.searchInsert(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
