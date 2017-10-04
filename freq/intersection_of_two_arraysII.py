#coding=utf-8

import unittest

"""
350. Intersection of Two Arrays II
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the 
memory at once?

Difficulty:Easy
Total Accepted:77.4K
Total Submissions:172.9K
Contributor: LeetCode
Subscribe to see which companies asked this question.

Related Topics 
Hash Table Two Pointers Binary Search Sort 
Similar Questions 
Intersection of Two Arrays 

"""
import collections

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        for follow 1, O(max(m,n)) time, O(1) space, assume already sorted
        :param nums1: 
        :param nums2: 
        :return: 
        """
        result = []
        i, j = 0, 0
        nums1.sort()
        nums2.sort()
        # don't forget to sort, the problem ask follow up, but originally not sorted
        while i < len(nums1) and j < len(nums2):
            a, b = nums1[i], nums2[j]
            if a == b:
                result.append(a)
                i += 1
                j += 1
            elif a < b:
                i += 1
            else:
                j += 1
        return result


    def intersect1(self, nums1, nums2):
        """
        use dict, for unsorted input, O(m or n) space, O(m+n) time
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        val_cnt = collections.Counter(nums1)
        for num in nums2:
            if num in val_cnt:
                result.append(num)
                val_cnt[num] -= 1
                if val_cnt[num] == 0:
                    del val_cnt[num]
                    if not val_cnt:  # can add this to break earlier
                        break
        return result


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums1 = [1, 2, 2, 1]
        nums2 = [2, 2]
        answer = [2, 2]
        result = self.sol.intersect(nums1, nums2)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()


"""

Follow up 3 discussion
https://discuss.leetcode.com/topic/45992/solution-to-3rd-follow-up-question

"""
#-*- coding:utf-8 -*-
