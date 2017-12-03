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
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # write your code here
        if n < 1:
            return []
        res = []
        self.generate(n, n, "", res)
        return res

    def generate(self, left, right, pares, res):
        # left should be equal or less than right
        if left == 0 and right == 0:
            res.append(pares)
            return
        if left == right:
            self.generate(left - 1, right, pares + "(", res)
        elif left < right:
            if left > 0:
                self.generate(left - 1, right, pares + "(", res)
            self.generate(left, right - 1, pares + ")", res)

class Solution1(object):
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
        if n<=0:
            return []
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
                #print one_str
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
        ]
        result = self.sol.generateParenthesis(n)
        self.assertEqual(sorted(answer), sorted(result))

    def test_case2(self):
        n = 0
        answer = []
        result = self.sol.generateParenthesis(n)
        self.assertEqual(sorted(answer), sorted(result))

    def test_case3(self): # ====> Output Limit Exceeded, Last executed input: 8
        n = 2
        answer = ["()()", "(())"]
        result = self.sol.generateParenthesis(n)
        self.assertEqual(sorted(answer), sorted(result))


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTestor)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()

"""
Two main constraints when dfs:
(1) when adding ), make sure that ( should be no less than )
(2) when adding (, as long as they are no more than n

"""