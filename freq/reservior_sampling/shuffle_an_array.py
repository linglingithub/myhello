#coding=utf-8

import unittest

"""

384. Shuffle an Array
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();


Medium

"""

import copy
import random


class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.__bak = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.__bak

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        res = [x for x in self.__bak]
        for i in range(len(res)):
            # idx = random.randint(1, i + 1) - 1
            idx = random.randint(0, i)
            res[i], res[idx] = res[idx], res[i]
        return res

class Solution_notgood(object):
    def __init__(self, nums):  # 21+% --> hide __bak, add __n, ~34%
        """
        :type nums: List[int]
        """
        self.__bak = nums  # a good habit to hide the bak
        self.__n = len(self.__bak)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.__bak


    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        res = self.__bak[:]

        for i in range(self.__n):
            idx = random.randint(0, self.__n-1)
            res[i], res[idx] = res[idx], res[i]
        return res  # don't forget this

class Solution_slow(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.bak = nums
        self.nums = copy.deepcopy(self.bak)


    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.nums = copy.deepcopy(self.bak)
        return self.nums


    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in range(len(self.bak)):
            idx = random.randint(0, len(self.bak)-1)
            self.nums[i], self.nums[idx] = self.nums[idx], self.nums[i]
        return self.nums   # don't forget this


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()


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

"""

https://yjk94.wordpress.com/2017/03/17/%E6%B4%97%E7%89%8C%E7%9A%84%E6%AD%A3%E7%A1%AE%E5%A7%BF%E5%8A%BF-knuth-shuffle%E7%AE%97%E6%B3%95/

洗牌的正确姿势-Knuth shuffle算法

2017年3月17日 ~ JKYU
关于洗牌问题：

怎样用计算机模拟出足够随机的洗牌结果，看似很简单，但其实它比给一副乱糟糟的牌排好序可能还更难一些。洗牌问题的描述很简单：即如何通过打乱顺序，
让一副扑克牌变成随机的排列，而且每一种可能的排列有相同机会出现。关键点在于“相同机会”，即各种随机排列是等可能的。
下面先简单介绍一个常见的错误做法，然后看看如何改进变成Knuth 洗牌算法。

 

先看看一个很直接的做法（一副牌在这里用一个数组表示）：

对数组从头到尾扫描一遍，扫描过程中，每次都从整个数组随机选一个元素，跟当前扫描到的元素交换位置。

也就是，先拿起第一张牌，把它跟从整副牌里随机挑出的另一张牌（把它叫做随机牌）交换位置（随机牌也可能是第一张牌自己，这个时候就相当于不交换位置）；
接着拿起第二张牌，也把它跟随机选出的另一张牌交换位置；一直重复直到把最后一张牌跟随机牌交换位置。

用python实现起来也只有几行：


def shuffleSort(a):
  N = len(a)
  for i in range(N):
    j = random.randint(0, N-1)
    a[j], a[i] = a[i], a[j]
    
    
这样随机交换之后，每种排列出现的可能性会是等概率的吗？看起来好像会，但事实上，经过这样交换，总有一部分排列出现的概率更高一些，
这个洗牌过程并没有很公平。

为什么不够公平？要从直觉上能够理解清楚还不是那么容易。我们用一个简单的例子来看看，假设这副牌只有三张，分别是{A，B， C}.

按照前面说的方法，第一轮把第一张牌A跟随机一张牌进行交换，会产生三个等可能的结果：

no change:      {A, B,  C}
swap with B:    {B,  A, C}
swap with C:   {C, B,  A}

第二轮从上述三种排列出发，把第二张牌跟随机的一张牌交换，得到九种（有重复）等可能的排列。第三轮也类似。用树状图表示可以看得直观些。

shuffle_v1

可以看到，最后产生的27个结果里面，{A, B, C}, {C, A, B}, {C, B, A}都出现了4次，而{A, C, B}, {B, A, C}, {B, C, A}都出现了5次。
也就是说有些排序出现的可能性是4/27，有些却是5/27. 而且，随着牌数目的增加，这个概率的不均衡会更加严重。

我们重新看看这个方法。A,B,C三张牌的全排列只有6种，但是在这个方法里，一共产生了27个结果（27个分支），它不是6的倍数，
怎么都没法给6种排列平均分嘛。所以，要让结果够公平，一个必要条件就是产生的分支是6的整数倍，也就是N!的整数倍。

Knuth洗牌算法

所以牌该怎么洗呢？在上述方法的基础上，做一处修改，就能剪去一些分支，让分支数是N!的整数倍。这就是Knuth洗牌算法。



def shuffleSort(a):
  N = len(a)
  for i in range(N):
    j = random.randint(0, i)
    a[j], a[i] = a[i], a[j]
    
唯一修改的就是随机牌j选取的方法，在拿起第i张牌时，只从它前面的牌随机选出j，而不是从整副牌里面随机选取。

Really? 就只是这样吗？

是的。就这么简单。

还是用{A, B, C}这三张牌作为例子看看。

第一轮拿起牌A， 现在随机牌只能是A，经过第一轮之后，其实没有发生变换，还是{A,B,C}; (这一步也可以省略)

第二轮拿起牌B， 从{A，B}里面随机选一张牌跟B交换，会得到两种等可能的结果：

swap with A: {B, A, C}
no change: {A, B, C}

第三轮从上面两种可能的排列出发，拿起最后一张牌（这里都是C）， 再从所有牌里面随机选一张跟它交换。树状图如下：shuffle_v2

最终得到的结果只有6个，正好是三张牌的所有6种排列结果，每种出现一次。所以，Knuth洗牌算法是公平的。

做个实验验证一下，把牌数增加到5张{A,B,C,D,E},分别用以上两种洗牌算法做50w次使用，看5张牌的所有120种排列出现的次数是否足够接近。

 算法1实验结果 算法2（Knuth shuffle）实验结果
 
第一种算法的洗牌结果中，各种排序出现次数在2500~7500之间有很大波动，而在Knuth洗牌算法的结果中，每种排序出现的次数都在4000左右，
符合计算结果（50w/120=4166.7）。




=======================

这道题让我们给数组洗牌，也就是随机打乱顺序，那么由于之前那道题Linked List Random Node我们接触到了水塘抽样的思想，这道题实际上这道题也是
用类似的思路，我们遍历数组每个位置，每次都随机生成一个坐标位置，然后交换当前遍历位置和随机生成的坐标位置的数字，这样如果数组有n个数字，那么
我们也随机交换了n组位置，从而达到了洗牌的目的，


=======================

Python hack
Just for fun.

class Solution(object):   # 51% performance
    def __init__(self, nums):
        self.reset = lambda: nums
        self.shuffle = lambda: random.sample(nums, len(nums))
        
        

"""

#-*- coding:utf-8 -*-
