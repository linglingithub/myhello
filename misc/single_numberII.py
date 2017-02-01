#coding=utf-8
__author__ = 'linglin'
"""

137. Single Number II

Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Subscribe to see which companies asked this question

Hide Tags Bit Manipulation
Hide Similar Problems (E) Single Number (M) Single Number III


Medium

"""

import unittest


class Solution(object):
    def singleNumber(self, nums): #185ms, 3.74%
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        common = 3
        single = 1
        result = 0
        for i in range(31):
            sum = 0
            mask = 1 << i
            for j in range(len(nums)):
                if nums[j] >= 0:
                    tmp = nums[j] & mask
                else:
                    b_str = '{0:032b}'.format(nums[j])
                    tmp = int(b_str[-i-1])
                if tmp == 0:
                    continue
                else:
                    sum += 1
            result += (((sum % common)/single)<<i)
        sign = 0
        sign_mask = 1<<31
        for j in range(len(nums)):
            sign += nums[j]&sign_mask
        sign = (sign%3)/single
        if sign == 0:
            return result
        else:
            if result == 0:
                return -2147483648
            return -result


    def singleNumber_ref(self, A): #python AC, 10.13%
        ans = 0
        for i in xrange(0,32):
            count = 0
            for a in A:
                if ((a >> i) & 1):
                    count+=1
            ans |= ((count%3) << i)
        return self.convert(ans)

    def convert(self,x):
        if x >= 2**31:
            x -= 2**32
        return x


    def singleNumber_good_wrong4neg(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        common = 3
        single = 1
        result = 0
        for i in range(32):
            sum = 0
            mask = 1 << i
            for j in range(len(nums)):
                tmp = nums[j] & mask
                if tmp == 0:
                    continue
                else:
                    sum += 1
            result += (((sum % common)/single)<<i)
        return result


    def singleNumber_ref_wrong4negative_javaAC(self, nums):
        if not nums:
            return -1
        result = 0
        bits = [0 for i in range(32)]
        for i in range(32):
            for j in range(len(nums)):
                bits[i] += ((nums[j] >> i) & 1)
                bits[i] %= 3
            result |= (bits[i] << i)
        return result


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case5(self): #====> min int
            nums = [-401451,-177656,-2147483646,-473874,-814645,-2147483646,-852036,-457533,-401451,-473874,-401451,-216555,-917279,-457533,-852036,-457533,-177656,-2147483646,-177656,-917279,-473874,-852036,-917279,-216555,-814645,2147483645,-2147483648,2147483645,-814645,2147483645,-216555]
            answer = -2147483648
            result = self.sol.singleNumber(nums)
            self.assertEqual(answer, result)


    def test_case3(self):
        nums = [-2,-2,-2,-1]
        answer = -1
        result = self.sol.singleNumber(nums)
        self.assertEqual(answer, result)

    def test_case1(self):
        nums = [1,1,2,3, 1, 3,3]
        answer = 2
        result = self.sol.singleNumber(nums)
        self.assertEqual(answer, result)



    def test_case2(self): #====> pay attent to negative number
            nums = [-2,-2,1,1,-3,1,-3,-3,-4,-2]
            answer = -4
            result = self.sol.singleNumber(nums)
            self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-


"""


由于x^x^x = x，无法直接利用I的方法来解。但可以应用类似的思路，即利用位运算来消除重复3次的数。以一个数组[14 14 14 9]为例，将每个数字以二进制表达：

1110
1110
1110
1001
_____
4331    对每一位进行求和
1001    对每一位的和做%3运算，来消去所有重复3次的数


"""