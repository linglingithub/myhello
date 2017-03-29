#coding=utf-8

import unittest

"""
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it
is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue
section) are being trapped. Thanks Marcos for contributing this image!

Subscribe to see which companies asked this question.

Hide Tags Array Stack Two Pointers
Hide Similar Problems (M) Container With Most Water (M) Product of Array Except Self (H) Trapping Rain Water II

Hard

"""



class Solution(object):
    def trap(self, height):  # stack, O(N)， #69ms, 24%
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height)<3:
            return 0
        stack = [0] # should remember it's the index of height , not the height[0]
        n = len(height)
        result = 0
        for i in range(1,n):
            if not stack:
                stack.append(i)
                continue
            if height[i] <= height[stack[-1]]:
                stack.append(i)
            else:
                bottom = height[stack.pop()]
                while stack and height[stack[-1]]<=height[i]:
                    left = stack.pop()
                    #result += (height[left] - bottom)*(i - left) # should add -1 here , otherwise wrong
                    result += (height[left] - bottom) * (i - left - 1)
                    bottom = height[left]
                if stack and height[stack[-1]] > height[i]: #need to add cases when new height is smaller than left, case2
                    left = stack[-1]
                    result += (height[i]-bottom) * (i-left-1)
                stack.append(i)

        return result






    def trap2(self, height):  #two pointers, O(N)， #69ms, 32%
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        result = 0
        n = len(height)
        lefts = [0 for _ in range(n)]
        rights = [0 for _ in range(n)]
        left = 0
        for i in range(n):
            lefts[i] = left
            left = max(left, height[i])
        right = 0
        for i in range(n-1, 0, -1):
            rights[i] = right
            right = max(right, height[i])
            # calc the hight here
            h = min(lefts[i], rights[i])
            result += max(h-height[i], 0)
        return result

    def trap1(self, height):  #two pointers, O(N)， #85ms, 17%
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        result = 0
        n = len(height)
        lefts = [0 for _ in range(n)]
        rights = [0 for _ in range(n)]
        left = 0
        for i in range(n):
            lefts[i] = left
            left = max(left, height[i])
        right = 0
        for i in range(n-1, 0, -1):
            rights[i] = right
            right = max(right, height[i])
        for i in range(n):
            h = min(lefts[i], rights[i])
            result += max(h-height[i], 0)
        return result



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [0,1,0,2,1,0,1,3,2,1,2,1]
        answer = 6
        result = self.sol.trap(nums)
        self.assertEqual(answer, result)

    def test_case2(self): #===> wrong for stack way, list index out of range
        nums = [4,2,3]
        answer = 1
        result = self.sol.trap(nums)
        self.assertEqual(answer, result)



def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()


"""

This problem is similar to Candy. It can be solve by scanning from both sides and then get the total. ???

===========================

http://bangbingsyb.blogspot.com/2014/11/leetcode-trapping-rain-water.html

思路1：stack解法

能积水的地方必然是一个中间低两边高的凹陷。所以寻找的目标是一个递减序列之后的递增。由于积水量只有在递增时才能计算，而计算又可能需要用到递减序
列中的多个bar。因此必须将递减序列cache起来。这里使用stack。为了便于面积计算中宽度的计算，stack存放的不是递减序列bar的高度，而是每个bar的
坐标。


class Solution {
public:
    int trap(int A[], int n) {
        if(n<3) return 0;
        stack<int> s;
        s.push(0);
        int water = 0;

        for(int i=1; i<n; i++) {
            if(A[i]>A[s.top()]) {
                int bottom = A[s.top()];
                s.pop();
                while(!s.empty() && A[i]>=A[s.top()]) {
                    water += (A[s.top()]-bottom)*(i-s.top()-1);
                    bottom = A[s.top()];
                    s.pop();
                }
                if(!s.empty()) water += (A[i]-bottom)*(i-s.top()-1);
            }
            s.push(i);
        }

        return water;
    }
};

思路2：two pointers解法

对任意位置i，在i上的积水，由左右两边最高的bar：A[left] = max{A[j], j<i}, A[right] = max{A[j], j>i}决定。定义Hmin = min(A[left],
 A[right])，则积水量Si为：

Hmin <= A[i]时，Si = 0
Hmin > A[i]时，Si = Hmin - A[i]


class Solution {
public:
    int trap(int A[], int n) {
        if(n<3) return 0;
        vector<int> leftHeight(n,0);
        vector<int> rightHeight(n,0);
        int water = 0;

        for(int i=1; i<n; i++)
            leftHeight[i] = max(leftHeight[i-1], A[i-1]);

        for(int i=n-2; i>=0; i--) {
            rightHeight[i] = max(rightHeight[i+1], A[i+1]);
            int minHeight = min(leftHeight[i], rightHeight[i]);
            if(minHeight>A[i]) water += (minHeight - A[i]);
        }

        return water;
    }
};


====================

[解题思路]
对于任何一个坐标，检查其左右的最大坐标，然后相减就是容积。所以，
1. 从左往右扫描一遍，对于每一个坐标，求取左边最大值。
2. 从右往左扫描一遍，对于每一个坐标，求最大右值。
3. 再扫描一遍，求取容积并加和。
#2和#3可以合并成一个循环，

http://fisherlei.blogspot.com/2013/01/leetcode-trapping-rain-water.html


"""

#-*- coding:utf-8 -*-
