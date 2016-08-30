__author__ = 'linglin'

"""
Given an array of n integers nums and a target, find the number

of index triplets i, j, k with 0 <= i < j < k < n that satisfy the

condition nums[i] + nums[j] + nums[k] < target.

For example, given nums = [-2, 0, 1, 3], and target = 2.

Return 2. Because there are two triplets which sums are less than 2:

[-2, 0, 1]
[-2, 0, 3]
Follow up: Could you solve it in O(n2) runtime?

"""

import unittest


class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count = 0
        nums.sort()
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum < target:
                    count += 1
                    j += 1
                else:
                    k -= 1
        return count



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [-2, 0, 1, 3]
        target = 2
        answer = 2
        result = self.sol.threeSumSmaller(nums, target)
        self.assertEqual(result, answer)


def main():
    test_suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(test_suite)


if __name__ == "__main__":
    main()

