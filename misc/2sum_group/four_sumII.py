#coding=utf-8

import unittest

"""

454. 4Sum II
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that 
A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of 
-228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

Difficulty:Medium
Total Accepted:20.5K
Total Submissions:43.7K
Contributor: Samuri
Subscribe to see which companies asked this question.

Related Topics 
Hash Table Binary Search 
Similar Questions 
4Sum 

"""


class Solution(object):
    def fourSumCount(self, A, B, C, D):  #82%
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        A.sort()
        B.sort()
        C.sort()
        D.sort()
        vals = {}
        cnt = 0
        for i in range(len(A)):
            for j in range(len(B)):
                val = A[i] + B[j]
                vals[val] = vals.get(val, 0) + 1
        for i in range(len(C)):
            for j in range(len(D)):
                val = C[i] + D[j]
                if -val in vals:
                    cnt += vals[-val]
        return cnt


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        A = [1, 2]
        B = [-2, -1]
        C = [-1, 2]
        D = [0, 2]
        answer = 2   # (0, 0, 0, 1) and (1, 1, 0, 0)
        result = self.sol.fourSumCount(A, B, C, D)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""

Easy 2 lines O(N^2) Python
def fourSumCount(self, A, B, C, D):   # AC, 34%
    AB = collections.Counter(a+b for a in A for b in B)
    return sum(AB[-c-d] for c in C for d in D)
    
================================================    
    
Clean java solution O(n^2)
public int fourSumCount(int[] A, int[] B, int[] C, int[] D) {
    Map<Integer, Integer> map = new HashMap<>();
    
    for(int i=0; i<C.length; i++) {
        for(int j=0; j<D.length; j++) {
            int sum = C[i] + D[j];
            map.put(sum, map.getOrDefault(sum, 0) + 1);
        }
    }
    
    int res=0;
    for(int i=0; i<A.length; i++) {
        for(int j=0; j<B.length; j++) {
            res += map.getOrDefault(-1 * (A[i]+B[j]), 0);
        }
    }
    
    return res;
}

Time complexity:  O(n^2)
Space complexity: O(n^2)    

"""

#-*- coding:utf-8 -*-
