#coding=utf-8

import unittest


"""
Kth Largest in N Arrays

Find K-th largest element in N arrays.

 Notice

You can swap elements in the array

Have you met this question in a real interview? Yes
Example
In n=2 arrays [[9,3,2,4,7],[1,2,3,4,8]], the 3rd largest element is 7.

In n=2 arrays [[9,3,2,4,8],[1,2,3,4,2]], the 1st largest element is 9, 2nd largest element is 8, 3rd largest element is
7 and etc.

Tags
Heap
Related Problems
Medium Largest Number

"""



class Solution:
    # @param {int[][]} arrays a list of array
    # @param {int} k an integer
    # @return {int} an integer, K-th largest element in N arrays
    def KthInArrays(self, arrays, k):
        # Write your code here
        if not arrays or k < 1:
            return None
        for arr in arrays:
            arr.sort(reverse=True)
        heap = []
        import heapq
        for i in range(len(arrays)):
            if arrays[i]: # need to check, otherwise wrong for case 5
                heapq.heappush(heap, (-arrays[i][0], i, 0))
        cnt = 0
        while cnt < k-1:
            tmp = heapq.heappop(heap)
            result, row, col = -tmp[0], tmp[1], tmp[2]
            if col+1 < len(arrays[row]):
                heapq.heappush(heap, (-arrays[row][col+1], row, col+1))
            cnt += 1
        result = -heapq.heappop(heap)[0]
        return result





class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        arrays = [[9,3,2,4,7],[1,2,3,4,8]]
        k = 3
        answer = 7
        result = self.sol.KthInArrays(arrays, k)
        self.assertEqual(answer, result)

    def test_case2(self):
        arrays = [[9,3,2,4,8],[1,2,3,4,2]]
        k = 1
        answer = 9
        result = self.sol.KthInArrays(arrays, k)
        self.assertEqual(answer, result)

    def test_case3(self):
        arrays = [[9,3,2,4,8],[1,2,3,4,2]]
        k = 2
        answer = 8
        result = self.sol.KthInArrays(arrays, k)
        self.assertEqual(answer, result)

    def test_case4(self):
        arrays = [[9,3,2,4,8],[1,2,3,4,2]]
        k = 3
        answer = 4
        result = self.sol.KthInArrays(arrays, k)
        self.assertEqual(answer, result)

    def test_case5(self):
        arrays = [[],[],[1],[1,2,3,4],[11,10,9,8,7]]
        k = 5
        answer = 7
        result = self.sol.KthInArrays(arrays, k)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
