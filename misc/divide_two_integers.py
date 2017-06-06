#coding=utf-8
"""
Divide Two Integers

Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.

Subscribe to see which companies asked this question

Hide Tags Math Binary Search


"""

import unittest

class Solution(object):

    def divide(self, dividend, divisor):
        # Write your code here
        INT_MAX = (1 << 31) - 1  # don't forget to -1 here, don't forget to add () here
        if divisor == 0:
            return INT_MAX
        neg = dividend < 0 < divisor or divisor < 0 < dividend
        a, b = abs(dividend), abs(divisor)
        ans, shift = 0, 0
        while b <= a:
            shift += 1
            b <<= 1
        #if 32>= shift > 0:
        if shift > 0:
            shift -= 1
            b >>= 1
            ans = (1 << shift)
            remain = a - b
            while remain >= abs(divisor):  # should be >= here, not > , case 7
                # remain -= b
                # ans += (1<<shift)
                shift -= 1    # do this after update remain and ans
                b >>= 1
                if remain >= b:  # should add this, not every shift of b can be added to result, case 8
                    remain -= b
                    ans += (1<<shift) if shift >= 0 else 0  # should do this after updating shift and b, case 6

        # elif shift > 32:
        #     ans = INT_MAX


        if neg:
            ans = - ans
        if ans > INT_MAX or ans < -INT_MAX-1:
            return INT_MAX
        return ans


    def divide_wrong(self, dividend, divisor):
        # Write your code here
        INT_MAX = 1 << 31 - 1  # don't forget to -1 here
        if divisor == 0:
            return INT_MAX
        neg = dividend < 0 < divisor or divisor < 0 < dividend
        a, b = abs(dividend), abs(divisor)
        ans, shift = 0, 0
        while b <= a:
            shift += 1
            b <<= 1
        shift -= 1
        b >>= 1
        ans = (1 << shift)
        remain = a - b
        while remain > abs(divisor):
            remain -= b
            ans += (1<<shift)
            shift -= 1    # do this after update remain and ans
            b >>= 1

        if neg:
            ans = - ans
        if ans > INT_MAX or ans < -INT_MAX-1:
            return INT_MAX
        return ans


    def divide1(self, dividend, divisor):  # good, 78ms
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

    def test_case08(self):
        a = 2147483647
        b = 3
        answer = 715827882  # wrong output 805306368
        result = self.sol.divide(a, b)
        self.assertEqual(answer, result)


    def test_case7(self):
        a = 2147483647
        b = 1
        answer = 2147483647   # wrong output 2147483644
        result = self.sol.divide(a, b)
        self.assertEqual(answer, result)


    def test_case6(self):
        a = 10
        b = 3
        answer = 3    # wrong output 4
        result = self.sol.divide(a, b)
        self.assertEqual(answer, result)


    def test_case5(self):
        a = 5
        b = 4
        answer = 1
        result = self.sol.divide(a, b)
        self.assertEqual(answer, result)


    def test_case4(self):
        a = 3
        b = 4
        answer = 0
        result = self.sol.divide(a, b)
        self.assertEqual(answer, result)


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

    def test_case3(self):
        a = 0
        b = 1
        answer = 0
        result = self.sol.divide(a, b)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()


"""

1. 先找到a使x*2^a <= y < x*2^(a+1)，res += 2^a，y = y - x*2^a

2. if(y >= x*2^(a-1) {res+=2^(a-1); y = y - x*2^(a-1);} 

3. if(y >= x*2^(a-2) {res+=2^(a-2); y = y - x*2^(a-2);}

...

但题目不允许用乘法，可以用移位代替：x*2^i = x<<i：

corner case，非常重要：

(1) x, y可能会是负数
(2) x可能为0时，返回INT_MAX或INT_MIN
(3) INT_MIN / -1 > INT_MAX，overflow



================================================================================================================================================================


10 3

0  3 * 2 ^ 0 = 3
1   3 * 2^1 = 6
2   3 * 2 ^2 = 12


2 ~ 4 

ans = 2

b = 6

shift = 1

10 - 6 = 4

shift - 1 = 0

tmp = 4 - 3 * 2^ shift = 4 - 3 = 1

ans + 2^shift = 2+1 = 3

tmp < 3, stop

"""