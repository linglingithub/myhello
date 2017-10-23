"""

48. Rotate Image

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?

Subscribe to see which companies asked this question

Hide Tags Array


"""

import unittest


class Solution(object):
    def rotate(self, matrix): #42ms, 91.18%
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        tt = [list(i)[::-1] for i in zip(*matrix)]
        matrix[:] = tt  # matrix = tt could not change matrix when out of the method


    def rotate_ref(self, matrix): # 52ms, 75%
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        input = [[1,2,3],[4,5,6]]
        answer = [[4,1],[5,2],[6,3]]
        self.sol.rotate(input)
        self.assertEqual(answer, input)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""
/*
 * clockwise rotate
 * first reverse up to down, then swap the symmetry 
 * 1 2 3     7 8 9     7 4 1
 * 4 5 6  => 4 5 6  => 8 5 2
 * 7 8 9     1 2 3     9 6 3
*/
void rotate(vector<vector<int> > &matrix) {
    reverse(matrix.begin(), matrix.end());
    for (int i = 0; i < matrix.size(); ++i) {
        for (int j = i + 1; j < matrix[i].size(); ++j)
            swap(matrix[i][j], matrix[j][i]);
    }
}

/*
 * anticlockwise rotate
 * first reverse left to right, then swap the symmetry
 * 1 2 3     3 2 1     3 6 9
 * 4 5 6  => 6 5 4  => 2 5 8
 * 7 8 9     9 8 7     1 4 7
*/
void anti_rotate(vector<vector<int> > &matrix) {
    for (auto vi : matrix) reverse(vi.begin(), vi.end());
    for (int i = 0; i < matrix.size(); ++i) {
        for (int j = i + 1; j < matrix[i].size(); ++j)
            swap(matrix[i][j], matrix[j][i]);
    }
}

======================================================================


You can use zip with * to get transpose of a matrix:

>>> A = [[ 1, 2, 3],[ 4, 5, 6]]
>>> zip(*A)
[(1, 4), (2, 5), (3, 6)]
>>> lis  = [[1,2,3],
... [4,5,6],
... [7,8,9]]
>>> zip(*lis)
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
If you want the returned list to be a list of lists:

>>> [list(x) for x in zip(*lis)]
[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
#or
>>> map(list, zip(*lis))
[[1, 4, 7], [2, 5, 8], [3, 6, 9]]

"""


#-*- coding:utf-8 -*-
#coding=utf-8