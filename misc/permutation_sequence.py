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

import math
import unittest



class Solution(object):
    def getPermutation(self, n, k): #39ms, 89%
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        result = ""
        nums = [i for i in range(1, n+1)]
        if n == 0 or k > math.factorial(n):
            return ""
        for i in range(n, 1, -1):
            fac = math.factorial(i-1) # should be i-1 not n-1 here, otherwise wrong
            digit = (k-1) / fac  # should be k-1 here
            result += str(nums[digit])
            del nums[digit]
            k %= fac
        result += str(nums[0])
        return result



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        n = 3
        k = 4 # 123, 132, 213, 231,
        answer = '231'
        result = self.sol.getPermutation(n, k)
        self.assertEqual(answer, result)

    def test_case2(self):
        n = 3
        k = 1  # 123
        answer = '123'
        result = self.sol.getPermutation(n, k)
        self.assertEqual(answer, result)

    def test_case3(self):
        n = 3
        k = 5  # 123, 132, 213, 231, 312
        answer = '312'
        result = self.sol.getPermutation(n, k)
        self.assertEqual(answer, result)

    def test_case4(self): #=======>
        n = 4
        k = 2  # 1234, 1243
        answer = '1243'
        result = self.sol.getPermutation(n, k)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8