#coding=utf-8

import unittest

"""

locked

[LEETCODE 163] MISSING RANGES
Link:
https://leetcode.com/problems/missing-ranges/

Question:
Given a sorted integer array where the range of elements are [lower, upper] inclusive, return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].

Hints:
Compare the gap between two words.

For start = 3 and end = 50, return "4->49" (start + 1 -> end - 1)

If lower = 0, the first element is 6, return "0->5"
So, start should be (lower - 1). Similarly, end should be (upper + 1).



"""



class Solution:
    # @param {integer[]} nums
    # @param {integer} lower
    # @param {integer} upper
    # @return {string[]}
    def findMissingRanges(self, nums, lower, upper):
        if not nums:
            return [self.get_range(lower, upper)]
        if len(nums) == lower-upper+1:
            return []
        result = []
        target = lower
        missing = []
        for num in nums:
            if num < target:
                continue
            elif num == target:
                target += 1
            else:
                result.append(self.get_range(target, min(upper,num-1)))
                target = num + 1
            if target > upper:
                return result
        if target < upper:
            result.append(self.get_range(target, upper))
        return result



    def get_range(self, l, r):
        if l == r:
            return str(l)
        return "->".join([str(l), str(r)])


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):   # ===>
        nums, lower, upper = [0, 1, 3, 50, 75], 0, 99
        answer = ["2", "4->49", "51->74", "76->99"]
        result = self.sol.findMissingRanges(nums, lower, upper)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums, lower, upper = [0, 1, 3, 50, 75], 3, 50
        answer = ["4->49"]
        result = self.sol.findMissingRanges(nums, lower, upper)
        self.assertEqual(answer, result)

    def test_case3(self):
        nums, lower, upper = [6, 50, 75], 0, 50
        answer = ["0->5", "7->49"]
        result = self.sol.findMissingRanges(nums, lower, upper)
        self.assertEqual(answer, result)

    def test_case4(self):
        nums, lower, upper = [6, 50, 75], 0, 50
        answer = ["0->5", "7->49"]
        result = self.sol.findMissingRanges(nums, lower, upper)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""
精力旺盛症。
自己做的时候，想的太复杂，做起了binarysearch,企图节省时间。
下次要算清楚，是否有意义。
binarySearch的确logn,但是在lower 和upper之间的数字，很可能还是O(n).
因此一开始就for一遍也是O(n), 而code会相对来说简单许多。

想法：
两个pointer， 每次计较prev和curr之间的部分。
然后prev = curr，向前移动一格。

/*
Given a sorted integer array where the range of elements are [lower, upper] inclusive, return its missing ranges.
For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].
Tags: Array
Similar Problems: (E) Summary Ranges
*/
/*
Attempt2, Thoughts:
Use two pointer to mark the prev and curr value, then verify the range in between.
matching conditoin: prev +2 >= curr.
That is,
1,...,3
1. When print range: print the missing [x,y]
2. missing x = prev+1, missing y = curr - 1;
3. Make sure prev represents the consecutive integer before missing x. 
*/

public class Solution {
    public List<String> findMissingRanges(int[] nums, int lower, int upper) {
        List<String> rst = new ArrayList<String>();
        if (nums == null || nums.length == 0) {//Though, also covered in the for
        	rst.add(printRange(lower, upper));
        	return rst;
        } else if (lower > upper) {
        	return rst;
        }
        int prev = lower - 1;
        int curr;
        for (int i = 0; i <= nums.length; i++) {
        	curr = (i == nums.length) ? upper + 1 : nums[i];
        	if (prev + 2 <= curr) {
        		rst.add(printRange(prev + 1, curr - 1));
        	}
        	prev = curr;
        }
        return rst;
    }

    public String printRange(int from, int to) {
    	return (from == to) ? String.valueOf(from) : from + "->" + to;
    }
}


/*
Old solution: attempted to do binary search for lower and upper, then calculate the mid range. O(logn) + O(upper - lower) = O(n)
Therefore, don't have to do that; just do a run through.
*/

"""

#-*- coding:utf-8 -*-
