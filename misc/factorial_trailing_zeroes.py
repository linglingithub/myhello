#coding=utf-8

import unittest
#import math

"""
172. Factorial Trailing Zeroes

Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

Subscribe to see which companies asked this question.

Hide Tags Math
Hide Similar Problems (H) Number of Digit One


Easy

"""



class Solution(object):
    def trailingZeroes1(self, n): #49ms, 39%
        """
        2,5,10..., 2 always more than 5, 0 can be made with the number of 5s?
        how to count 5s? NOTE that 25 has 2 5s!!, 50 , 75 also have 2 5s, then 125 has 3 5s

        :type n: int
        :rtype: int
        """
        if n <= 0: #if use math.log, need to include 0 here. otherwise wrong for case11
            return 0
        result = 0
        while n>0:
            tmp = n/5
            result += tmp
            n = tmp
        return result

    def trailingZeroes(self, n): #39ms, 86%, ref the recursive way
        """
        :type n: int
        :rtype: int
        """
        return 0 if n <= 0 else n/5 + self.trailingZeroes(n/5)


    def trailingZeroes_wrong(self, n):
        """
        2,5,10..., 2 always more than 5, 0 can be made with the number of 5s?
        how to count 5s? NOTE that 25 has 2 5s!!

        :type n: int
        :rtype: int
        """
        if n <= 0: #if use math.log, need to include 0 here. otherwise wrong for case11
            return 0
        import math
        return n/5 + sum([x for x in range(int(math.log(n,5)))])





class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = 1
        answer = 0
        result = self.sol.trailingZeroes(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = 2
        answer = 0
        result = self.sol.trailingZeroes(nums)
        self.assertEqual(answer, result)

    def test_case3(self):
        nums = 5
        answer = 1
        result = self.sol.trailingZeroes(nums)
        self.assertEqual(answer, result)

    def test_case4(self):
        nums = 9
        answer = 1
        result = self.sol.trailingZeroes(nums)
        self.assertEqual(answer, result)

    def test_case5(self):
        nums = 10
        answer = 2
        result = self.sol.trailingZeroes(nums)
        self.assertEqual(answer, result)

    def test_case6(self):
        nums = 15
        answer = 3
        result = self.sol.trailingZeroes(nums)
        self.assertEqual(answer, result)

    def test_case7(self):
        nums = 20
        answer = 4
        result = self.sol.trailingZeroes(nums)
        self.assertEqual(answer, result)

    def test_case8(self):
        nums = 25
        answer = 6
        result = self.sol.trailingZeroes(nums)
        self.assertEqual(answer, result)

    def test_case9(self): #====>
        nums = 30
        answer = 7
        result = self.sol.trailingZeroes(nums)
        self.assertEqual(answer, result)

    def test_case10(self):
        nums = 125
        answer = 31 # not 28 as self designed test case
        result = self.sol.trailingZeroes(nums)
        self.assertEqual(answer, result)

    def test_case11(self): #====>
        nums = 0
        answer = 0
        result = self.sol.trailingZeroes(nums)
        self.assertEqual(answer, result)


    def test_case12(self): #====>
        nums = 50
        answer = 12 # wrong one returned 11
        result = self.sol.trailingZeroes(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
"""

1 - 0
2 - 0
...
5 - 1
6 - 1
...
10 - 2
...
15 - 3
...
20 - 4
...
25 - 6 ( 25/5 + 5/5 + 1/ 5 = 6)
...
30 - 7
...
35,8
40,9
45,10
50 - 12 ( 50/5 + 10/5 + 2/5 = 12)
 ...
 55,13
 60,14
 65,15
 70,16
 75 - 18  (75/5 + 15/5 + 3/5 = 18)
...

"""