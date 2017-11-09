#coding=utf-8

import unittest

"""
Input:
2d grid, with some numbers and blank space, to solve it, fill the blank places with . or #
'.': water
'#': island

constraits:
no 2*2 blocks of water
no other characters in the grid (only ., #, number), no space left
all water is connected ( up-down-left-right, not diagonally)
each connected group of islands contains exactly one number square


the problem is not to solve, but to check if the input is a valid solve.


Output:
True or False ( if the puzzle is valid )

"""



class Solution(object):
    def searchInsert(self, nums):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or not nums[0]:
            return 0
        clusters = [i for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i][j] == 0:
                    continue
                self.update_cluster(i, j, nums, clusters)
        return len(set(clusters))

    def update_cluster(self, x, y, nums, clusters):
        xcluster = self.find_cluster(clusters, x)
        ycluster = self.find_cluster(clusters, y)
        if xcluster != ycluster:
            # clusters[xcluster] = ycluster
            # this is important!!!, otherswise wrong for case 1
            # if the old way, need to refresh the clusters again,
            # because y is bigger than x, the newly connected one will overwrite the old one with a different id
            # so best way is to update the new one with old cluster id
            clusters[ycluster] = xcluster

    def find_cluster(self, clusters, x):
        if x != clusters[x]:
            clusters[x] = self.find_cluster(clusters, clusters[x])
        return clusters[x]




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [
            [1,1,0,0],
            [1,1,1,0],
            [0,1,1,0],
            [0,0,0,1],
        ]
        answer = 2
        result = self.sol.searchInsert(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [
            [1,0,0,0],
            [0,1,0,0],
            [0,0,1,0],
            [0,0,0,1],
        ]
        answer = 4
        result = self.sol.searchInsert(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
