#coding=utf-8

import unittest

"""
Input:
n : size of matrix
zombies: n * n matrix with values 0 or 1,  where [i][j] means zombie i knows zombie j, two way relation, which means 
[i][j] = [j][i]
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
            '.#2.1',
            '.....',
            '#2.#.',
            '...2.',
            '#2..1',
        ]
        answer = True
        result = self.sol.searchInsert(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [
            '..2.1',
            '..#..',
            '#2.#.',
            '...2.',
            '#2..1',
        ]
        answer = False  # there is 2*2 water, and the water group is disconnected with other water
        result = self.sol.searchInsert(nums)
        self.assertEqual(answer, result)



def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
