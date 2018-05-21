#coding=utf-8

import unittest

"""
418. Sentence Screen Fitting
DescriptionHintsSubmissionsDiscussSolution
Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given sentence can be fitted on the screen.

Note:

A word cannot be split into two lines.
The order of words in the sentence must remain unchanged.
Two consecutive words in a line must be separated by a single space.
Total words in the sentence won't exceed 100.
Length of each word is greater than 0 and won't exceed 10.
1 ≤ rows, cols ≤ 20,000.
Example 1:

Input:
rows = 2, cols = 8, sentence = ["hello", "world"]

Output: 
1

Explanation:
hello---
world---

The character '-' signifies an empty space on the screen.
Example 2:

Input:
rows = 3, cols = 6, sentence = ["a", "bcd", "e"]

Output: 
2

Explanation:
a-bcd- 
e-a---
bcd-e-

The character '-' signifies an empty space on the screen.
Example 3:

Input:
rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]

Output: 
1

Explanation:
I-had
apple
pie-I
had--

The character '-' signifies an empty space on the screen.

Difficulty:Medium
Total Accepted:20.1K
Total Submissions:71K
Contributor:LeetCode
Companies 

Related Topics 
Dynamic Programming

"""


class Solution:
    def wordsTyping(self, sentence, rows, cols):
        """
        Brute force way:
            loop through the rows, and loop through the sentence, check row by row how the sentence will be fitted, and keep                             count of how many times the sentence is finished. The returned count will be the result.
            Time: O(rows) * O(sentence)
            Space: O(1)

        Optimize:
            There can be repeated cases when at the beginning of each row, with the k-th word in sentence, (1) what to expect at
            the next row, l-th word? (2) does this need to increase ( 0, 1 or more?) the sentence count fitted?
            whith this info, loop through the rows and cal the total count.
            Time: O(rows) + O(sentence) * O(cols)
            Space: O(sentence)

        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        # sanity check
        if not sentence:
            return -1
        start_word_cache = self._preprocess(sentence, cols)
        # return a list with dp[i] : begin at i-indx word in sentence, (j, cnt)
        # where j is the j-idx word in sentence for next row, and cnt is the sentence
        # count to increase for finishing the row
        result = 0
        start = 0
        for i in range(rows):
            start, increase = start_word_cache[start]
            result += increase
        return result

    def _preprocess(self, sentence, cols):  # the ntimes_row optimization improves from 300+ms to 64ms (98% +???)
        nwords = len(sentence)
        word_len = [len(word) for word in sentence]
        dp = [(0, 0) for _ in range(nwords)]
        ntimes_row = (cols + 1) // (sum(word_len) + nwords)
        for widx in range(nwords):
            next_idx = widx
            increase = ntimes_row
            remains = cols - ntimes_row * (sum(word_len) + nwords)
            while remains > 0:
                if remains >= word_len[next_idx]:  #!!!! shou be next_idx here, not widx
                    remains -= word_len[next_idx] + 1  #!!! next_idx, and update remains before increase next_idx
                    next_idx += 1
                    if next_idx == nwords:
                        increase += 1
                        next_idx = 0
                else:
                    break
            dp[widx] = (next_idx, increase)
        return dp

    def _preprocess1(self, sentence, cols):
        nwords = len(sentence)
        word_len = [len(word) for word in sentence]
        dp = [(0, 0) for _ in range(nwords)]
        for widx in range(nwords):
            next_idx = widx
            increase = 0
            remains = cols
            while remains > 0:
                if remains >= word_len[next_idx]:  #!!!! shou be next_idx here, not widx
                    remains -= word_len[next_idx] + 1  #!!! next_idx, and update remains before increase next_idx
                    next_idx += 1
                    if next_idx == nwords:
                        increase += 1
                        next_idx = 0
                else:
                    break
            dp[widx] = (next_idx, increase)
        return dp


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = 1
        answer = 1
        result = self.sol.testm(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()


"""
https://leetcode.com/problems/sentence-screen-fitting/discuss/90881/Python-108ms-solution
My solution was to preprocess the sentence in order to determine at each index of the sentence how many more words can 
fit in the column. After that I simply iterate through the rows and increment the total word count.

class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        word_nums = self.preprocess(sentence, cols)          
        word_count = 0                
        for _ in xrange(rows):
            word_count += word_nums[word_count % len(sentence)]
        return word_count/len(sentence)
        
    # Preprocessing 
    def preprocess(self, sentence, cols):
        word_nums = [0] * len(sentence)
        word_ptr, word_sum = 0, 0
        word_len = len(sentence[0])
        for i, word in enumerate(sentence):
            while(word_sum + word_len <= cols):
                word_sum += word_len
                word_ptr += 1
                word_len = len(sentence[word_ptr % len(sentence)]) + 1
            word_nums[i] = word_ptr - i
            word_sum -= (len(word) + 1)
        return word_nums
        
        

"""
#-*- coding:utf-8 -*-
