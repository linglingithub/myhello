#coding=utf-8

import unittest

"""

Sliding Window Median

Given an array of n integer, and a moving window(size k), move the window at each iteration from the start of the array, 
find the median of the element inside the window at each moving. (If there are even numbers in the array, return the 
N/2-th number after sorting the element in the window. )

Have you met this question in a real interview? Yes
Example
For array [1,2,7,8,5], moving window size k = 3. return [2,7,7]

At first the window is at the start of the array like this

[ | 1,2,7 | ,8,5] , return the median 2;

then the window move one step forward.

[1, | 2,7,8 | ,5], return the median 7;

then the window move one step forward again.

[1,2, | 7,8,5 | ], return the median 7;

Challenge 
O(nlog(n)) time

Tags 
Heap LintCode Copyright
Related Problems 
Hard Paint House II 25 %
Super Building Outline 14 %
Super Sliding Window Maximum 27 %
Hard Data Stream Median

"""


class Solution:
    """
    @param nums: A list of integers.
    @return: The median of element inside the window at each moving.
    """
    def medianSlidingWindow(self, nums, k):
        # write your code here
        import heapq
        minheap = []
        heapq.heappush(minheap, nums[0])




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1,2,7,8,5]
        k = 3
        answer = [2,7,7]
        result = self.sol.medianSlidingWindow(nums, k)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""

class node:

    def __init__(self, id, number):
        self.id = id
        self.num = number

class HashHeap:
    def __init__(self):
        self.map = {}
        self.hashmaxheap = [0]
        self.map[0] = node(0, 1)
        self.currentSize = 0

    def put(self, data):
        if data in self.map:
            existData = self.map[data]
            self.map[data] = node(existData.id, existData.num + 1)
            self.currentSize += 1
            return 
        else:
            self.hashmaxheap.append(data)
            self.map[data] = node(len(self.hashmaxheap) - 1, 1)
            self.currentSize += 1
            self.siftUp(len(self.hashmaxheap) - 1)

    def peek(self):
        return self.hashmaxheap[1]

    def get(self):
        res = self.hashmaxheap[1]
        if self.map[res].num == 1:
            if self.map[res].id == len(self.hashmaxheap) - 1:
                del self.map[res]
                self.hashmaxheap.pop()
                self.currentSize -= 1
                return res
            del self.map[res]
            self.hashmaxheap[1] = self.hashmaxheap[-1]
            self.map[self.hashmaxheap[1]] = node(1, self.map[self.hashmaxheap[1]].num)
            self.hashmaxheap.pop()
            self.siftDown(1)
        else:
            self.map[res] = node(1, self.map[res].num - 1)
        self.currentSize -= 1
        return res

    def delete(self, data):
        existData = self.map[data]
        if existData.num == 1:
            del self.map[data]
            if existData.id == len(self.hashmaxheap) - 1:
                self.hashmaxheap.pop()
                self.currentSize -= 1
                return
            self.hashmaxheap[existData.id] = self.hashmaxheap[-1]
            self.map[self.hashmaxheap[-1]] = node(existData.id, self.map[self.hashmaxheap[-1]].num)
            self.hashmaxheap.pop()
            self.siftUp(existData.id)
            self.siftDown(existData.id)
        else:
            self.map[data] = node(existData.id, existData.num - 1)
        self.currentSize -= 1

    def siftUp(self, index):
        while index // 2 > 0:
            if self.hashmaxheap[index] < self.hashmaxheap[index // 2]:
                break
            else:
                numA = self.map[self.hashmaxheap[index]].num
                numB = self.map[self.hashmaxheap[index // 2]].num
                self.map[self.hashmaxheap[index]] = node(index // 2, numA)
                self.map[self.hashmaxheap[index // 2]] = node(index, numB)
                self.hashmaxheap[index], self.hashmaxheap[index // 2] = self.hashmaxheap[index // 2], self.hashmaxheap[index] 
            index = index // 2

    def siftDown(self, index):
        if index > (len(self.hashmaxheap) - 1) // 2:
            return
        if (index * 2 + 1) > (len(self.hashmaxheap) - 1) or self.hashmaxheap[index * 2] > self.hashmaxheap[index * 2 + 1]:
            maxChild = index * 2
        else:
            maxChild = index * 2 + 1
        if self.hashmaxheap[index] > self.hashmaxheap[maxChild]:
            return
        else:
            numA = self.map[self.hashmaxheap[index]].num
            numB = self.map[self.hashmaxheap[maxChild]].num
            self.map[self.hashmaxheap[index]] = node(maxChild, numA)
            self.map[self.hashmaxheap[maxChild]] = node(index, numB)
            self.hashmaxheap[index], self.hashmaxheap[maxChild] = self.hashmaxheap[maxChild], self.hashmaxheap[index] 
        self.siftDown(index * 2)
        self.siftDown(index * 2 + 1)

    def size(self):
        return self.currentSize

    def isEmpty(self):
        return self.currentSize == 0

class Solution:
    def medianSlidingWindow(self, nums, k):
        res = []
        if not nums:
            return res

        median = nums[0]
        minHeap = HashHeap()
        maxHeap = HashHeap()
        for i in range(len(nums)):
            if i != 0:
                if nums[i] > median:
                    minHeap.put(- nums[i])
                else:
                    maxHeap.put(nums[i])
            if i >= k:
                if median == nums[i - k]:
                    if not maxHeap.isEmpty():
                        median = maxHeap.get()
                    elif not minHeap.isEmpty():
                        median = - minHeap.get()
                elif median < nums[i - k]:
                    minHeap.delete(- nums[i - k])
                else:
                    maxHeap.delete(nums[i - k])

            while maxHeap.size() > minHeap.size():
                minHeap.put(- median)
                median = maxHeap.get()

            while minHeap.size() > maxHeap.size() + 1:
                maxHeap.put(median)
                median = - minHeap.get()

            if i + 1 >= k:
                res.append(median)

        return res
        
        

"""