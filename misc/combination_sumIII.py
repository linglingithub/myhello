"""

Combination Sum III

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used

and each combination should be a unique set of numbers.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]
Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.

Subscribe to see which companies asked this question

Hide Tags Array Backtracking
Hide Similar Problems (M) Combination Sum


"""

import unittest



class Solution(object):
    def combinationSum3(self, k, n): # 49ms, 79.67%, remove if before each calling, make it faster
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if k < 1 or n < 1:
            return []
        result = []
        for num in range(1, 10):
            self.dfs(result, [num], num, k-1, n-num)
        return result

    def dfs(self, result, combi, num, cnt, target):
        if target < 0 or cnt < 0:
            return
        if target == 0 and cnt == 0:
            result.append(combi)
            return
        for i in range(num+1, 10): # from the test case, you can see that every 1-9 can only appear ONCE, although the problem does not put that in word.
            self.dfs(result, combi+[i], i, cnt-1, target - i)


    def combinationSum3_slower(self, k, n): # 105ms, 3.29%
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if k < 1 or n < 1:
            return []
        result = []
        for num in range(1, 10):
            if n-num >= 0:
                self.dfs1(result, [num], num, k-1, n-num)
        return result

    def dfs1(self, result, combi, num, cnt, target):
        if target == 0 and cnt == 0:
            result.append(combi)
            return
        for i in range(num+1, 10): # from the test case, you can see that every 1-9 can only appear ONCE, although the problem does not put that in word.
            if target - i >= 0 and cnt >= 1:
                self.dfs1(result, combi+[i], i, cnt-1, target - i)


    def combinationSum3_ref(self, k, n): #45ms, 88.91%
        ans = []
        def search(start, cnt, sums, nums):
            if cnt > k or sums > n:
                return
            if cnt == k and sums == n:
                ans.append(nums)
                return
            for x in range(start + 1, 10):
                search(x, cnt + 1, sums + x, nums + [x])

        search(0, 0, 0, [])
        return ans

    def combinationSum3_ref2(self, k, n): # 46ms, 88.09%, not recommended, kind of cheating, but accepted and fast
        import itertools
        return [item for item in itertools.combinations([i for i in xrange(1, 10)], k) if sum(item) == n]

    def combinationSum3_ref_iter(self, k, n): #98ms, 4.3%
        i = 0
        solution = [0] * (k)
        result = []

        while i != -1:
            if i == k:
                if sum(solution) == n and len(set(solution)) == len(solution):
                    result.append(solution[:])
                i -= 1
                continue

            solution[i] = solution[i] + 1

            if i != 0:
                if solution[i] <= solution[i - 1]:
                    continue

            if solution[i] != 10:
                i += 1
            else:
                solution[i] = 0
                i -= 1

        return result




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        k = 3
        n = 7
        answer = [[1,2,4]]
        result = self.sol.combinationSum3(k, n)
        answer.sort()
        result.sort()
        self.assertEqual(answer, result)

    def test_case2(self):
        k = 3
        n = 9
        answer = [[1,2,6], [1,3,5], [2,3,4]]
        result = self.sol.combinationSum3(k, n)
        answer.sort()
        result.sort()
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()