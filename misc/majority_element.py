#coding=utf-8

import unittest

"""

169. Majority Element

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

Subscribe to see which companies asked this question.

Hide Tags Array Divide and Conquer Bit Manipulation
Hide Similar Problems (M) Majority Element II

Easy

"""



class Solution(object):
    def majorityElement(self, nums):# 55ms, 91%, Moore voting
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate, cnt = None, 0
        for num in nums:
            if cnt == 0:
                candidate = num
                cnt = 1
            else:
                if candidate == num:
                    cnt += 1
                else:
                    cnt -= 1
        return candidate

    def majorityElement1(self, nums):# 82ms, 40%, hash way
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt_dict = {}
        n = len(nums)
        for num in nums:
            if num in cnt_dict:
                cnt_dict[num] += 1
            else:
                cnt_dict[num] = 1
            if cnt_dict[num] > n/2:
                return num



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,2,3,4,1,1,1,5,1]
        answer = 1
        result = self.sol.majorityElement(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""

这个题解法很多，官方就给了七种

1. Runtime: O(n2) — Brute force solution: Check each element if it is the majority element.

2. Runtime: O(n), Space: O(n) — Hash table: Maintain a hash table of the counts of each element, then find the most
    common one.

3. Runtime: O(n log n) — Sorting: As we know more than half of the array are elements of the same value, we can sort the
    array and all majority elements will be grouped into one contiguous chunk. Therefore, the middle (n/2th) element must
     also be the majority element.

4. Average runtime: O(n), Worst case runtime: Infinity — Randomization: Randomly pick an element and check if it is the
    majority element. If it is not, do the random pick again until you find the majority element. As the probability to
    pick the majority element is greater than 1/2, the expected number of attempts is < 2.

5. Runtime: O(n log n) — Divide and conquer: Divide the array into two halves, then find the majority element A in the
    first half and the majority element B in the second half. The global majority element must either be A or B. If
    A == B, then it automatically becomes the global majority element. If not, then both A and B are the candidates for
    the majority element, and it is suffice to check the count of occurrences for at most two candidates. The runtime
    complexity, T(n) = T(n/2) + 2n = O(n log n).

6. Runtime: O(n) — Moore voting algorithm: We maintain a current candidate and a counter initialized to 0. As we iterate
 the array, we look at the current element x:
If the counter is 0, we set the current candidate to x and the counter to 1.
If the counter is not 0, we increment or decrement the counter based on whether x is the current candidate.
After one pass, the current candidate is the majority element. Runtime complexity = O(n).

7. Runtime: O(n) — Bit manipulation: We would need 32 iterations, each calculating the number of 1's for the ith bit of
all n numbers. Since a majority must exist, therefore, either count of 1's > count of 0's or vice versa (but can never be
 equal). The majority number’s ith bit must be the one bit that has the greater count.

Update (2014/12/24): Improve algorithm on the O(n log n) sorting solution: We do not need to 'Find the longest
contiguous identical element' after sorting, the n/2th element is always the majority.

"""