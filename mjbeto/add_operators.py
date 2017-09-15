#coding=utf-8

import unittest

"""


282. Expression Add Operators


Add Operators 

 Description
 Notes
 Testcase
 Judge
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators 
(not unary) +, -, or * between the digits so they evaluate to the target value.

Have you met this question in a real interview? Yes
Example
"123", 6 -> ["1+2+3", "1*2*3"] 
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []
Tags 
Divide and Conquer Facebook Google
Related Problems 
Medium Combination Sum II 29 %
Medium Combinations 32 %
Medium Combination Sum

"""



class Solution:
    # @param {string} num a string contains only digits 0-9
    # @param {int} target an integer
    # @return {string[]} return all possibilities
    def addOperators(self, nums, target):   # ref idea, 71.9%
        # Write your code here
        if not nums:  # can't put not target here, see case4
            return []
        result = []
        self.dfs_helper(nums, target, 0, 0, 0, "", result)
        return result

    def dfs_helper(self, nums, target, idx, now_res, pre_val, path, result):
        if idx == len(nums):
            if target == 0:
                result.append(path)
            return
        for i in range(idx, len(nums)):
            cur_val = int(nums[idx: i+1])
            # need to check if there are continued '0's, like '00', '0', only one 0 is needed, -- case 4
            # also non-0 val with leading 0 is not valid, case3
            #if cur_val == 0 and i != idx:
            if (cur_val == 0 and i != idx) or (nums[idx] == '0' and cur_val != 0 and i != idx):
                break
            if idx == 0:
                self.dfs_helper(nums, target-cur_val, i+1, cur_val, cur_val, path+str(cur_val), result)
            else:
                # +
                self.dfs_helper(nums, target-cur_val, i+1, now_res+cur_val, cur_val, path+"+"+str(cur_val), result)
                # -
                self.dfs_helper(nums, target+cur_val, i+1, now_res-cur_val, -cur_val, path +"-"+ str(cur_val),
                                result)
                # *
                # target + pre_val - pre_val*cur_val
                self.dfs_helper(nums, target + pre_val - pre_val*cur_val, i + 1, now_res - pre_val + pre_val* cur_val, pre_val*cur_val, path + "*" + str(cur_val),
                                result)








class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()


    def test_case04(self):
        nums, target = "00", 0
        answer = ["0+0", "0-0", "0*0"]
        result = self.sol.addOperators(nums, target)
        self.assertEqual(sorted(answer), sorted(result))

    def test_case1(self):
        nums, target = "123", 6
        answer = ["1+2+3", "1*2*3"]
        result = self.sol.addOperators(nums, target)
        self.assertEqual(sorted(answer), sorted(result))


    def test_case2(self):
        nums, target = "232", 8
        answer = ["2*3+2", "2+3*2"]
        result = self.sol.addOperators(nums, target)
        self.assertEqual(sorted(answer), sorted(result))

    def test_case3(self):
        nums, target = "105", 5
        answer = ["1*0+5","10-5"]
        result = self.sol.addOperators(nums, target)
        self.assertEqual(sorted(answer), sorted(result))



    def test_case5(self):
        nums, target = "3456237490", 9191
        answer = []
        result = self.sol.addOperators(nums, target)
        self.assertEqual(sorted(answer), sorted(result))


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



"""

https://segmentfault.com/a/1190000003797204

深度优先搜索
复杂度
时间 O(N^2) 空间 O(N)

思路
因为要输出所有可能的情况，必定是用深度优先搜索。问题在于如何将问题拆分成多次搜索。加减法很好处理，每当我们截出一段数字时，将之前计算的结果加
上或者减去这个数，就可以将剩余的数字字符串和新的计算结果代入下一次搜索中了，直到我们的计算结果和目标一样，就完成了一次搜索。然而，乘法如何处
理呢？这里我们需要用一个变量记录乘法当前累乘的值，直到累乘完了，遇到下一个加号或减号再将其算入计算结果中。这里有两种情况:

乘号之前是加号或减号，例如2+3*4，我们在2那里算出来的结果，到3的时候会加上3，计算结果变为5。在到4的时候，因为4之前我们选择的是乘号，这里3就
应该和4相乘，而不是和2相加，所以在计算结果时，要将5先减去刚才加的3得到2，然后再加上3乘以4，得到2+12=14，这样14就是到4为止时的计算结果。
另外一种情况是乘号之前也是乘号，如果2+3*4*5，这里我们到4为止计算的结果是14了，然后我们到5的时候又是乘号，这时候我们要把刚才加的3*4给去掉，
然后再加上3*4*5，也就是14-3*4+3*4*5=62。这样5的计算结果就是62。
因为要解决上述几种情况，我们需要这么几个变量，一个是记录上次的计算结果currRes，一个是记录上次被加或者被减的数prevNum，一个是当前准备处理的
数currNum。当下一轮搜索是加减法时，prevNum就是简单换成currNum，当下一轮搜索是乘法时，prevNum是prevNum乘以currNum。

注意
第一次搜索不添加运算符，只添加数字，就不会出现+1+2这种表达式了。
我们截出的数字不能包含0001这种前面有0的数字，但是一个0是可以的。这里一旦截出的数字前导为0，就可以return了，因为说明前面就截的不对，从这之
后都是开始为0的，后面也不可能了。


jsahalf · 1月2日
赞大神的解法，唯一有一个疑问，我觉得时间复杂度应该是O(4^n)
 赞 回复

huangge0385 · 7月14日
请问复杂度时间 O(N^2) 空间 O(N)如何得到？愚以为应该是O(4^n)

========================================================================================================================



This problem can be solved using DFS algorithm. For example, given the input “123456“, suppose we encounter the last digit “6”, at which we already have the result of solve(“12345“). Then there are three cases:

solve(“123456”) = solve(“12345”) + 6

solve(“123456”) = solve(“12345”) – 6

solve(“123456”) = cal( solve(“12345”) , 6, *), this have the following three cases:

suppose solve(“12345”) = solve(“1234”) + 5,  so we have solve(“123456”) = solve(“1234“) + 5 * 6
suppose solve(“12345”) = solve(“123”) + 4  * 5,  so we have solve(“123456”) = solve(“123“) + 4 * 5 * 6
suppose solve(“12345”) = solve(“1234”)  –  5,  so we have solve(“123456”) = solve(“1234“) - 5 * 6. 
From the above three cases , we can see that in the step of solve(“123456“), we already have solve(“12345“), we also need to have the value of solve(“1234“), and 5 for case 1, 3; and solve(“123”) and 4*5 for case 2. 

In the above case 1, we define preSum = solve(“1234”) + 5, and preVal = 5, then we have solve(“1234”) = solve(“12345”) – 5 = preSum – preVal. 

In the above case 2, we define preSum = solve(“123”) + 4*5 ,and preVal = 4 * 5, then we have solve(“123”) = solve(“12345”) – 4*5 = preSum – preVal.

in the above case 3, we define preSum = solve(“1234”) – 5, and preVal = -5, then we have solve(“1234”) = solve(“12345”) – (-5) = preSum – preVal. 

So in the recursive process, we need to track the preSum, and preVal based on the operators. See the following Java implementation for details.


"""


#-*- coding:utf-8 -*-
