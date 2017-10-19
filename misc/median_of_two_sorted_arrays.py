__author__ = 'linglin'

"""
4. Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
Subscribe to see which companies asked this question

Hide Tags Binary Search Array Divide and Conquer

Difficulty: Hard

"""


import unittest

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1, len2 = len(nums1), len(nums2)
        if (len1+len2) %2 == 1:
            return self.get_kth(nums1, nums2, int((len1+len2)/2)+1)
        else:
            return ( self.get_kth(nums1, nums2, int((len1+len2)/2)) + self.get_kth(nums1, nums2, int((len1+len2)/2)+1) ) *0.5
            # ===> if use /2 above the OJ will say 2.5 != 2.500000, expecting float, so use *0.5 is better

    def get_kth(self, nums1, nums2, k):
        len1, len2 = len(nums1), len(nums2)
        if len1>len2:
            return self.get_kth(nums2, nums1, k)
        if len1 == 0:
            return nums2[k-1]
        if k==1:
            return min(nums1[0], nums2[0])
        pos1 = min(len1, int(k/2))
        pos2 = k - pos1
        if nums1[pos1-1] <= nums2[pos2-1]:
            return self.get_kth(nums1[pos1:], nums2, k-pos1)
        else:
            return self.get_kth(nums1, nums2[pos2:], k-pos2)





class Solution1(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1:
            nums1, nums2 = nums2, nums1
        # if not nums2:  # should be checking nums1 again, case 3
        if not nums1:
            return None
        m, n = len(nums1), len(nums2)
        if m < n:
            nums1, nums2 = nums2, nums1
            m, n = n, m
        # the above makes sure nums1 is the longer array, to simplify the following process
        mid = (m + n) / 2
        if (m + n) % 2 == 0:
            mid -= 1
        i, j, tag = 0, 0, 1
        #while i < m and j < n and i + j <= mid + 1: # should not be <= here, should be <
        while i < m and j < n and i + j < mid + 1:
            if nums1[i] < nums2[j]:
                i += 1
                tag = 1
            else:
                j += 1
                tag = 2
        if j >= n and i + j < mid + 1:
            tag = 1
            delta = mid + 1 - (i + j)
            i += delta

        if tag == 1:
            result = nums1[i-1]  # should be one step backward
        else:
            result = nums2[j-1]  # should be one step backward

        if (m + n) % 2 == 0:  # add consideration for even number, see case 2
            #next = min(nums1[i], nums2[j]) if i < m and j < n else nums1[i] , wrong when result is at the end of nums1, case2
            if i < m and j < n:
                next = min(nums1[i], nums2[j])
            elif i < m:
                next = nums1[i]
            else:
                next = nums2[j]
            result = (result + next) / 2.0
        return result




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case3(self):
        nums1 = [2]
        nums2 = []
        answer = 2.0   #wrong output None
        result = self.sol.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(answer, result)

    def test_case1(self):
        nums1 = [1, 3]
        nums2 = [2]
        answer = 2
        result = self.sol.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums1 = [1, 2]
        nums2 = [3, 4]
        answer = 2.5
        result = self.sol.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8

"""

http://www.cnblogs.com/zuoyuan/p/3759682.html

原题地址：https://oj.leetcode.com/problems/median-of-two-sorted-arrays/

题意：There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The 
overall run time complexity should be O(log (m+n)).

解题思路：这道题要求两个已经排好序的数列的中位数。中位数的定义：如果数列有偶数个数，那么中位数为中间两个数的平均值；如果数列有奇数个数，那么
中位数为中间的那个数。比如{1，2，3，4，5}的中位数为3。{1，2，3，4，5，6}的中位数为（3+4）/ 2 = 3.5。那么这题最直接的思路就是将两个数列
合并在一起，然后排序，然后找到中位数就行了。可是这样最快也要O((m+n)log(m+n))的时间复杂度，而题目要求O(log(m+n))的时间复杂度。这道题其实
考察的是二分查找，是《算法导论》的一道课后习题，难度还是比较大的。

　　　　   首先我们来看如何找到两个数列的第k小个数，即程序中getKth(A, B , k)函数的实现。用一个例子来说明这个问题：A = {1，3，5，7}；
B = {2，4，6，8，9，10}；如果要求第7个小的数，A数列的元素个数为4，B数列的元素个数为6；k/2 = 7/2 = 3，而A中的第3个数A[2]=5；B中的第3个
数B[2]=6；而A[2]<B[2]；则A[0]，A[1]，A[2]中必然不可能有第7个小的数。因为A[2]<B[2]，所以比A[2]小的数最多可能为A[0], A[1], B[0], 
B[1]这四个数，也就是说A[2]最多可能是第5个大的数，由于我们要求的是getKth(A, B, 7)；现在就变成了求getKth(A', B, 4)；即A' = {7}；B不变，
求这两个数列的第4个小的数，因为A[0]，A[1]，A[2]中没有解，所以我们直接删掉它们就可以了。这个可以使用递归来实现。

代码：

复制代码
class Solution:
    # @return a float
    # @line20 must multiply 0.5 for return a float else it will return an int
    def getKth(self, A, B, k):
        lenA = len(A); lenB = len(B)
        if lenA > lenB: return self.getKth(B, A, k)
        if lenA == 0: return B[k - 1]
        if k == 1: return min(A[0], B[0])
        pa = min(k/2, lenA); pb = k - pa
        if A[pa - 1] <= B[pb - 1]:
            return self.getKth(A[pa:], B, pb)
        else:
            return self.getKth(A, B[pb:], pa)
    
    def findMedianSortedArrays(self, A, B):
        lenA = len(A); lenB = len(B)
        if (lenA + lenB) % 2 == 1: 
            return self.getKth(A, B, (lenA + lenB)/2 + 1)
        else:
            return (self.getKth(A, B, (lenA + lenB)/2) + self.getKth(A, B, (lenA + lenB)/2 + 1)) * 0.5
复制代码


"""