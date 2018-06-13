#coding=utf-8

import unittest

"""

448. Find All Numbers Disappeared in an Array

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

Difficulty:Easy
Total Accepted:94K
Total Submissions:183.8K
Contributor:yuhaowang001

Companies 

Related Topics 

Similar Questions 
First Missing PositiveFind All Duplicates in an Array


"""



class Solution:
    def findDisappearedNumbers(self, nums):
        """
        basid idea: numbers [1.. n], on array of length n (index 0 , n - 1)
        try to make a mapping between 1..n --> 0..n-1
        for all a[i], mark the value on (a[i] - 1) to negative one
        if all 1..n appears, then all the values on 0..n-1 will turn to negative values
        but there're some missing values, so loop throught 0.n-1 positions,
        for the position x that hold positive value, means that x+1 is not showing in previous loop

        """
        if not nums:
            return []
        for num in nums:
            # !!!! nums[num - 1] = - nums[num - 1]  # for appean twice will turn to pos again
            idx = abs(num) - 1
            nums[idx] = -abs(nums[idx])
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
        # result = []
        # for i in range(len(nums)):
        #     if nums[i] > 0:
        #         result.append(i + 1)
        # return result



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = 1
        answer = 1
        result = self.sol.testm(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""
For each number i in nums,
we mark the number that i points as negative.
Then we filter the list, get all the indexes
who points to a positive number.
Since those indexes are not visited.

"""

#-*- coding:utf-8 -*-
