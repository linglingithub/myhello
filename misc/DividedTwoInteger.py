__author__ = 'linglin'


class Solution:
    # @return an integer
    def divide_1(self, dividend, divisor):
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            if abs(dividend) < abs(divisor):
                return 0
        sum = 0; count = 0; res = 0
        a = abs(dividend); b = abs(divisor)
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
        return res

    def divide2(self, dividend, divisor):
        isNegative = (dividend<0) ^ (divisor<0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        count = 1
        while dividend >= (divisor<<1):
            divisor <<= 1
            count <<=1
        result = 0
        while dividend > 0 and divisor>=1:
            if dividend>=divisor:
                dividend -= divisor
                result += count
            divisor >>= 1
            count >>=1
        if isNegative:
            return -result
        else:
            return result


    def divide(self, dividend, divisor):
        sign = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        while dividend >= divisor:
            k = 0; tmp = divisor
            while dividend >= tmp:
                quotient += 1 << k
                dividend -= tmp
                tmp <<= 1
                k += 1
        return quotient * sign

if __name__ == '__main__':
    sol = Solution()
    print sol.divide(20,3)