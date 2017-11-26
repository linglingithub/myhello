#coding=utf-8

import unittest

"""

634. Word Squares 

 Description
 Notes
 Testcase
 Judge
Given a set of words without duplicates, find all word squares you can build from them.

A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max
(numRows, numColumns).

For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both 
horizontally and vertically.

b a l l
a r e a
l e a d
l a d y
 Notice

There are at least 1 and at most 1000 words.
All words will have the exact same length.
Word length is at least 1 and at most 5.
Each word contains only lowercase English alphabet a-z.
Have you met this question in a real interview? Yes
Example
Given a set ["area","lead","wall","lady","ball"]
return [["wall","area","lead","lady"],["ball","area","lead","lady"]]
Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word 
square matters).

Given a set ["abat","baba","atan","atal"]
return [["baba","abat","baba","atan"],["baba","abat","baba","atal"]]
Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word 
square matters).
Tags 
Trie Backtracking Google
Related Problems 
Hard Boggle Game 18 %
Hard K Edit Distance 26 %
Medium Implement Trie


"""


class Solution:
    """
    # run time 2338ms, use self implemented trie to keep prefix, slower than using dict, see solution 1
    @param: words: a set of words without duplicates
    @return: all word squares
    """

    def wordSquares(self, words):
        # write your code here
        if not words:
            return []
        m, n = len(words), len(words[0])
        trie = TrieTree()
        for word in words:
            trie.add_word(word)
        res = []
        # print(wdict)
        self.dfs(words, trie, [], 0, res)
        return res

    def dfs(self, words, trie, matrix, idx, res):
        # print(idx, '---', matrix)
        if idx >= len(words[0]):
            res.append(matrix)
            return
        if idx == 0:
            for word in words:
                self.dfs(words, trie, [word], 1, res)
        else:
            prefix = "".join([row[idx] for row in matrix])
            # print("prefix: ", prefix)
            next_words = trie.get_prefix_words(prefix)
            if not next_words:
                return
            for next_word in next_words:
                self.dfs(words, trie, matrix + [next_word], idx + 1, res)


class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.words = []


class TrieTree(object):
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root
        for char in word:
            tmp = node.children.get(char)
            if not tmp:
                node.children[char] = TrieNode()
            node.children[char].words.append(word)
            node = node.children[char]
        return self.root

    def get_prefix_words(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return node.words



class Solution1:
    """
    runs 1263ms, use dict to keep prefix
    @param: words: a set of words without duplicates
    @return: all word squares
    """

    def wordSquares(self, words):
        # write your code here
        if not words:
            return []
        m, n = len(words), len(words[0])
        wdict = {}
        for word in words:
            for j in range(n):
                prefix = word[:j + 1]
                wdict[prefix] = wdict.get(prefix, []) + [word]
        res = []
        # print(wdict)
        self.dfs(words, wdict, [], 0, res)
        return res

    def dfs(self, words, wdict, matrix, idx, res):
        # print(idx, '---', matrix)
        if idx >= len(words[0]):
            res.append(matrix)
            return
        if idx == 0:
            for word in words:
                self.dfs(words, wdict, [word], 1, res)
        else:
            prefix = "".join([row[idx] for row in matrix])
            # print("prefix: ", prefix)
            next_words = wdict.get(prefix)
            if not next_words:
                return
            for next_word in next_words:
                self.dfs(words, wdict, matrix + [next_word], idx + 1, res)


class Solution_wrong_problemShowsThatWordCanBeUsedRepeatedly:
    """
    @param: words: a set of words without duplicates
    @return: all word squares
    """

    def wordSquares(self, words):
        # write your code here
        if not words:
            return []
        m, n = len(words), len(words[0])
        wdict = {}
        for word in words:
            for j in range(n):
                prefix = word[:j + 1]
                wdict[prefix] = wdict.get(prefix, []) + [word]
        res = []
        used = {}
        print(wdict)
        self.dfs(words, wdict, [], 0, used, res)
        return res

    def dfs(self, words, wdict, matrix, idx, used, res):
        print(idx, '---', matrix)
        if idx >= len(words[0]):
            res.append(matrix)
            return
        if idx == 0:
            for word in words:
                self.dfs(words, wdict, [word], 1, {word: True}, res)
        else:
            prefix = "".join([row[idx] for row in matrix])
            print("prefix: ", prefix)
            next_words = wdict.get(prefix)
            if not next_words:
                return
            for next_word in next_words:
                if not used.get(next_word):
                    used.update({next_word: True})
                    self.dfs(words, wdict, matrix + [next_word], idx + 1, used, res)
                    del used[next_word]

class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = ["area","lead","wall","lady","ball"]
        answer = [["wall","area","lead","lady"],["ball","area","lead","lady"]]
        result = self.sol.testm(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = ["abat","baba","atan","atal"]
        answer = [["baba","abat","baba","atan"],["baba","abat","baba","atal"]]
        result = self.sol.testm(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()


"""

https://scottduan.gitbooks.io/leetcode-review/word_squares.html

My first approach is brute-force, try every possible word sequences, and use the solution of Problem 422 
(https://leetcode.com/problems/valid-word-square/) to check each sequence. This solution is straightforward, but too 
slow (TLE).
A better approach is to check the validity of the word square while we build it. Example: 
["area","lead","wall","lady","ball"] We know that the sequence contains 4 words because the length of each word is 4. 
Every word can be the first word of the sequence, let's take "wall" for example. Which word could be the second word? 
Must be a word start with "a" (therefore "area"), because it has to match the second letter of word "wall". Which word 
could be the third word? Must be a word start with "le" (therefore "lead"), because it has to match the third letter of 
word "wall" and the third letter of word "area". What about the last word? Must be a word start with "lad" 
(therefore "lady"). For the same reason above.
The picture below shows how the prefix are matched while building the sequence.

In order for this to work, we need to fast retrieve all the words with a given prefix. There could be 2 ways doing this:
Using a hashtable, key is prefix, value is a list of words with that prefix. 
Trie, we store a list of words with the prefix on each trie node. The implemented below uses Trie.

public class Solution {
    class TrieNode {
        List<String> startWith;
        TrieNode[] children;

        TrieNode() {
            startWith = new ArrayList<>();
            children = new TrieNode[26];
        }
    }

    class Trie {
        TrieNode root;

        Trie(String[] words) {
            root = new TrieNode();
            for (String w : words) {
                TrieNode cur = root;
                for (char ch : w.toCharArray()) {
                    int idx = ch - 'a';
                    if (cur.children[idx] == null)
                        cur.children[idx] = new TrieNode();
                    cur.children[idx].startWith.add(w);
                    cur = cur.children[idx];
                }
            }
        }

        List<String> findByPrefix(String prefix) {
            List<String> ans = new ArrayList<>();
            TrieNode cur = root;
            for (char ch : prefix.toCharArray()) {
                int idx = ch - 'a';
                if (cur.children[idx] == null)
                    return ans;

                cur = cur.children[idx];
            }
            ans.addAll(cur.startWith);
            return ans;
        }
    }

    public List<List<String>> wordSquares(String[] words) {
        List<List<String>> ans = new ArrayList<>();
        if (words == null || words.length == 0)
            return ans;
        int len = words[0].length();
        Trie trie = new Trie(words);
        List<String> ansBuilder = new ArrayList<>();
        for (String w : words) {
            ansBuilder.add(w);
            search(len, trie, ans, ansBuilder);
            ansBuilder.remove(ansBuilder.size() - 1);
        }

        return ans;
    }

    private void search(int len, Trie tr, List<List<String>> ans,
            List<String> ansBuilder) {
        if (ansBuilder.size() == len) {
            ans.add(new ArrayList<>(ansBuilder));
            return;
        }

        int idx = ansBuilder.size();
        StringBuilder prefixBuilder = new StringBuilder();
        for (String s : ansBuilder)
            prefixBuilder.append(s.charAt(idx));
        List<String> startWith = tr.findByPrefix(prefixBuilder.toString());
        for (String sw : startWith) {
            ansBuilder.add(sw);
            search(len, tr, ans, ansBuilder);
            ansBuilder.remove(ansBuilder.size() - 1);
        }
    }
}

=============================================

http://bookshadow.com/weblog/2016/10/16/leetcode-word-squares/

解题思路：
深度优先搜索（DFS）+ 剪枝（Pruning）

首先构建一个单词前缀prefix->单词word的字典mdict

深度优先搜索search(word, line)，其中word是当前单词，line是行数

利用变量matrix记录当前已经生成的单词

前缀prefix = matrix[0..line][line]，如果prefix对应单词不存在，则可以剪枝

否则枚举mdict[prefix]，并递归搜索
Python代码：
class Solution(object):
    def wordSquares(self, words):

        m = len(words)
        n = len(words[0]) if m else 0
        mdict = collections.defaultdict(set)
        for word in words:
            for i in range(n):
                mdict[word[:i]].add(word)
        matrix = []
        ans = []
        def search(word, line):
            matrix.append(word)
            if line == n:
                ans.append(matrix[:])
            else:
                prefix = ''.join(matrix[x][line] for x in range(line))
                for word in mdict[prefix]:
                    search(word, line + 1)
            matrix.pop()
        for word in words:
            search(word, 1)
        return ans

##  1410 ms

"""
#-*- coding:utf-8 -*-
