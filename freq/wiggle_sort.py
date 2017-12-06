#coding=utf-8

import unittest

"""

locked

280. Wiggle Sort

Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].


"""



class Solution(object):
    def wiggleSort(self, nums):
        """
        For the sort and swap way, easy to understand, use O(nlogn) time.
        For the linear way, try to go through one example then it's obvious that the swap won't affect previous wiggle 
        shape of the nums.
        :param nums: 
        :return: 
        """
        if not nums:
            return None
        for i in range(1, len(nums)):
            if i%2==1 and nums[i]<nums[i-1] or i%2==0 and nums[i]>nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
        return nums





class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1, 5, 1, 1, 6, 4]
        answer = [1,5,1,6,1,4]  # may have other valid output
        result = self.sol.wiggleSort(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [1, 3, 2, 2, 3, 1]
        answer = [1, 3, 2, 3, 1, 2]  # may have other valid output
        result = self.sol.wiggleSort(nums)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""

https://segmentfault.com/a/1190000003783283

排序法

复杂度
时间 O(NlogN) 空间 O(1)

思路
根据题目的定义，摇摆排序的方法将会很多种。我们可以先将数组排序，这时候从第3个元素开始，将第3个元素和第2个元素交换。然后再从第5个元素开始，
将第5个元素和第4个元素交换，以此类推。就能满足题目要求。

public class Solution {
    public void wiggleSort(int[] nums) {
        // 先将数组排序
        Arrays.sort(nums);
        // 将数组中一对一对交换
        for(int i = 2; i < nums.length; i+=2){
            int tmp = nums[i-1];
            nums[i-1] = nums[i];
            nums[i] = tmp;
        }
    }
}


交换法

复杂度
时间 O(N) 空间 O(1)

思路
题目对摇摆排序的定义有两部分：

如果i是奇数，nums[i] >= nums[i - 1]
如果i是偶数，nums[i] <= nums[i - 1]
所以我们只要遍历一遍数组，把不符合的情况交换一下就行了。具体来说，如果nums[i] > nums[i - 1]， 则交换以后肯定有nums[i] <= nums[i - 1]。

public class Solution {
    public void wiggleSort(int[] nums) {
        for(int i = 1; i < nums.length; i++){
            // 需要交换的情况：奇数时nums[i] < nums[i - 1]或偶数时nums[i] > nums[i - 1]
            if((i % 2 == 1 && nums[i] < nums[i-1]) || (i % 2 == 0 && nums[i] > nums[i-1])){
                int tmp = nums[i-1];
                nums[i-1] = nums[i];
                nums[i] = tmp;
            }
        }
    }
}



"""

#-*- coding:utf-8 -*-
