"""
Combinations

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Subscribe to see which companies asked this question

Hide Tags Backtracking
Hide Similar Problems (M) Combination Sum (M) Permutations


"""


import unittest


class Solution(object):
    def combine(self, n, k): #
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n < 1 or k < 1 or n < k:
            return []
        result = []
        self.dfs(result, [], 0, k, n)
        return result

    def dfs(self, result, combi, curr, remain, n): #225ms, 92%, to compare with the following dfs_compare
        if remain == 0:
            result.append(combi)
            return # this line important
        for i in range(curr+1, n+2-remain):
            self.dfs(result, combi + [i], i, remain-1, n)


    def dfs_compare(self, result, combi, curr, remain, n): #245ms, 69.38%, to compare with the previous dfs
        if remain == 0:
            result.append(combi)
        # for i in range(curr+1, n+2-remain):
        #     self.dfs(result, combi + [i], i, remain-1, n)
        for i in range(curr+1, n+1):
            if n - i >= remain-1:
                self.dfs(result, combi + [i], i, remain-1, n)

        """
        # You can stop much earlier if you notice that number of remaining elements is smaller
        # than needed to fill combination:
        # optimize here to prune unnecessary dfs.
        # because we use forward fetching to avoid duplicated combi, if the positoin of i is too
        # close to n, and the remaining numbers to fetch is larger, then there will be not enough
        # numbers to get to make totally k numbers. that mean, n - i >= remain -1.
        # i.e. i <= n + 1 - remain. So we can acutally put it into one line.
        # if forgot to do "return" when remain ==0, recursion will continue with remain <0 and cause stack overflow
        # --- old code --->
        for i in range(curr+1, n+1):
            if n - i >= remain-1:
                self.dfs(result, combi + [i], i, remain-1, n)
        # <------
        """



    def combine_slower(self, n, k): #296ms, 28.73%
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n < 1 or k < 1 or n < k:
            return []
        result = []
        for i in range(1, n+1):
            self.dfs2(result, [i], i, k-1, n, k)
        return result

    def dfs2(self, result, combi, curr, remain, n, k):
        if remain == 0:
            result.append(combi)
        for i in range(curr+1, n+1):
            # You can stop much earlier if you notice that number of remaining elements is smaller
            # than needed to fill combination:
            if len(combi) + (n - curr) >= k: # optimize here to prune unnecessary dfs. --?? not complete correct here.
                self.dfs2(result, combi + [i], i, remain-1, n, k)


    def dfs_tle_cas2(self, result, combi, curr, remain, n):
        if remain == 0:
            result.append(combi)
        if remain < 0:
            return
        for i in range(curr+1, n+1):
            self.dfs(result, combi+[i], i, remain-1, n)


    def combine_ref(self, n, k): #252ms, 64.77%
        return self.solve([], 1, [], n, k)


    def solve(self, ret, start, sofar, n, k):
        for i in range(start, n - k + 2):
            if k == 1:
                ret.append(sofar + [i])
            else:
                self.solve(ret, i + 1, sofar + [i], n, k - 1)
        return ret

    def combine_ref2(self, n, k): #252ms, 64%
        if k == 1:
            return [[i] for i in range(1, n + 1)]
        if n == k:
            return [[i for i in range(1, n + 1)]]
        return [i + [n] for i in self.combine(n - 1, k - 1)] + [i for i in self.combine(n - 1, k)]

    def combine_ref3(self, n, k):#299ms, 27%
        if k == 1:
            return [[i] for i in range(1, n + 1)]
        elif k == n:
            return [[i for i in range(1, n + 1)]]
        else:
            rs = []
            rs += self.combine(n - 1, k)
            part = self.combine(n - 1, k - 1)
            for ls in part:
                ls.append(n)
            rs += part
            return rs

class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        n = 4
        k = 2
        answer = [
          [2,4],
          [3,4],
          [2,3],
          [1,2],
          [1,3],
          [1,4],
        ]
        result = self.sol.combine(n, k)
        answer.sort()
        result.sort()
        self.assertEqual(answer, result)

    def test_case2(self): # ====> TLE, but runs 1s 619ms locally
        n = 20
        k = 16
        answer = [
        ]
        result = self.sol.combine(n, k)
        answer.sort()
        result.sort()
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()