"""
Selection Sort
Given an array of integers, sort the elements in the array in ascending order. The selection sort algorithm should be used to solve this problem.

Examples

{1} is sorted to {1}
{1, 2, 3} is sorted to {1, 2, 3}
{3, 2, 1} is sorted to {1, 2, 3}
{4, 2, -3, 6, 1} is sorted to {-3, 1, 2, 4, 6}
Corner Cases

What if the given array is null? In this case, we do not need to do anything.
What if the given array is of length zero? In this case, we do not need to do anything.
"""

class Solution(object):
    def solve(self, array):
      """
      array: int[]
      return: int[]
      """
      # write your solution here
      # check for None or 0-length case
      if not array:
        return []    # ===> should return [] instead of None
      # loop over 0 - (n - 1)
      for i in range(len(array)-1):
        # find the min value and its index for the remaining elements
        min_idx = i
        for j in range(i+1, len(array)):
          if array[j] < array[min_idx]:
            min_idx = j
        # swap
        array[i], array[min_idx] = array[min_idx], array[i]
      return array