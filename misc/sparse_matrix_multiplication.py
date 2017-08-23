#coding=utf-8

import unittest

"""

locked


311. Sparse Matrix Multiplication

Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]


     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
 
 
 
"""



class Solution(object):
    def multiply(self, A, B):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = 1
        answer = 1
        result = self.sol.searchInsert(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""

http://www.cnblogs.com/grandyang/p/5282959.html


这道题让我们实现稀疏矩阵相乘，稀疏矩阵的特点是矩阵中绝大多数的元素为0，而相乘的结果是还应该是稀疏矩阵，即还是大多数元素为0，那么我们使用传
统的矩阵相乘的算法肯定会处理大量的0乘0的无用功，所以我们需要适当的优化算法，使其可以顺利通过OJ，我们知道一个 i x k 的矩阵A乘以一个 k x j 
的矩阵B会得到一个 i x j 大小的矩阵C，那么我们来看结果矩阵中的某个元素C[i][j]是怎么来的，
起始是A[i][0]*B[0][j] + A[i][1]*B[1][j] + ... + A[i][k]*B[k][j]，那么为了不重复计算0乘0，我们首先遍历A数组，要确保A[i][k]不为0，
才继续计算，然后我们遍历B矩阵的第k行，如果B[K][J]不为0，我们累加结果矩阵res[i][j] += A[i][k] * B[k][j]; 这样我们就能高效的算出稀疏矩
阵的乘法，参见代码如下：

 

解法一：

复制代码
class Solution {
public:
    vector<vector<int>> multiply(vector<vector<int>>& A, vector<vector<int>>& B) {
        vector<vector<int>> res(A.size(), vector<int>(B[0].size()));
        for (int i = 0; i < A.size(); ++i) {
            for (int k = 0; k < A[0].size(); ++k) {
                if (A[i][k] != 0) {
                    for (int j = 0; j < B[0].size(); ++j) {
                        if (B[k][j] != 0) res[i][j] += A[i][k] * B[k][j];
                    }
                }
            }
        }
        return res;
    }
};


再来看另一种方法，这种方法其实核心思想跟上面那种方法相同，稍有不同的是我们用一个二维矩阵矩阵来记录每一行中，各个位置中不为0的列数和其对应的
值，然后我们遍历这个二维矩阵，取出每行中不为零的列数和值，然后遍历B中对应行进行累加相乘，参见代码如下：

 

解法二：

复制代码
class Solution {
public:
    vector<vector<int>> multiply(vector<vector<int>>& A, vector<vector<int>>& B) {
        vector<vector<int>> res(A.size(), vector<int>(B[0].size()));
        vector<vector<pair<int, int>>> v(A.size(), vector<pair<int,int>>());
        for (int i = 0; i < A.size(); ++i) {
            for (int k = 0; k < A[i].size(); ++k) {
                if (A[i][k] != 0) v[i].push_back({k, A[i][k]});
            }
        }
        for (int i = 0; i < A.size(); ++i) {
            for (int k = 0; k < v[i].size(); ++k) {
                int col = v[i][k].first;
                int val = v[i][k].second;
                for (int j = 0; j < B[0].size(); ++j) {
                    res[i][j] += val * B[col][j];
                }
            }
        }
        return res;
    }
};


===================================

1. Naive Method

public int[][] multiply(int[][] A, int[][] B) {
    //validity check
 
    int[][] C = new int[A.length][B[0].length];
    for(int i=0; i<C.length; i++){
        for(int j=0; j<C[0].length; j++){
            int sum=0;
            for(int k=0; k<A[0].length; k++){
                sum += A[i][k]*B[k][j];
            }
            C[i][j] = sum;
        }
    }
 
    return C;
}
2. Optimized Method

public int[][] multiply(int[][] A, int[][] B) {
    //validity check
 
    int[][] C = new int[A.length][B[0].length];
    for(int i=0; i<C.length; i++){
        for(int k=0; k<A[0].length; k++){
            if(A[i][k]!=0){
                for(int j=0; j<C[0].length; j++){
                    C[i][j] += A[i][k]*B[k][j];
                }
            }
        }
    }
 
    return C;
}



"""