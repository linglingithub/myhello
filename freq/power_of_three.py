#coding=utf-8

import unittest

"""
326. Power of Three
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.

Difficulty:Easy
Total Accepted:103.8K
Total Submissions:257.1K
Contributor: LeetCode
Subscribe to see which companies asked this question.

Related Topics 
Math 
Similar Questions 
Power of Two Power of Four 

"""

import math

class Solution(object):
    def isPowerOfThree(self, n):
        #1162261467 is 3 ^ 19, 3 ^ 20 is bigger than int
        #return (n > 0 and 1162261467 % n == 0)
        maxPowerOfThree = math.pow(3, int(math.log(0x7fffffff) / math.log(3)))
        return (n > 0 and maxPowerOfThree % n == 0)

    def isPowerOfThree_wrong(self, n):
        """  
        precision not good enough, case2
        :type n: int
        :rtype: bool
        """
        import math
        return n > 0 and float(3 ** float(math.log(n, 3))) == float(n)



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = 1
        answer = True
        result = self.sol.isPowerOfThree(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = 243   #float(3 ** float(math.log(n, 3))) = 242.99999999999977
        answer = True
        result = self.sol.isPowerOfThree(nums)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()


"""

解法I：求对数，然后乘方，判断得数是否相等

Python代码：
class Solution(object):
    def isPowerOfThree(self, n):

        return n > 0 and 3 ** round(math.log(n,3)) == n

解法II： 递归法

Python代码：
class Solution(object):
    def isPowerOfThree(self, n):

        if n == 1:
            return True
        if n == 0 or n % 3 > 0:
            return False
        return self.isPowerOfThree(n / 3)

=======================

1 line java solution without loop / recursion
public class Solution {
public boolean isPowerOfThree(int n) {
    // 1162261467 is 3^19,  3^20 is bigger than int  
    return ( n>0 &&  1162261467%n==0);
}
}

====================


1 line C++ no recursion/loop
class Solution {
public:
    bool isPowerOfThree(int n) {
        return fmod(log10(n)/log10(3), 1)==0;
    }
};


====================

** A summary of `all` solutions (new method included at 15:30pm Jan-8th)
Well, this problem doesn't seem to be quite interesting or worthwhile to think about at a first glance. I had the same feeling at the beginning. However, after seeing a couple of posts, I saw a couple of interesting ways. So here is a summary post and hope you learn something from others' solutions.

Two trivial solutions first:
#Recursive Solution#

public boolean isPowerOfThree(int n) {
    return n>0 && (n==1 || (n%3==0 && isPowerOfThree(n/3)));
}
#Iterative Solution#

update following Stefan's answer below:

public boolean isPowerOfThree(int n) {
    if(n>1)
        while(n%3==0) n /= 3;
    return n==1;
}
my original code:
public boolean isPowerOfThree(int n) {
while(n>1) {
if(n%3!=0) return false;
n /= 3;
}
return n<=0 ? false : true;
}

#It's all about MATH...#

Method 1

Find the maximum integer that is a power of 3 and check if it is a multiple of the given input. (related post)

public boolean isPowerOfThree(int n) {
    int maxPowerOfThree = (int)Math.pow(3, (int)(Math.log(0x7fffffff) / Math.log(3)));
    return n>0 && maxPowerOfThree%n==0;
}
Or simply hard code it since we know maxPowerOfThree = 1162261467:

public boolean isPowerOfThree(int n) {
    return n > 0 && (1162261467 % n == 0);
}
It is worthwhile to mention that Method 1 works only when the base is prime. For example, we cannot use this algorithm to check if a number is a power of 4 or 6 or any other composite number.

Method 2

If log10(n) / log10(3) returns an int (more precisely, a double but has 0 after decimal point), then n is a power of 3. (original post). But be careful here, you cannot use log (natural log) here, because it will generate round off error for n=243. This is more like a coincidence. I mean when n=243, we have the following results:

log(243) = 5.493061443340548    log(3) = 1.0986122886681098
   ==> log(243)/log(3) = 4.999999999999999

log10(243) = 2.385606273598312    log10(3) = 0.47712125471966244
   ==> log10(243)/log10(3) = 5.0
This happens because log(3) is actually slightly larger than its true value due to round off, which makes the ratio smaller.

public boolean isPowerOfThree(int n) {
    return (Math.log10(n) / Math.log10(3)) % 1 == 0;
}
Method 3 related post

public boolean isPowerOfThree(int n) {
    return n==0 ? false : n==Math.pow(3, Math.round(Math.log(n) / Math.log(3)));
}
Method 4 related post

public boolean isPowerOfThree(int n) {
    return n>0 && Math.abs(Math.log10(n)/Math.log10(3)-Math.ceil(Math.log10(n)/Math.log10(3))) < Double.MIN_VALUE;
}
Cheating Method

This is not really a good idea in general. But for such kind of power questions, if we need to check many times, it might be a good idea to store the desired powers into an array first. (related post)

public boolean isPowerOfThree(int n) {
    int[] allPowerOfThree = new int[]{1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907, 43046721, 129140163, 387420489, 1162261467};
    return Arrays.binarySearch(allPowerOfThree, n) >= 0;
}
or even better with HashSet:

public boolean isPowerOfThree(int n) {
    HashSet<Integer> set = new HashSet<>(Arrays.asList(1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907, 43046721, 129140163, 387420489, 1162261467));
    return set.contains(n);
}
#New Method Included at 15:30pm Jan-8th#

Radix-3 original post

The idea is to convert the original number into radix-3 format and check if it is of format 10* where 0* means k zeros with k>=0.

public boolean isPowerOfThree(int n) {
    return Integer.toString(n, 3).matches("10*");
}
Any other interesting solutions?

If you are interested in my other posts, please feel free to check my Github page here: https://github.com/F-L-A-G/Algorithms-in-Java

=====================

题目翻译

给定一个整数，判断它是否是3的倍数。 
进一步：能否不用循环或递归实现？

思路方法

思路一

先不考虑进一步的要求，用循环的做法是：每次尝试将输入的数除以3，观察是否能整除，若不能则说明不是3的倍数；若能，则用除以3的结果循环上述过程，直至得到1，说明输入是3的幂次。

代码

class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        while n%3 == 0:
            n /= 3
        return n == 1

思路二

先不考虑进一步的要求，用递归的做法也尝试一下。

代码

class Solution(object):
    def isPowerOfThree(self, n):

        if n <= 0:
            return False
        if n == 1:
            return True
        if n%3 == 0:
            return self.isPowerOfThree(n/3)
        else:
            return False

思路三

当然，题目说了不能循环或递归，上面的解法能AC但不太符合题意。考虑到输入是“Integer”，是有范围的（<2147483648），所以存在能输入的最大的3的幂次，即 3^19=1162261467。所以只要检查输入能否被它整除即可

代码

class Solution(object):
    def isPowerOfThree(self, n):
        return n > 0 and 1162261467 % n == 0

思路四

还可以算出能输入的所有3的幂次，保存到list或dict中，对每次输入判断是否在这些数中即可。

代码

class Solution(object):
    def isPowerOfThree(self, n):

        nums = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907, 43046721, 129140163, 387420489, 1162261467]
        return n in nums



"""
#-*- coding:utf-8 -*-
