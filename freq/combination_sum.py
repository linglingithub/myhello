"""

Combination Sum

Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate

numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]
Subscribe to see which companies asked this question

Hide Tags Array Backtracking
Hide Similar Problems (M) Letter Combinations of a Phone Number (M) Combination Sum II (M) Combinations
(M) Combination Sum III (M) Factor Combinations (M) Combination Sum IV

"""


import unittest


class Solution(object):
    def combinationSum_ref(self, candidates, target): # won't pass case2 (case by self), but AC online
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            self.dfs(nums, target - nums[i], i, path + [nums[i]], res)

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates or target <= 0:
            return []
        res = []
        candidates = list(set(candidates))
        candidates.sort()
        self.helper(candidates, target, 0, [], res)
        return res

    def helper(self, nums, target, idx, combi, res):
        if target == 0:
            res.append(combi)
            return
        if idx >= len(nums) or nums[idx] > target:
            return
        for i in range(idx, len(nums)):
            val = nums[i]
            if val > target:
                break
            k = 1
            while k * val <= target:
                remain = target - k * val
                # if remain <= val:
                    # # k += 1   # wrong if put remain <= val then continue, remain can be 0, just check == case to remove duplicates
                    # # continue  # avoid duplicates like (2,2)
                    # break
                self.helper(nums, remain, i + 1, combi + [val] * k, res)  # should be i+1, not idx+1
                k += 1

class Solution_wrong(object):
    def combinationSum(self, candidates, target):
        """
        should not use dp trying to break down target, hard to remove duplicated combis
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates or target <= 0:
            return []
        combis = {}
        m = len(candidates)
        dp = [False for _ in range(target + 1)]
        dp[0] = True
        combis[0] = [[]]
        for i in range(m):
            for j in range(target):
                val = candidates[i]
                if val > j:
                    continue
                k = 1
                while k * val <= j:
                    if dp[j - k * val]:  # can have duplicates here, eg, 1*2 + 4, 2*2 + 2, 3*2; same for 2+5, 3+4
                        dp[j] = True
                        self.update_combi(combis, j, j - k * val, [val] * k)
                    k += 1
        return combis[target] if combis[target] else []

    def update_combi(self, combis, target, smaller, numlist):
        if not combis.get(target):
            combis[target] = []
        for small_list in combis[smaller]:
            copylist = [x for x in small_list]
            copylist.extend(numlist)
            combis[target].append(copylist)


class Solution1(object):
    def combinationSum(self, candidates, target): #109ms, 77.13%, pass more parameters than _slower,
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if candidates is None or len(candidates) == 0:
            return []
        result = []
        candidates = list(set(candidates)) #important, if the problem does not assume that the candiates are unique,
        # this is to guarantee there is no duplicate combi.
        candidates.sort() # important

        for i in range(len(candidates)):
            combi = self.dfs(result, candidates, [candidates[i]], i, target-candidates[i])
        return result #run time error if do "list(set(result))"

    def dfs(self, result, candidates, combi, idx, target):
        if target == 0:
            result.append(combi)
        for i in range(idx, len(candidates)):
            num = candidates[i]
            if target - num >= 0:
                self.dfs(result, candidates, combi + [num], i, target - num)


    def combinationSum_slower(self, candidates, target): #212ms, 21.55%
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if candidates is None or len(candidates) == 0:
            return []
        Solution.result = [] # make it class level, to save one parameter passing
        candidates = list(set(candidates)) #important
        candidates.sort() # important
        Solution.nums = candidates

        for i in range(len(candidates)):
            num = Solution.nums[i]
            combi = self.generateCombination([num], i, target-num)
        return Solution.result #run time error if do "list(set(result))"

    def generateCombination(self, combi, idx, target):
        if target == 0:
            Solution.result.append(combi)
        for i in range(idx, len(Solution.nums)):
            num = Solution.nums[i]
            if target - num >= 0:
                self.generateCombination(combi + [num], i, target - num)


    def generateCombination_wrong4repeatedanswer(self, res, combi, nums, target):
        """
        wrong answer as "[[2, 2, 3], [2, 3, 2], [3, 2, 2], [7]]" for case1
        :param res:
        :param combi:
        :param nums:
        :param target:
        :return:
        """
        if target == 0:
            res.append(combi)
        for num in nums:
            if target - num >= 0:
                self.generateCombination(res, combi + [num], nums, target - num)

    def combinationSum_ref(self, candidates, target): #99ms, 86.96%
        """
        It is accpeted online.
        But this one is not correct if the candidates contain duplicate integers,
        like case 2.
        :param candidates:
        :param target:
        :return:
        """
        candidates.sort()
        Solution.ret = []
        self.DFS_ref(candidates, target, 0, [])
        return Solution.ret

    def DFS_ref(self, candidates, target, start, valuelist):
        length = len(candidates)
        if target == 0:
            return Solution.ret.append(valuelist)
        for i in range(start, length):
            if target < candidates[i]:
                return
            self.DFS_ref(candidates, target - candidates[i], i, valuelist + [candidates[i]])


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case_notright(self):
        """
        sort() returns None as result
        :return:
        """
        nums = [2, 3, 6, 7]
        target = 7
        answer = [[7], [2, 2, 3]]
        result = self.sol.combinationSum(nums, target)
        self.assertEqual(answer.sort(), result.sort())

    def test_case1(self):
        nums = [2, 3, 6, 7]
        target = 7
        answer = [[7], [2, 2, 3]]
        result = self.sol.combinationSum(nums, target)
        answer.sort()
        result.sort()
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [2, 2,2, 3, 6, 7,7,7,7]
        target = 7
        answer = [[7], [2, 2, 3]]
        result = self.sol.combinationSum(nums, target)
        answer.sort()
        result.sort()
        self.assertEqual(answer, result)

    def test_case03(self):
        nums = [2, 3, 5]
        target = 8
        answer = [[2,2,2,2], [2,3,3], [3,5]]
        result = self.sol.combinationSum(nums, target)
        answer.sort()
        result.sort()
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()