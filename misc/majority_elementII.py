#coding=utf-8

import unittest

"""

229. Majority Element II

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in
linear time and in O(1) space.

Hint:

How many majority elements could it possibly have?
Do you have a better hint? Suggest it!
Subscribe to see which companies asked this question.

Hide Tags Array
Hide Similar Problems (E) Majority Element


Medium

"""



class Solution(object):
    def majorityElement(self, nums): #79ms, 23%
        """
        Use voting algorithm to find . need to consider , can be 0, 1 or at most 2 majority elements
        :type nums: List[int]
        :rtype: List[int]
        """
        a,b = 0,0
        ca, cb = 0, 0
        for num in nums:
            if ca == 0:
                if cb != 0 and num == b:  #need to check here, otherwise wrong for case1
                    cb += 1
                else:
                    a, ca = num, 1
            elif a == num:
                ca += 1
            elif cb == 0:
                b, cb = num, 1
            elif b == num:
                cb += 1
            else:
                ca -= 1
                cb -= 1
        print a, ca, b, cb
        ca, cb = 0, 0
        for num in nums:
            if num == a:
                ca += 1
            elif num == b:
                cb += 1
        return [x[0] for x in zip([a,b],[ca,cb]) if x[1] > len(nums)/3 ]


    def majorityElement_ref(self, nums): #52ms, 83%
        n1 = n2 = None
        c1 = c2 = 0
        for num in nums:
            if n1 == num:
                c1 += 1
            elif n2 == num:
                c2 += 1
            elif c1 == 0:
                n1, c1 = num, 1
            elif c2 == 0:
                n2, c2 = num, 1
            else:
                c1, c2 = c1 - 1, c2 - 1
        size = len(nums)
        return [n for n in (n1, n2)
                   if n is not None and nums.count(n) > size / 3]

    def majorityElement_wrong_case2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a,b = 0,0
        ca, cb = 0, 0
        for num in nums:
            if ca == 0:
                a, ca = num, 1
            elif a == num:
                ca += 1
            elif cb == 0:
                b, cb = num, 1
            elif b == num:
                cb += 1
            else:
                ca -= 1
                cb -= 1
        ca, cb = 0, 0
        for num in nums:
            if num == a:
                ca += 1
            if num == b:
                cb += 1
        return [x[0] for x in zip([a,b],[ca,cb]) if x[1] > len(nums)/3 ]






class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,2,2,4,1,1,1,5,1,2,2]
        answer = [1, 2]
        result = self.sol.majorityElement(nums)
        self.assertEqual(sorted(answer), sorted(result))

    def test_case2(self):
        nums = [0,0,0]
        answer = [0]
        result = self.sol.majorityElement(nums)
        self.assertEqual(sorted(answer), sorted(result))

    def test_case3(self):
        nums = [1,2,2,3,2,1,1,3]
        answer = [1,2]
        result = self.sol.majorityElement(nums)
        self.assertEqual(sorted(answer), sorted(result))


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""

For finding the majority elements, there is a very famous algorithm Boyer–Moore majority vote algorithm. But the
original algorithm is for finding the majority number that appears more than ⌊ n/2 ⌋ times. So we need to modify the
algorithm to find numbers that appears more than n/3. Use 2 counter to keep tracking of 2 candidate numbers.

For every number in array,

Check if it is one of the two candidate numbers.
Check if its’ counter is 0, if counter is 0, update candidate number and set counter to 1.
If it is not satisfy either of the above conditions. Decrement the counter by 1.
After the first round loop, we have two “majority” numbers but we don’t know if they appears more than n/3 time. So we
start another loop to count the occurrence time.

Finally, if the occurrence time is more than n/3, add it to result set.

=============================================================================================================================

这道题让我们求出现次数大于n/3的众数，而且限定了时间和空间复杂度，那么就不能排序，也不能使用哈希表，这么苛刻的限制条件只有一种方法能解了，那
就是摩尔投票法 Moore Voting，这种方法在之前那道题Majority Element 求众数中也使用了。题目中给了一条很重要的提示，让我们先考虑可能会有多
少个众数，经过举了很多例子分析得出，任意一个数组出现次数大于n/3的众数最多有两个，具体的证明我就不会了，我也不是数学专业的。那么有了这个信息，
我们使用投票法的核心是找出两个候选众数进行投票，需要两遍遍历，第一遍历找出两个候选众数，第二遍遍历重新投票验证这两个候选众数是否为众数即可，
选候选众数方法和前面那篇Majority Element 求众数一样，由于之前那题题目中限定了一定会有众数存在，故而省略了验证候选众数的步骤，这道题却没有
这种限定，即满足要求的众数可能不存在，所以要有验证。代码如下：

"""