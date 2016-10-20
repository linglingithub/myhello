"""
Divide Two Integers

Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.

Subscribe to see which companies asked this question

Hide Tags Math Binary Search


"""

import unittest

class Solution(object):
    def divide(self, dividend, divisor):  # 78ms
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX = (1 << 31) - 1
        if divisor == 0:
            return INT_MAX
        neg = dividend < 0 < divisor or dividend > 0 > divisor
        ans = 0
        shift = 0
        a, b = abs(dividend), abs(divisor)
        while (b << 1) <= a:
            shift += 1
            b <<= 1
        while shift >= 0: # should be >= 0, not > 0 here
            if a >= b:
                a -= b
                ans += (1 << shift)
            shift -= 1
            b >>= 1

        if neg:
            ans = 0 - ans
            if ans < 0 - INT_MAX - 1:
                ans = 0 - INT_MAX - 1
        else:
            if ans > INT_MAX:
                ans = INT_MAX
        return ans








    def divide_ref1(self, dividend, divisor): #69ms
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX = 2147483647
        if divisor == 0:
            return INT_MAX
        neg = dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0
        a, b = abs(dividend), abs(divisor)
        ans, shift = 0, 31
        while shift >= 0:
            if a >= b << shift:
                a -= b << shift
                ans += 1 << shift
            shift -= 1
        if neg:
            ans = - ans
        if ans > INT_MAX:
            return INT_MAX
        return ans


    def divide_ref2(self, dividend, divisor): # 69ms
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX = (1 << 31) -1  #2147483647
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            if abs(dividend) < abs(divisor):
                return 0
        sum = 0
        count = 0
        res = 0
        a = abs(dividend)
        b = abs(divisor)
        while a >= b:
            sum = b
            count = 1
            while sum + sum <= a:
                sum += sum
                count += count
            a -= sum
            res += count
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            res = 0 - res
        if res > INT_MAX:
            return INT_MAX
        return res



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        a = 6
        b = 4
        answer = 1
        result = self.sol.divide(a, b)
        self.assertEqual(answer, result)


    def test_case2(self):
        a = 689058569423859
        b = 1
        answer = 2147483647
        result = self.sol.divide(a, b)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()