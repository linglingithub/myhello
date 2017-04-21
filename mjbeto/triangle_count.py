#coding=utf-8

import unittest

"""



Triangle Count

Given an array of integers, how many three numbers can be found in the array, so that we can build an triangle whose
three edges length is the three numbers that we find?

Example
Given array S = [3,4,6,7], return 3. They are:
[3,4,6]
[3,6,7]
[4,6,7]
Given array S = [4,4,4,4], return 4. They are:
[4(1),4(2),4(3)]
[4(1),4(2),4(4)]
[4(1),4(3),4(4)]
[4(2),4(3),4(4)]

medium

(locked)

"""



class Solution:
    # @param S: a list of integers
    # @return: a integer
    def triangleCount(self, nums):
        if not nums or len(nums) < 3:
            return 0
        n = len(nums)
        result = 0
        sorted(nums)
        i, j, k = 0, 1, n-1
        result = 0
        while k > 1:
            i, j = 0, k-1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    result += j - i
                    j -= 1  #should not adjust i here. result += j-i means with give j, k, all possible i is included. shoud adjust j or k
                    i = 0
                else:
                    i += 1 # should not reset j=k-1 here, with given k, the inner loop should be trying to find sum larger than sums[k]
            k -= 1
        return result


    def triangleCount_wrong(self, nums):
        if not nums or len(nums) < 3:
            return 0
        n = len(nums)
        result = 0
        sorted(nums)
        i, j, k = 0, 1, n-1
        result = 0
        while k > 1:
            i, j = 0, k-1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    result += j - i
                    i += 1  #should not adjust i here. result += j-i means with give j, k, all possible i is included. shoud adjust j or k
                    j = k-1
                else:
                    i += 1
                    j = k-1
            k -= 1
        return result






class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [3,4,6,7]
        answer = 3
        result = self.sol.triangleCount(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [4,4,4,4]
        answer = 4
        result = self.sol.triangleCount(nums)
        self.assertEqual(answer, result)

    def test_case3(self):
        nums = [4,4]
        answer = 0
        result = self.sol.triangleCount(nums)
        self.assertEqual(answer, result)

    def test_case4(self):
        nums = [4,4,4]
        answer = 1
        result = self.sol.triangleCount(nums)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



"""
这道题跟2 sum II 非常类似。 因为我们要找的是三个元素A[x],A[y],A[z]满足,

A[x]+A[y] > A[z]

A[x]+A[z] > A[y]

A[y]+A[z] > A[x]

就可以了。 那么怎么样实现呢？朴素的解放是o(n^3)的， 那么怎么样优化时间复杂度呢？我们可以先把数组排序， 然后如果默认x< y < z的话，
可以推出，A[x] < A[y] < A[z] 所以上面条件里面2，3 一定成立。 那么接下来我们要做的就是对于每一个z我们要找x，y 使得A[x]+A[y]>A[z] ,
其实这样我们可以枚举所有的z， 然后固定z了后， 不就是找有多少个x和y的组合，使得他们的和大于 A[z] 这就是2 sum II 的问题，
我们可以借鉴2 sum II的方式来做， 最后的时间复杂度就是O(n^2)的时间复杂度。

参考代码：http://www.jiuzhang.com/solutions/triangle-count/


=======================================================================================================================

因为当s数组是单调递增的，当s[i]固定的时候，j递增的时候s[j]单调递增，也就是说对于原来满足s[i] + s[j] > s[k]的k来说，
s[i] + s[j+1] > s[k]同样满足，因此k只需要单调递增就行了，以前验证过的k就不用验证了。
举个栗子：
3，6，7，8，10
3 + 6 > 7, 8; 3 + 6 < 10
那3 + 7 肯定也大于7，8

你把k设成j+1是可以的，但是复杂度会变高

=========================

Thoughts:
Pick 3 integers that fits the condition:
A + B > C
B + C > A
A + C > B
If we sort the input, then we know A <= B <= C, so we can remove 2 conditoins above and only have:
A + B > C
That is, Pick one C, and pick two integers A,B in front. Similar to TWO SUM II.
Have a fixed C as target, and find A + B > target in the remaining array on left of C.
How about just use 2 pointers left, right, and compare with a C (s[i] in for loop)
Time: O(n^2)


===========================

    def triangleCount(self, S):
        edges = sorted(S, reverse=True)
        sum = 0
        for index, longest in enumerate(edges):
            i, j = index + 1, index + 2
            while j < len(edges) and edges[i] + edges[j] > longest:
                j += 1
            j -= 1
            while i < j:
                sum += j - i
                i += 1
                while i < j and edges[i] + edges[j] <= longest:
                    j -= 1
        return sum


"""
