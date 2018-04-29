#coding=utf-8
"""
78. Subsets

Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
Subscribe to see which companies asked this question

Hide Tags Array Backtracking Bit Manipulation
Hide Similar Problems (M) Generalized Abbreviation

Medium

"""

import unittest


class Solution:
    def subsets(self, nums):
        """Return the subsets with given array nums
        :type nums: List[int]
        :rtype: List[List[int]]

        [] or None => []
        [1,2] => [[], [1], [2], [1, 2]]

        Assumptions: no duplicates in nums
        """
        result = []
        if not nums:
            return result
        self.helper(nums, 0, [], result)
        return result

    def helper(self, nums, idx, cur, result):
        if idx == len(nums):
            result.append(cur)
            return  # !!!!! so important, don't forget
        self.helper(nums, idx + 1, cur, result)
        self.helper(nums, idx + 1, cur + [nums[idx]], result)


class Solution1(object):
    def subsets(self, S): # recursive way
        # write your code here
        if not S:
            return [[]]  # or [[]]?? to discuss
        S.sort()
        result = []
        self.subset_helper(S, 0, [], result)
        return result

    def subset_helper(self, S, idx, path, result):
        if idx == len(S):
            result.append(path)
            return
        self.subset_helper(S, idx + 1, path, result)
        self.subset_helper(S, idx + 1, path + [S[idx]], result)  # should be + [S[idx]], not + S[idx]


    def subsets2(self, S):  # mask way
        # write your code here
        if not S:
            return [[]]  # or [[]]?? to discuss
        S.sort()
        result = [[]]
        n = len(S)
        mask_num = 2 ** n
        pattern = "{0:0" + str(n) + "b}"
        for i in range(1, mask_num):
            mask = pattern.format(i)
            tmp = []
            for j in range(len(mask)):
                char = mask[j]
                if char == "1":
                    tmp.append(S[j])
            result.append(tmp)
        return result

    def subsets1(self, S):  # by inserting new elements into possible
        # write your code here
        if not S:
            return [[]]  # or [[]]?? to discuss
        S.sort()
        result = [[]]
        for i in range(len(S)):
            n = len(result)
            for j in range(n):
                tmp = result[j]
                print tmp + [S[i]]
                result.append(tmp + [S[i]])
        return result


class Solution1(object):
    def subsets_self(self, nums): #52ms, 75%, using bit as mask
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) == 0:
            return []
        result = []
        x = 2 ** len(nums)
        strformat = "{0:0"+str(len(nums))+"b}"
        for i in range(x):
            mask = strformat.format(i)
            tmp = []
            for idx in range(len(nums)):
                if mask[idx]=="1":
                    tmp.append(nums[idx])
            result.append(tmp)
        return result


    def subsets_ref_dfs(self, nums): #49ms, 81%
        """

        :type nums: List[int]
        :rtype: List[List[int]]

        [1, 2, 3]
        [1, 2]
        [1, 3]
        [1]
        [2, 3]
        [2]
        [3]
        []

        if swap the order of two recursive calls of search, output will be following. which is the same as bit-mask way:

        []
        [3]
        [2]
        [2, 3]
        [1]
        [1, 3]
        [1, 2]
        [1, 2, 3]

        """
        self.results = []
        self.search(sorted(nums), [], 0)
        return self.results

    def search(self, nums, S, index):
        if index == len(nums):
            print S
            self.results.append(S)
            return

        self.search(nums, S + [nums[index]], index + 1)
        self.search(nums, S, index + 1)




    def subsets_ref2_dfs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        方法1：backtracking
        与combination/combination sum I, II思路一样。区别在于单层扫描时不用跳过重复数字，而在进入下一层递归前就需要把当前subset
        压入结集中。

        []
        [1]
        [1, 2]
        [1, 2, 3]
        [1, 3]
        [2]
        [2, 3]
        [3]


        """

        def dfs(depth, start, valuelist):
            res.append(valuelist)
            print valuelist
            if depth == len(nums): return
            for i in range(start, len(nums)):
                dfs(depth + 1, i + 1, valuelist + [nums[i]])

        nums.sort()
        res = []
        dfs(0, 0, [])
        return res


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,2,3]
        answer = [
          [3],
          [1],
          [2],
          [1,2,3],
          [1,3],
          [2,3],
          [1,2],
          []
        ]
        result = self.sol.subsets(nums)
        answer.sort()
        result.sort()
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""
方法2：添加数字构建subset

起始subset集为：[]
添加S0后为：[], [S0]
添加S1后为：[], [S0], [S1], [S0, S1]
添加S2后为：[], [S0], [S1], [S0, S1], [S2], [S0, S2], [S1, S2], [S0, S1, S2]
红色subset为每次新增的。显然规律为添加Si后，新增的subset为克隆现有的所有subset，并在它们后面都加上Si。


方法3：bit manipulation

由于S[0: n-1]组成的每一个subset，可以看成是对是否包含S[i]的取舍。S[i]只有两种状态，包含在特定subset内，或不包含。所以subset的数量总
共有2^n个。所以可以用0~2^n-1的二进制来表示一个subset。二进制中每个0/1表示该位置的S[i]是否包括在当前subset中。

"""



#-*- coding:utf-8 -*-
