#coding=utf-8

import unittest

"""
325. Maximum Size Subarray Sum Equals k  (locked)


Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, 
return 0 instead.

Example 1:
Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

Example 2:
Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

Follow Up:
Can you do it in O(n) time?

"""



class Solution(object):
    def maxSubArrayLen(self, nums, k):
        if not nums:
            return 0
        pre_sum = {}
        sub_sum = 0
        res = 0
        for i in range(len(nums)):
            sub_sum += nums[i]
            if sub_sum == k:
                res = max(res, i+1)
            if sub_sum not in pre_sum:
                pre_sum[sub_sum] = i
            want_sum = sub_sum - k
            if want_sum in pre_sum:
                res = max(res, i - pre_sum[want_sum])
        return res




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1, -1, 5, -2, 3]
        k = 3
        answer = 4
        result = self.sol.maxSubArrayLen(nums, k)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [-2, -1, 2, 1]
        k = 1
        answer = 2
        result = self.sol.maxSubArrayLen(nums, k)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""
The subarray sum reminds me the range sum problem. Preprocess the input array such that you get
the range sum in constant time.
sum[i] means the sum from 0 to i inclusively
the sum from i to j is sum[j] - sum[i - 1] except that from 0 to j is sum[j].

j-i is equal to the length of subarray of original array. we want to find the max(j - i)
for any sum[j] we need to find if there is a previous sum[i] such that sum[j] - sum[i] = k
Instead of scanning from 0 to j -1 to find such i, we use hashmap to do the job in constant time.
However, there might be duplicate value of of sum[i] we should avoid overriding its index as we want the max j - i, so 
we want to keep i as left as possible.

public class Solution {
    public int maxSubArrayLen(int[] nums, int k) {
        if (nums == null || nums.length == 0)
            return 0;
        int n = nums.length;
        for (int i = 1; i < n; i++)
            nums[i] += nums[i - 1];
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, -1); // add this fake entry to make sum from 0 to j consistent
        int max = 0;
        for (int i = 0; i < n; i++) {
            if (map.containsKey(nums[i] - k))
                max = Math.max(max, i - map.get(nums[i] - k));
            if (!map.containsKey(nums[i])) // keep only 1st duplicate as we want first index as left as possible
                map.put(nums[i], i);
        }
        return max;
    }
}

"""