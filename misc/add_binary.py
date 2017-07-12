"""

Add Binary

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

Subscribe to see which companies asked this question

Hide Tags Math String
Hide Similar Problems (M) Add Two Numbers (M) Multiply Strings (E) Plus One


"""


import unittest


class Solution:
    # @param {string} a a number
    # @param {string} b a number
    # @return {string} the result
    def addBinary(self, a, b):
        # Write your code here
        if not a:
            return b
        if not b:
            return a
        m, n = len(a), len(b)
        result = []
        if m < n:
            a, b = b, a
            m, n = n, m
        carry = 0
        i = 0
        while i < n:
            tmp = int(a[m-1-i]) + int(b[n-1-i])
            digit = (tmp + carry) % 2
            carry = (tmp + carry) / 2
            result.append(str(digit))
            i += 1
        if n < m :
            for j in range(i, m):
                tmp = carry + int(a[m-1-j])
                digit = tmp % 2
                carry = tmp / 2
                result.append(str(digit))
        # remember the last carry on
        if carry:
            result.append(str(carry))
        result.reverse()
        return "".join(result)

    def addBinary_wrong(self, a, b):
        # Write your code here
        if not a:
            return b
        if not b:
            return a
        m, n = len(a), len(b)
        result = []
        if m < n:
            a, b = b, a
            m, n = n, m
        carry = 0
        i = 0
        while i < n:
            tmp = int(a[i]) + int(b[i])
            digit = (tmp + carry) % 2
            carry = (tmp + carry) / 2
            result.append(str(digit))
            i += 1
        if n < m :
            for j in range(i, m):
                tmp = carry + int(a[j])
                digit = tmp % 2
                carry = tmp / 2
                result.append(str(digit))
        # remember the last carry on
        if carry:
            result.append(str(carry))
        result.reverse()
        return "".join(result)



class Solution1(object):
    def addBinary(self, a, b): #52ms, 88.89%
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a is None or b is None:
            return a if a is not None else b
        carry = 0
        if len(a) < len(b):
            a, b = b, a
        result = ["" for i in range(len(a))]
        #for i in range(len(b)-1, -1, -1):
        set_off = len(a) - len(b)
        for i in range(len(b) - 1, -1, -1):
            tmp = int(a[i+set_off]) + int(b[i]) + carry  # index for a should add set_off
            result[i+set_off] = str(tmp % 2)  # result index should add set_off
            carry = tmp / 2
        for i in range(len(a)-len(b)-1, -1, -1): # starting index should be len(a)-len(b) -1, don't forget -1
            tmp = int(a[i]) + carry
            result[i] = str(tmp % 2)
            carry = tmp / 2
        if carry == 1:
            result.insert(0,"1")
        return "".join(result)




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        a = '11'
        b = '111'
        answer = '1010'
        result = self.sol.addBinary(a, b)
        self.assertEqual(answer, result)

    def test_case2(self):
        n1 = 35
        n2 = 100
        a = '{0:b}'.format(n1)
        b = '{0:b}'.format(n2)
        answer = n1 + n2
        result = self.sol.addBinary(a, b)
        self.assertEqual(answer, int(result,base=2))


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()