#coding=utf-8

import unittest

"""

Continuous Subarray Sum

Given an integer array, find a continuous subarray where the sum of numbers is the biggest. Your code should return the 
index of the first number and the index of the last number. (If their are duplicate answer, return anyone)

Have you met this question in a real interview? Yes
Example
Give [-3, 1, 3, -3, 4], return [1,4].

Tags 
Subarray Array
Related Problems 
Medium Continuous Subarray Sum II 14 %
Easy Maximum Subarray

"""



class Solution:
    # @param {int[]} A an integer array
    # @return {int[]}  A list of integers includes the index of the
    #                  first number and the index of the last number

    def continuousSubarraySum(self, A):  # ref
        # Write your code here
        if not A:
            return [-1, -1]
        result = A[0]
        result2 = [0, 0]
        rsum = 0
        left, right = 0, 0
        for i in range(len(A)):
            x = A[i]
            rsum += x
            if rsum > result:
                result = rsum
                result2 = [left, right]
            if rsum <= 0:
                left = i+1
                right = left
                rsum = 0
                continue
            right += 1
        #return [left, right]
        return result2


    def continuousSubarraySum(self, A):
        # Write your code here
        if not A:
            return [-1, -1]
        result = A[0]
        result2 = [0, 0]
        n = len(A)
        dp = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + A[i - 1]
        for i in range(n):
            if A[i] <= 0:
                continue
            for j in range(i + 1, n + 1):
                if A[j - 1] <= 0:
                    continue

                tmp = dp[j] - dp[i]
                if tmp > result:
                    result = tmp
                    result2 = [i, j - 1]
        return result2

    def continuousSubarraySum_TLE(self, A): #TLE with 61% passed
        # Write your code here
        if not A:
            return [-1, -1]
        result = A[0]
        result2 = [0, 0]
        n = len(A)
        dp = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            dp[i] = dp[i-1] + A[i-1]
        for i in range(n):
            for j in range(i+1, n+1):
                tmp = dp[j]-dp[i]
                if tmp > result:
                    result = tmp
                    result2 = [i, j-1]
        return result2


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [-3, 1, 3, -3, 4]
        answer = [1, 4]
        result = self.sol.continuousSubarraySum(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""

这道题跟LeetCode上的那道Maximum Subarray很类似，不同之处在于这道题让返回最大子数组的范围坐标，而之前那道题只需要返回最大和即可，所以这
道题我们要及时更新start和end变量，分别为子数组的起始和结束位置。我们用curSum来记录当前位置的累计和，如果某一个位置之前的累计和为负数，那
么我们直接从当前位置开始重新算即可，因为加上负数还不如不加，此时将start和end都更新为当前位置i；如果之前的累计和大于等于0，那么我们把累计和
curSum再加上当前的数字，然后更新end位置为i。此时我们更新最大子数组之和mx，以及res即可，参见代码如下：

class Solution {
public:
    /**
     * @param A an integer array
     * @return  A list of integers includes the index of 
     *          the first number and the index of the last number
     */
    vector<int> continuousSubarraySum(vector<int>& A) {
        vector<int> res(2, -1);
        int curSum = 0, mx = INT_MIN, start = 0, end = 0;
        for (int i = 0; i < A.size(); ++i) {
            if (curSum < 0) {
                curSum = A[i];
                start = end = i;
            } else {
                curSum += A[i];
                end = i;
            }
            if (mx < curSum) {
                mx = curSum;
                res[0] = start;
                res[1] = end;
            }
        }
        return res;
    }
};


"""