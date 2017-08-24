#coding=utf-8

import unittest

"""

274. H-Index
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the 
esearcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h 
citations each, and the other N − h papers have no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them had 
received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the 
remaining two with no more than 3 citations each, his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

Difficulty:Medium
Total Accepted:77.7K
Total Submissions:234.4K
Contributor: LeetCode
Subscribe to see which companies asked this question.

Related Topics 
Hash Table Sort 
Similar Questions 
H-Index II 

"""



class Solution(object):

    def hIndex(self, citations):  # no sorting, use extra O(n) space, time O(n)
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        n = len(citations)
        cnts = [0 for _ in range(n+1)]
        for citation in citations:
            if citation >= n:
                cnts[n] += 1
            else:
                cnts[citation] += 1
        papaer_cnt = n
        cit_sum = 0
        while papaer_cnt >= 0:
            cit_sum += cnts[papaer_cnt]
            if cit_sum >= papaer_cnt:   # paper_cnt is decreasing, cit_sum is increasing, target is max paper_cnt that cit_sum >= paper_cnt
                break
            papaer_cnt -= 1
        return papaer_cnt   # not cit_sum here

    def hIndex1(self, citations):  # sort citation then scan, O(nlogn) for sort and O(n) for scan, O(1) space, can also use binary search instead of scanning
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        citations.sort()     # don't forget to sort
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
        nums = [3, 0, 6, 1, 5]
        answer = 3
        result = self.sol.hIndex(nums)
        self.assertEqual(answer, result)

    def test_case02(self):
        nums = [2,1]
        answer = 1
        result = self.sol.hIndex(nums)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""

排序法
复杂度
时间 O(NlogN) 空间 O(1)

思路
先将数组排序，我们就可以知道对于某个引用数，有多少文献的引用数大于这个数。对于引用数citations[i]，大于该引用数文献的数量是
citations.length - i，而当前的H-Index则是Math.min(citations[i], citations.length - i)，我们将这个当前的H指数和全局最大的H指数来
比较，得到最大H指数。

public class Solution {
    public int hIndex(int[] citations) {
        // 排序
        Arrays.sort(citations);
        int h = 0;
        for(int i = 0; i < citations.length; i++){
            // 得到当前的H指数
            int currH = Math.min(citations[i], citations.length - i);
            if(currH > h){
                h = currH;
            }
        }
        return h;
    }
}


数组映射法
复杂度
时间 O(N) 空间 O(N)

思路
也可以不对数组排序，我们额外使用一个大小为N+1的数组stats。stats[i]表示有多少文章被引用了i次，这里如果一篇文章引用大于N次，我们就将其当为
N次，因为H指数不会超过文章的总数。为了构建这个数组，我们需要先将整个文献引用数组遍历一遍，对相应的格子加一。统计完后，我们从N向1开始遍历这
个统计数组。如果遍历到某一个引用次数时，大于或等于该引用次数的文章数量，大于引用次数本身时，我们可以认为这是H指数。之所以不用再向下找，因为
我们要取最大的H指数。那如何求大于或等于某个引用次数的文章数量呢？我们可以用一个变量，从高引用次的文章数累加下来。因为我们知道，如果有x篇文
章的引用大于等于3次，那引用大于等于2次的文章数量一定是x加上引用次数等于2次的文章数量。

public class Solution {
    public int hIndex(int[] citations) {
        int[] stats = new int[citations.length + 1];
        int n = citations.length;
        // 统计各个引用次数对应多少篇文章
        for(int i = 0; i < n; i++){
            stats[citations[i] <= n ? citations[i] : n] += 1;
        }
        int sum = 0;
        // 找出最大的H指数
        for(int i = n; i > 0; i--){
            // 引用大于等于i次的文章数量，等于引用大于等于i+1次的文章数量，加上引用等于i次的文章数量 
            sum += stats[i];
            // 如果引用大于等于i次的文章数量，大于引用次数i，说明是H指数
            if(sum >= i){
                return i;
            }
        }
        return 0;
    }
}

"""