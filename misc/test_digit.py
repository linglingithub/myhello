#coding=utf-8

import unittest

"""


"""



class Solution(object):
    def searchInsert(self, input_to_test):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not input_to_test:
            return False

        has_non_zero_numeric_char = False
        has_decimal_char = False
        chars_in_input = list(input_to_test)

        has_leading_zero = False
        idx0_zero = False
        idx1_zero_after_sign = False

        for idx, char in enumerate(chars_in_input):
            try:
                current_char_value = int(char)
            except ValueError:
                if char == '.':
                    if has_decimal_char is False:
                        has_decimal_char = True
                        continue
                    else:
                        return False
                elif char == '-':
                    if idx != 0:
                        return False
                    else:
                        continue
                else:
                    return False

            if current_char_value == 0:
                if idx == 0:
                    idx0_zero = True
                    continue
                elif has_decimal_char:
                    continue
                elif has_non_zero_numeric_char:
                    continue
                elif chars_in_input[idx-1] != 0:
                    continue
                return False
            else:
                has_non_zero_numeric_char = True
                continue

        if not has_non_zero_numeric_char:
            if idx0_zero and (len(chars_in_input ) == 1 or has_decimal_char or has_non_zero_numeric_char):
                return True
            return False

        return True



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case00(self):
        nums = '0'
        answer = True
        result = self.sol.searchInsert(nums)
        self.assertEqual(answer, result)

    def test_case01(self):
        nums = '-0.002'
        answer = True
        result = self.sol.searchInsert(nums)
        self.assertEqual(answer, result)

    def test_case02(self):
        nums = '0.'
        answer = True
        result = self.sol.searchInsert(nums)
        self.assertEqual(answer, result)

    def test_case3(self):
        nums = '-00'
        answer = False
        result = self.sol.searchInsert(nums)
        self.assertEqual(answer, result)

    def test_case4(self):
        nums = '-.'
        answer = False
        result = self.sol.searchInsert(nums)
        self.assertEqual(answer, result)

    def test_case5(self):
        nums = '.'
        answer = False
        result = self.sol.searchInsert(nums)
        self.assertEqual(answer, result)

    def test_case6(self):
        nums = '1.00'
        answer = True
        result = self.sol.searchInsert(nums)
        self.assertEqual(answer, result)

    def test_case7(self):
        nums = '.9'
        answer = True
        result = self.sol.searchInsert(nums)
        self.assertEqual(answer, result)

    def test_case8(self):
        nums = '9.'
        answer = True
        result = self.sol.searchInsert(nums)
        self.assertEqual(answer, result)

    def test_case9(self):
        nums = '-0.'
        answer = False
        result = self.sol.searchInsert(nums)
        self.assertEqual(answer, result)

    def test_case10(self):
        nums = '-.3'
        answer = True
        result = self.sol.searchInsert(nums)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
