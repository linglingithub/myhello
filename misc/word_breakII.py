#coding=utf-8

"""
140. Word Break II

Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid
dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].

Subscribe to see which companies asked this question

Hide Tags Dynamic Programming Backtracking
Hide Similar Problems (H) Concatenated Words

Hard

"""

import unittest


class Solution(object):
    def wordBreak(self, s, wordDict): #write according to ref2, 352ms, 8.6%
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        self.string_dict = {}
        self.parse_string(s, wordDict)
        return self.string_dict[s]

    def parse_string(self, s, wordDict):
        result = []
        if s in wordDict:
            result.append(s)

        for idx in range(0, len(s)-1):
            sub1, sub2 = s[:idx+1], s[idx+1:]
            if sub1 not in wordDict:
                continue
            # if sub2 in wordDict: # can this be simplified? -- yes
            #     rest.append([sub2])
            if sub2 in self.string_dict:
                rest = self.string_dict[sub2]
            else:
                rest = self.parse_string(sub2, wordDict)
            for one_break in rest:
                result.append(sub1 + " " + one_break)

        self.string_dict[s] = result
        return result






    def wordBreak_wrong(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        if not s or not wordDict:
            return []
        result = []
        n = len(s)
        #wordDict = sorted(wordDict,) # .sort() will not change # ask if we can assume the dictionary is sorted
        dp = [ [] for i in range(n)]
        self.wordBreakHelper1(result, dp, 0, "", s, wordDict)
        if dp[n-1]:
            result = [ x.strip() for x in dp[n-1] ]
            return result
        return []

    def wordBreakHelper1(self, result, dp, idx, current, s, wordDict):
        if idx>=len(s):
            return
        for word in wordDict:
            l = len(word)
            k = idx - l + 1
            if k >= len(s):
                continue
            if s[idx: k+1] == word:
                tmp = current + " " + word
                dp[k].append(tmp)
                self.wordBreakHelper1(result, dp, k+1, tmp, s, wordDict)
        
        
    def wordBreakHelper_TLE(self, result, dp, idx, current, s, wordDict):  # actually only DFS, did not use DP
        if idx>=len(s):
            return
        for word in wordDict:
            l = len(word)
            k = idx + l - 1
            if k >= len(s):
                #return #can not return here, because other words in dict are not sorted
                continue
            if s[idx: k+1] == word:
                tmp = current + " " + word
                dp[k].append(tmp)
                self.wordBreakHelper_TLE(result, dp, k+1, tmp, s, wordDict)


    def wordBreak_ref2(self, s, wordDict): #_ref2 92ms, 12%
        tokenDict = dict()
    
        def dfs(s):
            ans = []
            if s in wordDict:
                ans.append(s)
            for x in range(len(s) - 1):
                prefix, suffix = s[:x + 1], s[x + 1:]
                if prefix not in wordDict:
                    continue
                rest = []
                if suffix in tokenDict:
                    rest = tokenDict[suffix]
                else:
                    rest = dfs(suffix)
                for n in rest:
                    ans.append(prefix + ' ' + n)
            tokenDict[s] = ans
            return ans
    
        return dfs(s)


    def wordBreak_ref(self, s, dict): #79ms, 23%
        Solution.res = []
        self.dfs(s, dict, '')
        return Solution.res
        
    def check(self, s, dict):
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for k in range(0, i):
                if dp[k] and s[k:i] in dict:
                    dp[i] = True
        return dp[len(s)]

    def dfs(self, s, dict, stringlist):
        if self.check(s, dict):
            if len(s) == 0: Solution.res.append(stringlist[1:])
            for i in range(1, len(s) + 1):
                if s[:i] in dict:
                    self.dfs(s[i:], dict, stringlist + ' ' + s[:i])
                
                
            


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self): #====>
        s = "ab"
        wdict = ["a", "b"]
        answer = ["a b"]
        result = self.sol.wordBreak(s, wdict)
        self.assertEqual(sorted(answer), sorted(result))


    def test_case2(self): #=====> TLE, even did not run through for local test
        s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        wdict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
        answer = []
        result = self.sol.wordBreak(s, wdict)
        self.assertEqual(sorted(answer), sorted(result))

    def test_case3(self):
        s = "catsanddog"
        wdict = ["cat", "cats", "and", "sand", "dog"]
        answer = ["cats and dog", "cat sand dog"]
        result = self.sol.wordBreak(s, wdict)
        self.assertEqual(sorted(answer), sorted(result))


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""

解题思路：这道题不只像word break那样判断是否可以分割，而且要找到所有的分割方式，那么我们就要考虑dfs了。不过直接用dfs解题是不行的，为什么？
因为决策树太大，如果全部遍历一遍，时间复杂度太高，无法通过oj。那么我们需要剪枝，如何来剪枝呢？使用word break题中的动态规划的结果，在dfs之
前，先判定字符串是否可以被分割，如果不能被分割，直接跳过这一枝。实际上这道题是dp+dfs。

================================================================================================================================================

a java version of a solution

public class Solution {
    public List<String> wordBreak(String s, List<String> wordDict) {
        List<String> res = new ArrayList<String>();

        // 用来记录s.substring(i)这个字符串能否分解
        boolean[] possible = new boolean[s.length() + 1];
        Arrays.fill(possible, true);
        dfs(res, "", s, wordDict,  0, possible);
        return res;
    }

    public static void dfs(List<String> res, String cur, String s, List<String> wordDict, int start, boolean[] possible) {
        if (start == s.length()) {
            res.add(cur);
            return;
        }
        for (int i = start + 1; i <= s.length(); i++) {
            String str = s.substring(start, i);
            if (wordDict.contains(str) && possible[i]) {
                int prevSize = res.size();
                dfs(res, cur + (cur.equals("") ? "" : " ") + str, s, wordDict, i, possible);

                // DFS后面部分结果没有变化，说明后面是没有解的
                if (res.size() == prevSize)
                    possible[i] = false;
            }
        }
    }
}


"""


#-*- coding:utf-8 -*-
