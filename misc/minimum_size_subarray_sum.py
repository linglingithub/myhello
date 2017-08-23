#coding=utf-8

import unittest

"""

209. Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of
which the sum ≥ s. If there isn't one, return 0 instead.

Have you met this question in a real interview? Yes
Example
Given the array [2,3,1,2,4,3] and s = 7, the subarray [4,3] has the minimal length under the problem constraint.

Challenge
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

Tags
Two Pointers Array Facebook
Related Problems
Medium Subarray Sum Closest 19 %
Easy Subarray Sum

-----

More practice:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

Credits:
Special thanks to @Freezen for adding this problem and creating all test cases.

Array Two Pointers Binary Search
Hide Similar Problems (H) Minimum Window Substring (M) Maximum Size Subarray Sum Equals k

[1,2,2,3,3,4] 7
"""



class Solution(object):
    def minSubArrayLen(self, s, nums):  # ref, O(nlogn) time
        res = -1
        n = len(nums)
        sums = [nums[i] for i in range(n)]
        for i in range(1, n):
            sums[i] += sums[i-1]
        for i in range(n):
            right = self.search_right(i, sums, s)
            if right == n:
                break   # can't have longest possible array to sum up to val bigger than s
            res = min(res, right - i + 1, res) if res != -1 else right-i+1
        return res if res != -1 else 0

    def search_right(self, start, sums, s):
        i, j = start, len(sums)-1
        offset = sums[start-1] if start > 0 else 0
        while i <= j:
            m = i + (j-i)/2
            tmp = sums[m] - offset
            if tmp == s:
                return m
            elif tmp > s:
                j = m-1    # does this work? what if when j=m-1, tmp would be smaller than s, then i + 1 --> return l
            else:
                i = m+1
        return i

    def minSubArrayLen_ref(self, s, nums): #78%, O(N) time O(1) space
        # write your code here
        n = len(nums)
        if n==0: return 0
        left = right = total = 0
        ans = n+1
        while right<n:
            while right<n and total<s:
                total += nums[right]
                right += 1
            if total<s: break
            while left<right and total>=s:
                total -= nums[left]
                left += 1
            ans = min(ans, right-left+1)
        if ans==n+1: return 0
        else: return ans


    def minSubArrayLen1(self, s, nums): #68%, O(N)
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        i, j, sum = 0,0,0
        #nums.sort()
        result = n + 1 #add this to check if result has been achieved or not, see case4
        while j < n:
            while j < n and sum < s:
                sum += nums[j]
                j += 1
            if sum < s and j>=n:
                #return 0 # case 3
                #return result #case4
                return result if result <= n else 0

            result = min(result, j-i)
            while i<j and sum>=s:
                sum -= nums[i]
                i += 1
                if sum >= s:
                    result = min(result, j-i)
        return result


    def minSubArrayLen_deadloop(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        n = len(nums)
        result = n
        i, j, sum = 0, 0, 0
        while i < n:
            while j < n:
                sum += nums[j]
                if sum >= s:
                    result = min(result, j-i+1)
                    break
                j += 1
            while i<j and sum > s and j<n:
                sum -= nums[i]
                i += 1
                if sum >= s:
                    result = min(result, j-i+1)
                else:
                    break
            j+=1
        return result








class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case01(self):
        nums = [2,3,1,2,4,3]
        s = 7
        answer = 2
        result = self.sol.minSubArrayLen( s, nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = []
        s = 100
        answer = 0
        result = self.sol.minSubArrayLen( s, nums)
        self.assertEqual(answer, result)

    def test_case3(self): #====> ??? answer should be 7 ==> CONTINUOUS, which means can't sort array,
        s = 213
        nums = [12,28,83,4,25,26,25,2,25,25,25,12]
        answer = 8
        result = self.sol.minSubArrayLen( s, nums)
        self.assertEqual(answer, result)

    def test_case4(self): #====>
        nums = [1,1]
        s = 3
        answer = 0
        result = self.sol.minSubArrayLen( s, nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-


"""



https://leetcode.com/articles/minimum-size-subarray-sum/

O(nlogn) way:

We could further improve the Approach #2 using the binary search. Notice that we find the subarray with 
\text{sum} >=\text{s}sum>=s starting with an index ii in O(n)O(n) time. But, we could reduce the time to O(log(n))O(log(n)) 
using binary search. Note that in Approach #2, we search for subarray starting with index ii, until we 
find \text{sum}=\text{sums}[j] - \text{sums}[i] +\text{nums}[i]sum=sums[j]−sums[i]+nums[i] that is greater than \text{s}s. 
So, instead of iterating linearly to find the sum, we could use binary search to find the index that is not lower 
than \text{s}-\text{sums[i]}s−sums[i] in the \text{sums}sums, which can be done using lower_boundlower_bound function 
in C++ STL or could be implemented manually.

===========================

这道题给定了我们一个数字，让我们求子数组之和大于等于给定值的最小长度，跟之前那道 Maximum Subarray 最大子数组有些类似，并且题目中要求我们
实现O(n)和O(nlgn)两种解法，那么我们先来看O(n)的解法，我们需要定义两个指针left和right，分别记录子数组的左右的边界位置，然后我们让right向
右移，直到子数组和大于等于给定值或者right达到数组末尾，此时我们更新最短距离，并且将left像右移一位，然后再sum中减去移去的值，然后重复上面的
步骤，直到right到达末尾，且left到达临界位置，即要么到达边界，要么再往右移动，和就会小于给定值。


下面我们再来看看O(nlgn)的解法，这个解法要用到二分查找法，思路是，我们建立一个比原数组长一位的sums数组，其中sums[i]表示nums数组中
[0, i - 1]的和，然后我们对于sums中每一个值sums[i]，用二分查找法找到子数组的右边界位置，使该子数组之和大于sums[i] + s，然后我们更新最短
长度的距离即可。

=============================


O(N) - keep a moving window expand until sum>=s, then shrink util sum<s. Each time after shrinking, update length. (similar to other solutions, just removed unnecessary min value assignment)

public class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        int i = 0, j = 0, sum = 0, min = Integer.MAX_VALUE;
        while (j < nums.length) {
            while (sum < s && j < nums.length) sum += nums[j++];
            if(sum>=s){
                while (sum >= s && i < j) sum -= nums[i++];
                min = Math.min(min, j - i + 1);
            }
        }
        return min == Integer.MAX_VALUE ? 0 : min;
    }
}
O(NLogN) - search if a window of size k exists that satisfy the condition

public class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        int i = 1, j = nums.length, min = 0;
        while (i <= j) {
            int mid = (i + j) / 2;
            if (windowExist(mid, nums, s)) {
                j = mid - 1;
                min = mid;
            } else i = mid + 1;
        }
        return min;
    }


    private boolean windowExist(int size, int[] nums, int s) {
        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i >= size) sum -= nums[i - size];
            sum += nums[i];
            if (sum >= s) return true;
        }
        return false;
    }
}
Another O(NLogN) solution that first calculate cumulative sum and then for each starting point binary search for end position. This uses O(N) space

public class Solution {
 public int minSubArrayLen(int s, int[] nums) {
        int sum = 0, min = Integer.MAX_VALUE;

        int[] sums = new int[nums.length];
        for (int i = 0; i < nums.length; i++)
            sums[i] = nums[i] + (i == 0 ? 0 : sums[i - 1]);

        for (int i = 0; i < nums.length; i++) {
            int j = findWindowEnd(i, sums, s);
            if (j == nums.length) break;
            min = Math.min(j - i + 1, min);
        }
        
        return min == Integer.MAX_VALUE ? 0 : min;
    }

    private int findWindowEnd(int start, int[] sums, int s) {
        int i = start, j = sums.length - 1, offset = start == 0 ? 0 : sums[start - 1];
        while (i <= j) {
            int m = (i + j) / 2;
            int sum = sums[m] - offset;
        if (sum >= s) j = m - 1;
        else i = m + 1;
    }
    return i;
}

"""