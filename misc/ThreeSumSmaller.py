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
    def threeSumSmaller_self(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count = 0
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum >= target:
                    break
                while sum < target and j < k:
                    count += 1
                    k -= 1
                    sum = nums[i] + nums[j] + nums[k]
                j += 1
        return count

    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = 0
        for i in xrange(0, len(nums) - 2):
            if 3 * nums[i] >= target:
                return res
            start = i + 1
            end = len(nums) - 1
            while start < end:
                # print nums[i], nums[start], nums[end]
                if nums[i] + nums[start] + nums[end] < target:
                    res += end - start
                    start += 1
                else:
                    end -= 1

        return res



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

