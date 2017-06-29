#coding=utf-8

import unittest

"""

Continuous Subarray Sum II

Given an circular integer array (the next element of the last element is the first element), find a continuous subarray 
in it, where the sum of numbers is the biggest. Your code should return the index of the first number and the index of 
the last number.

If duplicate answers exist, return any of them.

Have you met this question in a real interview? Yes
Example
Give [3, 1, -100, -3, 4], return [4,1].

Tags 
Subarray Array
Related Problems 
Medium Continuous Subarray Sum

"""





class Solution:
    # @param {int[]} A an integer array
    # @return {int[]}  A list of integers includes the index of the
    #                  first number and the index of the last number
    def continuousSubarraySumII(self, A):  #ref
        # Write your code here
        if not A:
            return [-1, -1]
        result = A[0]
        result2 = [0, 0]
        rsum = 0
        left, right = 0, 0
        for i in range(len(A)):
            x = A[i]
            rsum += x
            if rsum > result:
                result = rsum
                result2 = [left, right]
            if rsum <= 0:
                left = i+1
                right = left
                rsum = 0
                continue
            right += 1

        result3 = A[0]
        result4 = [0, 0]
        rsum = 0
        left, right = 0, 0
        for i in range(len(A)):
            x = A[i]
            rsum += x
            if rsum < result3:
                result3 = rsum
                result4 = [left, right]
            if rsum >= 0:
                left = i + 1
                right = left
                rsum = 0
                continue
            right += 1
        result3 = sum(A) - result3
        a, b = result4[0], result4[1]
        n = len(A)
        if a==0 and b == len(A)-1:
            return result2
        # elif a==0 :
        #     result4 = [b+1, n-1]
        # elif b == n-1:
        #     result4 = [0, a-1]
        # else:
        #     result4 = [b+1, a-1]
        else:
            result4 = [(b+1)%n, (a-1)%n]
        res = result2 if result > result3 else result4
        return res



    def continuousSubarraySumII_wrong(self, A):
        # Write your code here
        if not A:
            return []
        n = len(A)
        nums = A * 2
        max_sum = nums[0]
        start, end = 0, 0
        sub_sum = 0
        result = [start, end]  # should have init value not []
        i = 0
        while i < len(nums):
            if i - start >= n:  # add check here for not exceeding length ??
                print "start, end, sub_sum, max_sum: ", start, end, sub_sum, max_sum
                sub_sum -= nums[start]
                start += 1
                end = start
                sub_sum = 0

            sub_sum += nums[i]
            # print "start, end, sub_sum, max_sum: ", start, end, sub_sum, max_sum
            if sub_sum > max_sum:
                max_sum = sub_sum
                end = (i - n) if i >= n else i
                result = [start, end]
            if sub_sum <= 0:  # not nums[i]
                print "==> neg sub_sum, i, start, end, sub_sum, max_sum: ", i, start, end, sub_sum, max_sum

                start = i + 1
                # end = start, no need
                sub_sum = 0
            if start >= n:  # important
                print "break , start = ", start, " ;  i = ", i
                break
            i += 1

        return result


    def continuousSubarraySumII_wrong(self, A):
        # Write your code here
        if not A:
            return []
        n = len(A)
        nums = A * 2
        max_sum = nums[0]
        start, end = 0, 0
        sub_sum = 0
        result = [start, end]  # should have init value not []
        for i in range(len(nums)):
            sub_sum += nums[i]
            if sub_sum > max_sum:
                max_sum = sub_sum
                end = (i - n) if i >= n else i
                result = [start, end]
            if nums[i] <= 0:
                start = i + 1
                # end = start, no need
                sub_sum = 0
        return result


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()


    def test_case3(self):  #====>
        from util.ini_file_util import IniFileUtil
        params = IniFileUtil.read_into_dict("continuous_subarray_sumII_case3.ini")
        nums = IniFileUtil.string_to_int_list(params.get("nums"))
        answer = [6794,6782]

        result = self.sol.continuousSubarraySumII(nums)
        print "sum1, sum2: ", sum(nums[result[0]: result[1]+1]), sum(nums[answer[0]:]) + sum(nums[:answer[1]])
        self.assertEqual(answer, result)

    def test_case2(self):  #====>
        nums = [1,2,-2,-100,1,2,-2]
        answer = [4, 1]
        result = self.sol.continuousSubarraySumII(nums)
        self.assertEqual(answer, result)


    def test_case01(self):
        nums = [3, 1, -100, -3, 4]
        answer = [4, 1]
        result = self.sol.continuousSubarraySumII(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""

http://www.lintcode.com/en/problem/continuous-subarray-sum-ii/#

在可以循环的数组里面找最大的subarray sum，最开始想的是复制一份数组，然后跟之前的subarray sum一样做，但是有test过不了。然后改进算法，
two pass记录第一次的位置然后搜索到当前的index的前一个index，但是这样时间复杂度太高了。看这题AC率才9%，有没有人成功通过的？求共享算法或者
代码交流


最大数组的范围只有两种可能：1. [ i ~ j ]，2. [ i ~ N-1] + [ 0 ~ j ]. 所以，你只要分别找到两种情况的最大者，取这两个最大者中较大的即
可。1和Continuous Subarray Sum I相同，就不多说了。2等价于找一个范围[j+1 ~i-1]，使得这个范围内的数组和最小。这又等价于将原数组取负号，
然后在这个负数组中找最大和的[j+1 ~ i+1]范围即可。


============================================================


课上陈老师讲过，遇到数组有环的有3种处理方法：1.拆成2个数组. 2.复制一个样的在后面。 3.取反
这道题的答案给的是取反，和老师上课讲的一样。我自己想用第二个方法即复制一个样的数组来求解，以下是代码。就是假设数组有2倍长，在对A数组取数的时
候和在记录结果的时候都给下标加一个%len; 这个解法在lintcode上跑前面能过，到了最后两个大case跑不过去，由于那个case有几千个输入所以不好
debug，希望助教老师帮看看这逻辑怎么不对，最好是能给我举一个简明易懂的反例。谢谢啦

    public ArrayList<Integer> continuousSubarraySumII(int[] A) {
        // Write your code here
        ArrayList<Integer> result = new ArrayList<>();
        if(A == null || A.length == 0){
            return result;
        }
        int sum = 0;
        int n = A.length;
        int max = Integer.MIN_VALUE;
        int start = 0;
        int end = 0;
        result.add(start);
        result.add(end);

        for(int i = 0; i < 2*n; i++){

            if(sum >= 0){
                sum += A[i%n];
            }
            else{//sum < 0
                sum = A[i%n];
                start = end = i;
            }
            if(sum > max){
                max = sum;
                end = i;
                result.set(0,start % n);
                result.set(1,end % n);
            }
        }
        return result;

    }
 (0)
4 个回复 


2017-04-25 刘助教
因为没有限制end - start小于len
也就是说，首尾相连的长度不能大于整个字符串的长度

 (0)

2017-04-25 王同学
哦哦，那应该怎么样在哪里处理这个问题呢？还是说用这个思路没法做这个题

 (1)

2017-04-26 刘助教
可以找出这个以前len长度的前缀和，找这些的最小值，用当前的前缀和减掉这个最小值，就是到当前的最大值

 (0)

2017-05-04 M同学
@王同学
我也有这个问题，请问你解决了吗？可以分享一下你的答案吗？
谢谢



============================================================


方法1

按I的方法求出的结果
从整个array中减去中间最小的subarray，需要rotate的array
思路是这样的，像楼上说的两种情况，不rotate的 和rorate的。不rotate的和Continuous Subarray Sum I做法一样，不说了。rotate的，可以这样
想，rotate的结果其实相当于是把原来的array中间挖了一段连续的array，那么挖哪一段呢？肯定是和最小的一段连续array。这样解法就出来了。
类似Continuous Subarray Sum I，在I里面是找到连续和最大的一段subarray，在这里，不仅找到和最大的一段连续array，并且也找到和最小的一段连
续array，然后用整个array的sum减去这个最小的和，如果大于不rotate的最大和，那么解就是挖去的这段array的（尾+1， 头-1）
有一个edge case就是当array全部为负时，要挖去的array就是整个array，这个要注意一下。


方法2

首尾可以相连的题目可以想到在array的尾部再加上另一个copy,然后用I的方法求结果，但是要注意长度不能超过原有array的长度


"""