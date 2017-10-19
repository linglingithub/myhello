"""
LongestPalindromicSubstring

Given a string S, find the longest palindromic substring in S.
You may assume that the maximum length of S is 1000,
and there exists one unique longest palindromic substring.

 String
Hide Similar Problems (H) Shortest Palindrome (E) Palindrome Permutation (H) Palindrome Pairs

http://www.geeksforgeeks.org/longest-palindrome-substring-set-1/
http://www.geeksforgeeks.org/longest-palindromic-substring-set-2/
http://www.programcreek.com/2013/12/leetcode-solution-of-longest-palindromic-substring-java/
http://www.cnblogs.com/zuoyuan/p/3777721.html

"""

import unittest


class Solution:
    # @param {string} s input string
    # @return {string} the longest palindromic substring
    def longestPalindrome(self, s):
        if not s:
            return ""
        n = len(s)
        res = s[0]  # not "", should be signle first char, case4
        dp = [ [True if i>=j else False for j in range(n)] for i in range(n)]  # thinks about when dp[i+1][j-1] comes to left >= right
        for i in range(n-2, -1, -1):  # think about how dp goes, i should start from n-1 downward
            for j in range(i+1, n):
                dp[i][j] = True if s[i] == s[j] and dp[i+1][j-1] else False
                if dp[i][j] and j-i+1 > len(res):
                    res = s[i: j+1]
        return res


    def longestPalindrome1(self, s):
        # Write your code here
        if not s:
            return ""
        n = len(s)
        result = ""
        for i in range(n):
            sub_odd = self.search_str(s, i, i)
            result = sub_odd if len(sub_odd) > len(result) else result
            sub_even = self.search_str(s, i, i + 1)
            result = sub_even if len(sub_even) > len(result) else result
        return result

    def search_str(self, s, i, j):
        res = ""
        l, r = i, j
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                l -= 1
                r += 1
            else:
                break
        res = s[l + 1: r]  #note here should use l+1, r, because s[l] != l[r] and it breaks the loop
        return res



class Solution1(object):
    def longestPalindrome(self, s):
        result = ""
        for i in range(len(s)):
            pal_odd = self.getlongestpalindrome(s, i, i)
            result = pal_odd if len(pal_odd) > len(result) else result
            pal_even = self.getlongestpalindrome(s, i, i+1)
            result = pal_even if len(pal_even) > len(result) else result
        return result

    def getlongestpalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r] # l+1 here because when out of loop, l is -1 to the unequal letter, r is +1 also, but substring will cut it. so only l+1

    def longestPalindrome2(self, s): #case 4 time limit exceed, DP is not necessarily the better way
        if s is None or len(s) < 1:
            return ""
        if len(s) == 1:
            return s
        palindrome_matrix = [[0 for j in range(len(s))] for i in range(len(s))]
        result = ""
        for i in range(len(s)):
            palindrome_matrix[i][i] = True
        for i in range(len(s)):
            for j in range(len(s)-1, i, -1):
                if self.isPalindrome_dp(s, i, j, palindrome_matrix):
                    if j-i+1 > len(result):
                        result = s[i:j+1]
        return result

    def isPalindrome_dp(self, s, start, end, palindrome_matrix):
        a = start
        b = end
        if a == b:
            return True
        else:
            if palindrome_matrix[a][b] == 0:
                if a + 1 <= b-1:
                    palindrome_matrix[a][b] = s[a] == s[b] and self.isPalindrome_dp(s, a+1, b-1, palindrome_matrix)
                else:
                    palindrome_matrix[a][b] = s[a] == s[b]
        return palindrome_matrix[start][end]



    def longestPalindrome1(self, s): # case 3 time limit exceeded
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) < 1:
            return ""
        if len(s) == 1:
            return s
        result = ""
        i = 0
        for i in range(0, len(s)):
            j = len(s) - 1
            while i < j:
                if self.isPalindrome(s[i: j+1]):
                    if len(s[i: j+1]) > len(result):
                        result = s[i: j+1]
                    break
                j -= 1
        return result

    def isPalindrome(self, s):
        if s is None or len(s)<1:
            return False
        is_palindrome = True
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                is_palindrome = False
                break
            i += 1
            j -= 1
        return is_palindrome





class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        s = "aba"
        answer = "aba"
        result = self.sol.longestPalindrome(s)
        self.assertEqual(answer, result)

    def test_case2(self):
        s = "abb"
        answer = "bb"
        result = self.sol.longestPalindrome(s)
        self.assertEqual(answer, result)

    def test_case3(self):
        s = "rgczcpratwyqxaszbuwwcadruayhasynuxnakpmsyhxzlnxmdtsqqlmwnbxvmgvllafrpmlfuqpbhjddmhmbcgmlyeypkfpreddyencsdmgxysctpubvgeedhurvizgqxclhpfrvxggrowaynrtuwvvvwnqlowdihtrdzjffrgoeqivnprdnpvfjuhycpfydjcpfcnkpyujljiesmuxhtizzvwhvpqylvcirwqsmpptyhcqybstsfgjadicwzycswwmpluvzqdvnhkcofptqrzgjqtbvbdxylrylinspncrkxclykccbwridpqckstxdjawvziucrswpsfmisqiozworibeycuarcidbljslwbalcemgymnsxfziattdylrulwrybzztoxhevsdnvvljfzzrgcmagshucoalfiuapgzpqgjjgqsmcvtdsvehewrvtkeqwgmatqdpwlayjcxcavjmgpdyklrjcqvxjqbjucfubgmgpkfdxznkhcejscymuildfnuxwmuklntnyycdcscioimenaeohgpbcpogyifcsatfxeslstkjclauqmywacizyapxlgtcchlxkvygzeucwalhvhbwkvbceqajstxzzppcxoanhyfkgwaelsfdeeviqogjpresnoacegfeejyychabkhszcokdxpaqrprwfdahjqkfptwpeykgumyemgkccynxuvbdpjlrbgqtcqulxodurugofuwzudnhgxdrbbxtrvdnlodyhsifvyspejenpdckevzqrexplpcqtwtxlimfrsjumiygqeemhihcxyngsemcolrnlyhqlbqbcestadoxtrdvcgucntjnfavylip"
        answer = "qgjjgq"
        result = self.sol.longestPalindrome(s)
        self.assertEqual(answer, result)

    def test_case4(self):
        s = "lcnvoknqgejxbfhijmxglisfzjwbtvhodwummdqeggzfczmetrdnoetmcydwddmtubcqmdjwnpzdqcdhplxtezctvgnpobnnscrmeqkwgiedhzsvskrxwfyklynkplbgefjbyhlgmkkfpwngdkvwmbdskvagkcfsidrdgwgmnqjtdbtltzwxaokrvbxqqqhljszmefsyewwggylpugmdmemvcnlugipqdjnriythsanfdxpvbatsnatmlusspqizgknabhnqayeuzflkuysqyhfxojhfponsndytvjpbzlbfzjhmwoxcbwvhnvnzwmkhjxvuszgtqhctbqsxnasnhrusodeqmzrlcsrafghbqjpyklaaqximcjmpsxpzbyxqvpexytrhwhmrkuybtvqhwxdqhsnbecpfiudaqpzsvfaywvkhargputojdxonvlprzwvrjlmvqmrlftzbytqdusgeupuofhgonqoyffhmartpcbgybshllnjaapaixdbbljvjomdrrgfeqhwffcknmcqbhvulwiwmsxntropqzefwboozphjectnudtvzzlcmeruszqxvjgikcpfclnrayokxsqxpicfkvaerljmxchwcmxhtbwitsexfqowsflgzzeynuzhtzdaixhjtnielbablmckqzcccalpuyahwowqpcskjencokprybrpmpdnswslpunohafvminfolekdleusuaeiatdqsoatputmymqvxjqpikumgmxaxidlrlfmrhpkzmnxjtvdnopcgsiedvtfkltvplfcfflmwyqffktsmpezbxlnjegdlrcubwqvhxdammpkwkycrqtegepyxtohspeasrdtinjhbesilsvffnzznltsspjwuogdyzvanalohmzrywdwqqcukjceothydlgtocukc"
        answer = "lbabl"
        result = self.sol.longestPalindrome(s)
        self.assertEqual(answer, result)

    def test_case5(self):  # ====>
        s = "a"
        answer = "a"
        result = self.sol.longestPalindrome(s)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner.run(suite)


if __name__ == '__main__':
    main()