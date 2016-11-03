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

    def lengthOfLongestSubstring(self, s):
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


if __name__ == '__main__':
    sol = Solution()
    s = 'aab'
    #s = 'eee'
    #s = "qwnfenpglqdq"
    print sol.lengthOfLongestSubstring(s)