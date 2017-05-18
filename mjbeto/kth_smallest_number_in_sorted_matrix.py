#coding=utf-8

import unittest

"""
Kth Smallest Number in Sorted Matrix


Find the kth smallest number in at row and column sorted matrix.

Have you met this question in a real interview? Yes
Example
Given k = 4 and a matrix:

[
  [1 ,5 ,7],
  [3 ,7 ,8],
  [4 ,8 ,9],
]
return 5

Challenge 
Solve it in O(k log n) time where n is the bigger one between row size and column size.

Tags 
Heap Priority Queue Matrix
Related Problems 
Hard Kth Smallest Sum In Two Sorted Arrays 26 %
Medium Kth Largest Element


"""


class Solution:
    # @param matrix: a matrix of integers
    # @param k: an integer
    # @return: the kth smallest number in the matrix
    def kthSmallest(self, matrix, k):
        # write your code here
        if not matrix or not matrix[0]:
            raise ValueError
        if k <1:
            return matrix[0][0]
        m, n = len(matrix), len(matrix[0])
        if k > m * n:
            return matrix[m-1][n-1]
        import heapq
        heap = []
        cnt = 0
        if m >= n:
            for i in range(m):
                heapq.heappush(heap, (matrix[i][0], i, 0))
            while cnt < k:
                val, row, col = heapq.heappop(heap)
                if col+1 < n:
                    heapq.heappush(heap, (matrix[row][col+1], row, col+1))
                cnt += 1
            return val
        else:
            for j in range(n):
                heapq.heappush(heap, (matrix[0][j], 0, j))
            while cnt < k:
                val, row, col = heapq.heappop(heap)
                if row+1 < m:
                    heapq.heappush(heap, (matrix[row+1][col], row+1, col))
                cnt += 1
            return val


    def kthSmallest_TLE(self, matrix, k): #91% cases passed
        # write your code here
        if not matrix or not matrix[0]:
            raise ValueError
        if k < 1:
            return matrix[0][0]
        m, n = len(matrix), len(matrix[0])
        if k > m * n:
            return matrix[m - 1][n - 1]
        import heapq
        heap = []
        cnt = 0
        if not m >= n:  # transpose the matrix takes too long (m*n)
            matrix = zip(*matrix)
            m, n = len(matrix), len(matrix[0])

        for i in range(m):
            heapq.heappush(heap, (matrix[i][0], i, 0))
        while cnt < k:
            val, row, col = heapq.heappop(heap)
            if col + 1 < n:
                heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))
            cnt += 1
        return val



    def kthSmallest_wrong(self, matrix, k):
        # write your code here
        if not matrix or not matrix[0]:
            raise ValueError
        if k < 1:
            return matrix[0][0]
        m, n = len(matrix), len(matrix[0])
        if k > m * n:
            return matrix[m - 1][n - 1]
        i, j, cnt = 0, 0, 1
        # while cnt <= k:
        for cnt in range(2, k + 1):
            if i == m - 1:
                j += 1
                continue
            if j == n - 1:
                i += 1
                continue
            if matrix[i][j + 1] < matrix[i + 1][j]:  # i or j is changed, can't use compare this way, not a downward or rightward move
                j += 1
            else:
                i += 1

        return matrix[i][j]


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [
          [1 ,5 ,7],
          [3 ,7 ,8],
          [4 ,8 ,9],
        ]
        k = 4
        answer = 5
        result = self.sol.kthSmallest(nums, k)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""

// Version 1 using heapq

import heapq

class Solution:
  
    def kthSmallest(self, matrix, k):
        # Write your code here
        m, n = len(matrix), len(matrix[0])
        visited = [[False] * n for _ in range(m)]
        queue = [(matrix[0][0], 0, 0)]
        result = None
        visited[0][0] = True
        for _ in range(k):
            result, i, j = heapq.heappop(queue)
            if i + 1 < m and not visited[i + 1][j]:
                visited[i + 1][j] = True
                heapq.heappush(queue, (matrix[i + 1][j], i + 1, j))
            if j + 1 < n and not visited[i][j + 1]:
                visited[i][j + 1] = True
                heapq.heappush(queue, (matrix[i][j + 1], i, j + 1))
        return result



// Version 2 
class Solution:
    # @param matrix: a matrix of integers
    # @param k: an integer
    # @return: the kth smallest number in the matrix
    def kthSmallest(self, matrix, k):
        # write your code here
        ind = 0
        val = 0
        index = []
        nums = [] 
        top = [] 
        last = []
        m = len(matrix)
        n = len(matrix[0])
        for i in xrange(m): self.heapAdd(nums, index, matrix[i][0], i)
        for i in xrange(m): last.append(0)
        while len(top)<k:
            val = nums[0]
            ind = index[0]
            self.heapDel(nums, index)
            if last[ind]!=n-1:
                last[ind] += 1
                self.heapAdd(nums, index, matrix[ind][last[ind]], ind)
            top.append(val)
        return top[len(top)-1]

    def heapAdd(self, nums, index, val, ind):
        nums.append(val)
        index.append(ind)
        n = len(nums)-1
        while n>0 and nums[n]<nums[(n-1)/2]:
            nums[n], nums[(n-1)/2] = nums[(n-1)/2], nums[n]
            index[n], index[(n-1)/2] = index[(n-1)/2], index[n]
            n = (n-1)/2

    def heapDel(self, nums, index):
        n = len(nums)-1
        if n>=0: nums[0] = nums[n]
        if n>=0: index[0] = index[n]
        if len(nums)>0: nums.pop()
        if len(index)>0: index.pop()
        n = 0
        while n*2+1<len(nums):
            t = n*2+1
            if t+1<len(nums) and nums[t+1]<nums[t]: t += 1
            if nums[n]<=nums[t]: break
            nums[n], nums[t] = nums[t], nums[n]
            index[n], index[t] = index[t], index[n]
            n = t



"""