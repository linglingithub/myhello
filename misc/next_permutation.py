"""
Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 --> 1,3,2
3,2,1 --> 1,2,3
1,1,5 --> 1,5,1
Subscribe to see which companies asked this question

Hide Tags Array
Hide Similar Problems (M) Permutations (M) Permutations II (M) Permutation Sequence (M) Palindrome Permutation II


"""

import unittest


class Solution(object):
    def nextPermutation(self, nums): # 66ms, 82.19% --- 72ms, 57.19%
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) < 2:
            return
        right_descending = (nums[-1] > nums[-2])
        if right_descending:
            nums[-1], nums[-2] = nums[-2], nums[-1]
        else:
            idx = len(nums)-1
            while nums[idx]<=nums[idx-1]:
                idx -= 1
                if idx==0:
                    break
            if idx==0: #already the biggest permu, return the first one
                nums.reverse()
            else:
                # nums[idx:] = sorted(nums[idx:])
                # or trying to do reverse, could be a little faster ===>
                swaplen = (len(nums) - idx) / 2
                for i in range(swaplen):
                    nums[idx+i], nums[-1-i] = nums[-1-i], nums[idx+i]
                # <====
                for i in range(idx, len(nums)):
                    if nums[i]<=nums[idx-1]:
                        continue
                    else:
                        nums[i], nums[idx-1] = nums[idx-1], nums[i]
                        break








class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,2,3]
        answer = [1,3,2]
        self.sol.nextPermutation(nums)
        self.assertEqual(answer, nums)

    def test_case2(self):
        nums = [3, 2, 1]
        answer = [1, 2, 3]
        self.sol.nextPermutation(nums)
        self.assertEqual(answer, nums)

    def test_case3(self):
        nums = [1,1,5]
        answer = [1,5,1]
        self.sol.nextPermutation(nums)
        self.assertEqual(answer, nums)

    def test_case4(self): # ====>
        nums = [1, 3, 2]
        answer = [2, 1, 3]
        self.sol.nextPermutation(nums)
        self.assertEqual(answer, nums)

    def test_case5(self):  # ====>
        nums = [2,3,1]
        answer = [3,1,2]
        self.sol.nextPermutation(nums)
        self.assertEqual(answer, nums)

    def test_case6(self):  # ====>
        nums = [1,5,1]
        answer = [5,1,1]
        self.sol.nextPermutation(nums)
        self.assertEqual(answer, nums)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()