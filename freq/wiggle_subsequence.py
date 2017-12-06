#coding=utf-8

import unittest

"""

376. Wiggle Subsequence
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate 
between positive and negative. The first difference (if one exists) may be either positive or negative. 
A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and 
negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences 
are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is 
obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining 
elements in their original order.

Examples:
Input: [1,7,4,9,2,5]
Output: 6
The entire sequence is a wiggle sequence.

Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].

Input: [1,2,3,4,5,6,7,8,9]
Output: 2
Follow up:
Can you do it in O(n) time?

Credits:
Special thanks to @agave and @StefanPochmann for adding this problem and creating all test cases.

Difficulty:Medium
Total Accepted:28.8K
Total Submissions:80K
Contributor: LeetCode
Subscribe to see which companies asked this question.

Related Topics 
Dynamic Programming Greedy 

"""


class Solution(object):
    def wiggleMaxLength(self, nums):  # self, 70% +
        """
        This method can give the sequence and also the length. Check ref for other ideas and 
        simpler algo for getting the length only.
        
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) <= 1:  # can't just assume this, not good for =get_starting_direction case, see case 4
            return len(nums)
        res = []
        # ascending = (nums[1] > nums[0])   # not good for case 5
        direction = self.get_starting_direction(nums)
        if direction == 0:
            return 1
        ascending = True if direction == 1 else False
        res.append(nums[0])
        n = len(nums)
        i = 1
        while i < n:
            if ascending:
                while i + 1 < n and nums[i + 1] >= nums[i]:
                    i += 1
                if nums[i] > res[-1]:    # add for case4
                    res.append(nums[i])
                    ascending = not ascending
            else:
                while i + 1 < n and nums[i + 1] <= nums[i]:
                    i += 1
                if nums[i] < res[-1]:    # add for case4
                    res.append(nums[i])
                    ascending = not ascending
            # res.append(nums[i])       # can't just add without checking = case, see case 4
            # ascending = not ascending
            i += 1
        return len(res)

    def get_starting_direction(self, nums):
        # return 1, 0, -1, which means ascending, equal, and not ascending
        i, n = 1, len(nums)
        while i < n and nums[i] == nums[0]:
            i += 1
        if i == n:
            return 0
        return 1 if nums[i] > nums[0] else -1


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,7,4,9,2,5]
        answer = 6
        result = self.sol.wiggleMaxLength(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [1,17,5,10,13,15,10,5,16,8]
        answer = 7
        result = self.sol.wiggleMaxLength(nums)
        self.assertEqual(answer, result)


    def test_case3(self):
        nums = [1,2,3,4,5,6,7,8,9]
        answer = 2
        result = self.sol.wiggleMaxLength(nums)
        self.assertEqual(answer, result)


    def test_case4(self):   #===>
        nums = [0, 0]
        answer = 1
        result = self.sol.wiggleMaxLength(nums)
        self.assertEqual(answer, result)

    def test_case05(self):   #===>
        nums = [1,1,7,4,9,2,5]
        answer = 6
        result = self.sol.wiggleMaxLength(nums)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""

https://leetcode.com/articles/wiggle-subsequence/


Approach #2 Dynamic Programming [Accepted]

Algorithm

To understand this approach, take two arrays for dp named upup and downdown.

Whenever we pick up any element of the array to be a part of the wiggle subsequence, that element could be a part of a rising wiggle or a falling wiggle depending upon which element we have taken prior to it.

up[i]up[i] refers to the length of the longest wiggle subsequence obtained so far considering i^{th}i
​th
​​  element as the last element of the wiggle subsequence and ending with a rising wiggle.

Similarly, down[i]down[i] refers to the length of the longest wiggle subsequence obtained so far considering i^{th}i
​th
​​ element as the last element of the wiggle subsequence and ending with a falling wiggle.

up[i]up[i] will be updated every time we find a rising wiggle ending with the i^{th}i
​th
​​  element. Now, to find up[i]up[i], we need to consider the maximum out of all the previous wiggle subsequences ending with a falling wiggle i.e. down[j]down[j], for every j<ij<i and nums[i]>nums[j]nums[i]>nums[j]. Similarly, down[i]down[i] will be updated.


public class Solution {
    public int wiggleMaxLength(int[] nums) {
        if (nums.length < 2)
            return nums.length;
        int[] up = new int[nums.length];
        int[] down = new int[nums.length];
        for (int i = 1; i < nums.length; i++) {
            for(int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    up[i] = Math.max(up[i],down[j] + 1);
                } else if (nums[i] < nums[j]) {
                    down[i] = Math.max(down[i],up[j] + 1);
                }
            }
        }
        return 1 + Math.max(down[nums.length - 1], up[nums.length - 1]);
    }
}

Complexity Analysis

Time complexity : O(n^2)O(n
​2
​​ ). Loop inside a loop.
Space complexity : O(n)O(n). Two arrays of the same length are used for dp.


Approach #3 Linear Dynamic Programming [Accepted]

Algorithm

Any element in the array could correspond to only one of the three possible states:

up position, it means nums[i] > nums[i-1]nums[i]>nums[i−1]
down position, it means nums[i] < nums[i-1]nums[i]<nums[i−1]
equals to position, nums[i] == nums[i-1]nums[i]==nums[i−1]
The updates are done as:

If nums[i] > nums[i-1]nums[i]>nums[i−1], that means it wiggles up. The element before it must be a down position. So up[i] = down[i-1] + 1up[i]=down[i−1]+1, down[i]down[i] remains the same as down[i-1]down[i−1]. If nums[i] < nums[i-1]nums[i]<nums[i−1], that means it wiggles down. The element before it must be a up position. So down[i] = up[i-1] + 1down[i]=up[i−1]+1, up[i]up[i] remains the same as up[i-1]up[i−1]. If nums[i] == nums[i-1]nums[i]==nums[i−1], that means it will not change anything becaue it didn't wiggle at all. So both down[i]down[i] and up[i]up[i] remain the same as down[i-1]down[i−1] and up[i-1]up[i−1].

At the end, we can find the larger out of up[length-1]up[length−1] and down[length-1]down[length−1] to find the max. wiggle subsequence length, where lengthlength refers to the number of elements in the given array.

The process can be illustrated with the following example:

public class Solution {
    public int wiggleMaxLength(int[] nums) {
        if (nums.length < 2)
            return nums.length;
        int[] up = new int[nums.length];
        int[] down = new int[nums.length];
        up[0] = down[0] = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > nums[i - 1]) {
                up[i] = down[i - 1] + 1;
                down[i] = down[i - 1];
            } else if (nums[i] < nums[i - 1]) {
                down[i] = up[i - 1] + 1;
                up[i] = up[i - 1];
            } else {
                down[i] = down[i - 1];
                up[i] = up[i - 1];
            }
        }
        return Math.max(down[nums.length - 1], up[nums.length - 1]);
    }
}

Complexity Analysis

Time complexity : O(n)O(n). Only one pass over the array length.
Space complexity : O(n)O(n). Two arrays of the same length are used for dp.





Approach #4 Space-Optimized Dynamic Programming [Accepted]

Algorithm

This approach relies on the same concept as Approach #3. But we can observe that in the DP approach, for updating elements up[i]up[i] and down[i]down[i], we need only the elements up[i-1]up[i−1] and down[i-1]down[i−1]. Thus, we can save space by not using the whole array, but only the last elements.

public class Solution {
    public int wiggleMaxLength(int[] nums) {
        if (nums.length < 2)
            return nums.length;
        int down = 1, up = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > nums[i - 1])
                up = down + 1;
            else if (nums[i] < nums[i - 1])
                down = up + 1;
        }
        return Math.max(down, up);
    }
}


Complexity Analysis

Time complexity : O(n)O(n). Only one pass over the array length.
Space complexity : O(1)O(1). Constant space is used.

Approach #5 Greedy Approach [Accepted]

Algorithm

We need not necessarily need dp to solve this problem. This problem is equivalent to finding the number of alternating max. and min. peaks in the array. Since, if we choose any other intermediate number to be a part of the current wiggle subsequence, the maximum length of that wiggle subsequence will always be less than or equal to the one obtained by choosing only the consecutive max. and min. elements.

This can be clarified by looking at the following figure: Wiggle Peaks

From the above figure, we can see that if we choose C instead of D as the 2nd point in the wiggle subsequence, we can't include the point E. Thus, we won't obtain the maximum length wiggle subsequence.

Thus, to solve this problem, we maintain a variable \text{prevdiff}prevdiff, where \text{prevdiff}prevdiff is used to indicate whether the current subsequence of numbers lies in an increasing or decreasing wiggle. If \text{prevdiff} > 0prevdiff>0, it indicates that we have found the increasing wiggle and are looking for a decreasing wiggle now. Thus, we update the length of the found subsequence when \text{diff}diff (nums[i]-nums[i-1]nums[i]−nums[i−1]) becomes negative. Similarly, if \text{prevdiff} < 0prevdiff<0, we will update the count when \text{diff}diff (nums[i]-nums[i-1]nums[i]−nums[i−1]) becomes positive.

When the complete array has been traversed, we get the required count, which represents the length of the longest wiggle subsequence.

public class Solution {
    public int wiggleMaxLength(int[] nums) {
        if (nums.length < 2)
            return nums.length;
        int prevdiff = nums[1] - nums[0];
        int count = prevdiff != 0 ? 2 : 1;
        for (int i = 2; i < nums.length; i++) {
            int diff = nums[i] - nums[i - 1];
            if ((diff > 0 && prevdiff <= 0) || (diff < 0 && prevdiff >= 0)) {
                count++;
                prevdiff = diff;
            }
        }
        return count;
    }
}

Complexity Analysis

Time complexity : O(n)O(n). We traverse the given array once.

Space complexity : O(1)O(1). No extra space is used.

"""

#-*- coding:utf-8 -*-
