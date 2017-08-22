#coding=utf-8
"""
Roman to Integer

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

Subscribe to see which companies asked this question

Hide Tags Math String
Hide Similar Problems (M) Integer to Roman

"""


import unittest

class Solution(object):
    # http://bangbingsyb.blogspot.com/2014/11/leetcode-roman-to-integer.html
    # http://www.cnblogs.com/zuoyuan/p/3779688.html
    # roman numeral chart http://literacy.kent.edu/Minigrants/Cinci/romanchart.htm
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        r2i_dict = {
            "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1
        }
        result = 0
        for i in range(len(s)):
            result = result + r2i_dict[s[i]]
            if i > 0 and r2i_dict[s[i]] > r2i_dict[s[i-1]]:  # deal with reversed weight order
                result = result - 2*r2i_dict[s[i-1]]
        return result




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        s = ""
        answer = 0
        result = self.sol.romanToInt(s)
        self.assertEqual(answer, result)

    def test_case2(self):
        s = "IV"
        answer = 4
        result = self.sol.romanToInt(s)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()


"""
罗马数字是拼凑成的, 如

XXXII -- 32
LXIII -- 63
DCCVII -- 707

大权重的字母排在前面。需要注意有倒序出现的时候，

4 = IV
LXIX= 69， 
XLVI = 46

后一个数字减去前一个数字， 一般在9 和4出现的时候 

"""