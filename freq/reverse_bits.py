#coding=utf-8

import unittest

"""

190. Reverse Bits
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 
(represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer

Credits:
Special thanks to @ts for adding this problem and creating all test cases.


Difficulty:Easy
Total Accepted:113.6K
Total Submissions:385K
Contributor: LeetCode
Subscribe to see which companies asked this question.

Related Topics 
Bit Manipulation 
Similar Questions 
Number of 1 Bits 

"""



class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        for i in range(32):
            ans <<= 1
            ans |= n & 1
            n >>= 1
        return ans

    def reverseBits2(self, n):  # from ref, actually no need to worry about -, it says unsigned integer
        """
        s = bin(3), '0b11'
        s = bin(-3), '-0b11'
        a = "3".zfill(8), '00000003'
        a = "0101".zfill(8), '00000101'
        actually no need to worry about -, it says unsigned integer, following AC
        
        def reverseBits(self, n):
            string = bin(n)
            string = string[:2] + string[2:].zfill(32)[::-1]
            return int(string, 2)
        
        :param n: 
        :return: 
        """
        string = bin(n)
        if '-' in string:
            string = string[:3] + string[3:].zfill(32)[::-1]
        else:
            string = string[:2] + string[2:].zfill(32)[::-1]
        return int(string, 2)

    def reverseBits_ref(self, n):
        oribin = '{0:032b}'.format(n)
        reversebin = oribin[::-1]
        return int(reversebin, 2)


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = 43261596
        answer = 964176192
        result = self.sol.reverseBits(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""
Python代码（朴素解法）：
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        for i in range(32):
            ans <<= 1
            ans |= n & 1
            n >>= 1
        return ans

优化方案：
参考：https://oj.leetcode.com/discuss/27338/8ms-c-code-some-ideas-about-optimization-spoiler

以4位为单位执行反转，将0x0至0xF的反转结果预存在一个长度为16的数组中，反转时直接查询即可。

C代码：
char tb[16] = {0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15};

uint32_t reverseBits(uint32_t n) {
        int curr = 0;
        uint32_t ret = 0;
        uint32_t msk = 0xF;
        for(int i = 0; i < 8; i++) {
            ret = ret << 4;
            curr = msk&n;
            ret |= tb[curr];
            n = n >> 4;
        }
        return ret;
}



"""