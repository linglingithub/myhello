"""
Unique Binary Search Trees

Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
Subscribe to see which companies asked this question

Hide Tags Tree Dynamic Programming
Hide Similar Problems (M) Unique Binary Search Trees II


"""

import unittest

class Solution(object):

    # http://fisherlei.blogspot.com/2013/03/leetcode-unique-binary-search-trees.html
    # different number as root and count the number of left child and right child.
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp = [ 0 for x in range(n+1)], can't init this way, if n is small, then will go out of index when return result for n <= 2
        # dp[0] = 1
        # dp[1] = 1
        # dp[2] = 2
        dp = [1, 1, 2]
        if n <= 2:
            return dp[n]
        k = 3
        while k <= n:
            result = 0
            for i in range(k):
                left = i
                right = k - (i + 1)
                result += dp[left] * dp[right]
                #print "k, i, result: ", k, i, result
            #dp.[k] = result
            dp.append(result)
            #print "k, dp[k]: ", k, dp[k]
            k += 1
        return dp[n]


    def numTrees_ref(self, n):
        # found this after solving problem, code looks simpler
        # http: // www.cnblogs.com / zuoyuan / p / 3747824.html
        dp = [1, 1, 2]
        if n <= 2:
            return dp[n]
        else:
            dp += [0 for i in range(n - 2)]
            for i in range(3, n + 1):
                for j in range(1, i + 1):
                    dp[i] += dp[j - 1] * dp[i - j]
            return dp[n]

    def numTrees_tle(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        if n == 2:
            return 2
        result = 0
        for k in range(n):
            left = k
            right = n - (k + 1)
            result += self.numTrees(left) * self.numTrees(right)
        return result



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        n = 3
        answer = 5
        result = self.sol.numTrees(n)
        self.assertEqual(answer, result)

    def test_case2(self): #Time Limit Exceeded
        n = 19
        answer = 1767263190
        result = self.sol.numTrees(n)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()