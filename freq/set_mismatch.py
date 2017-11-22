#coding=utf-8

import unittest

"""

645. Set Mismatch
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the 
set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number 
occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
Note:
The given array size will in the range [2, 10000].
The given array's numbers won't have any order.
"""


class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        val_cnt = Counter(nums)
        res1 = 0
        res2 = 0
        for val, cnt in val_cnt.items():
            if cnt == 2:
                res1 = val
                break
        n = len(nums)
        res2 = (1+n)*n/2 + res1 - sum(nums)
        return [res1, res2]


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,2,2,4]
        answer = [2, 3]
        result = self.sol.findErrorNums(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""

Count each element. We know the original elements must have been 1, 2, ..., len(A).
Once we have the counts, it is easy to scan through and see which element must have occurred twice, and which one never occurred.

In our implementation, we could also use collections.Counter(A).

def findErrorNums(self, A):
    N = len(A)
    count = [0] * (N+1)
    for x in A:
      count[x] += 1
    for x in xrange(1, len(A)+1):
        if count[x] == 2:
            twice = x
        if count[x] == 0:
            never = x
    return twice, never
Bonus solution: Say (x, y) is the desired answer. We know sum(A) - x + y = sum([1, 2, ..., N]), and 
sum(x*x for x in A) - x*x + y*y = sum([1*1, 2*2, ..., N*N]). So we know x-y and x*x-y*y. Dividing the latter by x-y, we 
know x+y. Hence, we know x and y.

def findErrorNums(self, A):
    N = len(A)
    alpha = sum(A) - N*(N+1)/2
    beta = (sum(x*x for x in A) - N*(N+1)*(2*N+1)/6) / alpha
    return (alpha + beta) / 2, (beta - alpha) / 2

"""