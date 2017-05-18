#coding=utf-8

import unittest


"""

Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.
For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
For "bbbbb" the longest substring is "b", with the length of 1.

Hash Table Two Pointers String
Hide Similar Problems (H) Longest Substring with At Most Two Distinct Characters


"""


class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s): # ref idea, use dict for position !!!
        if not s:
            return 0
        pos = {}
        result = 0
        i = 0
        for j in range(len(s)):
            char = s[j]
            if char not in pos or pos[char] < i:
                pos[char] = j
                result = max(result, j-i+1)
            else:
                char_pos = pos[char]
                pos[char] = j  # don't forget to update new pos of char here
                i = char_pos + 1
        return result

    def lengthOfLongestSubstring_wrongonref(self, s): # ref idea, use dict for position !!!, wrong for case2
        if not s:
            return 0
        pos = {}
        result = 0
        i = 0
        for j in range(len(s)):
            char = s[j]
            if char not in pos:
                pos[char] = j
                result = max(result, j-i+1)
            else:
                char_pos = pos[char]
                i = char_pos + 1
        return result


    def lengthOfLongestSubstring4(self, s): # good self idea, 20170517
        """
        rev keep non repeating character
        :param s: 
        :return: 
        """
        if not s:
            return 0
        i, j = 0, 0
        rev = {}
        result = 0
        while j < len(s):
            char = s[j]
            if char not in rev:
                rev[char] = 1
                result = max(result, j-i+1)
            else:
                rev[char] += 1
                while s[i] != char:
                    del rev[s[i]]
                    i += 1
                rev[char] -= 1
                i += 1
            j += 1
        return result


    def lengthOfLongestSubstring3(self, s): # can be simpler , 20170517
        # write your code here
        if not s:
            return 0
        i, j = 0, 0
        rev = {}
        result = 0
        while j < len(s):
            char = s[j]
            if char not in rev:
                rev[char] = 1
                j += 1
                result = max(result, j-i)
                continue
            else:
                rev[char] += 1
                while True:
                    tmp = s[i]
                    rev[tmp] -= 1
                    i += 1
                    if rev[tmp] == 0:
                        del rev[tmp]
                    if rev[char] <= 1:
                        break
                j += 1  # don't forget this , otherwise wrong
        return result

    def lengthOfLongestSubstring1(self, s):
        maxlen = 0
        subStr = ''
        tail = 0
        for head in xrange(len(s)):
            if s[head] not in subStr:
                subStr += s[head]
            else:
                maxlen = max(maxlen, len(subStr))
                while s[tail] != s[head]:
                    tail += 1
                tail += 1
                subStr = s[tail: head+1]
        return max(maxlen, len(subStr))

    def lengthOfLongestSubstring2(self, s):
        maxlen = 0
        subDict = {}
        lastRepeat = -1
        for head in xrange(len(s)):
            if s[head] not in subDict:
                subDict[s[head]] = head
            else:
                if lastRepeat < subDict[s[head]]:
                    maxlen = max(maxlen, head - 1 - lastRepeat)
                    lastRepeat = subDict[s[head]]
                    subDict[s[head]] = head
                else:
                    subDict[s[head]] = head
        return max(maxlen, len(s) - 1 - lastRepeat)

class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = "aaaa"
        answer = 1
        result = self.sol.lengthOfLongestSubstring(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = "an++--viaj"
        answer = 5
        result = self.sol.lengthOfLongestSubstring(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()

"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ans = 0
        # left用于记录合法的左边界位置，last用于记录字符上一次出现的位置
        left = 0
        last = {}
        for i in range(len(s)):
            # 子串中出现重复字符，变更left至上一次s[i]出现位置之后，使得子串合法
            if s[i] in last and last[s[i]] >= left:
                left = last[s[i]] + 1
            last[s[i]] = i
            ans = max(ans, i - left + 1)
        return ans
        

"""

# if __name__ == '__main__':
#     sol = Solution()
#     s = 'aab'
#     #s = 'eee'
#     #s = "qwnfenpglqdq"
#     print sol.lengthOfLongestSubstring(s)