#coding=utf-8

import unittest

"""


321. Create Maximum Number
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length 
k <= m + n from digits of the two. The relative order of the digits from the same array must be preserved. Return an 
array of the k digits. You should try to optimize your time and space complexity.

Example 1:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
return [9, 8, 6, 5, 3]

Example 2:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
return [6, 7, 6, 0, 4]

Example 3:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
return [9, 8, 9]

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.

Difficulty:Hard
Total Accepted:20.9K
Total Submissions:84.5K
Contributor: LeetCode
Subscribe to see which companies asked this question.

Related Topics 
Dynamic Programming Greedy 
Similar Questions 
Remove K Digits Maximum Swap 
Remove Duplicate Letters

===========================================================================

552. Create Maximum Number 

 Description
 Notes
 Testcase
 Judge
Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length 
k <= m + n from digits of the two. The relative order of the digits from the same array must be preserved. Return an 
array of the k digits. You should try to optimize your time and space complexity.

Have you met this question in a real interview? Yes
Example
Given nums1 = [3, 4, 6, 5], nums2 = [9, 1, 2, 5, 8, 3], k = 5
return [9, 8, 6, 5, 3]

Given nums1 = [6, 7], nums2 = [6, 0, 4], k = 5
return [6, 7, 6, 0, 4]

Given nums1 = [3, 9], nums2 = [8, 9], k = 3
return [9, 8, 9]

Tags 
Dynamic Programming Greedy Google

"""


import heapq

class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k <= 0:         # should add protection, case 7
            return []
        if nums1 is None:
            nums1 = []
        if nums2 is None:
            nums2 = []
        res = -1
        res_arr = []
        for i in range(k+1):
            j = k - i
            if i > len(nums1) or j > len(nums2):
                continue
            left = self.find_max(nums1, i)
            right = self.find_max(nums2, j)
            tmp = self.merge_max(left, right)
            tmp_val = self.to_number(tmp)
            if  tmp_val > res:
                res = tmp_val
                res_arr = tmp
            #res = max(res, self.to_number(tmp))
        #return [int(x) for x in list(str(res))]    # can't do this if not single digit array
        return res_arr

    def to_number(self, arr):
        res = 0
        for digit in arr:
            # res += res * 10 + digit
            res = res * 10 + digit
        return res

    def find_max(self, nums, k):
        """
        1) need to keep relative order of digits from nums stable
        2) need to make the int as big as possible
        ==> use a stack, as long as len(stack) + (n-i) >= k, if nums[i] is bigger than stack[-1], pop stack. this can make
        bigger digit to move to higher digits. The stack holds the already used digits, and there are are n-i digits left
        in nums to use.
        :param nums: 
        :param k: 
        :return: list of digits from nums that make a maximum number of length k
        """
        # here k is given to be <= len(nums)
        if k == 0:
            return []
        # need to add this, otherwise infinite loop

        stack = []
        i = 0
        n = len(nums)
        # while len(stack) <= k:
        #     stack.append(nums[i])
        #     i += 1
        while len(stack) + n - i > k:   # should be > instead >= here, because inside will pop
            if stack and nums[i] > stack[-1]:
                stack.pop()
                continue
            if len(stack) < k:
                stack.append(nums[i])
            i += 1       # here i += 1 should not be inside if len < k check, otherwise infinite loop when len == k
        while len(stack) < k:    # should be < instead of <=, because inside will append
            stack.append(nums[i])
            i += 1
        return stack

    def merge_max(self, arr1, arr2):
        i, j = 0, 0
        res = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] > arr2[j]:
                res.append(arr1[i])
                i += 1
            elif arr1[i] < arr2[j]:
                res.append(arr2[j])
                j += 1
            else:   # check for equal cases
                first = self.compare_tail(arr1, i+1, arr2, j+1)
                if first:
                    res.append(arr1[i])
                    i += 1
                else:
                    res.append(arr2[j])
                    j += 1

        if i < len(arr1):
            res.extend(arr1[i:])
        if j < len(arr2):
            res.extend(arr2[j:])
        return res

    def compare_tail(self, arr1, i, arr2, j):
        a1_bigger = True
        if i >= len(arr1) and j < len(arr2):
            return False
        if i <= len(arr1) and j >= len(arr2):
            return True
        if arr1[i] == arr2[j]:
            return self.compare_tail(arr1, i+1, arr2, j+1)
        else:
            return arr1[i] > arr2[j]


    def merge_max_wrong(self, arr1, arr2):  # ok for case 4, wrong for case 5
        """
        arr1 = [2, 5, 6, 4, 4, 0]
        arr2 = [7, 3, 8, 0, 6, 5, 7, 6, 2]
        check for the above case, when there are equal digit, arr1[-1] and arr2[3], which to choose and move the index?
        should choose the with bigger following digit.
        :param arr1: 
        :param arr2: 
        :return: list of merged result 
        """
        # if len(arr1) < len(arr2):
        #     arr1, arr2 = arr2, arr1
        i, j = 0, 0
        res = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] > arr2[j]:
                res.append(arr1[i])
                i += 1
            elif arr1[i] < arr2[j]:
                res.append(arr2[j])
                j += 1
            else:   # check for equal cases
                first = True
                i2 = i
                while i2 < len(arr1) and  arr1[i2] == arr1[i]:    # should not skip equal digits, because they also matters, case 5
                    i2 += 1
                sub1 = 0 if i2 >= len(arr1) else arr1[i2]
                j2 = j
                while j2 < len(arr2) and arr2[j2] == arr2[j]:
                    j2 += 1
                sub2 = 0 if j2 >= len(arr2) else arr2[j2]
                if sub2 > sub1:
                    first = False
                if first:
                    res.append(arr1[i])
                    i += 1
                else:
                    res.append(arr2[j])
                    j += 1

        if i < len(arr1):
            res.extend(arr1[i:])
        if j < len(arr2):
            res.extend(arr2[j:])
        return res





    def maxNumber_wrong(self, nums1, nums2, k):
        """
        Did not understand the problem at the beginning,
        Maximum number means the returned array is viewed as the digits of a number, and the target of this problem
        is to make the number biggest as possible!!!
        This solution thoughts that the target is to find top k values from two arrays and maintain the relative order.
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums1 is None or nums2 is None:
            return []  # or raise ValueError??
        m, n = len(nums1), len(nums2)
        if k == m+n:
            return nums1 + nums2
        heap = []
        for i in range(m):
            if len(heap) < k:
                heapq.heappush(heap, (nums1[i], i))
                continue
            if nums1[i] > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (nums1[i], i))
        for i in range(n):
            if len(heap) < k:
                heapq.heappush(heap, (nums2[i], i))
                continue
            if nums2[i] > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (nums2[i], i))
        res = [(x[1], x[0]) for x in heap]
        heapq.heapify(res)
        res = [x[1] for x in res]
        return res

class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums1 = [3, 4, 6, 5]
        nums2 = [9, 1, 2, 5, 8, 3]
        k = 5
        answer = [9, 8, 6, 5, 3]
        result = self.sol.maxNumber(nums1, nums2, k)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums1 = [6, 7]
        nums2 = [6, 0, 4]
        k = 5
        answer = [6, 7, 6, 0, 4]
        result = self.sol.maxNumber(nums1, nums2, k)
        self.assertEqual(answer, result)

    def test_case3(self):
        nums1 = [3, 9]
        nums2 = [8, 9]
        k = 3
        answer = [9, 8, 9]
        result = self.sol.maxNumber(nums1, nums2, k)
        self.assertEqual(answer, result)

    def test_case4(self):       # ====>
        nums1 = [2,5,6,4,4,0]
        nums2 = [7,3,8,0,6,5,7,6,2]
        k = 15
        answer = [7,3,8,2,5,6,4,4,0,6,5,7,6,2,0]    # wrong output as [7,3,8,2,5,6,4,4,0,0,6,5,7,6,2], wrong at merge
        result = self.sol.maxNumber(nums1, nums2, k)
        self.assertEqual(answer, result)

    def test_case5(self):       # ====> wrong output [4,3,1,6,5,4,7,3,9,5,3,7,8,4,1,1,4,1,3,5,9]
        nums1 = [1,6,5,4,7,3,9,5,3,7,8,4,1,1,4]
        nums2 = [4,3,1,3,5,9]
        k = 21
        answer = [4,3,1,6,5,4,7,3,9,5,3,7,8,4,1,3,5,9,1,1,4]
        result = self.sol.maxNumber(nums1, nums2, k)
        self.assertEqual(answer, result)

    def test_case6(self):       # ====> wrong output [8,5,9,5,2,6,4,3,8,4,1,1,6,9,0,7,2,9,2,8]
        nums1 = [8,5,9,5,1,6,9]
        nums2 = [2,6,4,3,8,4,1,0,7,2,9,2,8]
        k = 20
        answer = [8,5,9,5,2,6,4,3,8,4,1,6,9,1,0,7,2,9,2,8]
        result = self.sol.maxNumber(nums1, nums2, k)
        self.assertEqual(answer, result)

    def test_case7(self):       # ====> wrong output [0], from lintcode
        nums1 = [8,5,9,5,1,6,9]
        nums2 = [2,6,4,3,8,4,1,0,7,2,9,2,8]
        k = 0
        answer = []
        result = self.sol.maxNumber(nums1, nums2, k)
        self.assertEqual(answer, result)

    def test_case08(self):  # ====> wrong output [1,4,8], from lintcode, note that in leet input is single digit array
        nums1 = []
        nums2 = [11,13,14,8]
        k = 2
        answer = [14, 8]
        result = self.sol.maxNumber(nums1, nums2, k)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""

http://blog.csdn.net/u010025211/article/details/50527279

思想：从nums1中选择i个数，从nums2中选择k-i个数，使得合成的数最大。
分成两个子问题:
1. 如何从一个数组中选择i个数，使这i个数表示的数值是所有候选中最大的。
比如[9, 1, 2, 5, 8, 3] i = 2;如何得到 [9,8]。
2. 如何合并两个数组使得形成最大的值
比如[9, 8, 3] [6,5] ;如何得到[9,8,6,5,3]
Solution
To solve this problem, first let’s look at simpler version:

Easy Version No. 1

Given one array of length n, create the maximum number of length k.

The solution to this problem is Greedy with the help of stack. The recipe is as following

Initialize a empty stack
Loop through the array nums
pop the top of stack if it is smaller than nums[i] until
stack is empty
the digits left is not enough to fill the stack to size k
if stack size < k push nums[i]
Return stack
Since the stack length is known to be k, it is very easy to use an array to simulate the stack.
The time complexity is O(n) since each element is at most been pushed and popped once.


Easy Version No. 2

Given two array of length m and n, create maximum number of length k = m + n.

OK, this version is a lot closer to our original problem with the exception that we will use all the digits we have.

Still, for this version, Greedy is the first thing come to mind. We have k decisions to make, each time will just need to decide ans[i] is from which of the two. It seems obvious, we should always choose the larger one right? This is correct, but the problem is what should we do if they are equal?

This is not so obvious. The correct answer is we need to see what behind the two to decide. For example,

nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
ans = [6, 7, 6, 0, 4]
We decide to choose the 6 from nums1 at step 1, because 7 > 0. What if they are equal again? We continue to look the next digit until they are not equal. If all digits are equal then choose any one is ok. The procedure is like the merge in a merge sort. However due to the “look next until not equal”, the time complexity is O(nm).

As @lixx2100 mentioned that it is possible to have a linear time merge algorithm based on suffix array. See here andhere. But there isn’t a short implementation for suffix array construction in linear time.


Final Solution

Now let’s go back to the real problem. First, we divide the k digits required into two parts, i and k-i. We then find the maximum number of length i in one array and the maximum number of length k-i in the other array using the algorithm in section 1. Now we combine the two results in to one array using the algorithm in section 2. After that we compare the result with the result we have and keep the larger one as final answer.



"""