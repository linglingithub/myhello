#coding=utf-8
"""

240. Search a 2D Matrix II

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.

Subscribe to see which companies asked this question.

Hide Tags Binary Search Divide and Conquer
Hide Similar Problems (M) Search a 2D Matrix

Medium

"""

import unittest


class Solution(object):
    def searchMatrix(self, matrix, target): #use center point as starting point, get rid of 1/4 every time, 349ms, 13%
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m = len(matrix) - 1
        n = len(matrix[0]) - 1
        return self.search_helper(matrix, 0, 0, m, n, target)

    def search_helper(self, matrix, x0, y0, x1, y1, target):
        if x0 > x1 or y0 > y1:
            return False
        x_mid = (x0+x1) / 2
        y_mid = (y0+y1) / 2
        if matrix[x_mid][y_mid] == target:
            return True
        elif matrix[x_mid][y_mid] > target:
            return self.search_helper(matrix, x0, y0, x_mid-1, y1, target) or self.search_helper(matrix, x_mid, y0, x1, y_mid -1, target)
        else:
            return self.search_helper(matrix, x_mid+1,y0, x1, y1, target) or self.search_helper(matrix, x0, y_mid+1, x_mid, y1, target)

    def searchMatrix1(self, matrix, target): #ref, use upper right corner as starting (mid) point,O(m+n), 162ms, 31%
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        x = len(matrix)-1
        y = 0
        while x >= 0 and y < len(matrix[0]):
            if target == matrix[x][y]:
                return True
            elif target > matrix[x][y]:
                y += 1
            else:
                x -= 1
        return False







class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        matrix = [
          [1,   4,  7, 11, 15],
          [2,   5,  8, 12, 19],
          [3,   6,  9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]
        ]
        target = 5
        answer = True
        result = self.sol.searchMatrix(matrix, target)
        self.assertEqual(answer, result)

    def test_case2(self):
        matrix = [
          [1,   4,  7, 11, 15],
          [2,   5,  8, 12, 19],
          [3,   6,  9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]
        ]
        target = 20
        answer = False
        result = self.sol.searchMatrix(matrix, target)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""
self:
for the O(m+n) way, think it this way:

take starting point at (0, m-1) for example, ie the left bottom corner,
every time move one row or one column, because you can eliminate one row or one column, (actually right part of row and 
upper part of column). current point at (i, j) means that the future searching area is (x<=i, y>=j)

============================================================================================================================================


http://bookshadow.com/weblog/2015/07/23/leetcode-search-2d-matrix-ii/

O(m + n)解法：
从矩阵的右上角(屏幕坐标系）开始，执行两重循环

外循环递增枚举每行，内循环递减枚举列

Python代码：
class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        y = len(matrix[0]) - 1
        for x in range(len(matrix)):
            while y and matrix[x][y] > target:
                y -= 1
            if matrix[x][y] == target:
                return True
        return False

O(m * logn)解法：
循环枚举行，二分查找列

Python代码：
class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        y = len(matrix[0]) - 1
        def binSearch(nums, low, high):
            while low <= high:
                mid = (low + high) / 2
                if nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return high
        for x in range(len(matrix)):
            y = binSearch(matrix[x], 0, y)
            if matrix[x][y] == target:
                return True
        return False

O(n ^ 1.58)解法：
参考：https://leetcode.com/discuss/47528/c-with-o-m-n-complexity

分治法，以矩形中点为基准，将矩阵拆分成左上，左下，右上，右下四个区域

若中点值 < 目标值，则舍弃左上区域，从其余三个区域再行查找

若中点值 > 目标值，则舍弃右下区域，从其余三个区域再行查找

时间复杂度递推式：T(n) = 3T(n/2) + c

相关博文：http://articles.leetcode.com/2010/10/searching-2d-sorted-matrix-part-ii.html

Java代码：
public class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int n=matrix.length, m=matrix[0].length;
        return helper(matrix,0,n-1,0,m-1,target);
    }
    boolean helper(int[][] matrix, int rowStart, int rowEnd, int colStart, int colEnd, int target ){
        if(rowStart>rowEnd||colStart>colEnd){
            return false;
        }
        int rm=(rowStart+rowEnd)/2, cm=(colStart+colEnd)/2;
        if(matrix[rm][cm]== target){
            return true;
        }
        else if(matrix[rm][cm] >target){
            return helper(matrix, rowStart, rm-1,colStart, cm-1,target)||
                helper(matrix,  rm, rowEnd, colStart,cm-1,target) ||
                helper(matrix, rowStart, rm-1,cm, colEnd,target);
        }
        else{
            return helper(matrix, rm+1, rowEnd, cm+1,colEnd,target)||
                helper(matrix,  rm+1, rowEnd, colStart,cm,target) ||
                helper(matrix, rowStart, rm,cm+1, colEnd,target);
        }
    
}


============================================================================================================================================


在行和列排序好的二维数组中查找目标数字。这里我们用了一个很巧妙的方法，从矩阵的右上角开始找，相当于把这个元素当作mid，目标比mid大，则
row + 1，小则col + 1，相等则返回mid。也是类似二分查找的思想。

Time Complexity - O(m + n)， Space Complexity - O(1)


============================================================================================================================================

编写一个高效的算法，从一个m × n矩阵中寻找一个值。矩阵具有如下性质：

每一行的整数从左向右递增
每一列的整数从上往下递增

测试样例见题目描述。

解题思路：
O(m + n)解法：
从矩阵的右上角(屏幕坐标系）开始，执行两重循环

外循环递增枚举每行，内循环递减枚举列

Python代码：
class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        y = len(matrix[0]) - 1
        for x in range(len(matrix)):
            while y and matrix[x][y] > target:
                y -= 1
            if matrix[x][y] == target:
                return True
        return False



O(m * logn)解法：
循环枚举行，二分查找列

Python代码：
class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        y = len(matrix[0]) - 1
        def binSearch(nums, low, high):
            while low <= high:
                mid = (low + high) / 2
                if nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return high
        for x in range(len(matrix)):
            y = binSearch(matrix[x], 0, y)
            if matrix[x][y] == target:
                return True
        return False



O(n ^ 1.58)解法：
参考：https://leetcode.com/discuss/47528/c-with-o-m-n-complexity

分治法，以矩形中点为基准，将矩阵拆分成左上，左下，右上，右下四个区域

若中点值 < 目标值，则舍弃左上区域，从其余三个区域再行查找

若中点值 > 目标值，则舍弃右下区域，从其余三个区域再行查找

时间复杂度递推式：T(n) = 3T(n/2) + c

相关博文：http://articles.leetcode.com/2010/10/searching-2d-sorted-matrix-part-ii.html

Java代码：
public class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int n=matrix.length, m=matrix[0].length;
        return helper(matrix,0,n-1,0,m-1,target);
    }
    boolean helper(int[][] matrix, int rowStart, int rowEnd, int colStart, int colEnd, int target ){
        if(rowStart>rowEnd||colStart>colEnd){
            return false;
        }
        int rm=(rowStart+rowEnd)/2, cm=(colStart+colEnd)/2;
        if(matrix[rm][cm]== target){
            return true;
        }
        else if(matrix[rm][cm] >target){
            return helper(matrix, rowStart, rm-1,colStart, cm-1,target)||
                helper(matrix,  rm, rowEnd, colStart,cm-1,target) ||
                helper(matrix, rowStart, rm-1,cm, colEnd,target);
        }
        else{
            return helper(matrix, rm+1, rowEnd, cm+1,colEnd,target)||
                helper(matrix,  rm+1, rowEnd, colStart,cm,target) ||
                helper(matrix, rowStart, rm,cm+1, colEnd,target);
        }



本文链接：http://bookshadow.com/weblog/2015/07/23/leetcode-search-2d-matrix-ii/

"""

#-*- coding:utf-8 -*-
