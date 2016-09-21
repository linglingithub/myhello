"""
Palindrome Number

Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer",
you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.

Subscribe to see which companies asked this question

Hide Tags Math
Hide Similar Problems (E) Palindrome Linked List


"""

import unittest
import math

class Solution(object):
    def isPalindrome(self, x): # 15.95
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x == 0:
            return True
        if x % 10 == 0:
            return False

        rev = 0
        tmp = x
        while rev < x:
            rev = 10 * rev + tmp % 10
            tmp /= 10
        return rev == x


    def isPalindrome3(self, x): # 3.88%
        if x < 0:
            return False
        if x == 0:
            return True
        digit = int(math.log10(x))+1
        for i in range(0, digit // 2): # // mean floor int of divide ?
            head = (x // 10**(digit-i-1)) % 10 # ** means power
            tail = (x // 10**i) % 10
            if head != tail:
                return False
        return True

    def isPalindrome2(self, x): # 15.37%
        """
        :type x: int
        :rtype: bool
        """
        if x is None or type(x) is not int or x < 0:
            return False
        div = 1
        result = True
        while x/div >= 10:
            div *= 10
        while x:
            head = x / div
            tail = x % 10
            if head == tail:
                x = (x % div) / 10
                div = div / 100
            else:
                result = False
                break
        return result

    def isPalindrome1(self, x): # 11.21%
        """
        :type x: int
        :rtype: bool
        """
        if x is None or type(x) is not int or x < 0:
            return False
        digit = 1
        old = x
        result = True
        while x > 9:
            x = x / 10
            digit += 1
        x = old
        while x > 9:
            div = int(math.pow(10, (digit-1)))
            head = x / div
            tail = x % 10
            if head == tail:
                digit -= 2
                x = (x - (head * div) - tail) / 10 # don't forget to divide by 10, case5

            else:
                result = False
                break
        if digit > 1 and x > 0: # add digit because of case6, add >0 because of case7
            result = False
        return result


class SolutionTestor(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        x = 123
        answer = False
        result = self.sol.isPalindrome(x)
        self.assertEqual(answer, result)

    def test_case2(self):
        x = -1
        answer = False
        result = self.sol.isPalindrome(x)
        self.assertEqual(answer, result)

    def test_case3(self):
        x = 11
        answer = True
        result = self.sol.isPalindrome(x)
        self.assertEqual(answer, result)

    def test_case4(self):
        x = 101
        answer = True
        result = self.sol.isPalindrome(x)
        self.assertEqual(answer, result)


    def test_case5(self): # ======>
        x = 121
        answer = True
        result = self.sol.isPalindrome(x)
        self.assertEqual(answer, result)

    def test_case6(self): # ======>
        x = 1000021
        answer = False
        result = self.sol.isPalindrome(x)
        self.assertEqual(answer, result)

    def test_case7(self): # ======>
        x = 1001
        answer = True
        result = self.sol.isPalindrome(x)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTestor)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    main()