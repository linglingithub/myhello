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
    def wordBreak(self, s, wordDict):
        if not s:
            return []
        cache = {}
        self.parse_str(s, 0, wordDict, cache)
        return cache.get(0, [])

    def parse_str(self, s, idx, wordDict, cache):
        # print(idx, " -- ", cache)
        if idx in cache:
            return cache[idx]
        tmp = []
        if s[idx:] in wordDict:   # compare to method2, should be s[idx:] instead of s
            tmp.append(s[idx:])
        for i in range(idx, len(s) - 1):  # i start from idx
            substr = s[idx:i + 1]    # substr from idx
            if substr not in wordDict:
                continue
            right_list = self.parse_str(s, i + 1, wordDict, cache)
            for right_path in right_list:
                tmp.append(substr + " " + right_path)
        cache[idx] = tmp
        return cache[idx]

    def wordBreak2(self, s, wordDict):
        if not s:
            return []
        cache = {}
        self.parse_str(s, wordDict, cache)
        return cache.get(s, [])

    def parse_str2(self, s, wordDict, cache):
        if s in cache:
            return cache[s]
        tmp = []
        if s in wordDict:
            tmp.append(s)
        for i in range(0, len(s) - 1):
            substr = s[:i + 1]
            if substr not in wordDict:
                continue
            right = s[i + 1:]
            right_list = self.parse_str2(right, wordDict, cache)
            for right_path in right_list:
                tmp.append(substr + " " + right_path)
        cache[s] = tmp
        return tmp

    def wordBreak1(self, s, wordDict):
        if not s:
            return []
        res = []
        cache = self.init_right_breakable(s, wordDict)
        self.helper(s, 0, [], wordDict, cache, res)
        return res

    def init_right_breakable(self, s, wordDict):
        cache = {len(s): True}
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                substr = s[i: j + 1]
                if substr in wordDict and cache.get(j + 1):
                    cache[i] = True
                    break
        return cache

    def helper(self, s, idx, path, wordDict, cache, res):
        if idx >= len(s):
            res.append(" ".join(path))
            return
        for i in range(idx, len(s)):
            substr = s[idx: i + 1]
            if substr in wordDict and cache.get(i + 1):
                self.helper(s, i + 1, path + [substr], wordDict, cache, res)

    def wordBreak_TLE(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        res = []
        self.helper(s, 0, [], res, wordDict)
        return res

    def helper_TLE2(self, s, idx, path, res, wordDict):
        if idx >= len(s):
            res.append(" ".join(path))
            return
        for w in wordDict:
            wlen = len(w)
            if wlen + idx - 1 <= len(s) and s[idx: idx + wlen] == w:
                self.helper(s, idx + wlen, path + [w], res, wordDict)

    def helper_TLE(self, s, idx, path, res, wordDict):
        if idx >= len(s):
            res.append(" ".join(path))
            return
        for i in range(idx, len(s)):
            substr = s[idx: i + 1]
            if substr in wordDict:
                self.helper(s, i + 1, path + [substr], res, wordDict)


class Solution1(object):
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


=====================================================================================================================


http://www.cnblogs.com/yuzhangcmu/p/4037299.html

解答1 (dfs)：
让我们来继续切切切吧！

本题与上一题Word Break思路类似，但是一个是DP,一个是DFS。
让我们来回顾一下DP与DFS的区别：
DP是Bottom-up 而DFS是TOP-DOWN.

在本题的DFS中，我们这样定义：
用刀在字符串中切一刀。左边是i个字符，右边是len-i个字符。
i: 1- len
如果： 左边是字典里的词，右边是可以wordbreak的，那么把左边的字符串加到右边算出来的List中，生成新的list返回。
1. Base case:
当输入字符串为空的时候，应该给出一个空解。这个很重要，否则这个递归是不能运行的。
2. 递归的时候，i应该从1开始递归，因为我们要把这个问题分解为2个部分，如果你左边给0，那就是死循环。

记忆：
为了加快DFS的速度，我们应该添加记忆，也就是说，算过的字符串不要再重复计算。举例子：
apple n feng
app len feng
如果存在以上2种划分，那么feng这个字符串会被反复计算，在这里至少计算了2次。我们使用一个Hashmap把对应字符串的解记下来，这样就能避免重复的计算。 否则这一道题目会超时。


复制代码
 1 // 我们用DFS来解决这个问题吧 
 2     public static List<String> wordBreak1(String s, Set<String> dict) {
 3         HashMap<String, List<String>> map = new HashMap<String, List<String>>();
 4         if (s == null || s.length() == 0 || dict == null) {
 5             return null;
 6         }
 7 
 8         return dfs(s, dict, map);
 9     }
10 
11     // 解法1：我们用DFS来解决这个问题吧 
12     public static List<String> dfs(String s, Set<String> dict, HashMap<String, List<String>> map) {
13         if (map.containsKey(s)) {
14             return map.get(s);
15         }
16 
17         List<String> list = new ArrayList<String>();
18         int len = s.length();
19 
20         if (len == 0) {
21             list.add("");
22         } else {
23             // i 表示左边字符串的长度
24             for (int i = 1; i <= len; i++) {
25                 String sub = s.substring(0, i);
26 
27                 // 左边的子串可以为空，或是在字典内
28                 if (!dict.contains(sub)) {
29                     continue;
30                 }
31 
32                 // 字符串划分为2边，计算右边的word break.
33                 List<String> listRight = dfs(s.substring(i, len), dict, map);
34 
35                 // 右边不能break的时候，我们跳过.
36                 if (listRight.size() == 0) {
37                     continue;
38                 }
39 
40                 // 把左字符串加到右字符串中，形成新的解.
41                 for (String r: listRight) {
42                     StringBuilder sb = new StringBuilder();
43                     sb.append(sub);
44                     if (i != 0 && i != len) {
45                         // 如果左边为空，或是右边为空，不需要贴空格
46                         sb.append(" ");
47                     }
48                     sb.append(r);
49                     list.add(sb.toString());
50                 }
51             }
52         }
53 
54         map.put(s, list);
55         return list;
56     }
复制代码

解答2： dfs2：
参考了http://blog.csdn.net/fightforyourdream/article/details/38530983的 解法，我们仍然使用主页君用了好多次的递归模板。但是在LeetCode中超时，在进入DFS时加了一个『判断是不是wordBreak』的判断，终于过了。这是一种DFS+剪枝的解法

 View Code
 

解答3： dfs3：

感谢http://fisherlei.blogspot.com/2013/11/leetcode-wordbreak-ii-solution.html的解释，我们可以加一个boolean的数组，b[i]表示从i到len的的字串可不可以进行word break. 如果我们在当前根本没有找到任何的word， 也就表明这一串是不能word break的，记一个false在数组里。这样下次进入dfs这里的时候，直接就返回一个false.通过这个剪枝我们也可以减少复杂度。

 View Code
 

解答4： DP解法：

感谢大神的解法： https://gist.github.com/anonymous/92e5e613aa7b5ce3d4c5 以后再慢慢研究

主页君自己也写了一个先用动规算出哪些区间是可以解的，然后在DFS的时候，先判断某区间能否word break，如果不可以，直接退出。


复制代码
 1     /*
 2     // 解法4：先用DP来求解某些字段是否能word break，然后再做 
 3     */
 4     // 我们用DFS来解决这个问题吧 
 5     public static List<String> wordBreak4(String s, Set<String> dict) {
 6         if (s == null || s.length() == 0 || dict == null) {
 7             return null;
 8         }
 9         
10         List<String> ret = new ArrayList<String>();
11         
12         List<String> path = new ArrayList<String>();
13         
14         int len = s.length();
15         
16         // i: 表示从i索引开始的字串可以word break.
17         boolean[] D = new boolean[len + 1];
18         D[len] = true;
19         for (int i = len - 1; i >= 0; i--) {
20             for (int j = i; j <= len - 1; j++) {
21                 // 左边从i 到 j
22                 D[i] = false;
23                 if (D[j + 1] && dict.contains(s.substring(i, j + 1))) {
24                     D[i] = true;
25                     break;
26                 }
27             }
28         }
29 
30         dfs4(s, dict, path, ret, 0, D);
31         
32         return ret;
33     }
34 
35     public static void dfs4(String s, Set<String> dict, 
36             List<String> path, List<String> ret, int index,
37             boolean canBreak[]) {
38         int len = s.length();
39         if (index == len) {
40             // 结束了。index到了末尾
41             StringBuilder sb = new StringBuilder();
42             for (String str: path) {
43                 sb.append(str);
44                 sb.append(" ");
45             }
46             // remove the last " "
47             sb.deleteCharAt(sb.length() - 1);
48             ret.add(sb.toString());
49             return;
50         }
51         
52         // if can't break, we exit directly.
53         if (!canBreak[index]) {
54             return;
55         }
56 
57         for (int i =  index; i < len; i++) {
58             // 注意这些索引的取值。左字符串的长度从0到len
59             String left = s.substring(index, i + 1);
60             if (!dict.contains(left)) {
61                 // 如果左字符串不在字典中，不需要继续递归
62                 continue;
63             }
64             
65             // if can't find any solution, return false, other set it 
66             // to be true;
67             path.add(left);
68             dfs4(s, dict, path, ret, i + 1, canBreak);
69             path.remove(path.size() - 1);
70         }
71 
72     }
复制代码
 

比较与测试：

这里贴一下各种解法的时间：

Test
Computing time with DFS1: 7830.0 millisec.
Computing time with DFS2: 6400.0 millisec.
Computing time with DFS3: 4728.0 millisec.
Computing time with DFS4: 4566.0 millisec.


可见，四个方法里最好的是第四个，建议面试时可以采用第四个。如有错误，敬请指正。

====================


    def wordBreak(self, s, wordDict):
        memo = {len(s): ['']}
        def sentences(i):
            if i not in memo:
                memo[i] = [s[i:j] + (tail and ' ' + tail)
                           for j in range(i+1, len(s)+1)
                           if s[i:j] in wordDict
                           for tail in sentences(j)]
            return memo[i]
        return sentences(0)    

"""


#-*- coding:utf-8 -*-
