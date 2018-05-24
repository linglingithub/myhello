#coding=utf-8

import unittest

"""
760. Find Anagram Mappings

DescriptionHintsSubmissionsDiscussSolution

Given two lists Aand B, and B is an anagram of A. B is an anagram of A means B is made by randomizing the order of the
elements in A.

We want to find an index mapping P, from A to B. A mapping P[i] = j means the ith element in A appears in B at index j.

These lists A and B may contain duplicates. If there are multiple answers, output any of them.

For example, given

A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]
We should return
[1, 4, 3, 2, 0]
as P[0] = 1 because the 0th element of A appears at B[1], and P[1] = 4 because the 1st element of A appears at B[4],
and so on.
Note:

A, B have equal lengths in range [1, 100].
A[i], B[i] are integers in range [0, 10^5].

"""

from collections import deque, defaultdict
class Solution(object):
    def anagramMappings(self, A, B):
        """
        Assumption: A and B are valid anagram to each other.

        Basic idea:
        loop through A and B, for every index in A, find same element in B, record it.
        it the B's index is already used (keep record of visited), then keep searching for the next one
        Time: O(n ^ 2)
        Space: O(n)

        Idea 2:
        1. preprocess B, keep an inverted index of B like (element: [deque of indexes])
        2. loop through A, find matching index list, take the first index in the 'deque of indexes', then remove the first one
        Time: O(n) + O(n * average of repeated times of an element --> not really with deque if pop used) ==> O(n)
        Space: O(n)

        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        if not A or not B:
            return []
        indexes = self._process(B)  # the inverted index
        result = []
        for aidx in range(len(A)):
            bidx = indexes[A[aidx]].popleft() # with assumption, no need to worry about the IndexError here.
            result.append(bidx)
        return result

    def _process(self, B):
        res_dict = defaultdict(deque)
        for idx in range(len(B)):
            res_dict[B[idx]].append(idx)
        return res_dict




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
