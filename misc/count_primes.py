#coding=utf-8

import unittest

"""

204. Count Primes

Description:

Count the number of prime numbers less than a non-negative number, n.

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.


Difficulty:Easy
Total Accepted:120.9K
Total Submissions:455.4K
Contributor: LeetCode
Subscribe to see which companies asked this question.

Related Topics 
Hash Table Math 
Similar Questions 
Ugly Number Ugly Number II Perfect Squares 

"""


class Solution(object):
    def countPrimes(self, n):
        """
        primes are integers that are greater than 1, and has only 1 and itself as the two positive divisors, 
        ints greater than 1 that are not primes are composites. prime examples: 2, 3, 5, 7...
        :type n: int
        :rtype: int
        """
        if n <= 2:  # number of primes less than n
            return 0
        is_prime = [True for _ in range(n)]
        res = 0
        for i in range(2, n): # since ask for less than n, so should be (2, n) here, case 1
            if is_prime[i]:
                res += 1
                j = i
                while i * j < n:  # should be n, not n+1 here
                    is_prime[i * j] = False
                    j += 1
        return res


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = 3
        answer = 1
        result = self.sol.countPrimes(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
