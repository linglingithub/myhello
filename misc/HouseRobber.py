__author__ = 'linglin'

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if nums is None or len(nums) == 0:
            return 0
        max1 = nums[0]
        if len(nums) == 1:
            return max1
        max2 = nums[1]
        for i in range(2,len(nums)):
            maxn = max1 + nums[i]
            if max1 < max2:
                max1 = max2
            max2 = maxn

        return max(max1,max2)

if __name__ == '__main__':
    solu = Solution()
    house = [2,1,1,2]
    print solu.rob(house)