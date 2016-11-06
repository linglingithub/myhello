__author__ = 'linglin'

"""
4. Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
"""


class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        ind1 = 0
        ind2 = 0
        if m < n:
            nums1, nums2 = nums2, nums1
            m, n = n, m
        k = 1
        if (m+n) % 2 == 1:
            mid = (m+n)/2 + 1
        else:
            mid = (m+n)/2

        while ind1 + ind2 < mid:
            if ind1 < m and ind2 < n:
                if nums1[ind1] < nums2[ind2]:
                    ind1 += 1
                    k = 1
                else:
                    ind2 += 2
                    k = 2
            else:
                if ind1 >= m and ind2 < n-1:
                    k = 2
                    ind2 += 1
                elif ind2 >= n and ind1 < m-1:
                    k = 1
                    ind1 += 1
        if k == 1:
            if ind1:
            return nums1[ind1]
        else:
            return nums2[ind2]

if __name__ == '__main__':
    #ar1 = [0,7,12,14,15,16,20,43]
    #ar2 = [1,2,3,6,8]
    ar1 = [1]
    ar2 = [2]
    solu = Solution()
    print solu.findMedianSortedArrays(ar1,ar2)