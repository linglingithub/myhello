#coding=utf-8

import unittest

"""
264. Ugly Number II
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 
is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number, and n does not exceed 1690.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


Difficulty:Medium
Total Accepted:60.7K
Total Submissions:186.4K
Contributor: LeetCode
Subscribe to see which companies asked this question.

Related Topics 
Dynamic Programming Heap Math 
Similar Questions 
Merge k Sorted Lists Count Primes Ugly Number Perfect Squares Super Ugly Number 

"""

class Solution(object):
    def nthUglyNumber(self, n):  # ref idea, 90+%
        """
        1, 2，3，4, 5，6，8，9，10，
        :type n: int
        :rtype: int
        """
        res = [1 for _ in range(n)]
        cnt = 1
        idx2, idx3, idx5 = 0, 0, 0
        while cnt < n:
            cnt += 1
            a, b, c = res[idx2]*2, res[idx3]*3, res[idx5]*5
            next_min = min(a, b, c)
            res[cnt-1] = next_min
            if next_min == a:
                idx2 += 1
            if next_min == b:   # can't use elif here, see case2, when idx2 = 2 (3*2=6), idx3 = 1 (2*3=6), both idx2 and idx3 need to be updated
                idx3 += 1
            if next_min == c: #else:
                idx5 += 1
        #print "====:", res
        return res[n-1]


    def nthUglyNumber1(self, n): # slower, 3+%
        """
        1, 2，3，4, 5，6，8，9，10，12,15,16,18,20.....
        :type n: int
        :rtype: int
        """
        import heapq
        cnt = 0
        res = 1
        seeds = []
        heapq.heappush(seeds, 1)
        while cnt < n:   # pay attention, not <= here, otherwise res may be None and cause error
            res = heapq.heappop(seeds)
            cnt += 1
            for multiplier in 2,3,5:
                tmp = res * multiplier
                if tmp not in seeds:   # need to check here, otherwise wrong, there may be repeated values in seeds
                    heapq.heappush(seeds, tmp)
        return res


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = 1
        answer = 1
        result = self.sol.nthUglyNumber(nums)
        self.assertEqual(answer, result)


    def test_case2(self):
        nums = 7
        answer = 8
        result = self.sol.nthUglyNumber(nums)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""
Hint:

The naive approach is to call isUgly for every number until you reach the nth one. Most numbers are not ugly. Try to 
focus your effort on generating only the ugly ones.
An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.
The key is how to maintain the order of the ugly numbers. Try a similar approach of merging from three sorted lists: 
L1, L2, and L3.
Assume you have Uk, the kth ugly number. Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5).
 

这道题是之前那道Ugly Number 丑陋数的延伸，这里让我们找到第n个丑陋数，还好题目中给了很多提示，基本上相当于告诉我们解法了，根据提示中的信息，
我们知道丑陋数序列可以拆分为下面3个子列表：

(1) 1×2, 2×2, 3×2, 4×2, 5×2, …
(2) 1×3, 2×3, 3×3, 4×3, 5×3, …
(3) 1×5, 2×5, 3×5, 4×5, 5×5, …

仔细观察上述三个列表，我们可以发现每个子列表都是一个丑陋数分别乘以2,3,5，而要求的丑陋数就是从已经生成的序列中取出来的，我们每次都从三个列表
中取出当前最小的那个加入序列，请参见代码如下：

"""

#-*- coding:utf-8 -*-
