#coding=utf-8
__author__ = 'linglin'

"""
30. Substring with Concatenation of All Words

You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of
substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).

Subscribe to see which companies asked this question

Hide Tags Hash Table Two Pointers String
Hide Similar Problems (H) Minimum Window Substring

Hard

"""

import unittest


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        word_dict = {}
        for word in words:
            word_dict[word] = 1
        self.word_len = len(words[0])
        self.word_cnt = len(words)
        result = []
        i, j = 0, 0
        dp = [{} for _ in range(self.word_len)]
        end = len(s) - self.word_len * len(words)
        while i < end:
            self.search(s, word_dict, dp, result, i)
        return result

    def search(self, s, word_dict, dp, result, i):
        state = dp[i%self.word_len]

        j = i
        pos = j
        bag = {}
        potential = True
        if state != {}:
            j = state.get("j") + 1
            bag = state.get("bag")
            if i - self.word_len > 0 :
                bag[s[i-self.word_len: i]] -= 1
                if bag[s[i-self.word_len: i]] == 0:
                    del bag[s[i-self.word_len: i]]
        end = i + self.word_len * self.word_cnt -1
        while j <= end:
            tmp = s[j: j+self.word_len] # should not be j+self.word_len-1
            if tmp in word_dict:
                if tmp not in bag:
                    bag[tmp] = 1
                    pos = j + self.word_len - 1  # remember no only j here
                    j += self.word_len
                else:
                    potential = True # but can not update the bag or pos, cause there would be repeated words, and should break
                    break
            else:
                potential = False
                break
        if len(bag) == self.word_cnt:
            result.append(i)
        if potential:
            if pos != i:
                state["j"] = pos
                state["bag"] = bag
                dp[i%self.word_len] = state
        else:
            dp[i % self.word_len] = {}


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        s = "barfoothefoobarman"
        words = ["foo", "bar"]
        answer = [0, 9]
        result = self.sol.findSubstring(s, words)
        self.assertEqual(sorted(answer), sorted(result))


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
