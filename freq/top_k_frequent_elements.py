#coding=utf-8

import unittest

"""
347. Top K Frequent Elements
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

Difficulty:Medium
Total Accepted:76.8K
Total Submissions:158.4K
Contributor: LeetCode
Subscribe to see which companies asked this question.

Related Topics 
Hash Table Heap 
Similar Questions 
Word Frequency Kth Largest Element in an Array Sort Characters By Frequency Split Array into Consecutive Subsequences 
Top K Frequent Words 

"""


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        bucket sort, O(n) time, O(n) space
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import heapq
        from collections import Counter
        val_cnt = Counter(nums)
        n = len(nums)
        buckets = [[] for _ in range(n+1)]
        # the cnt of each val in nums can never be larger than n
        for val, cnt in val_cnt.items():
            buckets[cnt].append(val)
        k_cnt = 0
        res = []
        for i in range(n, 0, -1):  # start from n, not n+1
            if buckets[i]:
                res.extend(buckets[i])
                #k_cnt += (i * len(buckets[i]) )  # wrong, should not be i*len(bucket[i]), should be len()
                k_cnt += len(buckets[i])
                if k_cnt >= k:
                    break
        return res


    def topKFrequent1(self, nums, k):
        """
        heap sort with k size heap, time O(nlogk), O(n) sapce
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import heapq
        from collections import Counter
        val_cnt = Counter(nums)
        heap = []
        #for val, cnt in enumerate(val_cnt):  # remember to enumerate, wrong syntax
        for val, cnt in val_cnt.items():
            if len(heap) < k:
                heapq.heappush(heap, (cnt, val))   # remember to add heap here, 2 args
            else:
                if cnt > heap[0][0]:  # heap instead of heapq
                    heapq.heappop(heap)   # remember to add heap
                    heapq.heappush(heap, (cnt, val))  # remember to add heap here, 2 args
        return [x[1] for x in heap]


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,1,1,2,2,3]
        k = 2
        answer = [1,2]
        result = self.sol.topKFrequent(nums, k)
        self.assertEqual(sorted(answer), sorted(result))

    def test_case02(self):   # ===>
        nums = [1]
        k = 1
        answer = [1]
        result = self.sol.topKFrequent(nums, k)
        self.assertEqual(sorted(answer), sorted(result))

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
