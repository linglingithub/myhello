__author__ = 'linglin'

class Solution:
    # @param nums, a list of integers
    # @return an integer
    def maxProduct(self, nums):
        if nums is None or len(nums)==0:
            return 0
        globalmax = nums[0]
        lmax = nums[0]
        lmin = nums[0]
        for a in nums[1:]:
            tmp_max = lmax
            tmp_min = lmin
            lmax = max(a,max(tmp_max*a,tmp_min*a))
            lmin = min(a,min(tmp_max*a,tmp_min*a))
            globalmax = max (lmax,globalmax)
        return globalmax



if __name__ == "__main__":
    mpser = Solution()
    nums1=[2,3,-1,-9,8]
    nums2=[2,-1,3,4]
    nums3=[3,4,-1,6]
    #print mpser.maxProduct(nums1)
    print mpser.maxProduct(nums2)
    print mpser.maxProduct(nums3)

"""
Maximum Product Subarray

Find the contiguous subarray within an array (containing at least one number) which
has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""

"""
p(n) = p(n-1) * a(n)  (if a(n-1) in p(n-1)
     or  a(n)
"""