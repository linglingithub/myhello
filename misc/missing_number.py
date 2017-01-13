#coding=utf-8
__author__ = 'linglin'

"""

268. Missing Number

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

Subscribe to see which companies asked this question

Hide Tags Array Math Bit Manipulation
Hide Similar Problems (H) First Missing Positive (E) Single Number (H) Find the Duplicate Number

Medium

"""

import unittest
import operator


class Solution(object):
    def searchInsert(self, nums): #45ms, 95%
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        return (1+n)*n/2 - sum(nums)

    def searchInsert1(self, nums): #69ms, 36%
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        result = 0
        for i in range(1,n+1):
            result = result ^ i
        for i in nums:
            result = result ^ i
        return result


    def missingNumber_ref(self, nums): #55ms, 66%
        """
        :type nums: List[int]
        :rtype: int
        """
        a = reduce(operator.xor, nums)
        b = reduce(operator.xor, range(len(nums) + 1))
        return a ^ b

class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [0, 1, 3]
        answer = 2
        result = self.sol.searchInsert(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""

题目翻译: 从0到n之间取出n个不同的数，找出漏掉的那个。 注意：你的算法应当具有线性的时间复杂度。你能实现只占用常数额外空间复杂度的算法吗？

题目分析: 最直观的思路是对数据进行排序，然后依次扫描，便能找出漏掉的数字，但是基于比较的排序算法的时间复杂度至少是nlog(n)，不满足题目要求。

一种可行的具有线性时间复杂度的算法是求和。对0到n求和，然后对给出的数组求和，二者之差即为漏掉的数字。但是这种方法不适用于0是漏掉的数字的情况，
因为此时两个和是相同的。（或者也能由此得出漏掉的数字是0）

从CPU指令所耗费的时钟周期来看，比加法更高效率的运算是异或(XOR)运算。本题的标签里有位运算，暗示本题可以用位运算的方法解决。

异或运算的一个重要性质是，相同的数异或得0，不同的数异或不为0，且此性质可以推广到多个数异或的情形。本题的解法如下，首先将0到n这些数进行异或
运算，然后对输入的数组进行异或运算，最后将两个结果进行异或运算，结果便是漏掉的数字，因为其他数字在两个数组中都是成对出现的，异或运算会得到0。

时间复杂度：O(n) 空间复杂度：O(1)


"""


#-*- coding:utf-8 -*-
