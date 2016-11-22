#coding=utf-8

"""
69. Sqrt(x)

Implement int sqrt(int x).

Compute and return the square root of x.

Subscribe to see which companies asked this question

Hide Tags Binary Search Math
Hide Similar Problems (M) Pow(x, n) (M) Valid Perfect Square

Medium


"""


import unittest


class Solution(object):
    def mySqrt(self, x): #52ms, 70%
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x / 2 + 1
        res = (left+right) / 2
        while left <= right:
            tmp = res * res
            if tmp == x:
                return res
            elif tmp < x:
                left = res + 1
            else:
                right = res - 1
            res = (left + right) / 2 # update res at the end of each iteration so it will be the closer value ??
        return res


    def mySqrt_wrong(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        # right = x / 2
        right = x / 2 + 1  # need to +1 for x <4, otherwise wrong for case3, draw the y=x/2 and y=sqrt(x) and see why
        while left <= right:
            res = (left+right) / 2
            tmp = res * res
            if tmp == x:
                return res
            elif tmp < x:
                left = res + 1
            else:
                right = res - 1
        return res


    def mySqrt_ref2(self, x): #59ms, 54%
        if x == 0:
            return 0
        i = 1; j = x / 2 + 1
        while( i <= j ):
            center = ( i + j ) / 2
            if center ** 2 == x:
                return center
            elif center ** 2 > x:
                j = center - 1
            else:
                i = center + 1
        return j


    def mySqrt_ref(self, x): #72ms, 25%
        low, high, mid = 0, x, x / 2
        while low <= high:
            if mid * mid > x:
                high = mid - 1
            else:
                low = mid + 1
            mid = (low + high) / 2
        return mid




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case4(self):  # =====>
        nums = 2
        answer = 1
        result = self.sol.mySqrt(nums)
        self.assertEqual(answer, result)

    def test_case3(self): # =====>
        nums = 1
        answer = 1
        result = self.sol.mySqrt(nums)
        self.assertEqual(answer, result)

    def test_case1(self):
        nums = 4
        answer = 2
        result = self.sol.mySqrt(nums)
        self.assertEqual(answer, result)

    def test_case2(self): # this case means it will use floor int when the real sqrt is not an integer
        nums = 15
        answer = 3
        result = self.sol.mySqrt(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()


"""
A:

这里给出两种实现方法：一是二分搜索，二是牛顿迭代法。

1. 二分搜索
对于一个非负数n，它的平方根不会小于大于（n/2+1）（谢谢@linzhi-cs提醒）。在[0, n/2+1]这个范围内可以进行二分搜索，求出n的平方根。

复制代码
 1 int sqrt(int x) {
 2     long long i = 0;
 3     long long j = x / 2 + 1;
 4     while (i <= j)
 5     {
 6         long long mid = (i + j) / 2;
 7         long long sq = mid * mid;
 8         if (sq == x) return mid;
 9         else if (sq < x) i = mid + 1;
10         else j = mid - 1;
11     }
12     return j;
13 }
复制代码
注：在中间过程计算平方的时候可能出现溢出，所以用long long。

2. 牛顿迭代法

   为了方便理解，就先以本题为例：

   计算x2 = n的解，令f(x)=x2-n，相当于求解f(x)=0的解，如左图所示。

   首先取x0，如果x0不是解，做一个经过(x0,f(x0))这个点的切线，与x轴的交点为x1。

   同样的道理，如果x1不是解，做一个经过(x1,f(x1))这个点的切线，与x轴的交点为x2。

   以此类推。

   以这样的方式得到的xi会无限趋近于f(x)=0的解。

   判断xi是否是f(x)=0的解有两种方法：

   一是直接计算f(xi)的值判断是否为0，二是判断前后两个解xi和xi-1是否无限接近。



经过(xi, f(xi))这个点的切线方程为f(x) = f(xi) + f’(xi)(x - xi)，其中f'(x)为f(x)的导数，本题中为2x。令切线方程等于0，即可求出xi+1=xi - f(xi) / f'(xi)。

继续化简，xi+1=xi - (xi2 - n) / (2xi) = xi - xi / 2 + n / (2xi) = xi / 2 + n / 2xi = (xi + n/xi) / 2。

有了迭代公式，程序就好写了。关于牛顿迭代法，可以参考wikipedia以及百度百科。

复制代码
 1 int sqrt(int x) {
 2     if (x == 0) return 0;
 3     double last = 0;
 4     double res = 1;
 5     while (res != last)
 6     {
 7         last = res;
 8         res = (res + x / res) / 2;
 9     }
10     return int(res);
11 }
复制代码
牛顿迭代法也同样可以用于求解多次方程的解。

P.S. 本题是求解整数的平方根，并且返回值也是整型。在上述代码基础上稍微做修改，就可以同样适用于double（仅限方法2）。

复制代码
 1 double sqrt(double x) {
 2     if (x == 0) return 0;
 3     double last = 0.0;
 4     double res = 1.0;
 5     while (res != last)
 6     {
 7         last = res;
 8         res = (res + x / res) / 2;
 9     }
10     return res;
11 }
复制代码


关于LeetCode的其他题目，可以参考我的GitHub。

references：本文讲解牛顿迭代法使用的图片来自wikipedia。

原创文章，转载请注明出处：http://www.cnblogs.com/AnnieKim/


"""

#-*- coding:utf-8 -*-
#coding=utf-8