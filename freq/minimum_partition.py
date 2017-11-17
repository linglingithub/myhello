#coding=utf-8

import unittest

"""

Minimum Partition 

 Description
 Notes
 Testcase
 Judge
Given a set of integers, write a function to divide it into two sets S1 and S2 such that the absolute difference between 
their sums is minimum.

If there is a set S with n elements, then if we assume Subset1 has m elements, Subset2 must have n-m elements and the 
value of abs(sum(Subset1) – sum(Subset2)) should be minimum.

Have you met this question in a real interview? Yes
Example
Given nums = [1, 6, 11, 5], return 1

// Subset1 = [1, 5, 6], sum of Subset1 = 12 
// Subset2 = [11], sum of Subset2 = 11   
// abs(11 - 12) = 1     

Tags 
Dynamic Programming Google
Related Problems 
Hard Backpack III 54 %
Medium Backpack II 40 %
Medium Backpack



"""



class Solution:
    """
    ?? [-3, -1, 9], 5, 2.5 , [-1] [6] -- 7
    [1,5,6,11], 23, 11.5, [1, 5, 6] [11]
    [1, 78]
    assume each set has to have at least on element
    @param nums: the given array
    @return: the minimum difference between their sums 
    """

    def findMin1(self, nums): # ref idea, accept in java, tle for python
        # write your code here
        if not nums:
            return 0
        total = sum(nums)

        mid = int(total / 2)
        dp = [False for _ in range(mid + 1)]
        dp[0] = True
        for i in range(len(nums)):
            for j in range(mid, -1, -1):
                dp[j] |= (j >= nums[i] and dp[j - nums[i]])

        for i in range(mid, -1, -1):
            if dp[i]:
                return total - i - i
        return -1

    def findMin(self, nums):   # local runs 5s
        # write your code here
        if not nums:
            return 0
        total = sum(nums)
        nums.sort()
        #half = int(total / 2) +1
        half = int(total/2)
        dp = [False for _ in range(half+1)]
        dp[0] = True
        res = total
        for num in nums:
            #("num", num, nums)
            for j in range(half, -1, -1):
            #for j in range(1, half):
                if num > j:
                    #continue
                    break  # if sort first, may use break here
                dp[j] |= dp[j-num]
                # if dp[j]:  # can't add this, smaller dp also need to check
                #     break
                #print("j", j, dp[j], "j-num=", j-num, dp[j-num])
        #res = abs(total - dp[half-1]*2)
        for val in range(half, -1, -1):
            if dp[val]:
                res = min(abs(total - val*2), res)
                break
        return res

    def findMin_TLE_case3(self, nums):
        # write your code here
        if not nums:
            return 0
        total = sum(nums)
        #nums.sort()
        half = int(total / 2) + 1
        dp = [0 for _ in range(half)]
        res = total
        for num in nums:
            #("num", num, nums)
            for j in range(half-1, 0, -1):
            # for j in range(1, half): # wrong if update dp this way, cause it's 1d, the next round of dp for num, need
            # to find the
                if num > j:
                    continue
                dp[j] = max(dp[j], num + dp[j-num])
                #print("j", j, dp[j], "j-num=", j-num, dp[j-num])
        res = abs(total - dp[half-1]*2)
        return res


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,5,6,11]
        answer = 1
        result = self.sol.findMin(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [1, 78]
        answer = 77
        result = self.sol.findMin(nums)
        self.assertEqual(answer, result)

    def test_case3(self):  #TLE online, local about 12s
        from util.ini_file_util import IniFileUtil
        params = IniFileUtil.read_into_dict("minimum_partition_case3.ini")
        nums = IniFileUtil.string_to_int_list(params.get("nums"))
        # nums = IniFileUtil.string_to_int_list_list(params.get("nums"))   # for matrix input
        answer = 0
        result = self.sol.findMin(nums)
        self.assertEqual(answer, result)

    def test_case04(self):  # wrong for the true/false dp way
        nums = [616,202,595,876,388,120,238,296]
        answer = 15
        result = self.sol.findMin(nums)
        self.assertEqual(answer, result)

    def test_case_self03(self):  # can't work with this one
        nums = [-3, -1, 9]
        answer = 7
        result = self.sol.findMin(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
