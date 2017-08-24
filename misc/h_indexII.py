#coding=utf-8

import unittest

"""

275. H-Index II
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?

Difficulty:Medium
Total Accepted:50.5K
Total Submissions:147K
Contributor: LeetCode
Subscribe to see which companies asked this question.

Related Topics 
Binary Search 
Similar Questions 
H-Index 

"""



class Solution(object):
    def hIndex(self, citations):
        if not citations:
            return 0
        n = len(citations)
        l, r = 0, n-1
        last = n
        while l <= r:   # should be <=, otherwise wrong for case3
            m = l+(r-l)/2
            if n-m <= citations[m]:
                if m == last:
                    break
                r = m
                last = m
            else:
                l = m+1
        return n-l


    def hIndex_wrong(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        n = len(citations)
        l, r = 0, n-1
        last = n
        while l < r:
            m = l+(r-l)/2
            if n-m <= citations[m]:
                if m == last:
                    break
                l = m       # wrong here, m is too big, should adjust the right bound
                last = m
            else:
                r = m-1
        return n-l

    def hIndex_TLE(self, citations):  # already sorted , then binary search, linear scan will TLE
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        # citations.sort()
        n, res = len(citations), 0
        for i in range(n):
            tmp = min(citations[i], n-i)   # this is important, understand this
            res = max(res, tmp)
            if res == n-i:
                break
        return res


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [0,1,3,5,6]
        answer = 3
        result = self.sol.hIndex(nums)
        self.assertEqual(answer, result)

    def test_case02(self):
        nums = [1,2]
        answer = 1
        result = self.sol.hIndex(nums)
        self.assertEqual(answer, result)


    def test_case03(self):
        nums = [0]
        answer = 0
        result = self.sol.hIndex(nums)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""
The idea is to search for the first index from the sorted array so that :

citations[index] >= length(citations) - index. 

And return (length - index) as the result.
Here is the code:

public int hIndex(int[] citations) {
	int len = citations.length;
	int lo = 0, hi = len - 1;
	while (lo <= hi) {
		int med = (hi + lo) / 2;
		if (citations[med] == len - med) {
			return len - med;
		} else if (citations[med] < len - med) {
			lo = med + 1;
		} else { 
			//(citations[med] > len-med), med qualified as a hIndex,
		    // but we have to continue to search for a higher one.    # if after decrease hi, book is more and  cit is less,
			hi = med - 1;
		}
	}
	return len - lo;
}
=========================================

思路
在升序的引用数数组中，假设数组长为N，下标为i，则N - i就是引用次数大于等于下标为i的文献所对应的引用次数的文章数。如果该位置的引用数小于文章
数，则说明则是有效的H指数，如果一个数是H指数，那最大的H指数一定在它的后面（因为是升序的）。根据这点就可已进行二分搜索了。
这里min = mid + 1的条件是citations[mid] < n - mid，确保退出循环时min肯定是指向一个有效的H指数。

代码
public class Solution {
    public int hIndex(int[] citations) {
        int n = citations.length;
        if(n == 0) return 0;
        int min = 0, max = citations.length - 1;
        while(min <= max){
            int mid = (min + max) / 2;
            // 如果该点是有效的H指数，则最大H指数一定在右边
            if(citations[mid] < n - mid){
                min = mid + 1;
            // 否则最大H指数在左边
            } else {
                max = mid - 1;
            }
        }
        // n - min是min点的H指数
        return n - min;
    }
}

"""