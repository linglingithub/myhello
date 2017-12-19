"""


Recursion
Merge Sort
Given an array of integers, sort the elements in the array in ascending order. The merge sort algorithm should be used to solve this problem.

Examples

{1} is sorted to {1}
{1, 2, 3} is sorted to {1, 2, 3}
{3, 2, 1} is sorted to {1, 2, 3}
{4, 2, -3, 6, 1} is sorted to {-3, 1, 2, 4, 6}
Corner Cases

What if the given array is null? In this case, we do not need to do anything.
What if the given array is of length zero? In this case, we do not need to do anything.

"""

import unittest

class Solution(object):
    def mergeSort(self, array):
        """
        array: int[]
        return: int[]
        """
        # write your solution here
        if not array:
            return []
        return self.msort_helper(array, 0, len(array) - 1)

    def msort_helper(self, arr, left, right):
        # recurrsion returning condition
        if left >= right:
            return [arr[left]]  # ===> return single ele arr!!! ===> should return the arr here instead of None
        mid = int(left + (right - left) / 2)
        # sort left half and right half
        left_half = self.msort_helper(arr, left, mid)
        right_half = self.msort_helper(arr, mid + 1, right)
        # return merged result of the two halves
        return self.merge_helper(left_half, right_half)

    def merge_helper(self, left_arr, right_arr):
        res = []
        i, j = 0, 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                res.append(left_arr[i])
                i += 1
            else:
                res.append(right_arr[j])
                j += 1
        if i < len(left_arr):
            res.extend(left_arr[i:])
        else:
            res.extend(right_arr[j:])
        return res


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [3,2,5]
        answer = [2,3,5]
        result = self.sol.mergeSort(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [3]
        answer = [3]
        result = self.sol.mergeSort(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [3]
        answer = [3]
        result = self.sol.mergeSort(nums)
        self.assertEqual(answer, result)

    def test_case3(self):
        nums = []
        answer = []
        result = self.sol.mergeSort(nums)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()
