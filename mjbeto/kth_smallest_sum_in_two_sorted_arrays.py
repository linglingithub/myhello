#coding=utf-8

import unittest
from util.ini_file_util import IniFileUtil

"""
Kth Smallest Sum In Two Sorted Arrays

Given two integer arrays sorted in ascending order and an integer k. Define sum = a + b, where a is an element from the 
first array and b is an element from the second one. Find the kth smallest sum out of all possible sums.

Have you met this question in a real interview? Yes
Example
Given [1, 7, 11] and [2, 4, 6].

For k = 3, return 7.

For k = 4, return 9.

For k = 8, return 15.

Challenge 
Do it in either of the following time complexity:

O(k log min(n, m, k)). where n is the size of A, and m is the size of B.
O( (m + n) log maxValue). where maxValue is the max number in A and B.
Tags 
Heap Priority Queue Sorted Matrix
Related Problems 
Medium Kth Smallest Number in Sorted Matrix 23 %
Medium Search a 2D Matrix II

Hard

"""


class Solution:
    # @param {int[]} A an integer arrays sorted in ascending order
    # @param {int[]} B an integer arrays sorted in ascending order
    # @param {int} k an integer
    # @return {int} an integer
    def kthSmallestSum(self, A, B, k):
        # Write your code here
        if not A or not B:
            raise ValueError("Empty arrays!!")
        if k >= len(A) * len(B):
            return A[-1]+B[-1]
        import heapq
        i, j = 0, 0
        m, n = len(A), len(B)
        visited = {}
        heap = []
        heapq.heappush(heap, ((A[i]+B[j]), i, j))
        visited[(0,0)] = True
        for cnt in range(k):
            tmp, x, y = heapq.heappop(heap)
            if x+1 < m and not visited.get((x+1,y)):
                heapq.heappush(heap, (A[x+1]+B[y], x+1, y))
                visited[(x+1,y)] = True
            if y+1 < n and not visited.get((x,y+1)):
                heapq.heappush(heap, (A[x]+B[y+1], x, y+1))
                visited[(x,y+1)] = True
        return tmp

    def kthSmallestSum_MLE(self, A, B, k):
        # Write your code here
        if not A or not B:
            raise ValueError("Empty arrays!!")
        if k >= len(A) * len(B):
            return A[-1]+B[-1]
        import heapq
        i, j = 0, 0
        m, n = len(A), len(B)
        visited = [ [False for _ in range(n)] for _ in range(m)]
        heap = []
        heapq.heappush(heap, ((A[i]+B[j]), i, j))
        visited[0][0] = True
        for cnt in range(k):
            tmp, x, y = heapq.heappop(heap)
            if x+1 < m and not visited[x+1][y]:
                heapq.heappush(heap, (A[x+1]+B[y], x+1, y))
                visited[x+1][y] = True
            if y+1 < n and not visited[x][y+1]:
                heapq.heappush(heap, (A[x]+B[y+1], x, y+1))
                visited[x][y+1] = True
        return tmp





class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        a = [1, 7, 11]
        b = [2, 4, 6]
        k = 3
        answer = 7
        result = self.sol.kthSmallestSum(a, b, k)
        self.assertEqual(answer, result)

    def test_case2(self):
        a = [1, 7, 11]
        b = [2, 4, 6]
        k = 4
        answer = 9
        result = self.sol.kthSmallestSum(a, b, k)
        self.assertEqual(answer, result)

    def test_case3(self):
        a = [1, 7, 11]
        b = [2, 4, 6]
        k = 8
        answer = 15
        result = self.sol.kthSmallestSum(a, b, k)
        self.assertEqual(answer, result)

    def test_case4(self): #=====> MLE
        params = IniFileUtil.read_into_dict("kth_smallest_sum_in_two_sorted_arrays.ini")
        A = IniFileUtil.string_to_int_list(params.get("a"))
        B = IniFileUtil.string_to_int_list(params.get("b"))
        k = int(params.get("k"))
        answer = 160080
        result = self.sol.kthSmallestSum(A, B, k)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""

# faster way,  http://www.jiuzhang.com/solutions/kth-smallest-sum-in-two-sorted-arrays/

    def kthSmallestSum(self, A, B, k):
        # Write your code here
        if not A or not B:
            return 0
        import heapq
        m, n = len(A), len(B)
        def vertical_search(k):
            heap = []
            for i in range(min(k, n)):
                heapq.heappush(heap, (A[0] + B[i], 0, i))
            while k > 1:
                min_element = heapq.heappop(heap)
                x, y = min_element[1], min_element[2]
                if x + 1 < m:
                    heapq.heappush(heap, (A[x + 1] + B[y], x + 1, y))
                k -= 1
            return heapq.heappop(heap)[0]
        return vertical_search(k)

"""

#-*- coding:utf-8 -*-
