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
        # And for the last step, there is one multiply left, which can be done easily.
    """
    def myPow(self, x, n):
        """
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

    def myPow_ref(self, x, n):
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
        a = 2
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





def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()