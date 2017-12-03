#coding=utf-8

import unittest

"""

313. Super Ugly Number
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

Note:
(1) 1 is a super ugly number for any given primes.
(2) The given numbers in primes are in ascending order.
(3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
(4) The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.

Difficulty:Medium
Total Accepted:41.8K
Total Submissions:110.1K
Contributor: LeetCode
Subscribe to see which companies asked this question.

Related Topics 
Math Heap 
Similar Questions 
Ugly Number II 

==============================

518. Super Ugly Number 

 Description
 Notes
 Testcase
 Judge
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

 Notice

1 is a super ugly number for any given primes.
The given numbers in primes are in ascending order.
0 < k ≤ 100, 0 < n ≤ 10^6, 0 < primes[i] < 1000
Have you met this question in a real interview? Yes
Example
Given n = 6, primes = [2, 7, 13, 19] return 13

Tags 
Mathematics Heap Google
Related Problems 
Easy Ugly Number 35 %
Medium Ugly Number II

"""


import heapq
class Solution:
    """
    @param: n: a positive integer
    @param: primes: the given prime list
    @return: the nth super ugly number
    """

    def nthSuperUglyNumber(self, n, primes):  # good, same as ugly_numberII, leet 94%+
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if n <= 0 or not primes:
            return -1
        res = [1 for _ in range(n)]
        k = len(primes)
        idx_list = [0 for _ in range(k)]
        val_list = [prime for prime in primes]
        for i in range(1, n):
            row_min = min(val_list)
            res[i] = row_min
            for j in range(k):
                if val_list[j] == row_min:
                    idx_list[j] += 1
                    val_list[j] = primes[j] * res[idx_list[j]]
        return res[n - 1]


    def nthSuperUglyNumber_TLE(self, n, primes):  # TLE on leet, AC on lint
        # write your code here
        if not primes or n <= 0:
            return -1
        heap = [1]
        cnt = 0
        #res = -1
        last = -1
        while cnt < n:
            val = heapq.heappop(heap)
            if val != last:
                cnt += 1
                #res = val
                last = val
            for prime in primes:
                heapq.heappush(heap, val*prime )
        #return res
        return last


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [2, 7, 13, 19]
        n = 6
        answer = 13
        result = self.sol.nthSuperUglyNumber(n, nums)
        self.assertEqual(answer, result)

    def test_case2(self):  # TLE on leetcode, local runs 3m8s
        n = 100000
        nums = [7,19,29,37,41,47,53,59,61,79,83,89,101,103,109,127,131,137,139,157,167,179,181,199,211,229,233,239,241,251]
        answer = 1092889481
        result = self.sol.nthSuperUglyNumber(n, nums)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
