"""
String to Integer (atoi)

Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge,

please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs).

You are responsible to gather all the input requirements up front.

Update (2015-02-10):
The signature of the C++ function had been updated.

If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.

spoilers alert... click to show requirements for atoi.

Requirements for atoi:
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.

Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible,

and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number,
which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number,

or if no such sequence exists because either str is empty or it contains only whitespace characters,

no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

If the correct value is out of the range of representable values,

INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.


Subscribe to see which companies asked this question

Hide Tags Math String
Hide Similar Problems (E) Reverse Integer (H) Valid Number



"""

import unittest
import re

class Solution(object):

    def myAtoi(self, s): # online, only 2.02%
        res, sign, cur = 0, 1, 0
        while cur < len(s):
            if s[cur] == ' ':
                cur += 1
            elif s[cur] == '-':
                sign, cur = -1, cur + 1
                break
            elif s[cur] == '+':
                cur += 1
                break
            elif ord(s[cur]) > 57 or ord(s[cur]) < 48:
                cur += len(s)
            else:
                break

        while cur < len(s) and ord(s[cur]) <= 57 and ord(s[cur]) >= 48:
            res, cur = res * 10 + (ord(s[cur]) - 48), cur + 1
        res *= sign
        return min(res, 2147483647) if res > 0 else max(res, -2147483648)


    def myAtoi6(self, str): #####self, 21.52%
        re_expr = re.compile("^\s*([+-]?\d+)\D*")
        match_result = re_expr.search(str)
        if match_result:
            result = int(match_result.group(1))
            INT_MAX = 2147483647
            INT_MIN = -2147483648
            result = min(result, INT_MAX)
            result = max(result, INT_MIN)
            return result
        else:
            return 0




    def myAtoi5(self, str): #29.60%
        INT_MAX = 2147483647; INT_MIN = -2147483648
        sum = 0
        sign = 1
        i = 0
        if str == '':
            return 0
        while i < len(str) and str[i].isspace():
            i += 1
        if i < len(str) and str[i] == '-':
            sign = -1
        if i < len(str) and (str[i] == '-' or str[i] == '+'):
            i += 1
        while i < len(str) and str[i].isdigit():
            digit = int(str[i])
            if INT_MAX/10 >= sum:
                sum *= 10
            else:
                if sign == 1:
                    return INT_MAX
                else:
                    return INT_MIN
            if INT_MAX - digit >= sum:
                sum += digit
            else:
                if sign == 1:
                    return INT_MAX
                else:
                    return INT_MIN
            i += 1
        return sign*sum


    def myAtoi4(self, str): #12.56%
        pointer = 0
        isNegative = False
        while pointer < len(str) and str[pointer] == ' ':
            pointer += 1
        if pointer == len(str):
            return 0
        if str[pointer] == '-':
            isNegative = True
            pointer += 1
        elif str[pointer] == '+':
            isNegative = False
            pointer += 1
        solution = 0
        for pointer in range(pointer, len(str)):
            if not str[pointer].isdigit():
                break
            else:
                solution *= 10
                solution += int(str[pointer])

        # This is because leetcode question is not prepared to Python but to Java/C so we truncate it
        if not isNegative and solution > 2147483647:
            return 2147483647
        elif isNegative and solution > 2147483648:
            return -2147483648

        if isNegative:
            return -1 * solution
        else:
            return solution


    def myAtoi3(self, str): # 12.56%
        str = str.strip()
        newStr = []
        for i in xrange(len(str)):
            if '0' <= str[i] <= '9' or (str[i] in ('+', '-') and i == 0):
                newStr.append(str[i])
            else:
                break
        if newStr in ([], ['+'], ['-']):
            return 0
        elif -2147483648 <= int(''.join(newStr)) <= 2147483647:
            return int(''.join(newStr))
        elif int(''.join(newStr)) > 2147483647:
            return 2147483647
        else:
            return -2147483648


    def myAtoi2(self, str): # self, slower, but not using python features
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = (1 << 31) - 1
        INT_MIN = 0 - ((1 << 31) )
        result = 0
        digit_start = False
        negative = False

        for i in range(len(str)):
            if str[i].isdigit() or str[i] in ["+", "-"]:
                if not digit_start:
                    digit_start = True
                else:
                    if not str[i].isdigit():
                        break

                if str[i].isdigit():
                    if i > 0 and str[i - 1] == '-':
                        negative = True
                    if not negative:
                        if result < INT_MAX / 10 or result == INT_MAX / 10 and int(str[i]) < INT_MAX % 10:
                            result = result * 10 + int(str[i])
                        else:
                            result = INT_MAX
                            break
                    else:
                        if result < abs(INT_MIN) / 10 or result == abs(INT_MIN) / 10 and int(str[i]) < abs(INT_MIN) % 10:
                            result = result * 10 + int(str[i])
                        else:
                            result = abs(INT_MIN)
                            break
            else:
                if digit_start:
                    break
                else:
                    if str[i].isspace():
                        continue
                    else:
                        return 0

        if negative:
            result = 0 - result
        return result


    def myAtoi1(self, str): # not working
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = (1 << 31) - 1
        INT_MIN = 0 - ((1 << 31))
        result = 0
        digit_start = False
        negative = False

        for i in range(len(str)):
            if str[i].isdigit():
                if not digit_start:
                    digit_start = True
                    if i > 0 and str[i - 1] == '-':
                        negative = True
                    if i > 1 and (str[i - 1] == '-' or str[i - 1] == '+') and (str[i - 2] == '-' or str[i - 2] == '+'):
                        return 0
                if not negative:
                    if result < INT_MAX / 10 or result == INT_MAX / 10 and int(str[i]) < INT_MAX % 10:
                        result = result * 10 + int(str[i])
                    else:
                        result = INT_MAX
                        break
                else:
                    if result < abs(INT_MIN) / 10 or result == abs(INT_MIN) / 10 and int(str[i]) < abs(INT_MIN) % 10:
                        result = result * 10 + int(str[i])
                    else:
                        result = abs(INT_MIN)
                        break
            else:
                if digit_start:
                    break
        if negative:
            result = 0 - result
        return result









class SolutionTestor(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        str = "   fdsa 0  1  89 0"
        answer = 0
        result = self.sol.myAtoi(str)
        self.assertEqual(answer, result)


    def test_case2(self):
        str = "   fdsa - 0  1  89 0"
        answer = 0
        result = self.sol.myAtoi(str)
        self.assertEqual(answer, result)

    def test_case3(self):
        str = "    "
        answer = 0 #???
        result = self.sol.myAtoi(str)
        self.assertEqual(answer, result)

    def test_case4(self):
        str = ""
        answer = 0
        result = self.sol.myAtoi(str)
        self.assertEqual(answer, result)

    def test_case5(self):
        str = "      2147483648"
        answer = 2147483647
        result = self.sol.myAtoi(str)
        self.assertEqual(answer, result)

    def test_case6(self):
        str = "      -2147483649"
        answer = -2147483648
        result = self.sol.myAtoi(str)
        self.assertEqual(answer, result)

    def test_case7(self):
        str = "      +-2"
        answer = 0
        result = self.sol.myAtoi(str)
        self.assertEqual(answer, result)

    def test_case8(self):
        str = "-2147483647"
        answer = -2147483647
        result = self.sol.myAtoi(str)
        self.assertEqual(answer, result)

    def test_case9(self):
        str = "   - 321"
        answer = 0
        result = self.sol.myAtoi(str)
        self.assertEqual(answer, result)

    def test_case10(self):
        str = " b11228552307"
        answer = 0
        result = self.sol.myAtoi(str)
        self.assertEqual(answer, result)

    def test_case11(self):
        str = "   -04f"
        answer = -4
        result = self.sol.myAtoi(str)
        self.assertEqual(answer, result)

    def test_case12(self):
        str = "  -0012a42"
        answer = -12
        result = self.sol.myAtoi(str)
        self.assertEqual(answer, result)





def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTestor)
    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    main()

"""

I think we only need to handle four cases:

discards all leading whitespaces
sign of the number
overflow
invalid input
Is there any better solution? Thanks for pointing out!

int atoi(const char *str) {
    int sign = 1, base = 0, i = 0;
    while (str[i] == ' ') { i++; }
    if (str[i] == '-' || str[i] == '+') {
        sign = 1 - 2 * (str[i++] == '-'); 
    }
    while (str[i] >= '0' && str[i] <= '9') {
        if (base >  INT_MAX / 10 || (base == INT_MAX / 10 && str[i] - '0' > 7)) {
            if (sign == 1) return INT_MAX;
            else return INT_MIN;
        }
        base  = 10 * base + (str[i++] - '0');
    }
    return base * sign;
}

"""