#coding=utf-8
__author__ = 'linglin'
"""

260. Single Number III

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly
 twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

Subscribe to see which companies asked this question

Hide Tags Bit Manipulation
Hide Similar Problems (E) Single Number (M) Single Number II


Medium

"""

import unittest


class Solution(object):
    def singleNumber(self, nums): #42ms, 94%
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        xor = 0
        for num in nums:
            xor ^= num
        mask = 1
        while xor & mask == 0:
            mask <<= 1
        num1, num2 = xor, xor
        for num in nums:
            if num & mask:
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1, 2, 1, 3, 2, 5]
        answer = [3,5]
        result = self.sol.singleNumber(nums)
        self.assertEqual(sorted(answer), sorted(result))


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""

这道题是之前那两道Single Number 单独的数字和 Single Number II 单独的数字之二的再次延伸，说实话，这类位操作Bit Manipulation的题，如果
之前没有遇到过类似的题目，楞想是很难相出来的，于是我只能上网搜大神们的解法，发现还真是巧妙啊。这道题其实是很巧妙的利用了Single Number 单
独的数字的解法，因为那道解法是可以准确的找出只出现了一次的数字，但前提是其他数字必须出现两次才行。而这题有两个数字都只出现了一次，那么我们如
果能想办法把原数组分为两个小数组，不相同的两个数字分别在两个小数组中，这样分别调用Single Number 单独的数字的解法就可以得到答案。那么如何
实现呢，首先我们先把原数组全部异或起来，那么我们会得到一个数字，这个数字是两个不相同的数字异或的结果，我们取出其中任意一位为‘1’的位，为了方
便起见，我们用 a &= -a 来取出最右端为‘1’的位，然后和原数组中的数字挨个相与，那么我们要求的两个不同的数字就被分到了两个小组中，分别将两个
小组中的数字都异或起来，就可以得到最终结果了，参见代码如下：



复制代码
class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        int diff = accumulate(nums.begin(), nums.end(), 0, bit_xor<int>());
        diff &= -diff;
        vector<int> res(2, 0);
        for (auto &a : nums) {
            if (a & diff) res[0] ^= a;
            else res[1] ^= a;
        }
        return res;
    }
};

"""

#-*- coding:utf-8 -*-
#coding=utf-8