"""
Integer to Roman

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

Subscribe to see which companies asked this question

Hide Tags Math String
Hide Similar Problems (E) Roman to Integer (H) Integer to English Words


"""

import unittest

class Solution(object):
    # from discussion
    def intToRoman(self, num): # 186ms, 9.38%
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return M[num / 1000] + C[(num % 1000) / 100] + X[(num % 100) / 10] + I[num % 10]


    # http://www.cnblogs.com/zuoyuan/p/3779581.html, same idea, different data structure
    def intToRoman2(self, num): # 129ms, 32.99%
        """
        :type num: int
        :rtype: str
        """
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        list = ''
        for i in range(0, len(values)):
            while num >= values[i]:
                num -= values[i]
                list += numerals[i]
        return list


    # http://bangbingsyb.blogspot.com/2014/11/leetcode-integer-to-roman.html
    def intToRoman1(self, num): # 189ms, 9.03%
        """
        :type num: int
        :rtype: str
        """
        i2r_dict = {
            1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4 : "IV", 1 : "I"
        }
        result = ""
        keys = sorted(i2r_dict.keys(), reverse=True)
        for key in keys:
            if num > 0:
                cnt = num / key
                if cnt > 0:
                    result += i2r_dict[key] * cnt
                    num -= key * cnt
        return result


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        num = 0
        answer = ""
        result = self.sol.intToRoman(num)
        self.assertEqual(answer, result)

    def test_case2(self):
        num = 4
        answer = "IV"
        result = self.sol.intToRoman(num)
        self.assertEqual(answer, result)

    def test_case3(self):
        num = 3978
        answer = "MMMCMLXXVIII"
        result = self.sol.intToRoman(num)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()

