#coding=utf-8

import unittest

"""

384. Shuffle an Array
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();


Medium

"""

import copy
import random

class Solution(object):
    def __init__(self, nums):  # 21+% --> hide __bak, add __n, ~34%
        """
        :type nums: List[int]
        """
        self.__bak = nums  # a good habit to hide the bak
        self.__n = len(self.__bak)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.__bak


    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        res = self.__bak[:]

        for i in range(self.__n):
            idx = random.randint(0, self.__n-1)
            res[i], res[idx] = res[idx], res[i]
        return res  # don't forget this

class Solution_slow(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.bak = nums
        self.nums = copy.deepcopy(self.bak)


    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.nums = copy.deepcopy(self.bak)
        return self.nums


    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in range(len(self.bak)):
            idx = random.randint(0, len(self.bak)-1)
            self.nums[i], self.nums[idx] = self.nums[idx], self.nums[i]
        return self.nums   # don't forget this


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = 1
        answer = 1
        result = self.sol.searchInsert(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""

这道题让我们给数组洗牌，也就是随机打乱顺序，那么由于之前那道题Linked List Random Node我们接触到了水塘抽样的思想，这道题实际上这道题也是
用类似的思路，我们遍历数组每个位置，每次都随机生成一个坐标位置，然后交换当前遍历位置和随机生成的坐标位置的数字，这样如果数组有n个数字，那么
我们也随机交换了n组位置，从而达到了洗牌的目的，


=======================

Python hack
Just for fun.

class Solution(object):   # 51% performance
    def __init__(self, nums):
        self.reset = lambda: nums
        self.shuffle = lambda: random.sample(nums, len(nums))
        
        

"""

#-*- coding:utf-8 -*-
