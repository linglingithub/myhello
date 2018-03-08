#coding=utf-8

import unittest

"""



"""


class Solution(object):
    def longestCommonSubstring(self, s, t):
        """
        
        :param s: 
        :param t: 
        :return result: string of longest common substring of s and t 
        """
        if not s or not t:
            return ""
        map = {}
        result = ""
        if len(s) > len(t):
            s, t = t, s
        for idx, char in enumerate(s):
            # print("TRACE: ", char, map.get(char, []))
            # map[char] = map.get(char, []).append(idx)  // [].append return NONE!!!
            if map.get(char):
                map[char].append(idx)
            else:
                map[char] = [idx]
        for idx, char in enumerate(t):
            if char not in map:
                continue
            for sidx in map[char]:
                start, end = self.check_substr(s, t, sidx, idx)
                if (end - start + 1) > len(result):
                    result = t[start: end + 1]
        return result

    def check_substr(self, s, t, sidx, tidx):
        """
        
        :param s: 
        :param t: 
        :param sidx: 
        :param tidx: 
        :return: start, end index for string t
        """
        shift = 0 # current good one
        while sidx + shift + 1< len(s) and tidx + shift + 1 < len(t):
            if s[sidx + shift + 1] == t[tidx + shift + 1]:
                shift += 1
            else:
                break # !!! important, otherwise infinite loop
        return tidx, tidx + shift





class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        s, t = "aa", "bbb"
        answer = ""
        result = self.sol.longestCommonSubstring(s, t)
        self.assertEqual(answer, result)

    def test_case2(self):
        s, t = "aabbc", "bbb"
        answer = "bb"
        result = self.sol.longestCommonSubstring(s, t)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()