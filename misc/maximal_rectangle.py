#coding=utf-8

"""

85. Maximal Rectangle

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 6.
Subscribe to see which companies asked this question.

Hide Tags Array Hash Table Stack Dynamic Programming
Hide Similar Problems (H) Largest Rectangle in Histogram (M) Maximal Square

Hard

"""

import unittest


class Solution(object):
    # @param {boolean[][]} matrix, a list of lists of boolean
    # @return {int} an integer
    def maximalRectangle(self, matrix):
        # Write your code here
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        heights = [[1 if matrix[i][j] else 0 for j in range(n)] for i in range(m)]
        result = 0
        for i in range(1, m):
            for j in range(n):
                heights[i][j] = heights[i - 1][j] + 1 if matrix[i][j] else 0
        for i in range(m):
            area = self.largestRectangleArea(heights[i])
            result = max(result, area)
        return result

    def largestRectangleArea(self, heights):
        # write your code here
        if not heights:
            return 0
        result = 0
        stack = []
        n = len(heights)
        i = 0
        while i < n:
            if not stack or heights[i] > heights[
                stack[-1]]:  # should be >=, not <= here, careful!!, can not be =, case6
                stack.append(i)
                i += 1
            else:
                while True:  # need to have one pop at least, otherwise dead loop for case7
                    pos = stack.pop()
                    if stack:
                        area = heights[pos] * (i - 1 - stack[-1])
                    else:
                        # area = heights[pos] * (pos+1)  # need to check if stack or not, otherwise wrong for case 5
                        area = heights[
                                   pos] * i  # not pos, should be related to i, case 6, so far (0 to i) the lowest bar
                    result = max(result, area)
                    if not (stack and heights[stack[-1]] > heights[i]):
                        break

                        # while stack and heights[stack[-1]] > heights[i]:
                        #     pos = stack.pop()
                        #     if stack:
                        #         area = heights[pos] * (i-pos)
                        #     else:
                        #         #area = heights[pos] * (pos+1)  # need to check if stack or not, otherwise wrong for case 5
                        #         area = heights[pos] * i # not pos, should be related to i, case 6, so far (0 to i) the lowest bar
                        #     result = max(result, area)
        while stack:
            pos = stack.pop()
            if stack:
                area = heights[pos] * (n - 1 - stack[-1])
            else:
                area = n * heights[pos]
            result = max(area, result)
        return result









    def maximalRectangle_ref(self, matrix): #ref, 185ms, 33%
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])

        height = [ [0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0: # in leetcode, need to use '0'
                    height[i][j] = 0
                else:
                    height[i][j] = 1 if i == 0 else height[i - 1][j] + 1

        maxArea = 0
        for i in range(m):
            maxArea = max(maxArea, self.largestRectangleArea1(height[i]))
        return maxArea

    def largestRectangleArea1(self, heights): # ref, 86ms, 59%
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        result = 0
        stack = []
        i = 0
        while i < len(heights):
            # If this bar is higher than the bar on top stack, push it to stack
            if stack==[] or heights[stack[-1]]<heights[i]:
                stack.append(i)


            # If this bar is lower than top of stack, then calculate area of rectangle
            # with stack top as the smallest (or minimum height) bar.
            # 'i' is 'right index' for the top, and element before top in stack is 'left index'
            else:
                start = stack.pop()
                width = i if stack==[] else i - stack[-1] -1
                result = max(result, heights[start]*width)
                i -= 1
            i += 1

        # Now pop the remaining bars from stack and calculate area with every
        # popped bar as the smallest bar
        while stack:
            start = stack.pop()
            width = i if not stack else len(heights)-stack[-1]-1
            result = max(result, heights[start]*width)

        return result


    def largestRectangleArea_ref_wrong(self, heights):
        if not heights:
            return 0
        s = []
        result = 0
        i = 0
        while i < len(heights):
            if not s or heights[i] > heights[s[-1]]:
                s.append(i)
                i += 1
            else:
                t = s.pop()
                result = max(result, heights[t] * ( i if not s else i - s[-1] - 1))

        return result




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [
            [1, 0, 1, 0, 0],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 0, 0, 1, 0]
        ]
        answer = 6
        result = self.sol.maximalRectangle(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""

这题是一道难度很大的题目，至少我刚开始的时候完全不知道怎么做，也是google了才知道的。

这题要求在一个矩阵里面求出全部包含1的最大矩形面积，譬如这个：

    0 0 0 0
    1 1 1 1
    1 1 1 0
    0 1 0 0
我们可以知道，最大的矩形面积为6。也就是下图中虚线包围的区域。那么我们如何得到这个区域呢？

    0  0  0  0
   |--------|
   |1  1  1 |1
   |1  1  1 |0
   |--------|
    0  1  0  0
对于上面哪一题，我们先去掉最下面的一行，然后就可以发现，它可以转化成一个直方图，数据为[2, 2, 2, 0]，我们认为1就是高度，如果碰到0，譬如上面最右列，则高度为0，而计算这个直方图最大矩形面积就很容易了，我们已经在Largest Rectangle in Histogram处理了。

所以我们可以首先得到每一行的直方图，分别求出改直方图的最大区域，最后就能得到结果了。

代码如下：

class Solution {
public:
    int maximalRectangle(vector<vector<char> > &matrix) {
        if(matrix.empty() || matrix[0].empty()) {
            return 0;
        }

        int m = matrix.size();
        int n = matrix[0].size();

        vector<vector<int> > height(m, vector<int>(n, 0));
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(matrix[i][j] == '0') {
                    height[i][j] = 0;
                } else {
                    height[i][j] = (i == 0) ? 1 : height[i - 1][j] + 1;
                }
            }
        }

        int maxArea = 0;
        for(int i = 0; i < m; i++) {
            maxArea = max(maxArea, largestRectangleArea(height[i]));
        }
        return maxArea;
    }

    int largestRectangleArea(vector<int> &height) {
        vector<int> s;
        height.push_back(0);

        int sum = 0;
        int i = 0;
        while(i < height.size()) {
            if(s.empty() || height[i] > height[s.back()]) {
                s.push_back(i);
                i++;
            } else {
                int t = s.back();
                s.pop_back();
                sum = max(sum, height[t] * (s.empty() ? i : i - s.back() - 1));
            }
        }

        return sum;
    }
};

"""

#-*- coding:utf-8 -*-
