#coding=utf-8
__author__ = 'linglin'

"""

84. Largest Rectangle in Histogram

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given heights = [2,1,5,6,2,3],
return 10.

Subscribe to see which companies asked this question

Hide Tags Array Stack
Hide Similar Problems (H) Maximal Rectangle

Hard

"""



import unittest


class Solution(object):

    def largestRectangleArea(self, heights):
        # write your code here
        if not heights:
            return 0
        result = 0
        stack = []
        n = len(heights)
        i = 0
        while i < n:
            if not stack or heights[i] > heights[stack[-1]]:  # should be >=, not <= here, careful!!, can not be =, case6
                stack.append(i)
                i += 1
            else:
                while True:  # need to have one pop at least, otherwise dead loop for case7
                    pos = stack.pop()
                    if stack:
                        # area = heights[pos] * (i-pos) # width not i-pos , case 8
                        area = heights[pos] * (i-1 - stack[-1])
                    else:
                        #area = heights[pos] * (pos+1)  # need to check if stack or not, otherwise wrong for case 5
                        area = heights[pos] * i # not pos, should be related to i, case 6, so far (0 to i) the lowest bar
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
                #area = heights[pos] * (n-pos) # not n-pos, should be n-1 - stack[-1] , case 6
                area = heights[pos] * (n - 1 - stack[-1])
            else:
                area = n * heights[pos]
            result = max(area, result)
        return result



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
                i += 1

            # If this bar is lower than top of stack, then calculate area of rectangle
            # with stack top as the smallest (or minimum height) bar.
            # 'i' is 'right index' for the top, and element before top in stack is 'left index'
            else:
                start = stack.pop()
                width = i if stack==[] else i - stack[-1] -1
                area = heights[start]*width
                result = max(result, area)

        # Now pop the remaining bars from stack and calculate area with every
        # popped bar as the smallest bar
        while stack:
            start = stack.pop()
            width = len(heights) if not stack else len(heights)-stack[-1]-1
            area = heights[start]*width
            result = max(result, area)
        return result



    def largestRectangleArea_tle(self, heights): #local about 35s for case2
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        result = 0
        for i in range(len(heights)):
            tmp = heights[i]
            left = right = i
            while left-1 >= 0 and tmp <= heights[left-1]:
                left -= 1
            while right+1 < len(heights) and tmp <= heights[right+1]:
                right += 1
            result = max(result, tmp*(right-left+1))
        return result




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):  # case8 ========>
        nums = [3,5,5,2,5,5,6,6,4,4,1,1,2,5,5,6,6,4,1,3]
        answer = 24
        result = self.sol.largestRectangleArea(nums)
        self.assertEqual(answer, result)


    def test_case70(self):  # case7 ========>
        nums = [0, 0]
        answer = 0
        result = self.sol.largestRectangleArea(nums)
        self.assertEqual(answer, result)


    def test_case60(self):  #========>
        nums = [5,5,1,7,1,1,5,2,7,6]
        answer = 12
        result = self.sol.largestRectangleArea(nums)
        self.assertEqual(answer, result)

    def test_case50(self):  #========>
        nums = [5,4,1,2]
        answer = 8
        result = self.sol.largestRectangleArea(nums)
        self.assertEqual(answer, result)

    def test_case40(self):  #========> line
        nums = [0,2,0]
        answer = 2
        result = self.sol.largestRectangleArea(nums)
        self.assertEqual(answer, result)


    def test_case20(self):
        nums = [5,5,1,1,2,3,1,1,1,1,1,5,5]
        answer = 13
        result = self.sol.largestRectangleArea(nums)
        self.assertEqual(answer, result)


    def test_case10(self):
        nums = [2,1,5,6,2,3]
        answer = 10
        result = self.sol.largestRectangleArea(nums)
        self.assertEqual(answer, result)


    def test_case30(self): #===> TLE
        from util.ini_file_util import IniFileUtil
        params = IniFileUtil.read_into_dict("largest_rectangle_in_histogram_case3.ini")
        nums = IniFileUtil.string_to_int_list(params.get("nums"))
        answer = 100000000
        result = self.sol.largestRectangleArea(nums)
        self.assertEqual(answer, result)



def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
