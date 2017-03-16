#coding=utf-8

import unittest

"""

179. Largest Number

Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

Subscribe to see which companies asked this question.

Hide Tags Sort

Medium

"""



class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums): #68ms, 37%
        def compare(a,b):
            ab = int("".join([a,b]))
            ba = int("".join([b,a]))
            if ab>ba:
                return 1
            elif ab<ba:
                return -1
            else:
                return 0
        if not nums:
            return ""
        strs = [str(x) for x in nums]
        strs = sorted(strs, compare, reverse=True)
        #print strs
        result = "".join(strs)
        idx = 0
        while idx < len(result) and result[idx] == '0':
            idx += 1
        result = result[idx:]
        return result if result else "0"

        def compare_wrong1(a, b):
            a = str(a)
            b = str(b)
            n = min(len(a), len(b))
            for i in range(n):
                if a[i] > b[i]:
                    return 1
                elif a[i] < b[i]:
                    return -1
                else:
                    continue
            if len(a) < len(b):
                if b[n]=='0':
                    return 1
                else:
                    return a[n-1] > b[n]
            if len(a) > len(b):
                if a[n]=='0':
                    return -1
                else:
                    return a[n] > b[n-1]
            return 0


    def largestNumber_wrong(self, nums):
        if not nums:
            return ""
        strs = [str(x) for x in nums]
        strs.sort()
        result = "".join(strs[::-1])
        return result



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [3, 30, 34, 5, 9]
        answer = "9534330"
        result = self.sol.largestNumber(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [3, 30, 34, 90, 99, 9, 9, 91, 92]
        answer = "999992919034330"
        result = self.sol.largestNumber(nums)
        self.assertEqual(answer, result)

    def test_case3(self):
        nums = [3, 30, 34]
        answer = "34330"
        result = self.sol.largestNumber(nums)
        self.assertEqual(answer, result)

    def test_case4(self): #=====>
        nums = [0,0]
        answer = "0"
        result = self.sol.largestNumber(nums)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
