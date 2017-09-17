#coding=utf-8

import unittest

"""

[locked]

Word Pattern II

This is the extension problem of Word Pattern I.

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.

Examples:
pattern = "abab", str = "redblueredblue" should return true.
pattern = "aaaa", str = "asdasdasdasd" should return true.
pattern = "aabb", str = "xyzabcxzyabc" should return false.

"""


class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        char_word = {}
        word_char = {}
        i, j = 0, 0
        res = [False]
        self.helper(pattern, str, i, j, char_word, word_char, res)
        return res[0]

    def helper(self, pattern, str, i, j, char_word, word_char, res):
        if i >= len(pattern) and j >= len(str):
            res[0] = True
            return
        if i>= len(pattern) or j >= len(str):
            res[0] = False
            return
        char = pattern[i]
        for k in range(j, len(str)):
            word = str[j: k+1]
            if char in char_word:
                if char_word[char]==word and word in word_char and char_word[char]==word and word_char[word]==char:
                    self.helper(pattern, str, i+1, k+1, char_word, word_char, res)
                else:
                    continue
            else:
                if word not in word_char:
                    char_word[char] = word
                    word_char[word] = char
                    self.helper(pattern, str, i+1, k+1, char_word, word_char, res)
                    if not res[0]:
                        del char_word[char]
                        del word_char[word]
                else:
                    continue





class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        pattern = "abab"
        str = "redblueredblue"
        answer = True
        result = self.sol.wordPatternMatch(pattern, str)
        self.assertEqual(answer, result)

    def test_case2(self):
        pattern = "aaaa"
        str = "asdasdasdasd"
        answer = True
        result = self.sol.wordPatternMatch(pattern, str)
        self.assertEqual(answer, result)

    def test_case3(self):
        pattern = "aabb"
        str = "xyzabcxzyabc"
        answer = False
        result = self.sol.wordPatternMatch(pattern, str)
        self.assertEqual(answer, result)

    def test_case4(self):
        pattern = "abba"
        str = "dogdogdogdog"
        answer = False
        result = self.sol.wordPatternMatch(pattern, str)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""

回溯法
复杂度
时间 O(N) 空间 O(N)

思路
因为目标字符串可以任意划分，所以我们不得不尝试所有可能性。这里通过深度优先搜索的回溯法，对于pattern中每个字母，在str中尝试所有的划分方式，
如果划分出来的子串可以用这个字母映射，或者可以建立一个新的字母和字符串的映射关系，我们就继续递归判断下一个pattern中的字母。



public class Solution {
    
    Map<Character, String> map;
    Set<String> set;
    boolean res;
    
    public boolean wordPatternMatch(String pattern, String str) {
        // 和I中一样，Map用来记录字符和字符串的映射关系
        map = new HashMap<Character, String>();
        // Set用来记录哪些字符串被映射了，防止多对一映射
        set = new HashSet<String>();
        res = false;
        // 递归回溯
        helper(pattern, str, 0, 0);
        return res;
    }
    
    public void helper(String pattern, String str, int i, int j){
        // 如果pattern匹配完了而且str也正好匹配完了，说明有解
        if(i == pattern.length() && j == str.length()){
            res = true;
            return;
        }
        // 如果某个匹配超界了，则结束递归
        if(i >= pattern.length() || j >= str.length()){
            return;
        }
        char c = pattern.charAt(i);
        // 尝试从当前位置到结尾的所有划分方式
        for(int cut = j + 1; cut <= str.length(); cut++){
            // 拆出一个子串
            String substr = str.substring(j, cut);
            // 如果这个子串没有被映射过，而且当前pattern的字符也没有产生过映射
            // 则新建一对映射，并且继续递归求解
            if(!set.contains(substr) && !map.containsKey(c)){
                map.put(c, substr);
                set.add(substr);
                helper(pattern, str, i + 1, cut);
                map.remove(c);
                set.remove(substr);
            // 如果已经有映射了，但是是匹配的，也继续求解
            } else if(map.containsKey(c) && map.get(c).equals(substr)){
                helper(pattern, str, i + 1, cut);
            }
            // 否则跳过该子串，尝试下一种拆分
        }
    }
}

"""