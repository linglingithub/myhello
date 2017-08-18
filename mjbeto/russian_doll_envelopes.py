#coding=utf-8

import unittest

"""
354. Russian Doll Envelopes

 Description
 Notes
 Testcase
 Judge
You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into 
another if and only if both the width and height of one envelope is greater than the width and height of the other 
envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Example
Given envelopes = [[5,4],[6,4],[6,7],[2,3]], 
the maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

Tags 
Binary Search Dynamic Programming Facebook
Related Problems 
Medium Longest Increasing Subsequence

"""



class Solution(object):
    def maxEnvelopes(self, envelopes):
        if not envelopes:
            return 0
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = [envelopes[0][1]]
        for envelope in envelopes[1:]:
            idx = self.find_pos(envelope[1], dp)
            if idx >= len(dp):
                dp.append(envelope[1])
            else:
                dp[idx] = envelope[1]
        return len(dp)

    def find_pos(self, target, nums):
        left, right = 0, len(nums)-1
        last = -1
        while left <= right:
            mid = left+(right-left)/2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                if last == mid:
                    return mid
                right = mid
                last = mid
        return left





    # @param {int[][]} envelopes a number of envelopes with widths and heights
    # @return {int} the maximum number of envelopes
    def maxEnvelopes_TLE(self, envelopes):  #TLE with 77% cases passed, local runs 9s+
        # Write your code here
        if not envelopes:
            return 0
        result = 0
        envelopes.sort(key=lambda x: (x[0], -x[1]))  # when same width, put bigger length first.
        dp = [1 for _ in range(len(envelopes))]
        for i in range(1, len(envelopes)):
            for j in range(0, i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[j]+1, dp[i])
            result = max(result, dp[i])
        return result

    def maxEnvelopes_TLE(self, envelopes):  #TLE with 77% cases passed, local runs 9s+
        # Write your code here
        if not envelopes:
            return 0
        envelopes.sort(key=lambda x: (x[0], -x[1]))  # when same width, put bigger length first.
        dp = [1 for _ in range(len(envelopes))]
        for i in range(1, len(envelopes)):
            for j in range(0, i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[j]+1, dp[i])
        # return dp[len(envelops)-1]  # this is wrong, max value may not be where the envelope is sorted as latest
        return max(dp)


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [[5,4],[6,4],[6,7],[2,3]]
        answer = 3
        result = self.sol.maxEnvelopes(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        from util.ini_file_util import IniFileUtil
        params = IniFileUtil.read_into_dict("russian_doll_envelopes_case2.ini")
        #nums = IniFileUtil.string_to_int_list(params.get("nums"))
        nums = IniFileUtil.string_to_int_list_list(params.get("nums"))   # for matrix input
        answer = int(params.get("answer"))
        result = self.sol.maxEnvelopes(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""

http://bookshadow.com/weblog/2016/06/07/leetcode-russian-doll-envelopes/

参考Longest Increasing Subsequence（最长递增子序列）的解法。

以输入envelopes其中的一个维度进行排序，对另外一个维度求解LIS即可。

1. 对输入的envelopes进行排序：首先比较宽度，宽度小的在前；宽度相同时，高度大的在前（这样处理可以避免相同宽度的信封被重复统计）

2. 利用二分查找维护一个递增队列，以高度作为比较条件。

由于LeetCode OJ的最大测试用例规模超过4000，O(n ^ 2)的解法会超时。

class Solution(object):
    def maxEnvelopes(self, envelopes):

        nums = sorted(envelopes, 
                      cmp = lambda x,y: x[0] - y[0] if x[0] != y[0] else y[1] - x[1])
        size = len(nums)
        dp = []
        for x in range(size):
            low, high = 0, len(dp) - 1
            while low <= high:
                mid = (low + high) / 2
                if dp[mid][1] < nums[x][1]:
                    low = mid + 1
                else:
                    high = mid - 1
            if low < len(dp):
                dp[low] = nums[x]
            else:
                dp.append(nums[x])
        return len(dp)


"""