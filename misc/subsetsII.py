#coding=utf-8

"""
90. Subsets II

Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
Subscribe to see which companies asked this question

Hide Tags Array Backtracking

Medium

"""

import unittest


class Solution:
    def subsetsWithDup_wrong(self, nums):
        """Return subsets of nums, which might have duplicates in it.
        :type nums: List[int]
        :rtype: List[List[int]]

        [1, 2, 2],
        1. sort the nums to make same elements consecutive.
        2. do regular subset, but try to skip the ele that is repated value if it's ???.

        2,2,2
        1,1,1
        1,1,0
        1,0,0
        0,0,0


        1, 1, 1
        1, 1, 0
        1, 0, 1 --->
        1, 0, 0
        0, 1, 1 --
        0, 1, 0 --
        0, 0, 1 --
        0, 0, 0

        """
        if not nums:
            return []
        result = []
        self.helper(nums, 0, [], result)
        return result

    def helper(self, nums, idx, cur, result):
        if idx == len(nums):
            result.append(cur)
            return
        # check if it's repeated value with previous one
        if idx == 0 or nums[idx] != nums[idx - 1]:
            self.helper(nums, idx + 1, cur + [nums[idx]], result)
            self.helper(nums, idx + 1, cur, result)  # !!! does not take current one
        else:
            # repeated with previous one
            #  --> !!! here idx is already the 2nd element of repeated values, if trying to look forward, then the if
            # should do look forward way
            # process untill end or find the next non-repeating value
            end = idx
            while end + 1 < len(nums) and nums[end + 1] == nums[end]:
                end += 1
            for i in range(idx, end + 1):
                self.helper(nums, end + 1, cur + nums[idx: i + 1], result)
            self.helper(nums, end + 1, cur, result)  # !!! does not take any repeated one


class Solution1:
    """
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, S):
        if not S:
            return []
        result = []
        S.sort()
        self.dfs_subset(0, 0, [], result, S)
        return result

    def dfs_subset(self, depth, idx, path, result, nums):
        result.append(path)
        if depth == len(nums):
            return
        for i in range(idx, len(nums)):
            if i>idx and nums[i] == nums[i-1]:
                continue
            self.dfs_subset(depth+1, i+1, path+[nums[i]], result, nums)




    def subsetsWithDup_w(self, S):
        if not S:
            return []
        result = []
        self.dfs_subset_w(0, [], result, S)
        return result

    def dfs_subset_w(self, idx, path, result, nums):
        result.append(path)
        if idx == len(nums):
            return
        for i in range(idx, len(nums)):
            if i>idx and nums[i] == nums[i-1]:
                continue
            self.dfs_subset_w(idx+1, path+[nums[i]], result, nums)


    def subsetsWithDup_wrong1(self, S): # wrong output as [[1],[1,1]] for case 01
        # write your code here
        if S is None:
            return []
        if not S:
            return [[]]
        result = []
        S.sort()
        self.helper(S, 0, [], result)
        return result

    def helper_wrong1(self, S, idx, vals, result):
        if idx >= len(S):
            result.append(vals)
            return
        cur = S[idx]
        if idx > 0 and S[idx] == S[idx - 1]:
            self.helper(S, idx + 1, vals + [S[idx]], result)
        else:
            self.helper(S, idx + 1, vals, result)
            self.helper(S, idx + 1, vals + [S[idx]], result)

    def subsetsWithDup_wrong(self, S): # case01, wrong output as [[], [1]]
        # write your code here
        if S is None:
            return []
        if not S:
            return [[]]
        result = []
        S.sort()
        self.helper_wrong(S, 0, [], result)
        return result

    def helper_wrong(self, S, idx, vals, result):
        if idx >= len(S):
            result.append(vals)  # don't forget this one!!!
            return
        cur = S[idx]
        self.helper(S, idx + 1, vals, result)
        if vals + [cur] not in result:
            self.helper(S, idx + 1, vals + [cur], result)


class Solution1(object):
    def subsetsWithDup_wrongtest_trytoremovelength(self, nums):
        def dfs(start, subset):
            res.append(subset)
            print subset, start
            if len(nums) == len(nums):
                return
            for i in range(start, len(nums)):
                if i>start and nums[i]==nums[i-1]:
                    print "---- skip: ", subset, nums[i], start, i
                    continue
                dfs( i+1, subset+[nums[i]]) # should be i+1 here, not i

        nums.sort()
        res = []
        dfs( 0, [])
        return res

    def subsetsWithDup(self, nums): #116ms, 5%; 49ms, 97%; 92ms, 18%; 69ms, 61%
        """
        output for case1 like following:
        []
        [1]
        [1, 2]
        [1, 2, 2]
        ---- skip:  [1] 2
        [2]
        [2, 2]
        ---- skip:  [] 2
        ====== final result: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]

        :param S:
        :return:
        """
        def dfs(depth, start, subset):
            res.append(subset)
            print "adding: ", subset, depth, start
            if depth == len(nums):
                print "<<<<"
                return
            for i in range(start, len(nums)):
                if i>start and nums[i]==nums[i-1]:
                    print "---- skip: ", subset, nums[i], depth, start, i
                    continue
                dfs(depth+1, i+1, subset+[nums[i]]) # should be i+1 here, not i

        nums.sort()
        print "================ input: ", nums
        res = []
        dfs(0, 0, [])
        return res



    def subsetsWithDup_self_lettertree_imrove(self, nums): # 10% ~ 70% , add pruning and remove dupli check, 82ms, 32% 58ms, 88%, 56ms, 89%
        def dfs(res, current, idx):
            if idx == len(nums):
                #current.sort()  # no need to sort here
                #if current not in res:  # remove the dupli check
                #    res.append(current)
                res.append(current)
                return
            if not(idx>0 and len(current)>0 and nums[idx]==current[-1]): # add pruning
                dfs(res, current, idx + 1)
            dfs(res, current + [nums[idx]], idx + 1)

        if nums is None or len(nums) == 0:
            return []
        result = []
        nums.sort()
        dfs(result, [], 0)
        return result


    def subsetsWithDup_self_lettertree(self, nums): #92ms, 18%, 72ms, 53%
        """
        Adding to result in the order of following for case1:
        [], [2], [2] -- dup and no, [2,2], [1], [1,2], [1,2] -- dup and no, [1,2,2] .
        In the following letter tree, left branch means not taking the letter, right branch means taking the letter.

                                       []
                              /                   \               --- for 1st letter, 1
                            []                   [1]
                           /  \             /         \           --- for 2nd letter, 2
                        []    [2]         [1]        [1,2]
                       / \    / \         /  \        / \         --- for 3nd letter, 3
                    []  [2] [2] [2,2]  [1] [1,2]  [1,2]  [1,2,2]

        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) == 0:
            return []
        result = []
        nums.sort()
        self.dfs(result, nums, [], 0)
        return result

    def dfs(self, res, nums, current, idx):
        if idx == len(nums):
            current.sort()
            if current not in res:
                res.append(current)
            return
        self.dfs(res,nums,current,idx+1)
        self.dfs(res, nums, current + [nums[idx]], idx + 1)



    def subsetsWithDup_ref(self, S):  #72ms, 53%
        """
        解题思路：和上一道题一样，求一个集合的所有子集。和上一道题不一样的一点是集合可能有重复元素。这道题同样使用dfs来解题，
        只是需要在dfs函数里加一个剪枝的条件，排除掉同样的子集
        :param S:
        :return:
        """
        def dfs(depth, start, valuelist):
            if valuelist not in res:
                res.append(valuelist)
            if depth == len(S):
                return
            for i in range(start, len(S)):
                dfs(depth+1, i+1, valuelist+[S[i]])
        S.sort()
        res = []
        dfs(0, 0, [])
        return res


    def subsetsWithDup_wrong(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) == 0:
            return []
        result = []
        nums.sort()
        self.dfsw(result, nums, [], 0)
        return result

    def dfsw(self, res, nums, current, idx):
        if idx == len(nums):
            res.append(current)
            return
        if idx==0 or (idx>0 and nums[idx] != nums[idx-1]):
            self.dfsw(res,nums,current,idx+1)
        self.dfsw(res, nums, current + [nums[idx]], idx + 1)

    def subsetsWithDup_ref2(self, S): #76ms, 45%
        # write your code here
        S.sort()
        p = [[S[x] for x in range(len(S)) if i >> x & 1] for i in range(2 ** len(S))]
        func = lambda x, y: x if y in x else x + [y]
        p = reduce(func, [[], ] + p)
        return list(reversed(p))


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case01(self):
        nums = [1,1]
        answer = [[],[1],[1,1]]
        result = self.sol.subsetsWithDup(nums)
        print "====== final result:", result
        answer.sort()
        result.sort()
        self.assertEqual(answer, result)


    def test_case1(self):
        nums = [1,2,2]
        answer = [
          [2],
          [1],
          [1,2,2],
          [2,2],
          [1,2],
          []
        ]
        result = self.sol.subsetsWithDup(nums)
        print "====== final result:", result
        answer.sort()
        result.sort()
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [1, 2, 2, 3]
        answer = [
            [],[3],[2],[2,3],[2,2],[2,2,3],[1],[1,3],[1,2],[1,2,3],[1,2,2],[1,2,2,3]
        ]
        result = self.sol.subsetsWithDup(nums)
        print "====== final result:", result
        answer.sort()
        result.sort()
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
