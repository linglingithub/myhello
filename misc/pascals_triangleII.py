#coding=utf-8
__author__ = 'linglin'

"""
119. Pascal's Triangle II

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?

Subscribe to see which companies asked this question

Hide Tags Array
Hide Similar Problems (E) Pascal's Triangle


Easy

"""

import unittest


class Solution(object):
    def getRow(self, rowIndex): #38ms, 81%
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return []
        row = [1]
        if rowIndex>=1:
            row = [1,1]

        num = rowIndex+1
        while len(row) < num:
            tmp = [1]
            for j in range(len(row)-1):
                tmp.append(row[j]+row[j+1])
            tmp.append(1)
            row = tmp
        return row


    def getRow1(self, rowIndex): #42ms, 52%
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return []
        row = [1]
        if rowIndex>=1:
            row = [1,1]

        for i in range(2, rowIndex+2):
            tmp = [1]
            for j in range(i-2):
                tmp.append(row[j]+row[j+1])
            tmp.append(1)
            row = tmp
        return row


    def getRow_ref(self, rowIndex):#13%, code simple, not easy to understand
        """
        不同于上一题，这里我们仅仅需要得到的第k层的集合，但只能使用O(k)的空间。所以不能用前面二维数组的方式，只能使用一位数组滚动计算。

        在第一题里面，我们知道，帕斯卡三角的计算公式是这样的，A[k][n] = A[k-1][n-1] + A[k-1][n]。

        假设现在数组存放的第3层的数据，[1, 3, 3, 1]，如果我们需要计算第4层的数据，如果我们从前往后计算，譬如A[4][2]= A[3][1] + A[3][2]，
        也就是4，但是因为只有一个数组，所以需要将4这个值覆盖到2这个位置，那么我们计算A[4][3]的时候就会出现问题了，因为这时候A[3][2]不是3，而是4了。

        为了解决这个问题，我们只能从后往前计算，仍然是上面那个例子，我们实现计算A[4][3] = A[3][2] + A[3][3]，也就是6，我们将6直接覆盖到3这个位置，
        但不会影响我们计算A[4][2]，因为A[4][2] = A[3][1] + A[3][2]，已经不会涉及到3这个位置了。

        理解了如何计算，代码就很简单了：

        :type rowIndex: int
        :rtype: List[int]
        """

        result = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(1, i):
                result[i - j] += result[i - j - 1]
        return result

class SolutionTester(unittest.TestCase):
    """
                [
                 [1],
                [1,1],
               [1,2,1],
              [1,3,3,1],
             [1,4,6,4,1]
            ]
    """



    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        numRows = 2
        answer = [1,2,1]
        result = self.sol.getRow(numRows)
        self.assertEqual(answer, result)

    def test_case2(self):
        numRows = 3
        answer = [1,3,3,1]
        result = self.sol.getRow(numRows)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
