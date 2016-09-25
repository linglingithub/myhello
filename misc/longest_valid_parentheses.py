"""
Longest Valid Parentheses

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

Subscribe to see which companies asked this question

Hide Tags Dynamic Programming String
Hide Similar Problems (E) Valid Parentheses


"""

import unittest

class Solution(object):
    def longestValidParentheses_notworkingfromcase8(self, s): # naive way
        """
        :type s: str
        :rtype: int
        """
        stack = []
        maxlen = 0
        begin = len(s) # change from len(s) - 1 to len(s) for case 7
        end = -1 # change from 0 to -1 for case 8
        valid = False
        if len(s) == 0:
            return 0
        for i in range(len(s)):
            char = s[i]
            if char == "(":
                if not valid:
                    begin = i
                    valid = True
                stack.append(i)
            else:
                if len(stack) > 0:
                    left = stack.pop()
                    if len(stack)==0: # add this ==0 check is important
                        if left == end + 1:
                            pass
                        else:
                            begin = left
                        end = i
                else:
                    valid = False
                    del stack[:]
                    tmp = end - begin + 1
                    maxlen = max(maxlen, tmp)
        if valid and len(stack)==0:
            return max(maxlen, end-begin+1)
        else:
            return maxlen


    def longestValidParentheses_notworkingfromcase10(self, s):
        stack = []
        maxlen = 0
        left = -1
        right = -1

        if len(s) < 2:
            return 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                if stack:
                    nearest = stack.pop()
                    tmp = i - nearest + 1
                    if not stack or i == len(s)-1: # no open , check if connected with previous valid string
                        if right != -1 and nearest == right + 1: # connected with last closing )
                            tmp = right - left + 1 + tmp
                        else:
                            left = nearest
                        right = i
                    if left == -1:
                        left = nearest
                    if right == -1:
                        right = i
                    maxlen = max(maxlen, tmp)
                else:
                    continue

        return maxlen


    def longestValidParentheses1(self, s): # stack, beat 92.04%, 66ms, based on http://www.cnblogs.com/zuoyuan/p/3780312.html, not all the same
        maxlen = 0
        stack = []
        last = -1
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)     # push the INDEX into the stack!!!!
            else:
                if stack == []:
                    last = i  # record the last ) that not matched
                else:
                    stack.pop()
                    if stack == []: #### all left ( mathced, then current longest is "i - last ) not matched"
                        tmp = i - last
                        maxlen = max(maxlen, i-last)
                    else: #### all right ) matched but some ( left, then current longest is "i - last ( not matched"
                        tmp = i - stack[-1]
                        maxlen = max(maxlen, i-stack[-1])
        return maxlen



    def longestValidParentheses(self, s): # DP, slower, 41.79%, 99ms, based on https://discuss.leetcode.com/topic/8305/simple-java-solution
        maxlen = 0
        dp = [ 0 for i in range(len(s))]
        open = 0
        for i in range(len(s)):
            if s[i] == "(":
                open += 1
            else:
                if open > 0:
                    dp[i] = 2 + dp[i-1]
                    if dp[i] < i+1:
                        dp[i] += dp[i-dp[i]]
                    maxlen = max(maxlen, dp[i])
                    open -= 1
        return maxlen






class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        s = ""
        answer = 0
        result = self.sol.longestValidParentheses(s)
        self.assertEqual(answer, result)

    def test_case2(self):
        s = "()"
        answer = 2
        result = self.sol.longestValidParentheses(s)
        self.assertEqual(answer, result)

    def test_case3(self):
        s = ")("
        answer = 0
        result = self.sol.longestValidParentheses(s)
        self.assertEqual(answer, result)

    def test_case4(self):
        s = "()())"
        answer = 4
        result = self.sol.longestValidParentheses(s)
        self.assertEqual(answer, result)

    def test_case5(self): #=====>
        s = ")()())())()()(())()"
        answer = 10
        result = self.sol.longestValidParentheses(s)
        self.assertEqual(answer, result)

    def test_case6(self): #=====>
        s = "("
        answer = 0
        result = self.sol.longestValidParentheses(s)
        self.assertEqual(answer, result)

    def test_case7(self):  # =====>
        s = ")"
        answer = 0
        result = self.sol.longestValidParentheses(s)
        self.assertEqual(answer, result)

    def test_case8(self):  # =====>
        s = "(()"
        answer = 2
        result = self.sol.longestValidParentheses(s)
        self.assertEqual(answer, result)

    def test_case9(self):  # =====>
        s = "(()()"
        answer = 4
        result = self.sol.longestValidParentheses(s)
        self.assertEqual(answer, result)

    def test_case10(self):  # =====>
        s = "(()()(())(("
        answer = 8
        result = self.sol.longestValidParentheses(s)
        self.assertEqual(answer, result)





def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()
