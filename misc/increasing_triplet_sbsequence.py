#coding=utf-8

import unittest

"""

334. Increasing Triplet Subsequence
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:
Return true if there exists i, j, k 
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.

Credits:
Special thanks to @DjangoUnchained for adding this problem and creating all test cases.

Similar Questions 
Longest Increasing Subsequence 

"""


class Solution(object):
    def increasingTriplet(self, nums):  #ref idea, simple and fast
        m1 = m2 = float('inf')
        for num in nums:
            if num <= m1:
                m1 = num
            elif num <= m2:
                m2 = num
            else:
                return True
        return False


    def increasingTriplet1(self, nums):  # similar to LIS way, not really fast for this case
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        dp = []
        for num in nums:
            if not dp or num > dp[-1]:
                dp.append(num)
                if len(dp) >= 3:
                    return True
            else:
                self.find_insert(dp, num)
        return len(dp) >= 3

    def find_insert(self, dp, target):
        idx = len(dp)-1  # should be -1, not -2 here, case4
        while idx >= 0:
            if dp[idx] > target:
                idx -=1
            elif dp[idx] == target:   # should add this, see case5, otherwise [1,2] with 1 ==> [1,1]
                return
            else:   # don't forget this, otherwise dead loop
                break
        idx += 1
        if 0 <= idx <= len(dp)-1 and dp[idx] > target:   # should be <= len()-1, not <, case4
            dp[idx] = target


    def find_insert_wrong(self, dp, target):
        for i in range(len(dp) - 1, -1, -1):
            if dp[i] > target:
                dp[i] = target
                break



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1, 2, 3, 4, 5]
        answer = True
        result = self.sol.increasingTriplet(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [5, 4, 3, 2, 1]
        answer = False
        result = self.sol.increasingTriplet(nums)
        self.assertEqual(answer, result)

    def test_case3(self):  # =====>
        nums = [2,1,5,0,3]
        answer = False
        result = self.sol.increasingTriplet(nums)
        self.assertEqual(answer, result)

    def test_case4(self):  # =====>
        nums = [2,5,3,4,5]
        answer = True
        result = self.sol.increasingTriplet(nums)
        self.assertEqual(answer, result)

    def test_case05(self):  # =====>
        nums = [1,2,1,2,1,2,1,2,1,2]
        answer = False
        result = self.sol.increasingTriplet(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""

Start with the maximum numbers for the first and second element. Then:
(1) Find the first smallest number in the 3 subsequence
(2) Find the second one greater than the first element, reset the first one if it's smaller

def increasingTriplet(nums):
    first = second = float('inf')
    for n in nums:
        if n <= first:
            first = n
        elif n <= second:
            second = n
        else:
            return True
    return False

"""