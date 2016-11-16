"""

60. Permutation Sequence

The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

123
132
213
231
312
321

Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.

Subscribe to see which companies asked this question

Hide Tags Backtracking Math
Hide Similar Problems (M) Next Permutation (M) Permutations

Medium

"""

import unittest


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        n = 3
        k = 4
        answer = '231'
        result = self.sol.getPermutation(n, k)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8