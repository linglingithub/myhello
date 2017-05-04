#coding=utf-8

import unittest

"""

Copy Books II

Given n books( the page number of each book is the same) and an array of integer with size k means k people to copy the
book and the i th integer is the time i th person to copy one book). You must distribute the continuous id books to one
people to copy. (You can give book A[1],A[2] to one people, but you cannot give book A[1], A[3] to one people, because
book A[1] and A[3] is not continuous.) Return the number of smallest minutes need to copy all the books.

Example
Given n = 4, array A = [3,2,4], .


Return 4( First person spends 3 minutes to copy book 1, Second person spends 4 minutes to copy book 2 and 3, Third
person spends 4 minutes to copy book 4. )


Hard

"""

class Solution:
    # @param n: an integer
    # @param times: a list of integers
    # @return: an integer
    def copyBooksII(self, n, times):
        # write your code here



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        n =4
        nums = [3,2,4]
        answer = 4
        result = self.sol.copyBooksII(n, nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
