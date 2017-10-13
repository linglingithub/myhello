#coding=utf-8

import unittest

"""

395. Longest Substring with At Least K Repeating Characters
"""



class Solution(object):
    def searchInsert(self, nums):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """


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

http://blog.csdn.net/u010900754/article/details/62159601

要求是找出最长的子串，子串中的每一个字符都要重复至少k次。
思路是分治法。
要找s[i,j]的最大子串，先统计频数，然后遍历一遍频数，找出第一个频数小于k且大于0的字符，然后找出这个字符的位置，接下来的分析很重要，这个字符
一定不能出现在任何的子串中，因为i,j是整个的子串，在ij里面频数都没有达到k，那么在ij的任何子串中，这个字符也不可能达到频数k。所以不能有这个
字符，那么就在这个位置做一个分治，返回前半部分和后半部分的最大值。
代码：
[html] view plain copy
public int longestSubstring(String s, int k) {  
        return longestSubstringSub(s, k, 0, s.length() - 1);  
    }  

    private int longestSubstringSub(String s, int k, int start, int end){  
        if(start > end) return 0;  
        int[] count = new int[26];  
        for(int i = start; i <= end; i++){  
            count[s.charAt(i) - 'a']++;  
        }  
        for(int i = 0; i < 26; i++){  
            if(count[i] > 0 && count[i] < k){  
                int pos = s.indexOf((char)(i + 'a'), start);  
                return Math.max(longestSubstringSub(s, k, start, pos - 1), longestSubstringSub(s, k, pos + 1, end));  
            }  
        }  
        return end - start + 1;  
    }  

时间复杂度分析：
最坏情况，每一次都只分1和n-1两部分，那么复杂度就是n-1 + n-2 + n - 3 +........，显然是On2的。
最好应该是Onlogn，因为每一次都分一半，那么T(n)=n+2T(n/2)，这个是nlogn的。

其实之前也做过一些longestsubstring的题目，之前有一种模板方法可以求解一类型，但是不可以用在这里，先看下之前那道题。
https://leetcode.com/problems/longest-substring-without-repeating-characters/#/description
这个题目的思路是，双指针，快指针往后遍历，只要发现当前start到end的子串不符合，就把start后移，直到符合，然后end继续。这个思路是一个On级别
的方法。其关键点在于，当发现一个重复时，那么意味着start到end之间只有一个字符出现了两次，那么还能包含其中的一个，包含前一个已经处理过了，那
么就处理包含后一个，那就需要从前面找到前一个字符，然后start移至它的后一个位置。

之前的题目我没有想出来运用这个思路的方法，因为使用这个思路的前提是最开始的时候一定是符合要求的，之前题目并不是这样的。而且count变量不好
控制。所以暂且弃用。

目前处理子串的方法有：
（1）双指针；
（2）dp；
（3）分治；

"""

#-*- coding:utf-8 -*-
