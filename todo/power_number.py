# coding=utf-8

import unittest

"""
power number: greater than 0, can be represented as x^y where x > 1 and y > 1
4 ( 2^2)
8
9
16
25
27
32
36
49
64
81
100
...

Input:
n 


Output:
find the n-th (zero index based) power number

"""


class Solution(object):
    def nth_power_num(self, n):
        import heapq
        if n < 0:
            return -1
        cnt = -1
        heap = [(4, 2, 2)]
        last = -1
        res = -1
        while cnt < n:
            res, i, j = heapq.heappop(heap)
            if res != last:
                cnt += 1
                last = res
            #i, j = pair[0], pair[1]
            heapq.heappush(heap, ((i+1)**j, i+1, j))
            heapq.heappush(heap, (i ** (j+1), i, j+1))
        return res



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        n = 0
        answer = 4
        result = self.sol.nth_power_num(n)
        self.assertEqual(answer, result)

    def test_case2(self):
        n = 11
        answer = 100
        result = self.sol.nth_power_num(n)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



# -*- coding:utf-8 -*-
