"""
167. Two Sum II - Input array is sorted

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a
specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be
less than index2.

Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2


Array Two Pointers Binary Search
(E) Two Sum


"""
import unittest

class Solution(object):
    def twoSum1(self, numbers, target): # this is faster
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        vals = {}
        for i in range(len(numbers)):
            a = numbers[i]
            b = target - a
            if b in vals:
                return [i+1, vals[b]+1] if i < vals[b] else [vals[b]+1, i+1]
            vals[a] = i

    def twoSum2(self, numbers, target): # slower than 1
        i = 0
        j = len(numbers) - 1
        while i < j:
            a, b = numbers[i], numbers[j]
            if a + b == target:
                return [i+1, j+1]
            elif a + b < target:
                i += 1
            else:
                j -= 1
        return [-1, -1]


    def twoSum3(self, numbers, target): # this is faster too
        # https://github.com/renzon/code_interview_training/blob/master/two_sum.py
        from bisect import bisect, bisect_left
        n = len(numbers)
        end = n
        start = 0

        while start < end:
            wanted = target - numbers[start]
            previous = bisect(numbers, wanted, start, end) - 1
            if previous >= 0 and wanted == numbers[previous] and start != previous:
                return start + 1, previous + 1
            another_start_val = target - numbers[end - 1]
            another_start = bisect_left(numbers, another_start_val, start + 1, previous + 1) - 1
            start = max(start + 1, another_start)
            end = previous + 1

        raise NotFound()


    def twoSum(self, numbers, target):  # this is faster too
        # https://github.com/renzon/code_interview_training/blob/master/two_sum.py
        from bisect import bisect, bisect_left
        n = len(numbers)
        end = n
        start = 0

        while start < end:
            wanted = target - numbers[start]
            previous = bisect(numbers, wanted, start, end) - 1
            if previous >= 0 and wanted == numbers[previous] and start != previous:
                return start + 1, previous + 1
            another_start_val = target - numbers[previous]
            another_start = bisect_left(numbers, another_start_val, start + 1, previous + 1) - 1
            start = max(start + 1, another_start)
            end = previous + 1

        return [-1,-1]

class NotFound(Exception):
    pass

class TwoSumIITester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [2, 7, 11, 15]
        target = 9
        result = self.sol.twoSum(nums, target)
        self.assertEqual([1, 2], result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TwoSumIITester)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    #main()
    nums = [2, 3, 4, 7, 11, 15, 18, 19]
    target = 19
    sol = Solution()
    print sol.twoSum(nums, target)
