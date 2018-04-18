"""Find max smaller ele in sorted array compared to target.
Assumptions:
1) fit in the memory
2) return None?? when no smaller than target

[1, 2, 5, 7] 6 => 5
[-1, 2, 5, 7] 5 => 2
[-1, 2, 5, 7]  10 => 7
[-1, 2, 5, 7]  -10 => None


l, r : current searching area is [l, r] (included) => m
1) arr[m] >= target : r = m - 1
2) arr[m] < target: record the arr[m] as candidate, and l = m + 1
3) exit condition: l > r
4) return candaate

=> Time: O(log n)
=> Space: O(1)

"""

import unittest

class Solution:
    def find_max_smaller(self, arr, target):
        if not arr:
            return None
        l, r = 0, len(arr) - 1
        result = None
        while l <= r:
            m = l + (r - l) // 2
            if arr[m] >= target:
                r = m - 1
            else:
                result = arr[m]
                l = m + 1
        return result



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1, 2, 5, 7]
        target = 6
        answer = 5
        result = self.sol.find_max_smaller(nums, target)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [1, 2, 5, 7]
        target = 5
        answer = 2
        result = self.sol.find_max_smaller(nums, target)
        self.assertEqual(answer, result)

    def test_case3(self):
        nums = [1, 2, 5, 7]
        target = 10
        answer = 7
        result = self.sol.find_max_smaller(nums, target)
        self.assertEqual(answer, result)

    def test_case4(self):
        nums = [1, 2, 5, 7]
        target = -5
        answer = None
        result = self.sol.find_max_smaller(nums, target)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()