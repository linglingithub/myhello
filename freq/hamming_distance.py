#coding=utf-8

import unittest

"""
461. Hamming Distance
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

Related Topics 
Bit Manipulation 
Similar Questions 
Number of 1 Bits Total Hamming Distance 

"""


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        diff = x ^ y
        cnt = 0
        while diff > 0:
            cnt += diff & 1
            diff >>= 1
        return cnt

    def hammingDistance1(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        diff = x ^ y
        cnt = 0
        while diff > 0:
            cnt += diff % 2
            diff >>= 1
        return cnt


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        a, b = 1, 4
        answer = 2
        result = self.sol.hammingDistance(a, b)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""
class Solution(object):
def hammingDistance(self, x, y):
    return bin(x^y).count('1')

"""