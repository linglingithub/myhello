#coding=utf-8

import unittest

"""
202. Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by
the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops
 endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Credits:
Special thanks to @mithmatt and @ts for adding this problem and creating all test cases.

Subscribe to see which companies asked this question.

Hide Tags Hash Table Math
Hide Similar Problems (E) Add Digits (E) Ugly Number

Easy

"""



class Solution(object):

    def isHappy(self, n):
        if n < 0:
            return False
        visited = {}
        while n not in visited:
            if n == 1:
                return True
            visited[n] = 1
            tmp = 0
            while n > 0:
                x = n % 10
                tmp += x*x
                n /= 10
            n = tmp
            #print tmp, visited
        return False

    def isHappy1(self, n): #45ms, 88%
        """
        :type n: int
        :rtype: bool
        """
        if n < 0:
            return False
        visited = {}
        while n not in visited: # should be str() here
            if n == 1:
                return True
            visited[n] = 1
            tmp = 0
            while n > 0:
                x = n % 10
                tmp += pow(x, 2)
                n /= 10
            n = tmp
            print tmp, visited
        return False

    def isHappy_ref(self, n): #code simpler, not faster, 62ms, 34%
        """
        :type n: int
        :rtype: bool
        """
        numSet = set()
        while n != 1 and n not in numSet:
            numSet.add(n)
            sum = 0
            while n:
                digit = n % 10
                sum += digit * digit
                n /= 10
            n = sum
        return n == 1


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = 19
        answer = True
        result = self.sol.isHappy(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = 2
        answer = False
        result = self.sol.isHappy(nums)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
