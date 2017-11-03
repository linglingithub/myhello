#coding=utf-8

import unittest

"""

128. Longest Consecutive Sequence

DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

Difficulty:Hard
Total Accepted:115.4K
Total Submissions:310.5K
Contributor: LeetCode
Subscribe to see which companies asked this question.

Related Topics 
Array Union Find 
Similar Questions 
Binary Tree Longest Consecutive Sequence 

"""


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        vals = {}
        for num in nums:
            vals[num] = True
        res = 1
        for k, v in vals.items():
            if k-1 in vals:
                continue
            low = k
            high = k
            while high+1 in vals:
                high += 1
            res = max(res, high-low+1)
        return res

    def longestConsecutive1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        vals = {}
        for num in nums:
            vals[num] = True
        res = 1
        while vals:
            tmp, _ = vals.popitem()
            l, r = self.get_range(vals, tmp)
            res = max(res, r - l + 1)
        return res

    def get_range(self, vals, target):
        l, r = target, target
        while l - 1 in vals:
            l -= 1
            vals.pop(l)
        while r + 1 in vals:
            r += 1
            vals.pop(r)
        return l, r

class Solution1(object):
    def longestConsecutive(self, nums):  # 79%
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        vals = {}
        for num in nums:
            vals[num] = 1
        res = 0
        while vals:
            tmp, _ = vals.popitem()
            l, r = self.expand_range(tmp, vals)
            res = max(res, r - l + 1)
        return res

    def expand_range(self, target, vals):
        l, r = target, target
        while l - 1 in vals:
            vals.pop(l - 1)
            l -= 1
        while r + 1 in vals:
            vals.pop(r + 1)
            r += 1
        return l, r




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = 1
        answer = 1
        result = self.sol.searchInsert(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()


"""

这道题利用HashSet的唯一性解决，能使时间复杂度达到O(n)。首先先把所有num值放入HashSet，然后遍历整个数组，如果HashSet中存在该值，
就先向下找到边界，找的同时把找到的值一个一个从set中删去，然后再向上找边界，同样要把找到的值都从set中删掉。所以每个元素最多会被遍历两边，
-- insert once, remove once
时间复杂度为O(n)。

=============================

主要有两种思路:
对于每一个n，可以检查n-1, n+1是否存在于这个set（或者map）中；对于map的每个操作都是O(1)的，所以最终是O(n);
对于每一个n，检查是否为一个consecutive sequence的边界，也就是n-1不存在于set中，再逐次检查n + 1, n + 2, n + 3...是否在set中，最终得到另一个上边界（+1）m，所以sequence的长度为m - n （也可以是n+1不存在于set中，则反向检查）。转为set，时间O(n)，之后对于set中的每一个元素，如果是一个连续序列的下边界，则对这个连续序列进行，因为对于每一个连续序列实际只会扫描一遍，所以这个循环最终是O(n)时间复杂度的。
另外，从题目对于时间复杂度的要求O(n)，可以推测那么解法可能是不可以是重循环。
对于第一种思路，具体的解释如下：https://leetcode.com/discuss/18886/my-really-simple-java-o-n-solution-accepted
Whenever a new element n is inserted into the map, do two things:
See if n - 1 and n + 1 exist in the map, and if so, it means there is an existing sequence next to n. Variables left and right will be the length of those two sequences, while 0 means there is no sequence and n will be the boundary point later. Store (left + right + 1) as the associated value to key n into the map.
Use left and right to locate the other end of the sequences to the left and right of n respectively, and replace the value with the new length.
Everything inside the for loop is O(1) so the total time is O(n)
第二种思路来源：https://leetcode.com/discuss/38619/simple-o-n-with-explanation-just-walk-each-streak
Solution

O(n) HashMap
public int longestConsecutive(int[] num) {
    int res = 0;
    HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
    for (int n : num) {
        if (!map.containsKey(n)) {
            int left = (map.containsKey(n - 1)) ? map.get(n - 1) : 0;
            int right = (map.containsKey(n + 1)) ? map.get(n + 1) : 0;
            // sum: length of the sequence n is in
            int sum = left + right + 1;
            map.put(n, sum);

            // keep track of the max length
            res = Math.max(res, sum);

            // extend the length to the boundary(s)
            // of the sequence
            // will do nothing if n has no neighbors
            map.put(n - left, sum);
            map.put(n + right, sum);
        }
        else {
            // duplicates
            continue;
        }
    }
    return res;
}
O(n) Convert to set, loop lower bound consecutive sequence
public class Solution {
    /**
     * @param nums: A list of integers
     * @return an integer
     */
    public int longestConsecutive(int[] nums) {
        // write you code here
        Set<Integer> hs = new HashSet<Integer>();
        for (int n : nums) {
            hs.add(n);
        }
        int longest = 0;
        for (int n : hs) {
            if (!hs.contains(n - 1)) {
                int m = n + 1;
                while (hs.contains(m)) {
                    m++;
                }
                longest = Math.max(longest, m - n);
            }
        }
        return longest;
    }
}

"""
#-*- coding:utf-8 -*-
