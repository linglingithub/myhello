#coding=utf-8
__author__ = 'linglin'

"""

279. Perfect Squares


Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which
sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

Subscribe to see which companies asked this question

Hide Tags Dynamic Programming Breadth-first Search Math
Hide Similar Problems (E) Count Primes (M) Ugly Number II


Medium

"""



import unittest
import collections


class Solution:
    """
    @param: n: a positive integer
    @return: An integer
    """

    def numSquares_self(self,
                        n):  # since recursion exceeds maximum depth, try to do iterative way, 20+%; TLE on lint, case 4
        """
        init with perfect square itself
        then from 2 to n
        2 = 1 + 1
        3 = 1 + 2
        4 
        5 = 1 + 4 or 4 + 1
        6 = 1 + 5 or 4 + 2
        7 = 1 + 6 or 4 + 2
        8 = 1 + 7 or 4 + 4 
        9
        10 = 1 + 9 or 4 + 6 or 9 + 1
        ....
        and try to remove some repeated calculation, like 5 (1+4 and 4+1), 10 (1+9 and 9 + 1), 
        when n = j*j + i, search can stop where j*j>n/2

        :param n: 
        :return: 
        """
        if n <= 1:
            return n
        i = 0
        _res = {}
        while i ** 2 <= n:
            _res[i ** 2] = 1
            i += 1
        if n in _res:
            return _res[n]
        for i in range(2, n + 1):
            if i in _res:
                continue
            j = 1
            while j * j <= i / 2:
                tmp = _res[i - j * j] + 1
                _res[i] = min(_res[i], tmp) if i in _res else tmp
                j += 1
        return _res[n]




    def numSquares_math(self, n):  # ref, math way
        """
        这道题说是给我们一个正整数，求它最少能由几个完全平方数组成。这道题是考察四平方和定理，to be honest, 这是我第一次听说这个定理，
        天啦撸，我的数学是语文老师教的么?! 闲话不多扯，回来做题。先来看第一种很高效的方法，根据四平方和定理，任意一个正整数均可表示为4个
        整数的平方和，其实是可以表示为4个以内的平方数之和，那么就是说返回结果只有1,2,3或4其中的一个，首先我们将数字化简一下，由于一个数如
        果含有因子4，那么我们可以把4都去掉，并不影响结果，比如2和8,3和12等等，返回的结果都相同，读者可自行举更多的栗子。还有一个可以化简
        的地方就是，如果一个数除以8余7的话，那么肯定是由4个完全平方数组成，这里就不证明了，因为我也不会证明，读者可自行举例验证。那么做完
        两步后，一个很大的数有可能就会变得很小了，大大减少了运算时间，下面我们就来尝试的将其拆为两个平方数之和，如果拆成功了那么就会返回
        1或2，因为其中一个平方数可能为0. (注：由于输入的n是正整数，所以不存在两个平方数均为0的情况)。注意下面的!!a + !!b这个表达式，可
        能很多人不太理解这个的意思，其实很简单，感叹号!表示逻辑取反，那么一个正整数逻辑取反为0，再取反为1，所以用两个感叹号!!的作用就是看
        a和b是否为正整数，都为正整数的话返回2，只有一个是正整数的话返回1
        
        int numSquares(int n) {
            int ub = sqrt(n);
            for (int a=0; a<=ub; ++a) {
                for (int b=a; b<=ub; ++b) {
                    int c = sqrt(n - a*a - b*b);
                    if (a*a + b*b + c*c == n)
                        return !!a + !!b + !!c;
                }
            }
            return 4;
        }
        
        Explanation

I happen to have given a little talk about just this topic a while back in a number theory seminar. This problem is completely solved, in the sense of being reduced to simple checks of a number's prime factorization. A natural number is...

... a square if and only if each prime factor occurs to an even power in the number's prime factorization.
... a sum of two squares if and only if each prime factor that's 3 modulo 4 occurs to an even power in the number's prime factorization.
... a sum of three squares if and only if it's not of the form 4a(8b+7) with integers a and b.
... a sum of four squares. Period. No condition. You never need more than four.
Of course single squares can also be identified by comparing a given number with the square of the rounded root of the number.

The problem statement says "1, 4, 9, 16, ...", for some reason apparently excluding 0, but it really is a perfect square and the above theorems do consider it one. With that, you can for example always extend a sum of two squares a2+b2 to the sum of three squares a2+b2+02. Put differently, if n isn't a sum of three squares, then it also isn't a sum of two squares. So you can read the above statements as "... a sum of m (or fewer) squares". Thanks to ruben3 for asking about this in the comments.

In my above solutions, I first divide the given number by 4 as often as possible and then do the three-squares check. Dividing by 4 doesn't affect the other checks, and the n % 8 == 7 is cheaper than the prime factorization, so this saves time in cases where we do need four squares.

Armed with just the knowledge that you never need more than four squares, it's also easy to write O(n) solutions, e.g.:
        
        :param n: 
        :return: 
        """
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4

        for i in xrange(n+1):
            temp = i * i
            if temp <= n:
                if int((n - temp)** 0.5 ) ** 2 + temp == n:
                    return 1 + (0 if temp == 0 else 1)
            else:
                break
        return 3



    def numSquares_recursionExceed(self, n): # case 3, too deep recursion, not good
        # write your code here
        if n <= 1:
            return n
        i = 0
        _res = {}
        while i ** 2 <= n:
            _res[i ** 2] = 1
            i += 1
        if n in _res:
            return _res[n]
        self.helper(n, _res)
        return _res[n]

    def helper(self, n, res):
        if n in res:
            return res[n]
        j = 1
        while j * j < n:
            # res[n] = min(res[n-j**2]+1, res[n])  # wrong way to write, key error
            tmp = self.helper(n - j * j, res) + 1
            res[n] = min(tmp, res[n]) if n in res else tmp
            j += 1
        return res[n]


class Solution_ref(object):  # from leetcode discussion, runs 90+% on leetcode, still TLE on lint
    _dp = [0]

    def numSquares(self, n):
        """
        https://discuss.leetcode.com/topic/23812/static-dp-c-12-ms-python-172-ms-ruby-384-ms
        The comma here seems to change the expression ( int val) into an iterable (actually tuple) and can be appended to
        the end of a list???, if removed runs error
        :param n: 
        :return: 
        """
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i * i] for i in range(1, int(len(dp) ** 0.5 + 1))) + 1,
        return dp[n]

class Solution1(object):
    _dp = {}
    def numSquares(self, n):
        """
        dp way to do
        :type n: int
        :rtype: int
        """
        if n<=0:
            return 0
        if n in self._dp:
            return self._dp[n]
        i = 1
        while i*i <= n:
            self._dp[i*i] = 1
            i += 1
        for i in range(1, n+1):
            j=1
            tmp = i+j*j
            while tmp<=n:
                if tmp not in self._dp or self._dp[i]+1< self._dp[tmp]:
                    self._dp[tmp] = self._dp[i]+1
                j += 1
                tmp = i+j*j
        return self._dp[n]


    def numSquares1(self, n): #idea same as slower, use dict instead of array, 1989ms, 10.04% --> 13% without checking n
        """
        dp way to do
        :type n: int
        :rtype: int
        """
        if n<=0:
            return 0
        dp = {}
        i = 1
        while i*i <= n:
            dp[i*i] = 1
            i += 1
        for i in range(1, n+1):
            j=1
            tmp = i+j*j
            while tmp<=n:
                if tmp not in dp or dp[i]+1< dp[tmp]:
                    dp[tmp] = dp[i]+1
                j += 1
                tmp = i+j*j
        return dp[n]



    def numSquares_slower(self, n): #4815ms, 2.98%
        """
        :type n: int
        :rtype: int
        """
        if n<=0:
            return 0
        dp = [0 for i in range(n+1)]
        # dp[1] = 1
        # dp[2] = 2
        i = 1
        while i*i <= n:
            dp[i*i] = 1
            i += 1
        for i in range(1, n+1):
            j=1
            tmp = i+j*j
            while tmp<=n:
                if dp[tmp] == 0 or dp[i]+1< dp[tmp]:
                    dp[tmp] = dp[i]+1
                j += 1
                tmp = i+j*j
        return dp[n]

    def numSquares_ref(self, n): # sometimes TLE
        """
        :type n: int
        :rtype: int
        """
        dp = collections.defaultdict(int)
        y = 1
        while y * y <= n:
            dp[y * y] = 1
            y += 1
        for x in range(1, n + 1):
            y = 1
            while x + y * y <= n:
                if x + y * y not in dp or dp[x] + 1 < dp[x + y * y]:
                    dp[x + y * y] = dp[x] + 1
                y += 1
        return dp[n]


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = 13
        answer = 2
        result = self.sol.numSquares(nums)
        self.assertEqual(answer, result)


    def test_case2(self):
        nums = 14
        answer = 3
        result = self.sol.numSquares(nums)
        self.assertEqual(answer, result)

    def test_case3(self): #RuntimeError: maximum recursion depth exceeded
        nums = 8829
        answer = 2
        result = self.sol.numSquares(nums)
        self.assertEqual(answer, result)

    def test_case4(self): # TLE, 51% pass on lint, local runs 15s+
        nums = 100000
        answer = 2
        result = self.sol.numSquares(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()


"""
解法I：数论（Number Theory）

时间复杂度：O(sqrt n)

四平方和定理(Lagrange's Four-Square Theorem)：所有自然数至多只要用四个数的平方和就可以表示。

参考链接：https://leetcode.com/discuss/56982/o-sqrt-n-in-ruby-and-c


==========================================================================================

This is a dp problem. The key is to find the relation which is dp[i] = min(dp[i], dp[i-square]+1). 
For example, dp[5]=dp[4]+1=1+1=2.

==========================================================================================

(1)
题目分析： 乍一看题目，比较天真的想法是，先从不大于n的最大的完全平方数开始组合，如果和超过了n，就换小一点的完全平方数。但问题是，最后如果凑
不齐的话，只能添加很多1，总量上就不是最少的了。例如12，题目中给的例子是4+4+4，需要3个完全平方数。如果从最大的开始组合，那么是9+1+1+1，需要
4个完全平方数。

从另一个角度来想，用穷举法来求解就是把不大于n的所有可能的完全平方数的组合都算出来，然后找出和为n的组合中数量最少的那种组合。如果不大于n的完
全平方数有m个的话，这个方法的时间复杂度是O(m^m)。显然穷举法时间复杂度过大，不是可行的方法。观察到，在枚举的过程中，有一些组合显然不是最优
的，比如把12拆成12个1相加。另外，如果我们能够记录已经找到的最小组合，那么稍大一些的数只需要在此基础上添加若干个完全平方数即可。这里面就包含
了动态规划的思想。

具体来说，我们用一个数组来记录已有的结果，初始化为正无穷(INT_MAX)。外层循环变量i从0到n，内层循环变量j在i的基础上依次加上每个整数的完全平
方，超过n的不算。那么i + j*j这个数需要的最少的完全平方数的数量，就是数组中当前的数值，和i位置的数值加上一，这两者之间较小的数字。如果当前
的值较小，说明我们已经找到过它需要的完全平方数的个数（最初都是正无穷）。否则的话，说明在i的基础上加上j的平方符合条件，所需的完全平方数的个
数就是i需要的个数加上一。

========================================================================================================================


(2)
There are so many "large" test cases that it's worthwhile to keep data between test cases rather than recomputing from
scratch all the time. At least in the slower languages. My dp tells the numbers of squares needed for the first integers,
and when asked about a new n, I extend dp just as much as necessary.

class Solution(object):
    _dp = [0]
    def numSquares(self, n):
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]


========================================================================================================================

(3)
Summary of 4 different solutions (BFS, DP, static DP and mathematics)
Came up with the 2 solutions of breadth-first search and dynamic programming. Also "copied" StefanPochmann's static dynamic programming solution (https://leetcode.com/discuss/56993/static-dp-c-12-ms-python-172-ms-ruby-384-ms) and davidtan1890's mathematical solution (https://leetcode.com/discuss/57066/4ms-c-code-solve-it-mathematically) here with minor style changes and some comments. Thank Stefan and David for posting their nice solutions!

1.Dynamic Programming: 440ms

class Solution
{
public:
    int numSquares(int n)
    {
        if (n <= 0)
        {
            return 0;
        }

        // cntPerfectSquares[i] = the least number of perfect square numbers
        // which sum to i. Note that cntPerfectSquares[0] is 0.
        vector<int> cntPerfectSquares(n + 1, INT_MAX);
        cntPerfectSquares[0] = 0;
        for (int i = 1; i <= n; i++)
        {
            // For each i, it must be the sum of some number (i - j*j) and
            // a perfect square number (j*j).
            for (int j = 1; j*j <= i; j++)
            {
                cntPerfectSquares[i] =
                    min(cntPerfectSquares[i], cntPerfectSquares[i - j*j] + 1);
            }
        }

        return cntPerfectSquares.back();
    }
};
2.Static Dynamic Programming: 12ms

class Solution
{
public:
    int numSquares(int n)
    {
        if (n <= 0)
        {
            return 0;
        }

        // cntPerfectSquares[i] = the least number of perfect square numbers
        // which sum to i. Since cntPerfectSquares is a static vector, if
        // cntPerfectSquares.size() > n, we have already calculated the result
        // during previous function calls and we can just return the result now.
        static vector<int> cntPerfectSquares({0});

        // While cntPerfectSquares.size() <= n, we need to incrementally
        // calculate the next result until we get the result for n.
        while (cntPerfectSquares.size() <= n)
        {
            int m = cntPerfectSquares.size();
            int cntSquares = INT_MAX;
            for (int i = 1; i*i <= m; i++)
            {
                cntSquares = min(cntSquares, cntPerfectSquares[m - i*i] + 1);
            }

            cntPerfectSquares.push_back(cntSquares);
        }

        return cntPerfectSquares[n];
    }
};
3.Mathematical Solution: 4ms

class Solution
{
private:
    int is_square(int n)
    {
        int sqrt_n = (int)(sqrt(n));
        return (sqrt_n*sqrt_n == n);
    }

public:
    // Based on Lagrange's Four Square theorem, there
    // are only 4 possible results: 1, 2, 3, 4.
    int numSquares(int n)
    {
        // If n is a perfect square, return 1.
        if(is_square(n))
        {
            return 1;
        }

        // The result is 4 if and only if n can be written in the
        // form of 4^k*(8*m + 7). Please refer to
        // Legendre's three-square theorem.
        while ((n & 3) == 0) // n%4 == 0
        {
            n >>= 2;
        }
        if ((n & 7) == 7) // n%8 == 7
        {
            return 4;
        }

        // Check whether 2 is the result.
        int sqrt_n = (int)(sqrt(n));
        for(int i = 1; i <= sqrt_n; i++)
        {
            if (is_square(n - i*i))
            {
                return 2;
            }
        }

        return 3;
    }
};
4.Breadth-First Search: 80ms

class Solution
{
public:
    int numSquares(int n)
    {
        if (n <= 0)
        {
            return 0;
        }

        // perfectSquares contain all perfect square numbers which
        // are smaller than or equal to n.
        vector<int> perfectSquares;
        // cntPerfectSquares[i - 1] = the least number of perfect
        // square numbers which sum to i.
        vector<int> cntPerfectSquares(n);

        // Get all the perfect square numbers which are smaller than
        // or equal to n.
        for (int i = 1; i*i <= n; i++)
        {
            perfectSquares.push_back(i*i);
            cntPerfectSquares[i*i - 1] = 1;
        }

        // If n is a perfect square number, return 1 immediately.
        if (perfectSquares.back() == n)
        {
            return 1;
        }

        // Consider a graph which consists of number 0, 1,...,n as
        // its nodes. Node j is connected to node i via an edge if
        // and only if either j = i + (a perfect square number) or
        // i = j + (a perfect square number). Starting from node 0,
        // do the breadth-first search. If we reach node n at step
        // m, then the least number of perfect square numbers which
        // sum to n is m. Here since we have already obtained the
        // perfect square numbers, we have actually finished the
        // search at step 1.
        queue<int> searchQ;
        for (auto& i : perfectSquares)
        {
            searchQ.push(i);
        }

        int currCntPerfectSquares = 1;
        while (!searchQ.empty())
        {
            currCntPerfectSquares++;

            int searchQSize = searchQ.size();
            for (int i = 0; i < searchQSize; i++)
            {
                int tmp = searchQ.front();
                // Check the neighbors of node tmp which are the sum
                // of tmp and a perfect square number.
                for (auto& j : perfectSquares)
                {
                    if (tmp + j == n)
                    {
                        // We have reached node n.
                        return currCntPerfectSquares;
                    }
                    else if ((tmp + j < n) && (cntPerfectSquares[tmp + j - 1] == 0))
                    {
                        // If cntPerfectSquares[tmp + j - 1] > 0, this is not
                        // the first time that we visit this node and we should
                        // skip the node (tmp + j).
                        cntPerfectSquares[tmp + j - 1] = currCntPerfectSquares;
                        searchQ.push(tmp + j);
                    }
                    else if (tmp + j > n)
                    {
                        // We don't need to consider the nodes which are greater ]
                        // than n.
                        break;
                    }
                }

                searchQ.pop();
            }
        }

        return 0;
    }
};
More...

========================================================================================================================

动态规划
复杂度
时间 O(N^2) 空间 O(N)

思路
如果一个数x可以表示为一个任意数a加上一个平方数bｘb，也就是x=a+bｘb，那么能组成这个数x最少的平方数个数，就是能组成a最少的平方数个数加上1
（因为b*b已经是平方数了）。

代码
public class Solution {
    public int numSquares(int n) {
        int[] dp = new int[n+1];
        // 将所有非平方数的结果置最大，保证之后比较的时候不被选中
        Arrays.fill(dp, Integer.MAX_VALUE);
        // 将所有平方数的结果置1
        for(int i = 0; i * i <= n; i++){
            dp[i * i] = 1;
        }
        // 从小到大找任意数a
        for(int a = 0; a <= n; a++){
            // 从小到大找平方数bｘb
            for(int b = 0; a + b * b <= n; b++){
                // 因为a+b*b可能本身就是平方数，所以我们要取两个中较小的
                dp[a + b * b] = Math.min(dp[a] + 1, dp[a + b * b]);
            }
        }
        return dp[n];
    }
}

"""
#-*- coding:utf-8 -*-


