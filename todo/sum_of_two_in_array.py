#coding=utf-8

import unittest

"""
INput:
1. An array of ints, a
2. A long int , k

Output:

an int denoting the number of DISTINCT pairs (ai, aj) where
i != j, 
ai + aj = k
(ai, aj) and (aj, ai) are considered the same pair
(ai, aj) and (a1, a2) are considered the same pair if ai = a1 or ai = a2 althoug i != 1


constraints:
1 <= n <= 5*(10^5)
0 <= ai <= 10^9

"""



class Solution(object):
    def find_pair_cnt(self, nums, k):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        vals = {}
        nums.sort()
        res = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                if nums[i] == k / 2:
                    if vals.get(nums[i]) == 1:
                        vals[nums[i]] = 2
                        res += 1
                    else:
                        vals[nums[i]] = vals.get(nums[i], 0) + 1
                continue
            target = k - nums[i]
            if target in vals and k not in vals:
                res += 1
            vals[nums[i]] = 1
        return res




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [6,1,3,46,1,3,9]
        k = 47
        answer = 1
        result = self.sol.find_pair_cnt(nums, k)
        self.assertEqual(answer, result)

    def test_case02(self):
        nums = [6,6,3,9,3,5,1]
        k = 12
        answer = 2
        result = self.sol.find_pair_cnt(nums, k)
        self.assertEqual(answer, result)

    def test_case3(self):
        nums = [0, 2, 2, 2, 4]
        k = 4
        answer = 2
        result = self.sol.find_pair_cnt(nums, k)
        self.assertEqual(answer, result)

    def test_case4(self):
        nums = [ 2, 2]
        k = 4
        answer = 1
        result = self.sol.find_pair_cnt(nums, k)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
