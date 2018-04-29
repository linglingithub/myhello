# coding=utf-8

import unittest
import collections

"""
301. Remove Invalid Parentheses
DescriptionHintsSubmissionsDiscussSolution
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]
Credits:
Special thanks to @hpplayer for adding this problem and creating all test cases.

Difficulty:Hard
Total Accepted:68.1K
Total Submissions:189.9K
Contributor:LeetCode
Subscribe to see which companies asked this question.

Related Topics 

Similar Questions 
Valid Parentheses

=======

BFS: achieve 'minimum' by doing edit level by level, so the first level that can be valid will be the 'minimum' edit.
DFS: achieve 'mininum' by checking the original string first and find out how many ( or ) to remove, than dfs accoring 
    to (_to_remove and )_to remove and keep currunt edited string valid, then of course the resulting valid string will 
    be all correct minimum candidate string

"""


class SolutionRef(object):
    def removeInvalidParentheses(self, s):  # DFS way, looks faster than BFS
        """
        :type s: str
        :rtype: List[str]
        """
        if not s: return ['']
        left_remove = right_remove = 0
        for c in s:
            if c == '(':
                left_remove += 1
            elif c == ')':
                if left_remove:
                    left_remove -= 1
                else:
                    right_remove += 1

        ans = set()
        self.dfs(0, left_remove, right_remove, 0, '', s, ans)
        return list(ans)

    def dfs(self, index, left_remove, right_remove, left_pare, cur, s, ans):
        if left_remove < 0 or right_remove < 0 or left_pare < 0: return
        if index == len(s):
            if left_remove == right_remove == left_pare == 0:
                ans.add(cur)
            return

        if s[index] == '(':
            self.dfs(index + 1, left_remove - 1, right_remove, left_pare, cur, s, ans)
            self.dfs(index + 1, left_remove, right_remove, left_pare + 1, cur + s[index], s, ans)
        elif s[index] == ')':
            self.dfs(index + 1, left_remove, right_remove - 1, left_pare, cur, s, ans)
            self.dfs(index + 1, left_remove, right_remove, left_pare - 1, cur + s[index], s, ans)
        else:
            self.dfs(index + 1, left_remove, right_remove, left_pare, cur + s[index], s, ans)

    def removeInvalidParentheses_BFS(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s: return ['']
        q, ans, vis = [s], [], set([s])
        found = False
        while q:
            cur = q.pop(0)
            if self.isValidParentheses(cur):
                found = True
                ans.append(cur)
            elif not found:
                for i in range(len(cur)):
                    if cur[i] == '(' or cur[i] == ')':
                        t = cur[:i] + cur[i + 1:]
                        if t not in vis:
                            q.append(t)
                            vis.add(t)
        return ans

    def isValidParentheses(self, s):
        cnt = 0
        for c in s:
            if c == '(':
                cnt += 1
            elif c == ')':
                if cnt == 0: return False
                cnt -= 1
        return cnt == 0


    def removeInvalidParentheses1(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def calc(s):
            a = b = 0
            for c in s:
                a += {'(' : 1, ')' : -1}.get(c, 0)
                b += a < 0
                a = max(a, 0)
            return a + b

        visited = set([s])
        ans = []
        queue = collections.deque([s])
        done = False
        while queue:
            t = queue.popleft()
            mi = calc(t)
            if mi == 0:
                done = True
                ans.append(t)
            if done:
                continue
            for x in range(len(t)):
                if t[x] not in ('(', ')'):
                    continue
                ns = t[:x] + t[x+1:]
                if ns not in visited and calc(ns) < mi:
                    visited.add(ns)
                    queue.append(ns)

        return ans

class Solution_Self:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        (() => [()]
        ((()()())) => [orginal]
        "()())()" -> ["()()()", "(())()"]
        ())()())) => [()()(), ()(())]

        if extra (, only one way to remove?
        if extra ), current consecutive ) place, and previous non consecutive ) place.

        1. first scan and use a stack to keep ('s  idx and pop when there is )
            when stack empty and need to pop, record the ) idexes. => extra_right_idx
            when at the end if there is remaining ( instack, --> modify the original string by removing it (right to left) => semi_rst
        2. upon semi_rst and extra_right_idx, if necessary, modify extra_right_idx
            remove ) at all possible ) ??  (area: previous extra ) idx to current extra ))
            <================== self idea, not good enough
            ref idea:
            use the BFS way to do.


        """
        # should not add this corner case, or need to return [""], see case3,
        # if not s:
        #     return []
        result = []
        candidates = set()
        candidates.add(s)
        self.bfs_check_modify(s, result, candidates)
        return result




    def bfs_check_modify(self, s, result, candidates):
        # for current s, if not valid modification will goto candidates, which is a set of string
        next_level = set()
        for cur in candidates:
            if self.is_valid(cur):
                result.append(cur)
            else:
                next_level.add(cur)
        if result:
            return
        candidates.clear()
        for cur in next_level:
            for idx in range(len(cur)):
                tmp = cur[: idx] + cur[idx + 1:]
                candidates.add(tmp)
        self.bfs_check_modify(s, result, candidates)



    # should have a level-order structure.
    # current version will lead to dfs on invalid ones
    # and also need to think about the systematic way to do it, eg. how to deal with "" result?
    def bfs_check_modify_wrong(self, s, result):
        if self.is_valid(s):
            result.append(s)
            return
        for idx in range(len(s)):
            # should skip non () chars here
            if s[idx] != "(" and s[idx] != ")":
                continue
            tmp = s[: idx] + s[idx + 1:]
            self.bfs_check_modify(tmp, result)


    def is_valid(self, s):
        balance = 0  # when ( +1, when ) -1, balance should always be >= 0, and end with 0, otherwise invalid
        for char in s:
            if char != "(" and char != ")":
                continue
            elif char == "(":
                balance += 1
            else:
                balance -= 1
                if balance < 0:
                    return False
        return balance == 0


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        s = "()())()"
        answer = ["(())()", "()()()"]
        result = self.sol.removeInvalidParentheses(s)
        self.assertCountEqual(answer, result)

    def test_case2(self):
        s = ")("
        answer = [""]
        result = self.sol.removeInvalidParentheses(s)
        self.assertCountEqual(answer, result)

    def test_case3(self):
        s = ""
        answer = [""]  # ==> wrong as []
        result = self.sol.removeInvalidParentheses(s)
        self.assertCountEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()


"""
https://www.hrwhisper.me/leetcode-remove-invalid-parentheses/  ==> better performance and code


http://bookshadow.com/weblog/2015/11/05/leetcode-remove-invalid-parentheses/



"""
