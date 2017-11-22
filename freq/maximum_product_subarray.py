#coding=utf-8
__author__ = 'linglin'

"""

152. Maximum Product Subarray

Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.

Subscribe to see which companies asked this question

Hide Tags Array Dynamic Programming
Hide Similar Problems (M) Maximum Subarray (E) House Robber (M) Product of Array Except Self


Medium


"""


import unittest


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp_max = [x for x in nums]
        dp_min = [x for x in nums]
        for i in range(1, len(nums)):
            tmp1 = dp_max[i - 1] * nums[i]
            tmp2 = dp_min[i - 1] * nums[i]
            dp_max[i] = max(dp_max[i], tmp1, tmp2)
            dp_min[i] = min(dp_min[i], tmp1, tmp2)

        return max(dp_max)

class Solution1:
    # @param nums: an integer[]
    # @return: an integer
    def maxProduct(self, nums):
        # write your code here
        if not nums:
            return 0
        max_pro = [x for x in nums]
        min_pro = [x for x in nums]
        for i in range(1,len(nums)):
            a, b = nums[i]*max_pro[i-1], nums[i]*min_pro[i-1]
            max_pro[i] = max(nums[i], a, b)
            min_pro[i] = min(nums[i], a, b)
        result = max(max_pro)
        return result


class Solution1(object):

    def maxProduct(self, nums): #59ms, 46%
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        n = len(nums)
        dp = [0 for i in range(n)]
        dp_abs = [0 for i in range(n)]
        dp_abs[0] = nums[0]
        dp[0] = nums[0]
        for i in range(1, n):
            tmp = nums[i]
            dp_abs[i] = min(tmp*dp_abs[i-1],tmp, dp[i-1]*tmp)
            dp[i] = max(dp[i-1]*tmp, tmp, dp_abs[i-1]*tmp)
        return max(dp)

    def maxProduct_wrong_case2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        n = len(nums)
        dp = [0 for i in range(n)]
        dp_abs = [0 for i in range(n)]
        dp_abs[0] = nums[0]
        dp[0] = nums[0]
        for i in range(1, n):
            tmp = nums[i]
            if abs(tmp*dp_abs[i-1]) >= abs(tmp):
                dp_abs[i] = tmp*dp_abs[i-1]
            else:
                dp_abs[i] = tmp
            dp[i] = max(dp[i-1]*tmp, tmp, dp_abs[i-1]*tmp)
        return max(dp)

    def maxProduct_ref(self, A): #52ms, 68%
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(A) == 0:
            return 0
        min_tmp = A[0]
        max_tmp = A[0]
        result = A[0]
        for i in range(1, len(A)):
            a = A[i] * min_tmp
            b = A[i] * max_tmp
            c = A[i]
            max_tmp = max(max(a,b),c)
            min_tmp = min(min(a,b),c)
            result = max_tmp if max_tmp > result else result
        return result


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case3(self): # actually problem means an array of int
        nums = [2,-5,-2,-0.4,3]
        answer = 20
        result = self.sol.maxProduct(nums)
        self.assertEqual(answer, result)


    def test_case2(self): #=======>
        nums = [2,-5,-2,-4,3]
        answer = 24
        result = self.sol.maxProduct(nums)
        self.assertEqual(answer, result)


    def test_case1(self):
        nums = [2,3,-2,4]
        answer = 6
        result = self.sol.maxProduct(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-



"""

这题是求数组中子区间的最大乘积，对于乘法，我们需要注意，负数乘以负数，会变成正数，所以解这题的时候我们需要维护两个变量，当前的最大值，
以及最小值，最小值可能为负数，但没准下一步乘以一个负数，当前的最大值就变成最小值，而最小值则变成最大值了。

我们的动态方程可能这样：

maxDP[i + 1] = max(maxDP[i] * A[i + 1], A[i + 1], minDP[i] * A[i + 1])
minDP[i + 1] = min(minDP[i] * A[i + 1], A[i + 1], maxDP[i] * A[i + 1]
dp[i + 1] = max(dp[i], maxDP[i + 1])
这里，我们还需要注意元素为0的情况，如果A[i]为0，那么maxDP和minDP都为0，我们需要从A[i + 1]重新开始。

"""





