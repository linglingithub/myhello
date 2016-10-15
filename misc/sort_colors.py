"""
Sort Colors

Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent,

with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

click to show follow up.


Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
Subscribe to see which companies asked this question

Subscribe to see which companies asked this question

Hide Tags Array Two Pointers Sort
Hide Similar Problems (M) Sort List (M) Wiggle Sort (M) Wiggle Sort II

"""


import unittest



class Solution(object):
    # http://fisherlei.blogspot.com/2013/01/leetcode-sort-colors.html
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) <= 1:
            return
        red_idx = 0
        blue_idx = len(nums) - 1
        current = 0 #1, if put 1 then fail case2
        while current <= blue_idx:
            tmp = nums[current]
            if tmp == 0:
                nums[red_idx], nums[current] = nums[current], nums[red_idx]
                red_idx += 1
                current += 1
            elif tmp == 2:
                nums[blue_idx], nums[current] = nums[current], nums[blue_idx]
                blue_idx -= 1
            else:
                current += 1





class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [0,2]
        answer = [0,2]
        self.sol.sortColors(nums)
        self.assertEqual(answer, nums)

    def test_case2(self): #===>
        nums = [2,1]
        answer = [1, 2]
        print "!!!", answer
        self.sol.sortColors(nums)
        self.assertEqual(answer, nums)

    def test_case3(self):
        nums = [1, 2]
        answer = [1, 2]
        self.sol.sortColors(nums)
        self.assertEqual(answer, nums)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()