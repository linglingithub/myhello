"""

53. Maximum Subarray

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.


More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach,
which is more subtle.

Subscribe to see which companies asked this question

Hide Tags Array Dynamic Programming Divide and Conquer
Hide Similar Problems (E) Best Time to Buy and Sell Stock (M) Maximum Product Subarray


Medium

"""


import unittest


class Solution(object):

    def maxSubArray(self, nums): # dp means subarry that ends at index i, O(1) space, O(n) time
        # write your code here
        if not nums:
            return 0
        dp = nums[0]
        result = dp
        for i in range(1, len(nums)):
            dp = max(dp,0) + nums[i]
            result = max(dp, result)
        return result


    def maxSubArray(self, nums): # dp means subarry that ends at index i, O(n) space, O(n) time
        # write your code here
        if not nums:
            return 0
        dp = [ x for x in nums]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1],0) + nums[i]
        return max(dp)


    def maxSubArray(self, nums): #59ms, 69.8%, simplified dp with O(1) space
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            #dp = max(dp + nums[i], nums[i]) # either this line or the following line
            dp = dp+nums[i] if nums[i]>0 else nums[i]
            result = max(result, dp)
        return result


    def maxSubArray_dp(self, nums): #65ms, 55.07%, dp[i] means the max sum of subarray that ends at i.
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) < 1:
            return 0
        dp = [0] * len(nums)
        dp[0] = max(0, nums[0])
        #result = dp[0]  #should be inited as dp[0], not 0 , otherwise wrong for case 2
        result = nums[0]  # should be nums[0], otherwise wrong for case3, look at the notes in case3
        for i in range(1, len(nums)):
            #dp[i] = max(dp[i-1]+nums[i], 0) # wrong for logic in case3
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            result = max(result, dp[i])
        return result



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        input = [-2,1,-3,4,-1,2,1,-5,4]
        answer = 6
        result = self.sol.maxSubArray(input)
        self.assertEqual(answer, result)

    def test_case2(self): #====>
        input = [1]
        answer = 1
        result = self.sol.maxSubArray(input)
        self.assertEqual(answer, result)

    def test_case3(self): #====>  this case means that you have to take a non-empty subarray, can't be empty,
        # which means if the array is all negative, you need to take all subarrays and find the maximum sum
        input = [-1]
        answer = -1
        result = self.sol.maxSubArray(input)
        self.assertEqual(answer, result)

    def test_case4(self): #====>
        input = [-2, -1]
        answer = -1
        result = self.sol.maxSubArray(input)
        self.assertEqual(answer, result)

    def test_case5(self):  # ====>
        input = [-1, -1]
        answer = -1
        result = self.sol.maxSubArray(input)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8


"""

Divide and conquer way -- not accepted , and O(nlogn) time -- todo

Step1. Select the middle element of the array.
So the maximum subarray may contain that middle element or not.

Step 2.1 If the maximum subarray does not contain the middle element, then we can apply the same algorithm to the the subarray to the left of the middle element and the subarray to the right of the middle element.

Step 2.2 If the maximum subarray does contain the middle element, then the result will be simply the maximum suffix subarray of the left subarray plus the maximum prefix subarray of the right subarray

Step 3 return the maximum of those three answer.

Here is a sample code for divide and conquer solution. Please try to understand the algorithm before look at the code

class Solution {
public:
    int maxSubArray(int A[], int n) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        if(n==0) return 0;
        return maxSubArrayHelperFunction(A,0,n-1);
    }

    int maxSubArrayHelperFunction(int A[], int left, int right) {
        if(right == left) return A[left];
        int middle = (left+right)/2;
        int leftans = maxSubArrayHelperFunction(A, left, middle);
        int rightans = maxSubArrayHelperFunction(A, middle+1, right);
        int leftmax = A[middle];
        int rightmax = A[middle+1];
        int temp = 0;
        for(int i=middle;i>=left;i--) {
            temp += A[i];
            if(temp > leftmax) leftmax = temp;
        }
        temp = 0;
        for(int i=middle+1;i<=right;i++) {
            temp += A[i];
            if(temp > rightmax) rightmax = temp;
        }
        return max(max(leftans, rightans),leftmax+rightmax);
    }
};

"""