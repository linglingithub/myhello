#coding=utf-8

import unittest

"""

Data Stream Median ( -- leetcode : 295. Fine Medium from Data Stream)

Numbers keep coming, return the median of numbers at every time a new number added.

Have you met this question in a real interview? Yes
Clarification
What's the definition of Median?
- Median is the number that in the middle of a sorted array. If there are n numbers in a sorted array A, the median is A[(n - 1) / 2]. For example, if A=[1,2,3], median is 2. If A=[1,19], median is 1.

Example
For numbers coming list: [1, 2, 3, 4, 5], return [1, 1, 2, 2, 3].

For numbers coming list: [4, 5, 1, 3, 2, 6, 0], return [4, 4, 4, 3, 3, 3, 3].

For numbers coming list: [2, 20, 100], return [2, 2, 20].

Challenge
Total run time in O(nlogn).

Tags
LintCode Copyright Heap Priority Queue Google
Related Problems
Hard Sliding Window Median 20 %
Easy Median 23 %
Hard Median of two Sorted Arrays

"""


class Solution:
    """
    @param nums: A list of integers.
    @return: The median of numbers
    """
    def medianII(self, nums):
        # write your code here
        if not nums:
            return []
        import heapq
        result = []
        min_heap = []
        max_heap = []
        odd = False
        for num in nums:
            odd = not odd
            if odd:  # also need to check here
                if min_heap:
                    tmp = min_heap[0]
                    if num > tmp:
                        heapq.heappop(min_heap)
                        heapq.heappush(max_heap, -tmp)
                        heapq.heappush(min_heap, num)
                    else:
                        heapq.heappush(max_heap, -num)
                else:
                    heapq.heappush(max_heap, -num)
            else:
                tmp = - max_heap[0]
                if tmp > num:
                    heapq.heappop(max_heap)
                    heapq.heappush(max_heap, -num)
                    heapq.heappush(min_heap, tmp)
                else:
                    heapq.heappush(min_heap, num)
            result.append(-max_heap[0])
        return result




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1, 2, 3, 4, 5]
        answer = [1, 1, 2, 2, 3]
        result = self.sol.medianII(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [4, 5, 1, 3, 2, 6, 0]
        answer = [4, 4, 4, 3, 3, 3, 3]
        result = self.sol.medianII(nums)
        self.assertEqual(answer, result)

    def test_case3(self):
        nums = [2, 20, 100]
        answer = [2, 2, 20]
        result = self.sol.medianII(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
