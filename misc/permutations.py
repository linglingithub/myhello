"""
Permutations

Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
Subscribe to see which companies asked this question

Hide Tags Backtracking
Hide Similar Problems (M) Next Permutation (M) Permutations II (M) Permutation Sequence (M) Combinations

"""

import unittest


class Solution(object):
    """
    check both the insertion way and recursive way
    """
    def permute_insertionway(self, nums): # insertion way, 78ms, 85.91%
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) < 1:
            return []
        result = [[nums[0]]]
        for num in nums[1:]:
            new_res = []
            for permu in result:
                for idx in range(len(permu)+1):
                    #new_permu = permu.insert(idx, num)  list.insert() returns None, use another way to create new_permu
                    permu.insert(idx, num)
                    new_permu = permu[:]
                    del permu[idx]
                    new_res.append(new_permu)
            result = new_res
        return result


    def permute_recursive(self, nums): # recursive way, 79ms, 79.05%
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) < 1:
            return []
        result = []
        self.dfs(result, [], 0, nums)
        return result

    def dfs(self, result, permu, idx, nums):
        if len(permu) == len(nums):
            result.append(permu)
            return
        for chg in range(idx, len(nums)):
            nums[idx], nums[chg] = nums[chg], nums[idx]
            self.dfs(result, permu+[nums[idx]], idx+1, nums)
            nums[idx], nums[chg] = nums[chg], nums[idx]


    def permute_ref(self, num): # 86ms, 58.79%
        if len(num) == 0: return []
        if len(num) == 1: return [num]
        res = []
        for i in range(len(num)):
            for j in self.permute(num[:i] + num[i + 1:]):
                res.append([num[i]] + j)
        return res

    def permute_ref2(self, nums):
        res = []
        self.dfs2(nums, [], res)
        return res

    def dfs2(self, nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in xrange(len(nums)):
            self.dfs2(nums[:i] + nums[i + 1:], path + [nums[i]], res)







class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,2,3]
        answer = [
          [1,2,3],
          [1,3,2],
          [2,1,3],
          [2,3,1],
          [3,1,2],
          [3,2,1]
        ]
        result = self.sol.permute(nums)
        answer.sort()
        result.sort()
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()