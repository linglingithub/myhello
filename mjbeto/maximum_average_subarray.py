#coding=utf-8

import unittest

"""

Maximum Average Subarray

Given an array with positive and negative numbers, find the maximum average subarray which length should be greater or
equal to given length k.

 Notice

It's guaranteed that the size of the array is greater or equal to k.

Have you met this question in a real interview? Yes
Example
Given nums = [1, 12, -5, -6, 50, 3], k = 3

Return 15.667 // (-6 + 50 + 3) / 3 = 15.667

Tags
Binary Search Subarray Google
Related Problems
Easy Maximum Subarray

Medium

"""



class Solution:
    # @param {int[]} nums an array with positive and negative numbers
    # @param {int} k an integer
    # @return {double} the maximum average
    def maxAverage(self, nums, k):  # ref
        if k <= 0:
            return 0
        left, right = min(nums), max(nums)
        epsilon = 1e-6
        while right - left >= epsilon:
            mid = (left+right)/2.0
            if self.compare_target_mid(nums, mid, k):
                left = mid
            else:
                right = mid
        return left

    def compare_target_mid(self, nums, mid, k):
        """
        returns True if mid is a number that is smaller than the maximum average, or False if the mid is bigger than 
        maximum average 
        :param nums: 
        :param mid: 
        :param k: 
        :return: 
        """
        n = len(nums)
        min_pre = 0
        # the purpose is to find the value of mid that makes mid - target => 0
        # min_pre keeps the minimum subsum[x] that is the prefix of
        subsum = [0 for _ in range(n)]
        subsum[0] = nums[0] - mid
        for i in range(1, n):
            subsum[i] = subsum[i-1] + nums[i] - mid
            if i >= k-1 and subsum[i] - min_pre >= 0:
                return True
                # mid can be bigger, because subsum (with length >= k) is bigger than min_pre, so there can have a
                # subarray in subsum sequence that have bigger sum (which means bigger average??
            if i >= k-1:
                # not k, should be k-1 here, because for subsum of length(k+1), already need to check if
                # subsum[i] >= min_pre in the next loop, so on the first time index reach k-1(the length is k), we
                # need to record the min_pre
                min_pre = min(min_pre, subsum[i-k+1])
                # after i >= k, start to record possible 'prefix' subarray that have lower value (can be excluded from
                # maximum average subarray)
        return False  # mid should be smaller, so that a continuous k subarray can be found

    def compare_target_mid1(self, nums, mid, k):
        n = len(nums)
        min_pre = 0
        subsum = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            subsum[i] = subsum[i-1] + nums[i-1] - mid
            if i >= k and subsum[i] - min_pre >= 0:
                return True
                # mid can be bigger, because subsum (with length >= k) is bigger than min_pre, so there can have a
                # subarray in subsum sequence that have bigger sum (which means bigger average??
            if i >= k:
                min_pre = min(min_pre, subsum[i-k+1])
        return False  # mid should be smaller, so that a continuous k subarray can be found





    def maxAverage_TLE_subsum(self, nums, k): #O(N^2), still runs around 12s locally
        # Write your code here
        if k <= 0:
            return 0
        result = None
        n = len(nums)
        end = n-k+1
        subsum = [num for num in nums]
        for i in range(1,n):
            subsum[i] += subsum[i-1]
        for i in range(end):
            tmp = subsum[i+k-1] - subsum[i] + nums[i]
            result = max(result, tmp * 1.0 / k)
            for j in range(i+k, n):
                tmp += nums[j]
                result = max(result, tmp * 1.0 / (j - i + 1))
        return result

    def maxAverage_TLE(self, nums, k): #O(N^2)
        # Write your code here
        if k <= 0:
            return 0
        result = None
        n = len(nums)
        end = n-k+1
        for i in range(end):
            tmp = 0
            for j in range(i, i+k):
                tmp += nums[j]
            result = max(result, tmp * 1.0 / (j - i + 1))
            for j in range(i+k, n):
                tmp += nums[j]
                result = max(result, tmp * 1.0 / (j - i + 1))
        return result



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case4(self):  #===> TLE, local around 12s
        import ConfigParser
        from util.string_to_list import string_to_int_list
        config = ConfigParser.RawConfigParser(allow_no_value=True)
        data_file = "../data/maximum_average_subarray_case4.ini"
        with open(data_file) as fin:
            config.readfp(fin)
            nums = config.get("data", "nums")
            nums = string_to_int_list(nums)
            k = int(config.get("data", "k"))
        answer = -21.916
        result = self.sol.maxAverage(nums, k)
        self.assertTrue(abs(answer-result) <= 1e-3)

    def test_case3(self):
        nums = [-1,-2,-3,-100,-1,-50]
        k = 4
        answer = -21.400
        result = self.sol.maxAverage(nums, k)
        self.assertTrue(abs(answer-result) <= 1e-3)

    def test_case2(self):
        nums = [5]
        k = 1
        answer = 5.0
        result = self.sol.maxAverage(nums, k)
        self.assertTrue(abs(answer-result) <= 1e-3)

    def test_case1(self):
        nums = [1, 12, -5, -6, 50, 3]
        k = 3
        answer = 15.667
        result = self.sol.maxAverage(nums, k)
        #self.assertEqual(answer, result)
        print result
        self.assertTrue(abs(answer-result) <= 1e-3)




def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=3).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""

个人理解：
1、一个数组的子数组的最大平均数一定在数组的最大值和最小值之间，所以二分法的第一步限定average位于[min,max]之中。
2、接下去要做的就是不断的缩小范围，直至max-min足够小（如1e-6），那我们就得到了想要的结果。
缩小范围的思想如下：
每一轮设置mid=(min+max)/2，然后将原数组中的每一个数减去这个mid，如果能找到（经过提醒，改正为：大于等于）k个相邻数的总和大于0的情况，那么
说明最终结果一定比这个mid要更大，限定下一轮寻找范围在[mid,max]之中。反之在限定在[min,mid]之中。
那么在实际算法中我们需要解决的关键一步就是，如何判断“有（大于等于）k个相邻数的总和大于0的情况存在”。
首先，我们可以用sum数组来存储减掉mid值的原数组的各总和（sum[i]存储num[0]-mid到num[i-1]-mid的总和），当sum[i]存储的总和个数超过k时
（即i>k），也就是说我们保证了这个子数组的长度达到k后，可以砍掉之前一些拖后腿的数。这些拖后腿的数在上述链接的代码中是用min_pre来实现的。当
之前拖后腿的数值小于min_pre时，更新min_pre=sum[i - k + 1]。sum[i]存储的是num[0]~num[i-1]减去mid的总和，而min_pre存储的是
num[0]~num[k]减掉mid的总和，这样sum[i]-min_pre得到的是sum[k+1]~sum[i-1]，它所记录的总和个数也就是到num[i]为止能够找到的最大平均数 
子数组的长度。


http://stackoverflow.com/questions/13093602/finding-subarray-with-maximum-sum-number-of-elements

Q: O(n^2) algorithm is easy. Does anyone have a better algorithm for this?

Answer:

You can use binary search.

For a searched value x, consider the array b[i] = a[i] - x. Now find the maximum sum subarray of length at least k.

This works because the average of a subarray of length k is (a[p] + ... + a[p + k - 1]) / k. So we have:

(a[p] + ... + a[p + k - 1]) / k >= avg
a[p] + ... + a[p + k - 1] >= avg * k
(a[p] - avg) + ... + (a[p + k - 1] - avg) >= 0
So, if you binary search for the average, by substracting it from each element, if you can find a positive-sum subarray 
(find the maximum one and check if it's positive) of length at least k, then avg is a valid answer: continue to search 
in [avg, max_avg] to see if you can find a better one. If not, reduce search to [0, avg].

shareimprove this answer
answered Oct 26 '12 at 21:14

IVlad
34.2k1067151
  	 	
Makes sense. The runtime order becomes O(N)*log(range of numbers). It's still not clear for me when to stop the binary 
search. – Mohammad Moghimi Oct 27 '12 at 2:59
  	 	
@MohammadMoghimi - you can stop it when the interval you're searching in becomes small enough for your purposes. Try 
stopping it when it becomes smaller than 10^-3 for example. If it's not good enough, decrease the exponent. 
– IVlad Oct 27 '12 at 7:19 


========================================================================================================================

class Solution:
    # @param {int[]} nums an array with positive and negative numbers
    # @param {int} k an integer
    # @return {double} the maximum average
    def maxAverage(self, nums, k):
        # Write your code here
        l, r = min(nums), max(nums)
        n = len(nums)
        prefix = [0] * (n + 1)
        while r - l >= 1e-6:
            mid, check = (l + r) / 2.0, False
            min_pre = 0
            for i in xrange(1, n + 1):
                prefix[i] = prefix[i - 1] + nums[i - 1] - mid;
                if i >= k and prefix[i] >= min_pre:
                    check = True
                    break
                if i >= k:
                    min_pre = min(min_pre, prefix[i - k + 1])

            if check:
                l = mid
            else:
                r = mid
        return l

"""