#coding=utf-8
"""

Find Peak Element II

There is an integer matrix which has the following features:

The numbers in adjacent positions are different.
The matrix has n rows and m columns.
For all i < m, A[0][i] < A[1][i] && A[n - 2][i] > A[n - 1][i].
For all j < n, A[j][0] < A[j][1] && A[j][m - 2] > A[j][m - 1].
We define a position P is a peek if:

A[j][i] > A[j+1][i] && A[j][i] > A[j-1][i] && A[j][i] > A[j][i+1] && A[j][i] > A[j][i-1]
Find a peak element in this matrix. Return the index of the peak.

 Notice

The matrix may contains multiple peeks, find any of them.

Have you met this question in a real interview? Yes
Example
Given a matrix:

[
  [1 ,2 ,3 ,6 ,5],
  [16,41,23,22,6],
  [15,17,24,21,7],
  [14,18,19,20,10],
  [13,14,11,10,9]
]
return index of 41 (which is [1,1]) or index of 24 (which is [2,2])

Challenge
Solve it in O(n+m) time.

If you come up with an algorithm that you thought it is O(n log m) or O(m log n), can you prove it is actually O(n+m) or
propose a similar but O(n+m) algorithm?

Tags
Binary Search LintCode Copyright Matrix
Related Problems
Medium Find Peak Element


================================================================================================================

Find Peak Element

There is an integer array which has the following features:

The numbers in adjacent positions are different.
A[0] < A[1] && A[A.length - 2] > A[A.length - 1].
We define a position P is a peek if:

A[P] > A[P-1] && A[P] > A[P+1]
Find a peak element in this array. Return the index of the peak.

"""

import unittest

class Solution:
    #@param A: An list of list integer
    #@return: The index of position is a list of integer, for example [2,2]
    def findPeakII(self, A):
        # write your code here
        if not A or not A[0]:
            return [-1,-1]
        self.find(A, 1, len(A)-2, 1, len(A[0])-2, 0)

    def find(self, matrix, x1, x2, y1, y2):
        m = x2-x1+1
        n = y2-y1+1
        if m <= 1 and n <= 1:
            return [x1, y1]
        midx = (x1+x2)/2
        midy = (y1+y2)/2
        if self.is_peak(matrix, midx, midy):
            return [midx, midy]
        if matrix[midx-1][midy] > matrix[midx][midy]:
            x2 = midx-1

            if matrix[midx][midy] > matrix[midx-1][midy]:
                self.find(matrix,)


        else:

    def is_peak(self, matrix, x, y):
        if matrix[x][y] > matrix[x-1][y] and matrix[x][y] > matrix[x+1][y] \
            and matrix[x][y] > matrix[x][y-1] and matrix[x][y] > matrix[x][y+1]:
                return True
        else:
            return False








class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        matrix = [
          [1 ,2 ,3 ,6 ,5],
          [16,41,23,22,6],
          [15,17,24,21,7],
          [14,18,19,20,10],
          [13,14,11,10,9]
        ]
        result = self.sol.findPeakII(matrix)
        answer = [(1,1), (2,2)]
        self.assertEqual(True, tuple(result) in answer)

    def test_case2(self):
        matrix =[
            [1, 2, 3, 6, 5],
            [6, 21, 22, 25, 8],
            [7, 22, 23, 24, 9],
            [10, 11, 12, 15, 14]
        ]
        result = self.sol.findPeakII(matrix)
        answer = [(1,3)]
        self.assertEqual(True, tuple(result) in answer)





if __name__ == '__main__':
    # arr = [1,2,3,1]
    # arr = [1,2,3,4]
    # arr = [1,2]
    arr = [3, 1]
    sol = Solution()
    # print sol.findPeakElement(arr)
    # print "LLLLLLLLLLL ========="
    # unittest.main()

    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

    # solTestSuite = unittest.TestSuite()
    # solTestSuite.addTest(SolutionTest('test_case1'))
    # solTestSuite.addTest(SolutionTest('test_case2'))
    # unittest.TextTestRunner(verbosity=2).run(solTestSuite)

"""

先横着二分，然后在竖着二分，这样交替二分就是O(n)时间复杂度。

第一种方法还是nlog(m)或者说mlog(n)的时间复杂度吧。因为还是只对于行使用了二分搜索。如果先对列，再对行进行二分搜索交替进行。才能达到O(m + n)的复杂度

"""