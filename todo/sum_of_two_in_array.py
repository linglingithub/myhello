#coding=utf-8

import unittest

"""
INput:
1. An array of ints, a
2. A long int , k

Output:

an int denoting the number of DISTINCT pairs (ai, aj) where
i != j, 
ai + aj = k
(ai, aj) and (aj, ai) are considered the same pair
(ai, aj) and (a1, a2) are considered the same pair if ai = a1 or ai = a2 althoug i != 1


constraints:
1 <= n <= 5*(10^5)
0 <= ai <= 10^9

"""



class Solution(object):
    def find_pair_cnt(self, nums, k):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [6,1,3,46,1,3,9]
        k = 47
        answer = 1
        result = self.sol.find_pair_cnt(nums, k)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [7,6,6,3,9,3,5,1]
        k = 12
        answer = 2
        result = self.sol.find_pair_cnt(nums, k)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
