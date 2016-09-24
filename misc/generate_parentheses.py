"""
Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
Subscribe to see which companies asked this question

Hide Tags Backtracking String
Hide Similar Problems (M) Letter Combinations of a Phone Number (E) Valid Parentheses

"""

import unittest


class Solution(object):
    def generateParenthesis(self, n): # faster
        def dfs(open, left, right, one_str, result):
            if open<0:
                return
            if left ==0 and right == 0 :
                result.append(one_str)
                return
            if left > 0 :
                dfs(open+1, left-1, right, one_str+"(", result)
            if right > 0:
                dfs(open-1, left, right - 1, one_str+")", result)

        result = []
        if n ==0:
            return []
        dfs(0,n, n, "", result)
        return result




    def generateParenthesis3(self, n): # faster
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        str = ""
        stack = 0
        self.dfs3(stack, n, str, ans, n, n)
        return ans

    def dfs3(self, stack, n, str, ans, nl, nr):
        if n == 0 and stack == 0:
            ans.append(str)
        else:
            if nl > 0 and stack <= n and (n != 1 or stack != 1):
                ntr = str + '('
                self.dfs3(stack + 1, n, ntr, ans, nl - 1, nr)
            if nr > 0 and stack > 0:
                ntr = str + ')'
                self.dfs3(stack - 1, n - 1, ntr, ans, nl, nr - 1)




    def generateParenthesis2(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        if n == 0:
            return result
        self.dfs_par(n, n, "", result)
        return result

    def dfs_par(self, left, right, one_str, result):
        if right < left:
            return
        if left == 0 and right == 0:
            result.append(one_str)
            return
        if left > 0:
            self.dfs_par(left - 1, right, one_str+"(", result)
        if right > 0:
            self.dfs_par(left, right-1, one_str+")", result)



    def generateParenthesis1(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def dfs_parentheses(indx, one_str, open, result):
            if indx == 2 * n:
                print one_str
                result.append(one_str)
                return
            else:
                if open >= 2*n - indx:
                    dfs_parentheses(indx+1, one_str+")", open - 1, result)
                elif open == 0:
                    dfs_parentheses(indx + 1, one_str + "(", open + 1, result)
                else: # open in (0, 2n-indx)
                    dfs_parentheses(indx + 1, one_str + "(", open + 1, result)
                    dfs_parentheses(indx + 1, one_str + ")", open - 1, result)
        result = []
        if n == 0:
            return result
        dfs_parentheses(0, "", 0, result)
        return result






class SolutionTestor(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        n = 3
        answer = [
          "((()))",
          "(()())",
          "(())()",
          "()(())",
          "()()()"
        ].sort()
        result = self.sol.generateParenthesis(n).sort()
        self.assertEqual(answer, result)

    def test_case2(self):
        n = 0
        answer = []
        result = self.sol.generateParenthesis(n)
        self.assertEqual(answer, result)

    def test_case3(self): # ====> Output Limit Exceeded, Last executed input: 8
        n = 8
        answer = [""]
        result = self.sol.generateParenthesis(n)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTestor)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()