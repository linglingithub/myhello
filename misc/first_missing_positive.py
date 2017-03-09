#coding=utf-8

import unittest

"""

41. First Missing Positive

Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.

Subscribe to see which companies asked this question.

Hide Tags Array
Hide Similar Problems (E) Missing Number (M) Find the Duplicate Number (E) Find All Numbers Disappeared in an Array

Hard

"""



class Solution(object):

    def firstMissingPositive(self, nums): #48ms, 57%
        """
        So actually the meaning is considering range(1, infinite max), the first missing positive in input.
        Not the first missing in range(min of input, max of input). See test case 3,4,5
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > i+1:
                continue
            else:
                while 0 < nums[i] < i+1 and nums[i] != nums[nums[i]-1]:
                    #print "swapping -- ", i, nums[i], nums[nums[i]-1]
                    nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        #print nums
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1


    def firstMissingPositive_wrong(self, nums):
        """
        So actually the meaning is considering range(1, infinite max), the first missing positive in input.
        Not the first missing in range(min of input, max of input). See test case 3,4,5
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > i+1:
                continue
            else:
                print "swapping -- ", i, nums[i], nums[nums[i]-1]
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
                #one swap is not enough, nums[i]-1 may also need further swap after swap, check case6
        print nums
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1

























    def firstMissingPositive_ref(self, A):
        # write your code here
        n = len(A)
        i = 0
        if n==0:
            return 1
        while i<n:
            while A[i]!=i+1 and A[i]<=n and A[i]>0 and A[i]!=A[A[i]-1]:
                t = A[i]
                A[i] = A[A[i]-1]
                A[t-1] = t
            i = i+1
        for i in xrange(n):
            if A[i]!=i+1:
                return i+1
        return n+1



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1, 2, 0] # min=1, max = 2,non = 1
        answer = 3
        result = self.sol.firstMissingPositive(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [3, 4, -1, 1] #min=1, max = 3, non = 1, len = 4
        answer = 2
        result = self.sol.firstMissingPositive(nums)
        self.assertEqual(answer, result)

    def test_case3(self):
        nums = [2,4,5,8,10] #min=2, max = 10, non = 0, len = 5
        answer = 1 #3
        result = self.sol.firstMissingPositive(nums)
        self.assertEqual(answer, result)

    def test_case4(self):
        nums = [2,2,3,8,10] #min=2, max = 10, non = 0, len = 5
        answer = 1 #4
        result = self.sol.firstMissingPositive(nums)
        self.assertEqual(answer, result)

    def test_case5(self):
        nums = [2,2,3,8,10] #min=2, max = 10, non = 0, len = 5
        answer = 1 #4
        result = self.sol.firstMissingPositive(nums)
        self.assertEqual(answer, result)

    def test_case6(self): #======>
        nums = [11,1,6,11,5,5,-6,9,-3,9,5,4,2,-8,16,-6,-4,2,3]
        answer = 7
        result = self.sol.firstMissingPositive(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""

无序数组的题目如果要O(n)解法往往要用到hash table，但这题要求constant space。所以可以用数组本身作为一个"hash table"：A[0] = 1,
A[1] = 2, .... A[n-1] = n。目标是尽可能将数字i放到数组第i-1个位置。

扫描数组中每个数：
1. 如果A[i]<1或者A[i]>n。说明A[i]一定不是first missing positive。跳过
2. 如果A[i] = i+1，说明A[i]已经在正确的位置，跳过
3. 如果A[i]!=i+1，且0<A[i]<=n，应当将A[i]放到A[A[i]-1]的位置，所以可以交换两数。
这里注意，当A[i] = A[A[i]-1]时会陷入死循环。这种情况下直接跳过。


========================================================================================================================


Sort all numbers and iterate through to find the first missing integer? No, most sorting algorithms take time at least
O(nlogn).
How about linear sorting algorithm? No, bucket sort requires O(n) space.
Mapping all positive integers to a hash table and iterate from 1 to the length of the array to find out the first
missing one? No, hash table requires O(n) space.

Then, how to solve this?

Let's take another look at the problem. It is asking for the first missing POSITIVE integer.
So, given a number in the array,

if it is non-positive, ignore it;
if it is positive, say we have A[i] = x, we know it should be in slot A[x-1]! That is to say, we can swap A[x-1] with
A[i] so as to place x into the right place.
We need to keep swapping until all numbers are either non-positive or in the right places. The result array could be
something like [1, 2, 3, 0, 5, 6, ...]. Then it's easy to tell that the first missing one is 4 by iterate through the
array and compare each value with their index.


"""

#-*- coding:utf-8 -*-
