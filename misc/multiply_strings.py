"""
Multiply Strings

Given two numbers represented as strings, return multiplication of the numbers as a string.

Note:
The numbers can be arbitrarily large and are non-negative.
Converting the input string to integer is NOT allowed.
You should NOT use internal library such as BigInteger.
Subscribe to see which companies asked this question

Hide Tags Math String
Hide Similar Problems (M) Add Two Numbers (E) Plus One (E) Add Binary (E) Add Strings


"""

import unittest


class Solution(object):
    """
    -- One important note: a * b, result will be no longer than len(a)+len(b) digits.

    Mulitplying two non-negative numbers, usually called "da shu xiang cheng", one typical operation is to reverse
    both nums strings. Second step is to do mulitiplication digit by digit, but don't hurry to do carry on. Tmp result
    of each digit mulitiplication can be stored in an array. Do the tmp array carry-on after all multiplication done.
    Remove excessive leading zeron in result array of len(a)+len(b)

    """

    def multiply(self, num1, num2): # around 350 ~400 ms, 50%
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]
        result = [0]*(len(num1)+len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                result[i+j] += int(num1[i]) * int(num2[j]) # don't forget to convert to int
        carry = 0
        for i in range(len(result)):
            tmp = result[i] + carry
            result[i] = str(tmp % 10) # don't forget to convert to str
            carry = tmp / 10
        # if carry > 0: # this actually won't got executed because result won't be larger than len(a)+len(b)
        #     result.append(carry)
        result = result[::-1]
        while result[0] == '0' and len(result)>1:  # don't forget to remove extra leading 0 here. !!! don't forget the case of result '0'
            del result[0]
        return "".join(result)



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        num1 = "123"
        num2 = "456"
        answer = '56088'
        result = self.sol.multiply(num1, num2)
        self.assertEqual(answer, result)

    def test_case2(self): # ====> error if don't add protection when removing leading 0
        num1 = "0"
        num2 = "456"
        answer = '0'
        result = self.sol.multiply(num1, num2)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()