"""
Plus One

Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

Subscribe to see which companies asked this question

Hide Tags Array Math
Hide Similar Problems (M) Multiply Strings (E) Add Binary (M) Plus One Linked List


"""


import unittest


class Solution(object):
    def plusOne1(self, digits): #52ms, 67.37%
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits is None or len(digits) < 1:
            return []
        result = []
        # carry = 0
        # tmp = digits[-1] + 1
        carry = 1
        for i in range(len(digits)-1, -1, -1): # or write as -- for i in reversed(xrange(len(digits))):
            tmp = digits[i] + carry
            carry = tmp / 10
            res = tmp % 10
            result.insert(0, res)
        if carry:
            result.insert(0, 1)
        return result

    def plusOne2(self, digits): # 38ms, 95.58% <--- 42ms, 90.05%
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits is None or len(digits) < 1:
            return []
        result = [0] * len(digits) # init the fixed size of result will improve efficiency too, to 38ms
        carry = 1
        for i in range(len(digits)-1, -1, -1): # or write as -- for i in reversed(xrange(len(digits))):
            tmp = digits[i] + carry
            carry = 1 if tmp == 10 else 0 # these calculation is much faster than divide and mod, faster to 42ms
            res = 0 if tmp == 10 else tmp
            # result.insert(0, res)
            result[i] = res
        if carry:
            result.insert(0, 1)
        return result

    def plusOne(self, digits): # run this multiple times, ranging from 80%+ to 10%+
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits is None or len(digits) < 1:
            return []
        carry = 1
        for i in range(len(digits)-1, -1, -1): # or write as -- for i in reversed(xrange(len(digits))):
            tmp = digits[i] + carry
            carry = 1 if tmp == 10 else 0 # these calculation is much faster than divide and mod, faster to 42ms
            res = 0 if tmp == 10 else tmp
            # result.insert(0, res)
            digits[i] = res
        if carry:
            digits.insert(0, 1)
        return digits


    def plusOne_ref(self, digits): #75ms, 14.38%, inplace, but slower
        flag = 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + flag == 10:
                digits[i] = 0
                flag = 1
            else:
                digits[i] = digits[i] + flag
                flag = 0

        if flag == 1:
            digits.insert(0, 1)
        return digits


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        digits = [9, 9, 9]
        answer = [1, 0, 0, 0]
        result = self.sol.plusOne(digits)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()