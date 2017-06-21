#coding=utf-8

import unittest

"""
Scramble String

Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

Have you met this question in a real interview? Yes
Example
Challenge 
O(n3) time

Tags 
String Dynamic Programming

"""


class Solution:
    # @param {string} s1 A string
    # @param {string} s2 Another string
    # @return {boolean} whether s2 is a scrambled string of s1
    def isScramble(self, s1, s2):  # ref, from jiuzhang
        # Write your code here
        if len(s1)!=len(s2): return False
        if s1==s2: return True
        l1=list(s1); l2=list(s2)
        l1.sort();l2.sort()
        if l1!=l2: return False
        length=len(s1)
        for i in range(1,length):
            if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]): return True
            if self.isScramble(s1[:i],s2[length-i:]) and self.isScramble(s1[i:],s2[:length-i]): return True
        return False

class Solution_wrong_understanding_case4:
    # @param {string} s1 A string
    # @param {string} s2 Another string
    # @return {boolean} whether s2 is a scrambled string of s1
    def isScramble(self, s1, s2):
        # Write your code here
        if not s1 or not s2:
            return False
        if len(s1) != len(s2):
            return False
        n = len(s1)
        dp = {}

        result = self.check_scramble(s1, s2, 0, n - 1, 0, n - 1, dp)
        return result

    def check_scramble(self, s1, s2, l1, r1, l2, r2, dp):
        if l1 > r1 or l2 > r2:
            return False
        if l1 == r1:
            if s1[l1] == s2[l2]:
                return True
            else:
                return False
        else:
            if (l1, r1, l2, r2) in dp:
                return dp[(l1, r1, l2, r2)]
            elif s1[l1:r1 + 1] == s2[l2:r2 + 1]:
                dp[(l1, r1, l2, r2)] = True
                return True
            #mid = (l1 + r1) / 2 - 1
            len = (r1-l1+1)/2
            mid = l1 + len - 1
            n = mid - l1
            tmp1 = self.check_scramble(s1, s2, l1, mid, l2, l2 - l1 + mid, dp) and self.check_scramble(s1, s2, mid + 1,
                                                                                                       r1,
                                                                                                       l2 - l1 + mid + 1,
                                                                                                       r2, dp)
            if tmp1:
                dp[(l1, r1, l2, r2)] = tmp1
                return tmp1
            tmp2 = self.check_scramble(s1, s2, l1, mid, r2 - n, r2, dp) and self.check_scramble(s1, s2, mid + 1, r1, l2,
                                                                                                l2 + r1 - mid - 1, dp)
            tmp = tmp1 or tmp2
            dp[(l1, r1, l2, r2)] = tmp
            return tmp






class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()


    def test_case4(self): #=======> ?? what does this mean, scramble can cut anywhere? not only in the middle?
        s1 = "abb"
        s2 = "bab"
        answer = True
        result = self.sol.isScramble(s1, s2)
        self.assertEqual(answer, result)

    def test_case3(self): #=======>
        s1 = "abb"
        s2 = "bba"
        answer = True
        result = self.sol.isScramble(s1, s2)
        self.assertEqual(answer, result)

    def test_case2(self):
        s1 = "great"
        s2 = "rgeat"
        answer = True
        result = self.sol.isScramble(s1, s2)
        self.assertEqual(answer, result)

    def test_case1(self):
        s1 = "great"
        s2 = "rgtae"
        answer = True
        result = self.sol.isScramble(s1, s2)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-


'''

jiuzhang Java version


 /**
  * 本代码由九章算法编辑提供。版权所有，转发请注明出处。
  * - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
  * - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，Big Data 项目实战班，
  * - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
  */ 

// 记忆化搜索
public class Solution {
    /**
     * @param s1 A string
     * @param s2 Another string
     * @return whether s2 is a scrambled string of s1
     */
    HashMap<String, Boolean> hash = new HashMap<String, Boolean>();
    
    public boolean isScramble(String s1, String s2) {
        // Write your code here
        if (s1.length() != s2.length())
            return false;
            
        if (hash.containsKey(s1 + "#" + s2))
            return hash.get(s1 + "#" + s2);
        
        int n = s1.length();
        if (n == 1) {
            return s1.charAt(0) == s2.charAt(0);
        }
        for (int k = 1; k < n; ++k) {
            if (isScramble(s1.substring(0, k), s2.substring(0, k)) &&
                isScramble(s1.substring(k, n), s2.substring(k, n)) ||
                isScramble(s1.substring(0, k), s2.substring(n - k, n)) &&
                isScramble(s1.substring(k, n), s2.substring(0, n - k))
                ) {
                hash.put(s1 + "#" + s2, true);
                return true;
            }
        }
        hash.put(s1 + "#" + s2, false);
        return false;
    }
}

// 递推
public class Solution {
    /**
     * @param s1 A string
     * @param s2 Another string
     * @return whether s2 is a scrambled string of s1
     */
    public boolean isScramble(String s1, String s2) {
        // Write your code here
        if (s1.length() != s2.length())
            return false;
        int n = s1.length();
        boolean[][][] dp = new boolean[n][n][n+1];
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                dp[i][j][1] = s1.charAt(i) == s2.charAt(j);
            
        for (int len = 2; len <= n; ++len)
            for (int x = 0; x < n && x + len <= n; ++x)
                for (int y = 0; y < n && y + len <=n; ++y)
                    for (int k= 1; k < len; ++k)
                    dp[x][y][len] |= dp[x][y][k] && dp[x + k][y + k][len - k]
                    || dp[x][y + len - k][k] && dp[x + k][y][len - k];
    
        return dp[0][0][n];
    }
}

// 普通搜索
public class Solution {
    /**
     * @param s1 A string
     * @param s2 Another string
     * @return whether s2 is a scrambled string of s1
     */
    public boolean isScramble(String s1, String s2) {
        // Write your code here
        if (s1.length() != s2.length()) {
            return false;
        }
        
        if (s1.length() == 0 || s1.equals(s2)) {
            return true;
        }
        
        if (!isValid(s1, s2)) {
            return false;
        }// Base Cases
        
        
        for (int i = 1; i < s1.length(); i++) {
            String s11 = s1.substring(0, i);
            String s12 = s1.substring(i, s1.length());
            String s21 = s2.substring(0, i);
            String s22 = s2.substring(i, s2.length());
            String s23 = s2.substring(0, s2.length() - i);
            String s24 = s2.substring(s2.length() - i, s2.length());
            
            if (isScramble(s11, s21) && isScramble(s12, s22)) return true;
            if (isScramble(s11, s24) && isScramble(s12, s23)) return true;// cut 
            
        }
        return false;
    }
    
    
    private boolean isValid(String s1, String s2) {
        char[] arr1 = s1.toCharArray();
        char[] arr2 = s2.toCharArray();
        Arrays.sort(arr1);
        Arrays.sort(arr2);
        if (!(new String(arr1)).equals(new String(arr2))) {
            return false;
        }
        return true;
    }
}

// 记忆化搜索
public class Solution {
    /**
     * @param s1 A string
     * @param s2 Another string
     * @return whether s2 is a scrambled string of s1
     */
     
     private boolean checkScramble(String s1,int start1, String s2, int start2, int k, int [][][]visit) {
		if(visit[start1][start2][k] == 1)
            return true;
        if(visit[start1][start2][k] ==-1)
            return false;
        
        
        if (s1.length() != s2.length()) {
            visit[start1][start2][k] = -1;
            return false;
        }
        
        if (s1.length() == 0 || s1.equals(s2)) {
            visit[start1][start2][k] = 1;
            return true;
        }
        
        if (!isValid(s1, s2)) {
            visit[start1][start2][k] = -1;
            return false;
        }// Base Cases
        
        
        for (int i = 1; i < s1.length(); i++) {
            String s11 = s1.substring(0, i);
            String s12 = s1.substring(i, s1.length());
            
            String s21 = s2.substring(0, i);
            String s22 = s2.substring(i, s2.length());
            
            String s23 = s2.substring(0, s2.length() - i);
            String s24 = s2.substring(s2.length() - i, s2.length());
            
            if (checkScramble(s11,start1, s21, start2, i, visit) && checkScramble(s12, start1+i, s22, start2+i,k-i, visit))  {
                visit[start1][start2][k] = 1;
                return true;
            }
            
            if (checkScramble(s11,start1, s24, start2+k-i, i, visit) && checkScramble(s12,start1+i, s23,start2, k-i, visit))
            {
                visit[start1][start2][k] = 1;
                return true;
            }
        }
        visit[start1][start2][k] = -1;
        return false;
    }
    public boolean isScramble(String s1, String s2) {
        int len = s1.length();
        int [][][] visit = new int[len][len][len + 1];
        return checkScramble(s1,0,s2,0, len, visit);
    }
    
    
    private boolean isValid(String s1, String s2) {
        char[] arr1 = s1.toCharArray();
        char[] arr2 = s2.toCharArray();
        Arrays.sort(arr1);
        Arrays.sort(arr2);
        if (!(new String(arr1)).equals(new String(arr2))) {
            return false;
        }
        return true;
    }
}



'''