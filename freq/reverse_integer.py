"""
Reverse Integer

Difficulty: Easy
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Subscribe to see which companies asked this question

Hide Tags Math
Hide Similar Problems (E) String to Integer (atoi)


Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows.

How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Update (2014-11-10):
Test cases had been added to test the overflow behavior.

"""

import unittest
import math

class Solution(object):
    def reverse(self, x):
        """
        !!! -1 % 10 = 9 in python
        :type x: int
        :rtype: int
        """
        int_min = - (1 << 31)
        int_max = (1 << 31) - 1
        res = 0
        is_negative = x < 0
        if is_negative:
            x = -x
        while x > 0:
            res = res * 10 + (x % 10)
            x = int(x/10)
            if is_negative and res > int_max+1 or not is_negative and res > int_max:
                return 0
        return -res if is_negative else res



    def reverse2(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        result = 0
        if x < 0:
            negative = True
            x = 0 - x
        while x > 0:
            result = result * 10 + x % 10
            x = x / 10
        if not negative:
            if result > math.pow(2, 31) - 1:
                result = 0
        else:
            result = 0 - result
            if result < 0 - math.pow(2, 31):
                result = 0
        return result



    def reverse1(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        result = 0
        if x < 0:
            negative = True
            x = 0 - x
        while x > 0:
            result = result * 10 + x % 10
            x = x / 10
        if negative:
            result = 0 - result
        return result


class SolutionTestor(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        x = 123
        answer = 321
        result = self.sol.reverse(x)
        self.assertEqual(answer, result)

    def test_case2(self):
        x = 10
        answer = 1
        result = self.sol.reverse(x)
        self.assertEqual(answer, result)

    def test_case3(self):
        x = -100
        answer = -1
        result = self.sol.reverse(x)
        self.assertEqual(answer, result)

    def test_case4(self): # required by leetcode, but not actually true for python
        x = 1534236469
        answer = 0
        result = self.sol.reverse(x)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTestor)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    main()