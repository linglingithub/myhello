#coding=utf-8

import unittest

"""
378. Kth Smallest Element in a Sorted Matrix

Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in
the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.

Subscribe to see which companies asked this question.

Hide Tags Binary Search Heap
Hide Similar Problems (M) Find K Pairs with Smallest Sums

Medium

"""



class Solution(object):

    def kthSmallest1(self, matrix, k): #202ms, 46%
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return None
        import heapq
        heap = []
        for idx, row in enumerate(matrix):
            heapq.heappush(heap, (row[0],idx,0))
        cnt = 1 #0 should start from 1 here
        while cnt < k:
            tmp = heapq.heappop(heap)
            rowidx = tmp[1]
            colidx = tmp[2]+1
            if colidx < len(matrix[rowidx]):
                heapq.heappush(heap, (matrix[rowidx][colidx], rowidx,colidx))
            cnt += 1
            #print "{0} -- {1} from row {2}".format(cnt, tmp[0], rowidx)
        return heapq.heappop(heap)[0]

    def kthSmallest(self, matrix, k): #69ms, 92%, ref
        n = len(matrix)
        L, R = matrix[0][0], matrix[n - 1][n - 1]
        while L < R:
            mid = L + ((R - L) >> 1)
            temp = self.search_lower_than_mid(matrix, n, mid)
            if temp < k:
                L = mid + 1
            else:
                R = mid
        return L

    def search_lower_than_mid(self, matrix, n, x):
        i, j = n - 1, 0
        cnt = 0
        while i >= 0 and j < n:
            if matrix[i][j] <= x:
                j += 1
                cnt += i + 1
            else:
                i -= 1
        return cnt


    def kthSmallest2(self, matrix, k): #199ms, 48%
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return None
        import heapq
        heap = []
        for idx, row in enumerate(matrix):
            heapq.heappush(heap, (row[0],[idx,0]))
        cnt = 1 #0 should start from 1 here
        while cnt < k:
            tmp = heapq.heappop(heap)
            rowidx = tmp[1][0]
            colidx = tmp[1][1]+1
            if colidx < len(matrix[rowidx]):
                heapq.heappush(heap, (matrix[rowidx][colidx], [rowidx,colidx]))
            cnt += 1
            #print "{0} -- {1} from row {2}".format(cnt, tmp[0], rowidx)
        return heapq.heappop(heap)[0]

    def kthSmallest1(self, matrix, k): #1.23%
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return None
        import heapq
        heap = []
        for idx, row in enumerate(matrix):
            heapq.heappush(heap, (row[0],idx))
            row[0] = False
        cnt = 1 #0 should start from 1 here
        while cnt < k:
            tmp = heapq.heappop(heap)
            rowidx = tmp[1]
            for colidx, val in enumerate(matrix[rowidx]):
                if val is False:
                    continue
                heapq.heappush(heap, (val, rowidx)) # don't forget to push together the rowidx here
                matrix[rowidx][colidx] = False
            cnt += 1
            #print "{0} -- {1} from row {2}".format(cnt, tmp[0], rowidx)
        return heapq.heappop(heap)[0]






class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [
           [ 1,  5,  9],
           [10, 11, 13],
           [12, 13, 15]
        ]
        k = 8
        answer = 13
        result = self.sol.kthSmallest(nums, k)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""
https://www.hrwhisper.me/leetcode-kth-smallest-element-sorted-matrix/

思路：
先想到的就是用堆。直接维护一个大小为k的堆，全部读入一遍，这样平均和最坏情况都为O(n^2 *  logk) 很暴力，没有利用有序的特点。
因为每一行和每一列都是有序的了，因此维护一个最小堆，每次取出堆顶的元素，然后把它下方的元素放进堆(如果是第一行，还要把它右边的元素放入，这样
不会重复。)
这样做K次后堆顶元素就是第K大的了。这样复杂度为多少呢？O(KlogK) 然而K最坏情况是n^2….. 因此，这个方法也一般。
PS: 本来写k  – – > 0 的，想到以前知乎上看到的 C语言有啥奇技淫巧， – – >是趋向于， 哈哈哈~ 一本正经的胡说八道


我觉得用二分做最好，这个方法只要求行有序，和列有木有序并没有关系。 （或者列有序，行有序无序都没关系）
设L = min(matrix) R= max(matrix)  , mid =( L + R ) / 2 ，mid为我们猜测的答案。
然后对于每一行，找它在该行中第几大（也是二分，找上界），累加和K比较。
值得注意的是枚举 答案应该用下界， 因为猜想的解不一定在数组中，不断的收缩直到找到在数组中的元素为止。
查找一行需要log(n) ，有n行所以nlog(n)，最坏下需要查找log(X)次（X= int最大值的时候logX仅仅才为32），X为最大最小数差值。  所以总复杂度为
O(nlogn *  logX)
PS：其实是我一开始看成就行有序→_→，然后就直接二分了

上述的解法并没有利用到列有序的性质。
而下面的解法利用了列有序的性质，并将复杂度降到了O(nlogX)   其中X = max – min
我们仍采用猜测法，设L = min(matrix) R= max(matrix) , mid =( L + R ) / 2 ，mid为我们猜测的答案。
对于mid，我们不必再所有的行或列种执行二分查找，我们可以从左下角出发，若matrix[i][j] <= mid，则下一次查询在右边（j++），并且，该列的所有
元素均比mid小，因此可以cnt += (i+1)
对于matrix[i][j] > mid，则 i – – 。 过程类似于240. Search a 2D Matrix II  (题解在最下方)




"""

#-*- coding:utf-8 -*-
