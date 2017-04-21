#coding=utf-8

"""
Sqrt(x) II (from lint)


Implement double sqrt(double x) and x >= 0.

Compute and return the square root of x.

 Notice

You do not care about the accuracy of the result, we will help you to output results.

Have you met this question in a real interview? Yes
Example
Given n = 2 return 1.41421356

Tags
Binary Search Mathematics Facebook
Related Problems
Easy Sqrt(x)


"""


import unittest


class Solution:
    # @param {double} x a double
    # @return {double} the square root of x
    def sqrt(self, x):  #381ms
        # Write your code here
        eps = 1e-12
        #left = 0.0 # can't be 1.0 here
        # right = x / 2.0  # can't use x/2 here, otherwise wrong and infinite for case x = 1
        #right = x/2.0 if x > 1 else 1.0
        #right = x
        if x >= 1:
            left, right = 1.0, x
        elif x >= 0:
            #left, right = x, 0.0
            left, right = x, 1.0
        else:
            raise ValueError("Input should be positive!")
        while abs(left-right) > eps:
        #while left < right:
            mid = (left+right)/2.0
            if abs(mid * mid - x) <= eps:
                return mid
            elif mid * mid > x:
                right = mid
            else:
                left = mid
        return left



    def intSqrt(self, x):
        left = 1
        right = x/2
        while left < right:
            mid = (left+right)/2
            if mid * mid > x:
                right = mid - 1
            elif mid * mid < x:
                left = mid + 1
            else:
                return mid
        return left

    def sqrt_ref(self, x): #368ms
        # Write your code here

        left = 0.0
        right = x
        eps = 1e-12

        if x < 1.0:
            right = 1.0

        while(right - left > eps):
            mid = (right + left) / 2
            if mid * mid < x:
                left = mid
            else:
                right = mid

        return left


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = 4
        answer = 2
        result = self.sol.sqrt(nums)
        self.assertEqual(answer, result)

    def test_case2(self): # this case means it will use floor int when the real sqrt is not an integer
        nums = 15
        answer = 3.87298335
        result = self.sol.sqrt(nums)
        self.assertEqual(answer, result)

    def test_case3(self): # =====>
        nums = 1
        answer = 1
        result = self.sol.sqrt(nums)
        self.assertEqual(answer, result)

    def test_case4(self):  # =====>
        nums = 2
        answer = 1.41421356
        result = self.sol.sqrt(nums)
        self.assertEqual(answer, result)

    def test_case5(self):  # =====>
        nums = 0.01
        answer = 0.1
        result = self.sol.sqrt(nums)
        self.assertEqual(answer, result)

    def test_case6(self):  # =====>
        nums = -1
        with self.assertRaises(ValueError):
            self.sol.sqrt(nums)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()


"""


            // 二分浮点数 和二分整数不同
            // 一般都有一个精度的要求 譬如这题就是要求小数点后八位
            // 也就是只要我们二分的结果达到了这个精度的要求就可以
            // 所以 需要让 right 和 left 小于一个我们事先设定好的精度值 eps
            // 一般eps的设定1e-8,因为这题的要求是到1e-8,所以我把精度调到了1e-12
            // 最后 选择 left 或 right 作为一个结果即可


==============================================================

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