#coding=utf-8

"""
134. Gas Station

There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1).
You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.

Subscribe to see which companies asked this question

Hide Tags Greedy

Medium


"""


import unittest

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        idx = 0
        res = 0
        diff_sum = 0
        while idx < len(gas):
            if diff_sum < 0:
                diff_sum = 0
                res = idx
            diff_sum += gas[idx] - cost[idx]
            idx += 1
        return res if diff_sum >= 0 else -1

    def canCompleteCircuit_wrong(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        diff = [gas[i] - cost[i] for i in range(len(gas))]
        min_diff = 0
        min_idx = 0
        for i in range(len(diff)):
            if diff[i] <= min_diff:
                min_diff = diff[i]
                min_idx = i
        return (min_idx+1) % len(diff)


class Solution1(object):
    def canCompleteCircuit(self, gas, cost): #55ms, 36.1%
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if not gas or not cost or len(gas) != len(cost):
            return -1
        total_diff = 0
        curr = 0
        idx = 0
        start = 0
        while idx < len(gas):
            total_diff += gas[idx] - cost[idx]
            curr += gas[idx] - cost[idx]
            if curr < 0:
                curr = 0
                start = idx + 1
            idx += 1
        if total_diff >= 0:
            return start
        else:
            return -1
            


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        gas = [1,2,3]
        cost = [3,2,1]
        answer = 1
        result = self.sol.canCompleteCircuit(gas, cost)
        self.assertEqual(answer, result)
        
    def test_case2(self):
        gas = [1,2,3]
        cost = [3,2,2]
        answer = -1
        result = self.sol.canCompleteCircuit(gas, cost)
        self.assertEqual(answer, result)


    def test_case3(self):
        gas = [1,2,3]
        cost = [3,2,2]
        answer = -1
        result = self.sol.canCompleteCircuit(gas, cost)
        self.assertEqual(answer, result)

    def test_case4(self):
        gas = [2, 3, 1]
        cost = [3, 1, 2]
        answer = 1
        result = self.sol.canCompleteCircuit(gas, cost)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""


蛮精巧的一道题。最直白的解法就是从每一个点开始，遍历整个环，然后找出最后剩余油量最大的点。这个是O(n^2)的。但是这题明显不会无聊到让做题人写
个两层循环这么简单。

仔细想一下，其实和以前求最大连续子数组和的题很像。

在任何一个节点，其实我们只关心油的损耗，定义：

diff[i] = gas[i] – cost[i]  0<=i <n

那么这题包含两个问题：

1. 能否在环上绕一圈？

2. 如果能，这个起点在哪里？

第一个问题，很简单，我对diff数组做个加和就好了，leftGas = ∑diff[i]， 如果最后leftGas是正值，那么肯定存在这么一个起始点。如果是负值，
那说明，油的损耗大于油的供给，不可能有解。得到第一个问题的答案只需要O(n)。

对于第二个问题，起点在哪里？

假设，我们从环上取一个区间[i, j], j>i， 然后对于这个区间的diff加和，定义

sum[i,j] = ∑diff[k] where i<=k<j

如果sum[i,j]小于0，那么这个起点肯定不会在[i,j]这个区间里，跟第一个问题的原理一样。举个例子，假设i是[0,n]的解，那么我们知道 任意
sum[k,i-1] (0<=k<i-1) 肯定是小于0的，否则解就应该是k。同理，sum[i,n]一定是大于0的，否则，解就不应该是i，而是i和n之间的某个点。所以第
二题的答案，其实就是在0到n之间，找到第一个连续子序列（这个子序列的结尾必然是n）大于0的。

至此，两个问题都可以在一个循环中解决。

==================================================================

这题的意思就是求出从哪一个油站开始，能走完整个里程，并且这个结果是唯一的。

首先我们可以得到所有油站的油量totalGas，以及总里程需要消耗的油量totalCost，如果totalCost大于totalGas，那么铁定不能够走完整个里程。

如果totalGas大于totalCost了，那么就能走完整个里程了，假设现在我们到达了第i个油站，这时候还剩余的油量为sum，如果
sum + gas[i] - cost[i]小于0，我们无法走到下一个油站，所以起点一定不在第i个以及之前的油站里面（都铁定走不到第i + 1号油站），起点只能
在i + 1后者后面。

==================================================================

解题思路：这道题也很tricky，自己想是很难想出来的。如果sum(gas)<sum(cost)的话，那么一定无解。diff是走完一站邮箱剩下的油，如果加上gas[i]
也到不了下一站，那么继续将下一站设置为起点，然后再检查，是不是很巧妙呢？

==================================================================

解题思路：
贪心算法（Greedy Algorithm)

分析题目可以得到两个隐含的结论：

结论1：若从加油站A出发，恰好无法到达加油站C（只能到达C的前一站）。则A与C之间的任何一个加油站B均无法到达C。

结论1的证明：反证法

假设从加油站A出发恰好无法到达加油站C，但是A与C之间存在加油站B，从B出发可以到达C。

而又因为从A出发可以到达B，所以A到B的油量收益（储油量 - 耗油量）为正值，进而可以到达C。

推出矛盾，假设不成立。
结论2：若储油量总和sum(gas) >= 耗油量总和sum(cost)，则问题一定有解。

结论2的证明：反证法

假设sum(gas) >= sum(cost)时，从环形内任意加油站出发，均无法走完一圈。

则从任意加油站A出发绕行一圈返回A之前，油量增益减为负值，假设恰好无法到达加油站B。

亦即：sum(gas[A~B]) < sum(cost[A~B])

而又因为加油站B出发绕行一圈返回B之前，油量增益减为负值，假设恰好无法到达加油站C。

亦即：sum(gas[B~C]) < sum(cost[B~C])

以此类推，最终将进入循环，假设循环的起点为P，中间点为M1, M2 ... Mk

则有：

储油量总和：sum(gas[P~M1] + ... + gas[Mk ~ P]) = c * sum(gas)

耗油量总和：sum(cost[P~M1] + ... + cost[Mk ~ P]) = c * sum(cost)

亦即：

c * sum(gas) < c * sum(cost) 等价于 sum(gas) < sum(cost)

推出矛盾，假设不成立。


==================================================================

这题要想清楚不容易，尽管想清楚后代码写起来很简单。

I.  显然当gas[i]<cost[i]时，i不能作为起点。

II. 当对所有加油站求和：sum(gas[i] - cost[i]) <0时，无法环绕一圈。反之，则一定能环绕一圈。

问题是如果可以环绕一圈，如何找起点？

性质1. 对于任意一个加油站i，假如从i出发可以环绕一圈，则i一定可以到达任何一个加油站。显而易见。

性质2. 如果这样的i是唯一的，则必然不存在j!=i， 从j出发可以到达i。

反证法：如果存在这样的j，则必然存在j->i->i的路径，而这个路径会覆盖j->j一周的路径。那么j也将是一个符合条件的起点。与唯一解的限制条件矛盾。

性质3. 假如i是最后的解，则由1可知，从0 ~ i-1出发无法达到i。而从i出发可以到达i+1 ~ n-1。

结合以上三条性质，得出解决的思路：

0. 如果对所有加油站的sum(gas[i] - cost[i])<0，则无解。否则进入1。

1. 从0开始计算sum(gas[i] - cost[i])，当遇到i1使sum<0时，说明从0出发无法到达i1。根据性质1，0不是起始点。而由于从0出发已经到达了
1 ~ i1-1。根据性质2，1 ~ i1-1一定不是正确的起始点。此时i1为起始点的候选。

2. 将sum清0，并从i1出发，假如又遇到i2使sum(gas[i] - cost[i]) < 0 时，说明i1出发无法绕一圈，更具性质1，排除i1。又因为i1+1 ~ i2-1都
能从i1出发到达,。根据性质2，它们也必然不是起始点。此时i2为起始点的候选。

3. 以此类推，直到遇到ik，使从ik出发可以到达ik+1 ~ n-1。

其中步骤0可以合并到1~3的扫描中，一个pass来得到解。

==================================================================

这道题也挺麻烦的。乍看不难，用最简单的算法就是一个一个点地计算，计算到没油了，证明这点不能作为出发点。移动到下一个点作为出发点。这样的话思路
还是挺简单的，不过这样写不accepted的，因为编译超时。
我觉得做这道题的关键是要可以总结出来这道题目的属性，注意Note这个地方，其属性主要有两个：
1 如果总的gas - cost小于零的话，那么没有解返回-1
2 如果前面所有的gas - cost加起来小于零，那么前面所有的点都不能作为出发点。
2013-12-1 update:
原创： 靖心http://write.blog.csdn.net/postedit/14106137
第一个属性的正确性很好理解。那么为什么第二个属性成立呢？
首先我们是从i =0个gas station计算起的，设开始剩油量为left=0，如果这个station的油是可以到达下一个station的，那么left=gas-cost为正数，
到了下一个station就有两种情况：
1 如果i=1个station的gas-cost也为正，那么前面的left加上当前station的剩油量也为正。
2 如果i=1个station的gas-cost为负，那么前面的left加上当前的station的剩油量也有两种情况：
一） left为正，那么可以继续到下一个station，重复前面计算i=2,i=3...，直到发生第二）种情况
 二）如果left为负，那么就不能到下一个station了，这个时候如果i=k(i<k<n)，这个时候是否需要从第i=1个station开始重新计算呢？不需要，因为第
 k个station之前的所有left都为正的，到了第k个station才变成负。
证明：
left(i)>0, 如果left(i+1)<0，从i+1个station重新开始测试是没有必要的；如果left(i+2) > 0呢？ 那么left(i) + left(i+1)>0;
 left(i) + left(i+1) +left(i+2) > left(i+2)那么从i+2个station开始也是没有必要的，以此类推……left(i) + ...+ left(k-2)>0, 那么
 left(i)+...+left(k-2) > left(k-1)， 那么就是没有必要从第k-1个节点重新开始计算了，现在到了第k个station的剩油量left变为负，也不能作
 为出发点，那么直接到k+1个计算就可以了。这就可以得出属性2了。
 
以前没重视数学的证明定理的方法，要去证明一个定理是很困难的。但是原来证明的方法主要不是用来证明定理的，而是用来发现规则和特征的。



"""


#-*- coding:utf-8 -*-
