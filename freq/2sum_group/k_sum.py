#coding=utf-8
__author__ = 'linglin'

"""

Not a leetcode problem, just a reference, may not be the good or best solution for every problem.

根据以上的2Sum, 3Sum, 3Sum Cloest， 还有4Sum，我相信只要认真看完每道题的解法的童鞋，都会发现一定的规律，相信这时候会有人想，如果变成
KSum问题，我们应该如何求解？这是个很好的想法，下面，我们来看看问题扩展.

首先，对于2Sum，我们用的解法是以空间复杂度来换取时间复杂度，那么，2Sum我们可不可以in place来解？时间复杂度又是多少？ 答案是当然可以，
我们可以先sort一遍，之后再扫一变，sort的时间复杂度是O(nlogn)，扫一遍是O(n),因此，这种解法的时间复杂度是O(nlogn), 当然，如果对于要找
index，leetcode上的题不能用这个方法，因为我们sort一遍之后，index会发生一些变化。但是我们可以用以下这个function来作为一个
Helper function对于K Sum(考虑到如果K > 2, sort一遍数组的时间开销不算是主要的时间开销了):

void twoSum(vector<int> &numbers, int begin, int first, int second, int target, vector<vector<int>>& ret) {
       if(begin >= numbers.size()-1)
            return;
        int b = begin;
        int e = numbers.size()-1;
        while(b < e)
        {
            int rest = numbers[b]+numbers[e];
            if(rest == target)
            {
                vector<int> tmp_ret;
                tmp_ret.push_back(first);
                tmp_ret.push_back(second);
                tmp_ret.push_back(numbers[b]);
                tmp_ret.push_back(numbers[e]);
                ret.push_back(tmp_ret);
                do{b++;}
                while(b<e && numbers[b] == numbers[b-1]);
                do{e--;}
                while(b<e && numbers[e] == numbers[e+1]);
            }
            else if(rest < target)
                ++b;
            else
                --e;
        }
    }


给个例子，对于4Sum，我们可以调用这个function，代码如下:


class Solution {
public:

    void twoSum(vector<int> &numbers, int begin, int first, int second, int target, vector<vector<int>>& ret) {
       if(begin >= numbers.size()-1)
            return;
        int b = begin;
        int e = numbers.size()-1;
        while(b < e)
        {
            int rest = numbers[b]+numbers[e];
            if(rest == target)
            {
                vector<int> tmp_ret;
                tmp_ret.push_back(first);
                tmp_ret.push_back(second);
                tmp_ret.push_back(numbers[b]);
                tmp_ret.push_back(numbers[e]);
                ret.push_back(tmp_ret);
                do{b++;}
                while(b<e && numbers[b] == numbers[b-1]);
                do{e--;}
                while(b<e && numbers[e] == numbers[e+1]);
            }
            else if(rest < target)
                ++b;
            else
                --e;
        }
    }
    vector<vector<int> > fourSum(vector<int> &num, int target) {
        vector<vector<int>> ret;
        if(num.size() <= 3) //invalid corner case check
            return ret;
        sort(num.begin(), num.end()); //cause we need the result in quadruplets should be non-descending
        for(int i = 0; i < num.size()-3; ++i)
        {
            if(i > 0 && num[i] == num[i-1])
                continue;
            for(int j = i+1; j < num.size()-2; ++j)
            {
                if(j > i+1 && num[j] == num[j-1])
                    continue;
                twoSum(num, j+1, num[i], num[j], target-(num[i]+num[j]), ret);
            }
        }
        return ret;
    }
};



以上解法可以延伸到KSum.不过是相当于对于n-2个数做嵌套循环。这么写出来使得思路清晰，以后遇到了类似问题可以解决。


"""




import unittest


class Solution(object):
    def searchInsert(self, nums):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """


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
