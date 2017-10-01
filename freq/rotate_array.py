#coding=utf-8

import unittest

"""
189. Rotate Array
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

[show hint]

Hint:
Could you do it in-place with O(1) extra space?
Related problem: Reverse Words in a String II



Credits:
Special thanks to @Freezen for adding this problem and creating all test cases.

Difficulty:Easy
Total Accepted:142.1K
Total Submissions:573K
Contributor: LeetCode
Subscribe to see which companies asked this question.

Related Topics 
Array 
Similar Questions 
Rotate List Reverse Words in a String II 


"""


class Solution(object):
    def rotate(self, nums, k):
        """
        step by step idx calculation and replace, 43%
        :param nums: 
        :param k: 
        :return: 
        """
        n = len(nums)
        k = k % n
        mov = 1   # should be 1 here, because initially move nums[-k]
        idx = 0
        move_val = nums[idx]
        distance = k
        # should add nums[idx] = nums[-k] here, for keeping the nums[-k] val, otherwise wrong
        # step into and understand
        nums[idx] = nums[-k]
        while mov < n:
            target = (idx + k) % n
            tmp = nums[target]
            nums[target] = move_val
            mov += 1

            distance = (distance + k) % n  # for case when n is multiply of k, case3
            if distance == 0:
                idx = (idx + 1) % n  # need to %n here, otherwise wrong for case5
                move_val = nums[idx]
                continue
            move_val = tmp
            idx = target



    def rotate1(self, nums, k):   #85%
        """
        O(n) time and space
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        # nums = nums[-k:] + nums[:-k]  # does not change nums out of method call
        nums[:] = nums[-k:] + nums[:-k]


    def rotate2(self, nums, k):  # 53%
        """
        O(n) time, O(1) space
        
        12345 --> 3 steps
        (1) 54321 (2) 34521 (3) 34512
        :param nums: 
        :param k: 
        :return: 
        """
        n = len(nums)
        k = k % n
        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)

    def reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case5(self):
        nums = [1,2,3]
        k = 2
        answer = [2,3,1]
        self.sol.rotate(nums, k)
        self.assertEqual(nums, answer)

    def test_case4(self):
        nums = [1,2,3]
        k = 1
        answer = [3,1,2]
        self.sol.rotate(nums, k)
        self.assertEqual(nums, answer)

    def test_case3(self):
        nums = [1,2,3, 4, 5, 6]
        k = 2
        answer = [5,6, 1,2,3, 4]
        self.sol.rotate(nums, k)
        self.assertEqual(nums, answer)

    def test_case2(self):
        nums = [1,2,3, 4, 5]
        k = 2
        answer = [4,5,1,2,3]
        self.sol.rotate(nums, k)
        self.assertEqual(nums, answer)

    def test_case1(self):
        nums = [1,2,3,4,5,6,7]
        k = 3
        answer = [5,6,7,1,2,3,4]
        self.sol.rotate(nums, k)
        self.assertEqual(nums, answer)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""

将包含n个元素的数组向右旋转k步

例如，数组[1,2,3,4,5,6,7]包含元素个数n = 7，向右旋转k = 3步，得到[5,6,7,1,2,3,4]。

至少有3种不同的解题方法，最好使用O(1)的额外空间，“就地”完成数组旋转。

解题思路及代码：
参考LeetCode Discuss（https://oj.leetcode.com/discuss/26088/two-solution-with-extra-memory-dont-know-the-third-one-yet-idea）

解法一 [ 时间复杂度O（n），空间复杂度O(1) ]：
以n - k为界，分别对数组的左右两边执行一次逆置；然后对整个数组执行逆置。

reverse(nums, 0, n - k - 1)
reverse(nums, n - k, n - 1)
reverse(nums, 0, n - 1)
Python代码：
class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n - k)
        self.reverse(nums, n - k, n)
        self.reverse(nums, 0, n)

    def reverse(self, nums, start, end):
        for x in range(start, (start + end) / 2):
            nums[x] ^= nums[start + end - x - 1]
            nums[start + end - x - 1] ^= nums[x]
            nums[x] ^= nums[start + end - x - 1]

注释：
Python中两个数交换可以用如下方法实现：

a, b = b, a
或者：

a ^= b
b ^= a
a ^= b
解法二 [ 时间复杂度O(n)，空间复杂度O(1) ]：
将数组元素依次循环向右平移k个单位

Python代码：
class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        n = len(nums)
        idx = 0
        distance = 0
        cur = nums[0]
        for x in range(n):
            idx = (idx + k) % n
            nums[idx], cur = cur, nums[idx]
            
            distance = (distance + k) % n
            if distance == 0:
                idx = (idx + 1) % n
                cur = nums[idx]

解法三 [ 时间复杂度O(n)，空间复杂度O(n) ]：

注：此方法需要构造新的数组，不满足提示描述中的“就地”旋转条件

class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        n = len(nums)
        if k > 0 and n > 1:
            nums[:] = nums[n - k:] + nums[:n - k]

"""