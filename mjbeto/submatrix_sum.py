#coding=utf-8

import unittest

"""

Submatrix Sum

Given an integer matrix, find a submatrix where the sum of numbers is zero. Your code should return the coordinate of 
the left-up and right-down number.

Have you met this question in a real interview? Yes
Example
Given matrix

[
  [1 ,5 ,7],
  [3 ,7 ,-8],
  [4 ,-8 ,9],
]
return [(1,1), (2,2)]

Challenge 
O(n3) time.

Tags 
Enumeration Matrix
Related Problems 
Medium Subarray Sum Closest 20 %
Easy Subarray Sum

"""


class Solution:
    # @param {int[][]} matrix an integer matrix
    # @return {int[][]} the coordinate of the left-up and right-down number
    def submatrixSum(self, matrix):  #ref

        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        if m == 1 and n==1:
            return [(0,0),(0,0)] if matrix[0][0] == 0 else []

        msum = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                msum[i][j] = matrix[i-1][j-1] + msum[i - 1][j] + msum[i][j - 1] - msum[i - 1][j - 1]
                if msum[i][j] == 0:
                    return [(0, 0), (i-1, j-1)]


        for r1 in range(0, m):
            for r2 in range(r1+1, m+1):
                submap = {}
                for col in range(n+1):
                    tmp = msum[r2][col] - msum[r1][col]
                    if tmp in submap:
                        col1 = submap.get(tmp)
                        #return [(r1, col1), (r2, col)] wrong, top-left corner is excluded
                        return [(r1, col1), (r2-1, col-1)]
                    else:
                        submap[tmp] = col
        return []


    def submatrixSum_AC_notBest(self, matrix):
        # Write your code here

        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        if m == 1 and n==1:
            return [(0,0),(0,0)] if matrix[0][0] == 0 else []

        msum = [[matrix[i][j] for j in range(n)] for i in range(m)]


        # init the msum
        for i in range(1, m):
            msum[i][0] += msum[i - 1][0]
            if msum[i][0] == 0:
                return [(0, 0), (i, 0)]

        for j in range(1, n):
            msum[0][j] += msum[0][j - 1]
            if msum[0][j] == 0:
                return [(0, 0), (0, j)]

        for i in range(1, m):
            for j in range(1, n):
                msum[i][j] = matrix[i][j] + msum[i - 1][j] + msum[i][j - 1] - msum[i - 1][j - 1]
                if msum[i][j] == 0:
                    return [(0, 0), (i, j)]

        # search over msum
        for r1 in range(0, m):
            singlerow = {} # should be here, not inside col loop, otherwise wrong
            for col in range(n):  # should deal with single row specially
                if msum[r1][col] in singlerow:
                    return [(r1, singlerow.get(msum[r1][col])+1), (r1, col)]
                else:
                    singlerow[msum[r1][col]] = col  # not 1 here

            for r2 in range(r1+1, m):  # note that single row and multiple row matrix has different logic!!!
                subm = {}
                for col in range(n):
                    tmp = msum[r2][col] - msum[r1][col]
                    if tmp in subm:
                        col1 = subm.get(tmp)
                        #return [(r1, col1), (r2, col)] wrong, top-left corner is excluded
                        return [(r1+1, col1+1), (r2, col)]
                    else:
                        subm[tmp] = col
        for col in range(0, n):
            colsub = {}
            for r1 in range(0, m):
                tmp = msum[r1][col]
                if tmp in colsub:
                    return [(colsub[tmp]+1, col),(r1, col)]
                else:
                    colsub[tmp] = r1

        return []


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case4(self): # =====> don't forget this corner case
        nums = [[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[-10],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]]
        answer = [(1,0), (11,0)]
        result = self.sol.submatrixSum(nums)
        self.assertEqual(answer, result)


    def test_case3(self): # =====> don't forget this corner case
        nums = [[1,1,1,1,1,1,1,1,1,1,1,-10,1,1,1,1,1,1,1,1,1,1,1]]
        answer = [(0,1), (0,11)]
        result = self.sol.submatrixSum(nums)
        self.assertEqual(answer, result)

    def test_case2(self): # =====> don't forget this corner case
        nums = [
          [0]
        ]
        answer = [(0,0), (0,0)]
        result = self.sol.submatrixSum(nums)
        self.assertEqual(answer, result)


    def test_case1(self):
        nums = [
          [1 ,5 ,7],
          [3 ,7 ,-8],
          [4 ,-8 ,9],
        ]
        answer = [(1,1), (2,2)]
        result = self.sol.submatrixSum(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""


这道题和求数组中哪些元素和为0的解决方法一样，只是数组中求的是前i个元素和前j个元素和相等，则i－j元素和为0，而这里只是变成2维的而已。
sum[i][j]表示matrix[0][0]到matrix[i-1][j-1]所有元素的和。
建立sum矩阵，为n＋1行，m＋1列。将第0行和第0列都初始化为0。
遍历matrix，根据公式 sum[i][j] = matrix[i - 1][j - 1] + sum[i][j - 1] + sum[i - 1][j] -sum[i - 1][j - 1] 计算所有sum。
然后取两个row：l1, l2。用一个线k从左到右扫过l1和l2，每次都用diff=sum[l1][k]-sum[l2][k]来表示l1-l2和0-k这个矩形元素的sum。如果在同
一个l1和l2中，有两条线（k1，k2）的diff相等，则表示l1-l2和k1-k2这个矩形中的元素和为0。


public class Solution {
    /**
     * @param matrix an integer matrix
     * @return the coordinate of the left-up and right-down number
     */
    public int[][] submatrixSum(int[][] matrix) {
        // Write your code here
        int[][] res = new int[2][2];
        if(matrix == null || matrix.length == 0 || matrix[0].length == 0){
            return res;
        }

        int m = matrix.length;
        int n = matrix[0].length;
        int[][] sum = new int[m + 1][n + 1];

        for(int i = 0; i < m; i++){
            sum[i][0] = 0;
        }

        for(int j = 0; j < n; j++){
            sum[0][j] = 0;
        }

        for(int i = 1; i <= m; i++){
            for(int j = 1; j <= n; j++){
                sum[i][j] = matrix[i - 1][j - 1] + sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1];
            }
        }

        for(int l = 0; l < m; l++){
            for(int h = l + 1; h <= m; h++){
                HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
                for(int k = 0; k <= n; k++){
                    int diff = sum[h][k] - sum[l][k];
                    if(map.containsKey(diff)){
                    ////在matrix中和sum对应的点的index都要－1，在matrix中，左上角的点应该是循环中的点的右下方的点：l+1-1,map.get(diff)+1-1（即不包含循环中的左上角的点），而右下角的点是包含循环中右下角的点：h-1,k-1
                        res[0][0] = l;
                        res[0][1] = map.get(diff);
                        res[1][0] = h - 1;
                        res[1][1] = k - 1;
                        return res;
                    }else{
                        map.put(diff, k);
                    }
                }
            }
        }

        return res;
    }
}


=========================================================================================================================

jiujiang answer:

    def submatrixSum(self, matrix): # not the best way, not n^3, the good point is use m+1, n+1 matrix
        # Write your code here
        lenM = len(matrix)
        lenN = len(matrix[0])

        # for i in xrange()

        if lenM == lenN == 1 and matrix[0][0] == 0: return [[0, 0], [0, 0]]
        f = [[0 for x in xrange(lenN+1)] for y in xrange(lenM+1)]

        for i in xrange(1, lenM+1):
            for j in xrange(1, lenN+1):
                f[i][j] = f[i-1][j] + f[i][j-1] - f[i-1][j-1] + matrix[i-1][j-1]
                for m in xrange(i):
                    for n in xrange(j):
                        if f[i][j] == f[i][n] - f[m][n] + f[m][j]:
                            return [[m, n], [i-1, j-1]]



"""