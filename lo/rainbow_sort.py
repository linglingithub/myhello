#coding=utf-8

import unittest

"""

Rainbow Sort
Given an array of balls, where the color of the balls can only be Red, Green or Blue, sort the balls such that all the 
Red balls are grouped on the left side, all the Green balls are grouped in the middle and all the Blue balls are grouped 
on the right side. (Red is denoted by -1, Green is denoted by 0, and Blue is denoted by 1).

Examples

{0} is sorted to {0}
{1, 0} is sorted to {0, 1}
{1, 0, 1, -1, 0} is sorted to {-1, 0, 0, 1, 1}
Assumptions

The input array is not null.
Corner Cases

What if the input array is of length zero? In this case, we should not do anything as well.

"""



class Solution(object):
    def rainbowSort(self, array):
      """
      array: int[]
      return: int[]
      """
      # write your solution here
      if not array:
        return []
      arr = array
      RED = -1
      GREEN = 0
      BLUE = 1
      i, j, k = 0, len(array) - 1, 0
      while k <= j:
        if arr[k] == RED:
          arr[i], arr[k] = arr[k], arr[i]
          i += 1
        elif arr[k] == GREEN:
          k += 1
        else:
          arr[j], arr[k] = arr[k], arr[j]
          j -= 1
      return arr


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [0]
        answer = [0]
        result = self.sol.rainbowSort(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [1, 0]
        answer = [0, 1]
        result = self.sol.rainbowSort(nums)
        self.assertEqual(answer, result)


    def test_case3(self):
        nums = [1, 0, 1, -1, 0]
        answer = [-1, 0, 0, 1, 1]
        result = self.sol.rainbowSort(nums)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
