"""

ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
Subscribe to see which companies asked this question

Hide Tags String

"""
import unittest

class Solution(object):
    def convert1(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if s is None or len(s) < 2 or numRows < 2:
            return s
        result = ""
        for row in range(numRows):
            for col in range((len(s)-1)/(2*numRows-2)+1):
                idx = row + (2*numRows-2)*col
                if idx < len(s): # note protection
                    result += s[idx]
                if 0 < row < numRows - 1: # note protection
                    idx = 2*numRows-2 - row + (2*numRows-2)*col
                    if idx < len(s): # note protection
                        result += s[idx]
        return result

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if s is None or len(s) < 2 or numRows < 2: # add, then change <1 to <2, then add numRows < 2
            return s

        result = ""
        print "total length of string: ", len(s)
        for row in range(numRows):
            print "======== ", row
            for col in range((len(s)-1)/(2*numRows-2)+1): # need protection outside
                print "||||| ", col
                idx = row + (2*numRows-2)*col
                if idx < len(s): # note protection
                    result += s[idx]
                    print ">>> ", row + (2*numRows-2)*col
                if 0 < row < numRows - 1: # note protection
                    idx = 2*numRows-2 - row + (2*numRows-2)*col
                    if idx < len(s): # note protection
                        result += s[idx]
                        print ">>> ", 2*numRows-2 - row + (2*numRows-2)*col
        return result


class SolutionTestor(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        s = "PAYPALISHIRING"
        numRows = 3
        answer = "PAHNAPLSIIGYIR"
        result = self.sol.convert(s, numRows)
        self.assertEqual(answer, result)

    def test_case2(self):
        s = ""
        numRows = 1
        answer = ""
        result = self.sol.convert(s, numRows)
        self.assertEqual(answer, result)

    def test_case3(self):
        s = "A"
        numRows = 1
        answer = "A"
        result = self.sol.convert(s, numRows)
        self.assertEqual(answer, result)

    def test_case4(self):
        s = "AB"
        numRows = 1
        answer = "AB"
        result = self.sol.convert(s, numRows)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTestor)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    main()