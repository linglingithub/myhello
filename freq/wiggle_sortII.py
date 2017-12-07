#coding=utf-8

import unittest

"""
todo

324. Wiggle Sort II


Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example:
(1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6]. 
(2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].

Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.

Difficulty:Medium
Total Accepted:30.7K
Total Submissions:117.9K
Contributor: LeetCode
Subscribe to see which companies asked this question.

Related Topics 
Sort 
Similar Questions 
Sort Colors Kth Largest Element in an Array Wiggle Sort 

"""

import random
import time



class Solution(object):  # ref
    def wiggleSort(self, nums):
        """
        用快排的思想查找中位数，然后再合并两边。
        最坏复杂度O(n^2)，平均复杂度O(n)
        :param nums: 
        :return: 
        """
        n = len(nums) - 1
        medium = self.findMedium(nums, 0, n - 1, (n + 1) >> 1)
        s = 0
        t = n - 1
        mid_index = (n + 1) >> 1
        temp = [0 for _ in range(n)]
        for i in range(n):
            if nums[i] < medium:
                temp[s] = nums[i]
                s += 1
            elif nums[i] > medium:
                temp[t] = nums[i]
                t -= 1

        while s < mid_index:
            temp[s] = medium
            s += 1
        while t >= mid_index:
            temp[t] = medium
            t -= 1

        t = n
        for i in range(n):
            if i & 1 == 0:  # for odd idx
                s -= 1
                nums[i] = temp[s]
            else:           # for even idx
                t -= 1
                nums[i] = temp[t]


    def findMedium(self, nums, left, right, k):
        if left >= right:
            return nums[right]
        i = self.partition(nums, left, right)
        cnt = i - left + 1
        if cnt == k:
            return nums[i]
        elif cnt > k:
            return self.findMedium(nums, left, i - 1, k)
        else:
            return self.findMedium(nums, i + 1, right, k - cnt)


    def partition(self, nums, left, right):
        val = nums[left]
        i, j = left, right + 1
        while True:
            i += 1
            while i < right and nums[i] < val:
                i += 1
            j -= 1
            while j > left and nums[j] > val:
                j -= 1
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]
        nums[left], nums[j] = nums[j], nums[left]
        return j




class Solution1(object):  # ref
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        mid = self.quickselect(nums, len(nums) / 2)

        # print "quick select: ", nums

        # mapping from index to wiggle index
        # example: [0, 1, 2, ... , n - 1, n] to [1, 3, 5, ... , 0, 2, 4, ...]
        N = len(nums)
        i, j, k = 0, 0, len(nums) - 1
        while j <= k:
            if nums[(1 + 2 * j) % (N | 1)] > mid:
                nums[(1 + 2 * i) % (N | 1)], nums[(1 + 2 * j) % (N | 1)] = nums[(1 + 2 * j) % (N | 1)], nums[
                    (1 + 2 * i) % (N | 1)]
                i += 1
                j += 1
            elif nums[(1 + 2 * j) % (N | 1)] < mid:
                nums[(1 + 2 * j) % (N | 1)], nums[(1 + 2 * k) % (N | 1)] = nums[(1 + 2 * k) % (N | 1)], nums[
                    (1 + 2 * j) % (N | 1)]
                k -= 1
            else:
                j += 1
                # My quickSelect module looks like this (based on pseudo code in WikiPedia):

    def partition(self, array, pivotId, left, right):
        pivotValue = array[pivotId]
        array[right], array[pivotId] = array[pivotId], array[right]

        pos = left
        for j in range(left, right):
            if array[j] < pivotValue:
                array[pos], array[j] = array[j], array[pos]
                pos += 1

        array[right], array[pos] = array[pos], array[right]
        return pos

    def quickselect(self, array, id):
        random.seed(time.time())
        return self.select(array, id, 0, len(array) - 1)

    def select(self, array, id, left, right):
        while left < right:
            pivot = random.randrange(left, right)

            pivotPos = self.partition(array, pivot, left, right)

            if pivotPos == id:
                return array[pivotPos]
            elif pivotPos < id:
                left = pivotPos + 1
            else:
                right = pivotPos - 1
        return array[right]


class Solution1(object):

    def wiggleSort_wrong(self, nums):  # ref- self idea, O(n) space,
        """
        0 1 2 3 4 5 6 --> 7/2 = 3
        0 3 1 4 2 5 6 --> not good, 5,6 still next to each other, if odd, later half need to start with n/2 + 1

        0 1 2 3 4 5 6 --> 7/2 + 1 = 4
        0 4 1 5 2 6 3 , which means 

        0 - 0
        1 - 2
        2 - 4   
        3 - 6
        4 - 1
        5 - 3
        6 - 5

        mid_idx = 4

        i -> 2 * ( i - mid ) +1 (i >= mid)
        i -> 2 * i ( i < mid ) 
        
        =========> not good, case [4,5,5,6]
        should put middle part towards two ends [5,4,6,5], then shuffle card [5,6,4,5]
        

        :param nums: 
        :return: 
        """
        n = len(nums)

        # find a median
        mid = n / 2 + (1 if n % 2 else 0)
        mid_idx = self.find_kth_ele_idx(nums, mid)

        nnums = nums[:mid][::-1] + nums[mid:][::-1]
        for i in range(n):
            if i < mid:
                nums[2*i] = nnums[i]
            else:
                nums[2*(i-mid_idx)+1] = nnums[i]
        #nums[:] = nnums  # note, if nums = nnums is wrong, nums = nnums[:] is wrong too, need to do nums[:] = nnums([;] or not)


    def wiggleSort_wrong(self, nums):  # ref- self idea, O(n) space, still have chance to have equal vals neighboring, case4
        """
        0 1 2 3 4 5 6 --> 7/2 = 3
        0 3 1 4 2 5 6 --> not good, 5,6 still next to each other, if odd, later half need to start with n/2 + 1
        
        0 1 2 3 4 5 6 --> 7/2 + 1 = 4
        0 4 1 5 2 6 3 , which means 
        
        0 - 0
        1 - 2
        2 - 4   
        3 - 6
        4 - 1
        5 - 3
        6 - 5
        
        mid_idx = 4
        
        i -> 2 * ( i - mid ) +1 (i >= mid)
        i -> 2 * i ( i < mid )
        
        :param nums: 
        :return: 
        """
        n = len(nums)

        # find a median
        mid = n/2 + (1 if n%2 else 0)
        mid_idx = self.find_kth_ele_idx(nums, mid)

        nnums = [-1 for _ in range(n)]
        for i in range(n):
            if i < mid:
                nnums[2 * i] = nums[i]
            else:
                nnums[2 * (i - mid_idx) + 1] = nums[i]
        nums[:] = nnums  # note, if nums = nnums is wrong, nums = nnums[:] is wrong too, need to do nums[:] = nnums([;] or not)


    def wiggleSort_idx_wrong(self, nums):  # ref idea
        n = len(nums)

        # find a median
        mid = n/2 + (1 if n%2 else 0)
        mid_idx = self.find_kth_ele_idx(nums, mid)

        i, j, k = 0, 0, n-1
        while j <= k:
            # index rewiring here
            idx = (1 + 2*j) % (n|1)
            if nums[idx] > mid:
                nidx = (1 + 2*i) % (n|1)
                nums[idx], nums[nidx] = nums[nidx], nums[idx]
                i += 1
                j += 1
            elif nums[idx] < mid:
                nidx = (1 + 2*k) % (n|1)
                nums[idx], nums[nidx] = nums[nidx], nums[idx]
                k -= 1
            else:
                j += 1

    def find_kth_ele_idx(self, nums, k):  # good
        # use quick select to find kth smallest element
        left, right = 0, len(nums) - 1
        # i, j = -1, 0    # should be reset within new partition range, otherwise wrong
        while left < right:
            i, j = left - 1, left
            pivot = nums[right]
            while j < right:
                if nums[j] <= pivot:  # because there are dupicated number, better to take that = in
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
                j += 1
            i += 1
            nums[i], nums[right] = nums[right], nums[i]
            if i == k:
                return k
            elif i > k:
                right = i - 1  # should be i not k here
            else:
                left = i + 1
        return left         # don't forget this !!!









    def wiggleSort1(self, nums): # ref, O(nlogn)
        """
        By putting biggest to smallest nums to 1,3,5...0, 2,4... places, avoid the equal situation, and make the wiggle shape
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        snums = sorted(nums)
        for x in range(1,n, 2) + range(0, n, 2):  # note that ending is always n, for odd/even number of len(n)
            nums[x] = snums.pop()

    def wiggleSort_wrong(self, nums):
        """
        For the sort and swap way, easy to understand, use O(nlogn) time.
        For the linear way, try to go through one example then it's obvious that the swap won't affect previous wiggle 
        shape of the nums.
        ===> for new requirement that <><>, the I way does not work anymore for duplicated values
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        if not nums:
            return

        for i in range(1, len(nums)):
            if i % 2 == 1 and nums[i] <= nums[i - 1] or i % 2 == 0 and nums[i] >= nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]





class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1, 5, 1, 1, 6, 4]
        answer = [1,5,1,6,1,4]  # may have other valid output
        result = self.sol.wiggleSort(nums)
        self.assertEqual(answer, nums)

    def test_case2(self):
        nums = [1, 3, 2, 2, 3, 1]
        answer = [1, 3, 2, 3, 1, 2]  # may have other valid output
        result = self.sol.wiggleSort(nums)
        self.assertEqual(answer, nums)

    def test_case3(self):  # ====>
        nums = [1,2,2,1,2,1,1,1,1,2,2,2]
        answer = [1,2,1,2,1,2,1,2,1,2,1,2] # may have other valid output, wrong output as [1,2,1,2,1,2,1,1,1,2,2,2]
        result = self.sol.wiggleSort(nums)
        self.assertEqual(answer, nums)

    def test_case4(self):  # ====>
        nums = [4,5,5,6]
        answer = [5,6,4,5] # may have other valid output, wrong output as [4,5,5,6]
        result = self.sol.wiggleSort(nums)
        self.assertEqual(answer, nums)

    def test_case05(self):  # ====>
        nums = [5,3,1,2,6,7,8,5,5]
        answer = [5,8,5,7,3,6,2,5,1] # may have other valid output, wrong output as [5,7,2,6,1,8,3,5,5]
        result = self.sol.wiggleSort(nums)
        self.assertEqual(answer, nums)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""

http://easyleetcode.blogspot.com/2016/03/leetcode-wiggle-sort-ii.html


Comparing with Wiggle Sort, the only difference here is that it does not allow duplicates.  The goal of this problem is to reorder this array, so that 
nums[0] < nums[1] > nums[2] < nums[3]...
Let me translate, so need to place larger numbers in array at the odd index (1,3,5...), and place smaller numbers at even index (0,2,4...).
Larger numbers means number larger than the median of this array, and smaller means smaller than median of array.
TASK 1: find median
What's the fastest way? Don't even think about sorting since it's completely unnecessary. If you check basic algorithm course material, the answer would be "quick select". Similar to quick sort, quick select uses random pivot and reorder array so that elements larger than pivot is ordered to the left of pivot whereas elements smaller than pivot are ordered to the right of pivot. Thus, runtime relation is
T(N) <= T(N/2) + O(N)
meaning this is a shrinking recursion tree, the runtime is O(N) on average. 

TASK2: reorder to wiggle sort
Now after running quick select, you know the median, you can iterate array and check if element is "larger" or "smaller". Then you can put "larger" ones at odd position and "smaller" ones at even position. The easiest way is always creating an additional array. But, as a follow up question, can we do this in space?
The answer is yes! It's actually not as complicated as you think. We already know how to reorder array to put "larger" elements to the right and "smaller" elements to the left. (as part of quick select algorithm). Doing that in place is easy. Wiggle sort is actually the same! Just different index mapping! So you're basically mapping array index in right half of array to odd index. Similarly, mapping index in left half to even index.
Example: 
[0, 1, 2, ... , n - 1, n] to [1, 3, 5, ... , 0, 2, 4, ...]
The relation is actually (consider even, odd cases separately then merge them to a single representation): 
j to (1 + 2*j)%(N|1)

Put everything in python:
class Solution(object):
    def wiggleSort(self, nums):
        mid = quickSelect.quickselect(nums, len(nums)/2)

        print "quick select: ", nums

        # mapping from index to wiggle index
        # example: [0, 1, 2, ... , n - 1, n] to [1, 3, 5, ... , 0, 2, 4, ...]
        N = len(nums)
        i, j, k = 0, 0, len(nums)-1
        while j <= k:
            if nums[(1 + 2*j)%(N|1)] > mid:
                nums[(1 + 2*i)%(N|1)], nums[(1 + 2*j)%(N|1)] = nums[(1 + 2*j)%(N|1)], nums[(1 + 2*i)%(N|1)]
                i+=1
                j+=1
            elif nums[(1 + 2*j)%(N|1)] < mid:
                nums[(1 + 2*j)%(N|1)], nums[(1 + 2*k)%(N|1)] =  nums[(1 + 2*k)%(N|1)], nums[(1 + 2*j)%(N|1)]
                k-=1
            else:
                j+=1
My quickSelect module looks like this (based on pseudo code in WikiPedia): 
 
import random
import time

def partition(array, pivotId, left, right):
    pivotValue = array[pivotId]
    array[right], array[pivotId] = array[pivotId], array[right]

    pos = left
    for j in range(left, right):
        if array[j] < pivotValue:
            array[pos], array[j] = array[j], array[pos]
            pos += 1

    array[right], array[pos] = array[pos], array[right]
    return pos

def quickselect(array, id):
    random.seed(time.time())
    return select(array, id, 0, len(array)-1)

def select(array, id, left, right):
    while left < right:
        pivot = random.randrange(left, right)

        pivotPos = partition(array, pivot, left, right)

        if pivotPos == id:
            return array[pivotPos]
        elif pivotPos < id:
            left = pivotPos+1
        else:
            right = pivotPos-1
    return array[right]


==============================================


http://liveasatree.blogspot.com/2016/01/leetcode-wiggle-sort-ii.html

参考：https://leetcode.com/discuss/77133/o-n-o-1-after-median-virtual-indexing

思路：
1）QucikSort 的方法找出中间值，时间O(n)，空间O(1)
2）参见参考链接，类似于给三种颜色排序，将高中低三种值各自规划成一组，由于其中涉及到数组索引的变换，使得实际得到的结果是高低穿插。例如：

数组值：高    高    高    中    中    低
原索引： 0      1      2      3      4      5
变换后： 3      0      4      1      5      2


依据变换索引给高中低值进行规划（顺序为高中低）：

变换后索引值： 0      1      2      3      4      5
数 组    值： 高     高      高     中     中     低
原     索引： 1      3      5      0      2      4

也就是

原     索     引： 0     1      2     3     4      5
数     组     值：中    高    中    高    低    中

这个方法的另一个好处是变换后中间值是相邻的，使得变换前中间值是岔开的，解决了[4, 5 , 5, 6]这种情况

时间O(n)，空间O(1)

代码：
public class Solution {
    public void wiggleSort(int[] nums) {
        if (nums == null || nums.length <= 1) return;
        int median = getMedian(nums);

        int higher = 0, lower = nums.length - 1, current = 0;
        while (current <= lower) {
            if (nums[reIndex(current, nums.length)] == median) {
                current++;
            }

            else if (nums[reIndex(current, nums.length)] < median) {
                swap(nums, reIndex(current, nums.length), reIndex(lower--, nums.length));
            }
            else swap(nums, reIndex(current++, nums.length), reIndex(higher++, nums.length));
        }
    }
   
    private int reIndex(int index, int n) {
        return (2*index + 1) % (n | 1);
    }

    private int getMedian(int[] nums) {
        int start = 0, end = nums.length - 1, target = nums.length / 2;
        while (true) {
            swap(nums, start, (start + end) / 2);
            int swapIndex = start, current = start + 1;
            while (current <= end) {
                if (nums[current] >= nums[start]) swap(nums, ++swapIndex, current);
                current++;
            }
            swap(nums, start, swapIndex);
            if (swapIndex - start == target) return nums[swapIndex];
            else if (swapIndex - start > target) end = swapIndex - 1;
            else {
                target -= (swapIndex - start + 1);
                start = swapIndex + 1;
            }
        }
    }

    private void swap(int[] nums, int index1, int index2) {
        int temp = nums[index1];
        nums[index1] = nums[index2];
        nums[index2] = temp;
    }
}




===========================================

http://bookshadow.com/weblog/2015/12/31/leetcode-wiggle-sort-ii/



解法I O(nlogn)时间排序+O(n)空间辅助数组解法：

1. 对原数组排序，得到排序后的辅助数组snums

2. 对原数组的偶数位下标填充snums的末尾元素

3. 对原数组的奇数位下标填充snums的末尾元素

class Solution(object):
    def wiggleSort(self, nums):

        size = len(nums)
        snums = sorted(nums)
        for x in range(1, size, 2) + range(0, size, 2):
            nums[x] = snums.pop()


解法II O(n)时间复杂度+O(1)空间复杂度解法：

1. 使用O(n)时间复杂度的quickSelect算法，从未经排序的数组nums中选出中位数mid

2. 参照解法I的思路，将nums数组的下标x通过函数idx()从[0, 1, 2, ... , n - 1, n] 映射到 [1, 3, 5, ... , 0, 2, 4, ...]，得到新下标ix

3. 以中位数mid为界，将大于mid的元素排列在ix的较小部分，而将小于mid的元素排列在ix的较大部分。

详见：https://leetcode.com/discuss/77133/o-n-o-1-after-median-virtual-indexing


C++伪代码：
void wiggleSort(vector<int>& nums) {
    int n = nums.size();

    // Find a median.
    auto midptr = nums.begin() + n / 2;
    nth_element(nums.begin(), midptr, nums.end());
    int mid = *midptr;

    // Index-rewiring.
    #define A(i) nums[(1+2*(i)) % (n|1)]

    // 3-way-partition-to-wiggly in O(n) time with O(1) space.
    int i = 0, j = 0, k = n - 1;
    while (j <= k) {
        if (A(j) > mid)
            swap(A(i++), A(j++));
        else if (A(j) < mid)
            swap(A(j), A(k--));
        else
            j++;
    }
}



"""

#-*- coding:utf-8 -*-
