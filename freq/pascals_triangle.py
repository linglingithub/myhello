#coding=utf-8
__author__ = 'linglin'

"""
118. Pascal's Triangle

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
Subscribe to see which companies asked this question

Hide Tags Array
Hide Similar Problems (E) Pascal's Triangle II

Easy

"""

import unittest


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        row = [1]
        result = [row]
        row_cnt = 1
        while row_cnt < numRow:
            tmp = [1]
            last = result[-1]
            for i in range(len(last) - 1):
                tmp.append(last[i] + last[i + 1])
            tmp.append(1)
            result.append(tmp)
            row_cnt += 1
        return result



class Solution1(object):

    def generate1(self, numRows): #42ms, 56%
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        result = [[1]]
        if numRows >= 2:
            result = [[1],[1,1]]
        for n in range(3, numRows+1):
            last = result[n-2]
            tmp = [1]
            for i in range(n-2):
                tmp.append(last[i]+last[i+1])
            tmp.append(1)
            result.append(tmp)
        return result


    def generate_ref(self, numRows): #45ms, 46%, cleaner code, different way
        """
        杨辉三角的特点是每一行的第一和最后一个元素是1，其它元素是上一行它左右两个元素之和。以[1,3,3,1]为例，下一行的中间元素就是
        [1+3,3+3,3+1]，也就是[1,3,3]和[3,3,1]对应数字求和。
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        result = [[1]]
        while numRows > 1:
            result.append([1] + [a + b for a, b in zip(result[-1][:-1], result[-1][1:])] + [1])
            numRows -= 1
        return result





class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        numRows = 5
        answer = [
                 [1],
                [1,1],
               [1,2,1],
              [1,3,3,1],
             [1,4,6,4,1]
            ]
        result = self.sol.generate(numRows)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
