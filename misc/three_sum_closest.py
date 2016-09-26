"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

 Array Two Pointers
Hide Similar Problems (M) 3Sum (M) 3Sum Smaller

"""

import unittest

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        min_diff = 1 << 31 # or None
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                diff = sum - target
                # remember to separate min_diff and the result
                if abs(diff) < min_diff:
                    closest = sum
                    min_diff = abs(diff)
                if sum == target:
                    return target
                elif sum > target:
                    k -= 1
                else:
                    j += 1
        return closest


class SolutionTestor(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        s = [-1, 2, 1, - 4]
        target = 1
        answer = 2
        result = self.sol.threeSumClosest(s, target)
        self.assertEqual(answer, result)


def main():
    test_suite = unittest.TestLoader().loadTestsFromTestCase(Solution)
    unittest.TextTestRunner(verbosity=2).run(test_suite)


if __name__ == "__main__":
    main()
