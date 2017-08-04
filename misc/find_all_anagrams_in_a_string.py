#coding=utf-8

import unittest

"""
438. Find All Anagrams in a String  (lincode: Substring Anagrams)

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".


Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

Easy

"""


class Solution(object):
    def findAnagrams(self, s, p):  # self rewrite according to ref
        if not s or not p:
            return []
        result = []
        from collections import Counter
        char_cnts = Counter(p)
        left, right = 0, 0
        total_cnt = len(p)
        while right < len(s):
            char = s[right]
            if char_cnts[char] > 0: # still needs the char
                total_cnt -= 1
            char_cnts[char] = char_cnts.get(char, 0) - 1
            if right >= len(p)-1:
                if total_cnt == 0:
                    result.append(left)
                lchar = s[left]
                if char_cnts[lchar] >= 0:
                    total_cnt += 1
                char_cnts[lchar] += 1
                left += 1
            right += 1
        return result





    def findAnagrams_self(self, s, p):
        """
        self, basic idea, 
        use the window to keep track of the target chars and counts(no non-target chars),
        use total_cnts to maintain that only valid number of (no more than required for each target char) chars are counted
        :param s: 
        :param p: 
        :return: 
        """
        if not s or not p:
            return []
        from collections import Counter
        char_cnts = Counter(p)
        total_cnts = 0
        window = {}
        left, right = 0, 0
        result = []
        while right < len(s):
            char = s[right]
            tmp_window_debug = s[left:right+1]
            if char in char_cnts:
                window[char] = window.get(char, 0) + 1
                if window.get(char) <= char_cnts[char]:
                    total_cnts += 1
            if right-left+1 == len(p):
                if total_cnts == len(p):
                    result.append(left)
                #else:   # should not put in else here, every time should check lchar, otherwise wrong for case1
                lchar = s[left]
                if lchar in char_cnts:
                    if window[lchar] <= char_cnts[lchar]: # should do this before window[lchar] -= 1
                        total_cnts -= 1
                    window[lchar] -= 1
                left += 1   # don't forget this !!!
            right += 1
        return result

    def findAnagrams_wrong(self, s, p):
        if not s or not p:
            return []
        from collections import Counter
        counts = Counter(p)
        left, right = 0, 0
        result = []
        count = len(p)
        import copy
        dict = copy.deepcopy(counts)
        while right < len(s):
            char = s[right]
            if char not in dict:
                right += 1
                left = right
                dict = copy.deepcopy(counts)
                continue

            if dict.get(char) > 0:
                count -= 1
                dict[char] -= 1


            if count == 0:
                result.append(left)
            if right - left == len(p)-1:
                dict[s[left]] += 1
                count += 1
                left += 1
            right += 1
        return result



    def findAnagrams_ref_explanation_below(self, s, p):  # _ref_

        ls, lp = len(s), len(p)
        count = lp
        from collections import Counter
        cp = Counter(p)
        ans = []
        for i in range(ls):
            char = s[i]
            tmp_debug_window = s[i-lp+1: i+1]
            if cp[char] >=1 :
                count -= 1
            cp[char] -= 1
            if i >= lp:
                char_l = s[i - lp]
                if cp[char_l] >= 0:
                    count += 1
                cp[char_l] += 1
            if count == 0:
                ans.append(i - lp + 1)
        return ans

    def findAnagrams_self_good(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if not p or not s or len(p) > len(s):
            return []
        from collections import Counter
        pattern = Counter(p)
        start, end = 0, 0
        m, n = len(s), len(p)
        count = n
        result = []
        while end < len(s):
            if s[end] not in pattern:
                end += 1
                start = end
                continue
            if start == end:
                pattern = Counter(p)
                count = n

            char = s[end]
            pattern[char] -= 1
            count -= 1
            if pattern[char] >= 0:
                if count == 0:
                    result.append(start)
                if end-start >= n-1:  # should not have chance to be >
                    lchar = s[start]
                    pattern[lchar] += 1
                    count += 1
                    start += 1
            else:
                while start < end and s[start] != char:
                    pattern[s[start]] += 1  # should be before start += 1, otherwise wrong, case5
                    start += 1
                    count += 1

                start += 1
                pattern[char] += 1
                count += 1
                if count == 0:
                    result.append(start)

            end += 1 #don't forget this

        return result









class Solution_AC_butNotGood(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if not p or not s or len(p) > len(s):  # check the length too, case 4
            return []
        from collections import Counter
        self.pattern = Counter(p)
        start, end = 0, 0
        match = {}
        count = 0
        n = len(s)
        result = []
        while end < len(p):
            char = s[end]
            if char in match:
                match[char] += 1
            else:
                match[char] = 1
            end += 1
        end -= 1 # don't forget this, otherwise wrong

        #while end < len(s):
        while True:
            if self.valid_match(match):
                result.append(start)
            if end == n-1:
                break
            a, b = s[start], s[end + 1]
            match[a] -= 1
            if match[a] == 0:
                del match[a]
            if b in match:
                match[b] += 1
            else:
                match[b] = 1
            start += 1
            end += 1
        return result

    def valid_match(self, match):
        if len(self.pattern) != len(match):
            return False
        for k in self.pattern.keys():
            if k in match and match[k] == self.pattern[k]:
                continue
            else:
                return False
        return True


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case5(self):  #====> p can be longer than s
        s = "abaacbabc"
        p = "abc"
        answer = [3,4,6]
        result = self.sol.findAnagrams(s, p)
        self.assertEqual(answer, result)

    def test_case4(self):  #====> p can be longer than s
        s = "aaaaaaaaaa"
        p = "aaaaaaaaaaaaa"
        answer = []
        result = self.sol.findAnagrams(s, p)
        self.assertEqual(answer, result)


    def test_case3(self):  #====> p can have repeated chars
        s = "baa"
        p = "aa"
        answer = [1]
        result = self.sol.findAnagrams(s, p)
        self.assertEqual(answer, result)


    def test_case1(self):
        s = "cbaebabacd"
        p = "abc"
        answer = [0, 6]
        result = self.sol.findAnagrams(s, p)
        self.assertEqual(answer, result)

    def test_case2(self):
        s = "abab"
        p = "ab"
        answer = [0, 1, 2]
        result = self.sol.findAnagrams(s, p)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""
some very simple codes, not easy to write like this


class Solution(object):
    def findAnagrams(self, s, p):

        ls, lp = len(s), len(p)
        count = lp
        cp = collections.Counter(p)
        ans = []
        for i in range(ls):
            if cp[s[i]] >=1 :
                count -= 1
            cp[s[i]] -= 1
            if i >= lp:
                if cp[s[i - lp]] >= 0:
                    count += 1
                cp[s[i - lp]] += 1
            if count == 0:
                ans.append(i - lp + 1)
        return ans
        
        
=======================================================
        
public List<Integer> findAnagrams(String s, String p) {
    List<Integer> list = new ArrayList<>();
    if (s == null || s.length() == 0 || p == null || p.length() == 0) return list;
    
    int[] hash = new int[256]; //character hash
    
    //record each character in p to hash
    for (char c : p.toCharArray()) {
        hash[c]++;
    }
    
    //two points, initialize count to p's length
    int left = 0, right = 0, count = p.length();
    
    while (right < s.length()) {
        //move right everytime, if the character exists in p's hash, decrease the count
        //current hash value >= 1 means the character is existing in p
        
        if (hash[s.charAt(right++)]-- >= 1) count--; 
        
        //when the count is down to 0, means we found the right anagram
        //then add window's left to result list
        
        if (count == 0) list.add(left);
    
        //if we find the window's size equals to p, then we have to move left (narrow the window) to find the new match window
        //++ to reset the hash because we kicked out the left
        //only increase the count if the character is in p
        //the count >= 0 indicate it was original in the hash, cuz it won't go below 0
        
        if (right - left == p.length() && hash[s.charAt(left++)]++ >= 0) count++;
    }
    return list;
}        
        

"""