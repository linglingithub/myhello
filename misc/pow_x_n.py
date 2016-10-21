"""
Pow(x, n)

Implement pow(x, n).

Subscribe to see which companies asked this question

Hide Tags Binary Search Math
Hide Similar Problems (M) Sqrt(x) (M) Super Pow


"""

import unittest, sys

class Solution(object):
    """
    The purpose is to use multiply, divide and mod, etc??  only to calculate the result.
        # to do this in a bottom-up way for the power number n is not a good idea, cause
        # at the last step ( power * 2 < n) , power could already be (less than half of a big nubmer)
        # if n is a very big number.
        # To tackle in a reasonable way, think like this. Since n is int, it can only be even or odd.
        # So it is better to do recursively in a top-down way -- divide the n by 2 each recursion.
        # <---- the above made some sense, for the recursive version.
        But does not show the key point for the iterative version.
        x^7 = x^4 * x^2 * x^1
        x^8 = x^8
        x^15 = x^8 * x^4 * x^2 * x^1
        ...
        so think about the power n as binary code, 7 = 111, 8 = 1000, 15 = 1111
    """
    def myPow_recursive(self, x, n):
        """
        -- recursive version
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 1 or x == 0:
            return x
        elif n == 0:
            return 1.0
        elif n < 0:
            return 1 / self.myPow(x, 0-n)
        elif n % 2:
            return x * self.myPow(x*x, n/2)
        else:
            return self.myPow(x*x, n/2)

    def myPow(self, x, n):
        """
        -- iterative way
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 1 or x == 0 or n == 1:
            return x
        elif n == 0:
            return 1.0
        elif n == -1:
            return 1.0/x # make sure result is float
        power = n
        reverse = False

        if n < 0:
            power = 0-n
            reverse = True

        result = 1
        multiplier = x
        while power > 0:
            if power % 2: # or power & 1
                result *= multiplier
            power /= 2 # or power = (power >> 1)
            multiplier *= multiplier
        #result *= multiplier
        if reverse:
            result = 1.0 / result
        return result


    def myPow_ref_iterative(self, x, n):
        if x == 0:
            if n == 0:
                return 1.0
            else:
                return 0
        if n == 0:
            return 1.0
        pos = True
        if n < 0:
            pos = False
            n = abs(n)
        np = x
        res = 1
        while n > 0:
            if n % 2:
                res *= np
            np *= np
            n /= 2
        return res if pos else 1.0 / res


    def myPow_tle(self, x, n):
            """
            :type x: float
            :type n: int
            :rtype: float
            """
            if x == 0 and n == -1:
                return sys.float_info.max
            if n == 0:
                return 1.0  # should be float, so can't not return 1
            reverse = False
            if n < 0:
                reverse = True
                n = 0 - n
            if n == 1:
                result = x
            else:
                power = 1
                result = x
                while power * 2 <= n:
                    result *= result
                    power *= 2
                while power < n:
                    result *= x
                    power += 1
            if reverse:
                result = float(1) / float(result)
            return result

    def myPow_ref_recursive(self, x, n):
        if n == 0:
            return 1.0
        elif n < 0:
            return 1 / self.myPow(x, -n)
        elif n % 2:
            return self.myPow(x * x, n / 2) * x
        else:
            return self.myPow(x * x, n / 2)



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        a = 2
        b = 1
        answer = 2.0
        result = self.sol.myPow(a, b)
        self.assertEqual(answer, result)

    def test_case2(self):
        a = 2
        b = -1
        answer = 0.5
        result = self.sol.myPow(a, b)
        self.assertEqual(answer, result)

    def test_case3(self):
        a = 2.0
        b = 3
        answer = 8.0
        result = self.sol.myPow(a, b)
        self.assertEqual(answer, result)

    def test_case4(self): ######=====> TLE
        a = 0.00001
        b = 2147483647
        answer = 0.0
        result = self.sol.myPow(a, b)
        self.assertEqual(answer, result)


    def test_case5(self):  ######=====> wrong anser for iterative version
        a = 3.89707
        b = 2
        answer = 15.187154584899998
        result = self.sol.myPow(a, b)
        self.assertEqual(answer, result)

    def test_case6(self):  ######=====> wrong anser for iterative version
        a = 4.70975
        b = -6
        answer = 0.00009162476446700508
        result = self.sol.myPow(a, b)
        self.assertEqual(answer, result)



def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()