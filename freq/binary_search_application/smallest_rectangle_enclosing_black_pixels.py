#coding=utf-8

import unittest

"""

600. Smallest Rectangle Enclosing Black Pixels 

 Description
 Notes
 Testcase
 Judge
An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels are 
connected, i.e., there is only one black region. Pixels are connected horizontally and vertically. Given the location 
(x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

Have you met this question in a real interview? Yes
Example
For example, given the following image:

[
  "0010",
  "0110",
  "0100"
]
and x = 0, y = 2,
Return 6.

Tags 
Binary Search Google

"""


class Solution:
    """
    @param: image: a binary matrix with '0' and '1'
    @param: x: the location of one of the black pixels
    @param: y: the location of one of the black pixels
    @return: an integer
    """

    def minArea(self, image, x, y):
        # write your code here
        if not image or not image[0]:
            return -1

        m, n = len(image), len(image[0])
        left = self.binary_search(0, y, True, True, image)
        right = self.binary_search(y, n - 1, True, False, image)  # should have -1 here, same for m
        top = self.binary_search(0, x, False, True, image)
        bottom = self.binary_search(x, m - 1, False, False, image)
        print(left, right, top, bottom)
        return (right - left + 1) * (bottom - top + 1)

    def binary_search(self, low, high, search_col, find_min, image):
        last = -1
        found = False
        while low < high:
            mid = low + int((high - low) / 2)
            found = False   # don't forget to reset here

            # if mid == last:
            #     # return mid  #wrong for case 2
            #     if find_min:
            #         return mid
            #     else:
            #         return high
            # last = mid
            if search_col:
                for i in range(len(image)):
                    if image[i][mid] == '1':  # should be str here
                        found = True
                        break
            else:
                for j in range(len(image[0])):
                    if image[mid][j] == '1':
                        found = True
                        break
            if found:
                if find_min:
                    high = mid
                else:
                    low = mid
                    if low == last:   # special case here, need to think all different cases carefully
                        #if and found in low+1:
                        found_in_high = False
                        if search_col:
                            for i in range(len(image)):
                                if image[i][low+1] == '1':  # should be str here
                                    found_in_high = True
                                    break
                        else:
                            for j in range(len(image[0])):
                                if image[low+1][j] == '1':
                                    found_in_high = True
                                    break
                        if found_in_high:
                            return low + 1
                        else:
                            return low    # don't forget this else
                last = mid
            else:
                if find_min:
                    low = mid + 1
                else:
                    high = mid - 1

        return low
        #return high if find_min else low


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [
          "0010",
          "0110",
          "0100"
        ]
        x, y = 0, 2
        answer = 6
        result = self.sol.minArea(nums, x, y)
        self.assertEqual(answer, result)


    def test_case2(self):   # ===>
        nums = [
            "1111111101",
            "1000000101",
            "1011110101",
            "1010010101",
            "1010110101",
            "1010000101",
            "1011111101",
            "1000000001",
            "1111111111"
        ]
        x, y = 4, 4
        answer = 90   # wrong out put as 72, (0, 8, 0, 7) , should be (0, 9, 0, 8)
        result = self.sol.minArea(nums, x, y)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
