"""

Find Peak Element

A peak element is an element that is greater than its neighbors.

Given an input array where num[i] <> num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -infinite.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

click to show spoilers.

Note:
Your solution should be in logarithmic complexity.

=======

Next challenges: (M) Summary Ranges  (M) Kth Smallest Element in a BST  (E) Closest Binary Search Tree Value

"""

import unittest

class Solution(object):
    def findPeakElement1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        mid = (left + right) / 2
        while mid <= len(nums) - 1 and mid >= 0:
            # for array
            if left == right:
                return left
            if left == mid:
                return [left, right][0 if nums[left] > nums[right] else 1]
            if mid == 0 or mid == len(nums) - 1:
                return mid
            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid - 1] < nums[mid]:
                left = mid
            else:
                right = mid
            mid = (right + left) / 2
            #print "mid = ", mid, "left = ", left, "right = ", right
        return mid

    def findPeakElement(self, nums):
        if nums is None or len(nums) == 0:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            if left == right:
                return left
            mid = (left+right)/2
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid



class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case3(self):
        result = self.sol.findPeakElement([5, 4])
        #print result
        self.assertEqual(result, 0)

    def test_case1(self):
        result = self.sol.findPeakElement([1, 2, 3, 1])
        #print result
        self.assertEqual(result, 2)

    def test_case2(self):
        result = self.sol.findPeakElement([1, 2, 3, 4])
        #print result
        self.assertEqual(result, 3)

    def test_case4(self):
        result = self.sol.findPeakElement([1])
        # print result
        self.assertEqual(result, 0)

    def test_case5(self):
        result = self.sol.findPeakElement([])
        # print result
        self.assertEqual(result, -1)



            # def testcase1(self):
    #     s = "hello world"
    #     self.assertEqual(s.split(), ['hello', 'world'])


if __name__ == '__main__':
    # arr = [1,2,3,1]
    # arr = [1,2,3,4]
    # arr = [1,2]
    arr = [3, 1]
    sol = Solution()
    # print sol.findPeakElement(arr)
    # print "LLLLLLLLLLL ========="
    # unittest.main()

    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

    # solTestSuite = unittest.TestSuite()
    # solTestSuite.addTest(SolutionTest('test_case1'))
    # solTestSuite.addTest(SolutionTest('test_case2'))
    # unittest.TextTestRunner(verbosity=2).run(solTestSuite)
