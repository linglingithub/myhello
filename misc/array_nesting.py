#coding=utf-8

import unittest

"""
565. Array Nesting
DescriptionHintsSubmissionsDiscussSolution
A zero-indexed array A of length N contains all integers from 0 to N-1. Find and return the longest length of set S,
where S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to the rule below.

Suppose the first element in S starts with the selection of element A[i] of index = i, the next element in S should be
A[A[i]], and then A[A[A[i]]]… By that analogy, we stop adding right before a duplicate element occurs in S.

Example 1:
Input: A = [5,4,0,3,1,6,2]
Output: 4
Explanation:
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

One of the longest S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
Note:
N is an integer within the range [1, 20,000].
The elements of A are all distinct.
Each element of A is an integer within the range [0, N-1].

Difficulty:Medium
Total Accepted:19.6K
Total Submissions:39.6K
Contributor:fallcreek
Companies

Related Topics

Similar Questions
Nested List Weight SumFlatten Nested List IteratorNested List Weight Sum II

"""



class Solution(object):
    def arrayNesting(self, nums):
        """
        Basic Idea:
        keep tracking of each num in nums, vist by loop, and keep records of current set, and mark the size
        1. use a current set id
        2. use a sid array to mark whether an index is visited or not.

        Time: O(n)
        Space: O(n)

        ===> if nums can be changed then can try reuse nums to optimize space to O(1)
        for example, set visited value to -1 * original, then if need to recover nums, after done, use O(n) time to
        convert back by * (-1) again.

        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        sid = [-1 for _ in range(n)]  # record set id of each element
        cur_id = 1
        global_max = [0]
        # start looping through nums
        for idx in range(n):
            if sid[idx] != -1:
                continue
            self._search(idx, 0, nums, sid, cur_id, global_max)
            cur_id += 1
        return global_max[0]

    def _search(self, idx, count, nums, sid, cur_id, global_max):
        sid[idx] = cur_id # mark
        count += 1
        a = nums[idx]  # get next
        if sid[a] != cur_id:
            self._search(a, count, nums, sid, cur_id, global_max)
        else:
            global_max[0] = max(global_max[0], count)



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = 1
        answer = 1
        result = self.sol.testm(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
