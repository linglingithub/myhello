#coding=utf-8

import unittest

"""
 
398. Random Pick Index

Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume 
that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);

Related Topics 
Reservoir Sampling 
Similar Questions 
Linked List Random Node 

Medium

"""
import random

class Solution(object):
    def __init__(self, nums): # AC, beats 50+%
        """
        reservoir sampling way, according to ref idea
        save the memory.
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        cnt = 0
        result = -1
        for idx, num in enumerate(self.nums):
            if num != target:
                continue
            cnt += 1
            lottery = random.randint(1, cnt)
            if lottery == 1:
                result = idx
        return result


class Solution_ref(object):  # just most basic and simple way, pass 13 cases with 90+% performance!!!
    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):
        return random.choice([k for k, v in enumerate(self.nums) if v == target])

class Solution_MLE(object):
    def __init__(self, nums): #
        """
        MLE with 13 cases passed, case inputs check random_pick_index_caseMLE.ini, need to think about how to 
        save the memory.
        :type nums: List[int]
        :type numsSize: int
        """
        self.vals = {}
        for idx, num in enumerate(nums):
            self.vals[num] = self.vals.get(num, []) + [idx]

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        import random
        res = self.vals.get(target)
        if not res:
            return -1
        return random.choice(res)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = 1
        answer = 1
        result = self.sol.searchInsert(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""

What on earth is meant by too much memory?
Because I've made a rather naive map-of-index-lists Java solution and it was happily accepted by the OJ. So far I see 
three types of solutions:

Like mine, O(N) memory, O(N) init, O(1) pick.

Like @dettier's Reservoir Sampling. O(1) init, O(1) memory, but O(N) to pick.

Like @chin-heng's binary search: O(N) memory, O(N lg N) init, O(lg N) pick.

Are all three kinds acceptable?

=======================================================================================================================

How does this work?
To prove that this solution works perfectly, we must prove that the probability that any item stream[i] where 0 <= i < n 
will be in final reservoir[] is k/n. Let us divide the proof in two cases as first k items are treated differently.

Case 1: For last n-k stream items, i.e., for stream[i] where k <= i < n 
For every such stream item stream[i], we pick a random index from 0 to i and if the picked index is one of the first k 
indexes, we replace the element at picked index with stream[i]

To simplify the proof, let us first consider the last item. The probability that the last item is in final reservoir 
= The probability that one of the first k indexes is picked for last item 
= k/n (the probability of picking one of the k items from a list of size n)

Let us now consider the second last item. The probability that the second last item is in final reservoir[] 
= [Probability that one of the first k indexes is picked in iteration for stream[n-2]] X [Probability that the index 
picked in iteration for stream[n-1] is not same as index picked for stream[n-2] ] 
= [k/(n-1)]*[(n-1)/n] 
= k/n.

Similarly, we can consider other items for all stream items from stream[n-1] to stream[k] and generalize the proof.

Case 2: For first k stream items, i.e., for stream[i] where 0 <= i < k 
The first k items are initially copied to reservoir[] and may be removed later in iterations for stream[k] to stream[n].
The probability that an item from stream[0..k-1] is in final array 
= Probability that the item is not picked when items stream[k], stream[k+1], …. stream[n-1] are considered 
= [k/(k+1)] x [(k+1)/(k+2)] x [(k+2)/(k+3)] x … x [(n-1)/n] 
= k/n

References:
http://en.wikipedia.org/wiki/Reservoir_sampling

Please write comments if you find anything incorrect, or you want to share more information about the topic discussed 
above.


========================================================================

http://hongzheng.me/leetcode/leetcode-398-random-pick-index/

这种随机数的题目很少做。这个题目用到了蓄水池抽样算法(Reservoir Sampling). wikipedia里有详细说明。

For sample size 1:

Suppose we see a sequence of items, one at a time. We want to keep a single item in memory, and we want it to be 
selected at random from the sequence. If we know the total number of items (n), then the solution is easy: select an 
index i between 1 and n with equal probability, and keep the i-th element. The problem is that we do not always know n 
in advance. A possible solution is the following:

Keep the first item in memory.
When the i-th item arrives (for i>1):
with probability 1/i, keep the new item (discard the old one)
with probability 1-1/i, keep the old item (ignore the new one)
So:

when there is only one item, it is kept with probability 1;
when there are 2 items, each of them is kept with probability 1/2;
when there are 3 items, the third item is kept with probability 1/3, and each of the previous 2 items is also kept with 
probability (1/2)(1-1/3) = (1/2)(2/3) = 1/3;
by induction, it is easy to prove that when there are n items, each item is kept with probability 1/n.


"""