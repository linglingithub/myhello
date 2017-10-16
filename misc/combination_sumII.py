"""

Combination Sum II

Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the 
candidate numbers sums to T.

Each number in C may only be used ONCE in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Subscribe to see which companies asked this question

Hide Tags Array Backtracking
Hide Similar Problems (M) Combination Sum


"""


import unittest


class Solution(object):
    def combinationSum2(self, candidates, target): #96ms, 80.7%
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if candidates is None or len(candidates) == 0:
            return []
        result = []
        #candidates = list(set(candidates))  # important
        candidates.sort()   #important, if the problem does not assume that the candiates are unique,
        # this is to guarantee there is no duplicate combi.

        for i in range(len(candidates)):
            if i >= 1 and candidates[i] == candidates[i-1]: # important, avoid to have duplicate combi
                continue
            combi = self.dfs(result, candidates, [candidates[i]], i, target - candidates[i])
        return result  # run time error if do "list(set(result))"

    def dfs(self, result, candidates, combi, idx, target):
        if target == 0:
            result.append(combi)
        for i in range(idx+1, len(candidates)):
            if i > idx+1 and candidates[i] == candidates[i-1]: #important, to avoid wrong answer for case2
                continue
            num = candidates[i]
            if target - num >= 0:
                self.dfs(result, candidates, combi + [num], i, target - num)




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()


    def test_case1(self):
        nums = [10, 1, 2, 7, 6, 1, 5]
        target = 8
        answer = [[1, 7], [1, 2, 5],  [2, 6],  [1, 1, 6]]
        result = self.sol.combinationSum2(nums, target)
        answer.sort()
        result.sort()
        self.assertEqual(answer, result)

    def test_case2(self): #======> wrong answer
        nums = [2,2,2]
        target = 4
        answer = [[2,2]]
        result = self.sol.combinationSum2(nums, target)
        answer.sort()
        result.sort()
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()