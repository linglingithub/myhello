#coding=utf8
"""
75. Sort Colors

Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent,

with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

click to show follow up.


Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's,
then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
Subscribe to see which companies asked this question

Subscribe to see which companies asked this question

Hide Tags Array Two Pointers Sort
Hide Similar Problems (M) Sort List (M) Wiggle Sort (M) Wiggle Sort II

Medium

"""


import unittest



class Solution(object):
    def sortColors1(self, nums): #66ms, 14%; 45ms, 68%
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        left, right = 0, len(nums)-1
        while left < len(nums) and nums[left] == 0: #need to add index protection, see case4
            left += 1
        while right >= 0 and nums[right] == 2:
            right -= 1

        i = left
        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i -= 1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
                i -= 1
            i += 1
            if i <= left:  # need this, see case 6, if after swap nums[i] is still 0/2, then
                i = left + 1
            if i > right:
                break


















    # http://fisherlei.blogspot.com/2013/01/leetcode-sort-colors.html
    def sortColors(self, nums):  #45ms, 68%
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

    def test_case4(self): #===>
        nums = [0]
        answer = [0]
        self.sol.sortColors(nums)
        self.assertEqual(answer, nums)

    def test_case5(self):  #===>
        nums = [2]
        answer = [2]
        self.sol.sortColors(nums)
        self.assertEqual(answer, nums)

    def test_case6(self):  #===>
        nums = [2, 0, 0]
        answer = [0, 0, 2]
        self.sol.sortColors(nums)
        self.assertEqual(answer, nums)

    def test_case7(self):
        nums = [2, 0, 0, 1]
        answer = [0, 0, 1, 2]
        self.sol.sortColors(nums)
        self.assertEqual(answer, nums)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()

"""


这里要求one pass完成排序，需要利用只有数组元素只有3个数的特性，否则无法完成。排序完成后一定是0...01...12....2，所以可以扫描数组，当遇到
0时，交换到前部，当遇到1时，交换到后部。用双指针left, right来记录当前已经就位的0序列和2序列的边界位置。

假设已经完成到如下所示的状态：

0......0   1......1  x1 x2 .... xm   2.....2
              |           |               |
            left        cur          right

(1) A[cur] = 1：已经就位，cur++即可
(2) A[cur] = 0：交换A[cur]和A[left]。由于A[left]=1或left=cur，所以交换以后A[cur]已经就位，cur++，left++
(3) A[cur] = 2：交换A[cur]和A[right]，right--。由于xm的值未知，cur不能增加，继续判断xm。
cur > right扫描结束。

"""