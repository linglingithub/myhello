#coding=utf-8

import unittest

"""

Input:
2d grid, with some numbers and blank space, to solve it, fill the blank places with . or #
'.': water
'#': island

constraits:
no 2*2 blocks of water
no other characters in the grid (only ., #, number), no space left
all water is connected ( up-down-left-right, not diagonally)
each connected group of islands contains exactly one number square


the problem is not to solve, but to check if the input is a valid solve.


Output:
True or False ( if the puzzle is valid )

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
