#coding=utf-8
"""

Find Peak Element II (lint)

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
    def findPeakII(self, A): # O(m+n), 899ms,
        if not A or not A[0]:
            return [-1, -1]
        m, n = len(A), len(A[0])
        return self.search(A, 1, m-2, 1, n-2, True)

    def search(self, A, x1, x2, y1, y2, bisectRow):
        if bisectRow:
            mid = (x1+x2)/2
            idx = 0
            for col in range(y1, y2+1):
                if A[mid][col] > A[mid][col+1] and A[mid][col] > A[mid][col-1]:
                    idx = col
                    break
            if x1 == x2:
                return [x1, idx]
            if A[mid][idx] < A[mid+1][idx]:
                return self.search(A, mid+1, x2, y1, y2, not bisectRow)
            elif A[mid][idx] < A[mid-1][idx]:
                return self.search(A, x1, mid-1, y1, y2, not bisectRow)
            else:
                return [mid, idx]
        else:
            mid = (y1+y2)/2
            idx = 0
            for row in range(x1, x2+1):
                if A[row][mid] > A[row+1][mid] and A[row][mid] > A[row-1][mid]:
                    idx = row
                    break
            if y1 == y2:
                return [idx, y1]
            if A[idx][mid] < A[idx][mid+1]:
                return self.search(A, x1, x2, mid+1, y2, not bisectRow)
            elif A[idx][mid] < A[idx][mid-1]:
                return self.search(A, x1, x2, y1, mid-1, not bisectRow)
            else:
                return[idx, mid]



    def findPeakII1(self, A): #nlogm, 1403ms, 1116ms
        # write your code here
        if not A or not A[0]:
            return [-1,-1]
        m, n = len(A), len(A[0])
        start, end = 1, m-2
        while start < end:
            mid = (start+end)/2
            col = self.find_one(A, mid)
            if self.is_peak(A, mid, col):
                return [mid, col]
            elif A[mid][col] < A[mid-1][col]:
                end = mid-1
            else:
                start = mid + 1

        return [start, self.find_one(A,start)]  #can't return [start, col], see case4

    def find_one(self, A, row):
        for j in range(1, len(A[row])-1):
            if A[row][j] > A[row][j-1] and A[row][j] > A[row][j+1]:
                return j
        return -1

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

    def test_case3(self):
        matrix =[
            [0,0,0,0,0],
            [0,0,1,2,0],
            [0,2,3,8,0],
            [0,4,5,7,0],
            [0,0,0,0,0]
        ]
        result = self.sol.findPeakII(matrix)
        answer = [(2,3)]
        self.assertEqual(True, tuple(result) in answer)

    def test_case4(self):
        matrix =[
            [1,5,3],
            [4,10,9],
            [2,8,7]
        ]
        result = self.sol.findPeakII(matrix)
        answer = [(1,1)]
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

第一种方法还是nlog(m)或者说mlog(n)的时间复杂度吧。因为还是只对于行使用了二分搜索。如果先对列，再对行进行二分搜索交替进行。
才能达到O(m + n)的复杂度

=========================================================================================================

# jiuzhang answer,  8907ms, 7114ms, 5180ms,O(m+n)

class Solution {
    /**
     * @param A: An integer matrix
     * @return: The index of the peak
     */
    public List<Integer> find(int x1, int x2, int y1, int y2,
                              int[][] A, boolean flag) {

        if (flag) {
            int mid = x1 + (x2 - x1) / 2;
            int index = y1;
            for (int i = y1; i <= y2; ++i)
                if (A[mid][i] > A[mid][index])
                    index = i;

            if (A[mid - 1][index] > A[mid][index])
                return find(x1, mid - 1, y1, y2, A, !flag);
            else if (A[mid + 1][index] > A[mid][index])
                return find(mid + 1, x2, y1, y2, A, !flag);
            else
                return new ArrayList<Integer>(Arrays.asList(mid, index));
        } else {
            int mid = y1 + (y2 - y1) / 2;
            int index = x1;
            for (int i = x1; i <= x2; ++i)
                if (A[i][mid] > A[index][mid])
                    index = i;

            if (A[index][mid - 1] > A[index][mid])
                return find(x1, x2, y1, mid - 1, A, !flag);
            else if (A[index][mid + 1] > A[index][mid])
                return find(x1, x2, mid + 1, y2, A, !flag);
            else
                return new ArrayList<Integer>(Arrays.asList(index, mid));
        }
    }
    public List<Integer> findPeakII(int[][] A) {
        // write your code here
        int n = A.length;
        int m = A[0].length;
        return find(1, n - 2, 1, m - 2, A, true);
    }
}


=========================================================================================================

# jiuzhang answer,  5126ms, 5007ms, 8642ms, O(m*logn), onetime tle, 7944ms?? still faster than O(m+n) one

class Solution {
    /**
     * @param A: An integer matrix
     * @return: The index of the peak
     */


    public List<Integer> findPeakII(int[][] A) {
        // this is the nlog(n) method
        int low = 1, high = A.length-2;
        List<Integer> ans = new ArrayList<Integer>();
        while(low <= high) {
            int mid = (low + high) / 2;
            int col = find(mid, A);
            if(A[mid][col] < A[mid - 1][col]) {
                high = mid - 1;
            } else if(A[mid][col] < A[mid + 1][col]) {
                low = mid + 1;
            } else {
                ans.add(mid);
                ans.add(col);
                break;
            }
        }
        return ans;
    }
    int find(int row, int [][]A) {
        int col = 0;
        for(int i = 0; i < A[row].length; i++) {
            if(A[row][i] > A[row][col]) {
                col = i;
            }
        }
        return col;
    }
}





=========================================================================================================

# a very different way, 5341ms, but actually can lead to dead-end answer. Check the following case.

surounding elements can be other numbers less than insiders and with a different value. Here just put as all zero.
which will not affect the result.

A = [
[0,0,0,0,0],
[0,0,1,2,0],
[0,2,3,8,0],
[0,4,5,7,0],
[0,0,0,0,0]
]

answer = [2,3]

class Solution {
    /**
     * @param A: An integer matrix
     * @return: The index of the peak
     */

    public List<Integer> findPeakII(int[][] A) {
        List<Integer> res = new ArrayList<Integer>();
        if (A == null || A.length == 0 || A[0].length == 0) {
            return res;
        }
        int i = 1, j = 1;
        while (true) {
            if (isValid(A, i, j)) {
                res.add(i);
                res.add(j);
                return res;
            }
            if (A[i+1][j] > A[i][j+1]) {
                i++;
            } else {
                j++;
            }
        }
    }
    private boolean isValid(int[][] a, int i, int j) {
        if (i > 0 && i < a.length - 1 && j > 0 && j < a[0].length - 1
            && a[i-1][j] < a[i][j] && a[i+1][j] < a[i][j] && a[i][j+1] < a[i][j] && a[i][j+1] < a[i][j]) {
            return true;
        }
        return false;
    }
}

"""