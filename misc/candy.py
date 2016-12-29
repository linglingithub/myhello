#coding=utf-8

"""
135. Candy

There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Subscribe to see which companies asked this question

Hide Tags Greedy

Hard

"""

import unittest


class Solution(object):
    def candy(self, ratings): #85ms, 67%
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return 0
        n = len(ratings)
        candies = [1 for i in range(n)]
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                candies[i] = candies[i-1]+1
        total = candies[n-1]
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]: #should add 'and candies[i] <= candies[i+1]' otherwise wrong for case 5
                candies[i] = candies[i+1]+1
            total += candies[i]
        return total
            


    def candy_wrong(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return 0
        total = 1
        cnt = 1
        ratings.sort()
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                cnt += 1
            total += cnt
        return total
        
        


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    
    def test_case5(self): #====>
        nums = [4, 2, 3, 4, 1] # 1,1,2,3,1
        answer = 9
        result = self.sol.candy(nums)
        self.assertEqual(answer, result)
        

    def test_case4(self): #=====>
        """
        this case means that only need to have more candy than 'neighbors' if score is higher,
         does NOT mean same ratings get same candies.
         if neighbors have same rating, one of them may have less candies
        :return:
        """
        nums = [1,2,2]
        answer = 4
        result = self.sol.candy(nums)
        self.assertEqual(answer, result)

    def test_case1(self):
        nums = [12,43,54,7,1] # 1,2,3,2,1
        answer = 9
        result = self.sol.candy(nums)
        self.assertEqual(answer, result)
        
    def test_case2(self):
        nums = [1,43,54,7,1]
        answer = 9
        result = self.sol.candy(nums)
        self.assertEqual(answer, result)
        
    def test_case3(self):
        nums = [2,2,2]
        answer = 3
        result = self.sol.candy(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""
贪心算法（Greedy Algorithm）

评分同时低于左右两边的孩子只需分配一个糖果

评分相同的相邻孩子，分配的糖果可以不同

算法步骤如下：

1. 首先为每一个孩子分配1个糖果

记当前孩子序号为i，糖果数为candies[i]，评分为ratings[i]

2. 从左向右遍历，若ratings[i] > ratings[i - 1]，则令candies[i] = candies[i - 1] + 1

3. 从右向左遍历，若ratings[x] > ratings[x + 1]，则令candies[x] = max(candies[x], candies[x + 1] + 1)

"""

#-*- coding:utf-8 -*-
