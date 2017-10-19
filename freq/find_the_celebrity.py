#coding=utf-8

import unittest

"""

locked

277. Find the Celebrity


Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The 
definition of a celebrity is that all the other n - 1people know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is 
to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the 
celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int 
findCelebrity(n), your function should minimize the number of calls to knows.

Note: There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a 
celebrity in the party. If there is no celebrity, return -1.


=========================================================================

Problem link from GeeksForGeeks:

http://www.practice.geeksforgeeks.org/problem-page.php?pid=700253

Suppose you are at a party with $n$ people (labeled from $0$ to $n - 1$) and among them, there may exist one celebrity. 
The definition of a celebrity is that all the other $n - 1$ people know him/her but he/she does not know any of them. 
Your task is to find the stranger (celebrity) in party.

Input:

The first line of input contains an element T denoting the No of test cases. Then T test cases follow. Each test case 
consist of 2 lines. The first line of each test case contains a number denoting the size of the matrix M. Then in the 
next line are space separated values of the matrix M.

Output:

For each test case output will be the id of the celebrity if present (0 based index). Else -1 will be printed.



"""



class Solution(object):
    def findCelebrity(self, n):
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


"""

双指针，O(n)时间，O(1)空间。

复制代码
 1 // Forward declaration of the knows API.
 2 bool knows(int a, int b);
 3 
 4 class Solution {
 5 public:
 6     int findCelebrity(int n) {
 7         int l = 0, r = n - 1;
 8         while (l < r) {
 9             if (knows(l, r)) ++l;
10             else --r;
11         }
12         for (int i = 0; i < n; ++i) if (i != l) {
13             if (knows(l, i) || !knows(i, l)) return -1;
14         }
15         return l;
16     }
17 };

==============================================================


http://www.cnblogs.com/grandyang/p/5310649.html

这道题让我们在一群人中寻找名人，所谓名人就是每个人都认识他，他却不认识任何人，限定了只有1个或0个名人，给定了一个API函数，输入a和b，用来判断
a是否认识b，让我们尽可能少的调用这个函数，来找出人群中的名人。我最先想的方法是建立个一维数组用来标记每个人的名人候选状态，开始均初始化为true，
表示每个人都是名人候选人，然后我们一个人一个人的验证其是否为名人，对于候选者i，我们遍历所有其他人j，如果i认识j，或者j不认识i，说明i不可能是
名人，那么我们标记其为false，然后验证下一个候选者，反之如果i不认识j，或者j认识i，说明j不可能是名人，标记之。对于每个候选者i，如果遍历了一
圈而其候选者状态仍为true，说明i就是名人，返回即可，如果遍历完所有人没有找到名人，返回-1，参见代码如下：

 

解法一：

复制代码
class Solution {
public:
    int findCelebrity(int n) {
        vector<bool> candidate(n, true);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (candidate[i] && i != j) {
                    if (knows(i, j) || !knows(j, i)) {
                        candidate[i] = false;
                        break;
                    } else {
                        candidate[j] = false;
                    }
                }
            }
            if (candidate[i]) return i;
        }
        return -1;
    }
};
复制代码
 

我们其实可以不用一维数组来标记每个人的状态，我们对于不是名人的i，直接break，继续检查下一个，但是由于我们没有标记后面的候选人的状态，所以有
可能会重复调用一些knows函数，所以下面这种方法虽然省了空间，但是调用knows函数的次数可能会比上面的方法次数要多，参见代码如下：

 

解法二：

复制代码
class Solution {
public:
    int findCelebrity(int n) {
        for (int i = 0, j = 0; i < n; ++i) {
            for (j = 0; j < n; ++j) {
                if (i != j && (knows(i, j) || !knows(j, i))) break;
            }
            if (j == n) return i;
        }
        return -1;
    }
};
复制代码
 

下面这种方法是网上比较流行的一种方法，设定候选人res为0，原理是先遍历一遍，对于遍历到的人i，若候选人res认识i，则将候选人res设为i，完成一遍
遍历后，我们来检测候选人res是否真正是名人，我们如果判断不是名人，则返回-1，如果并没有冲突，返回res，参见代码如下：

 

解法三：

复制代码
class Solution {
public:
    int findCelebrity(int n) {
        int res = 0;
        for (int i = 0; i < n; ++i) {
            if (knows(res, i)) res = i;
        }
        for (int i = 0; i < n; ++i) {
            if (res != i && (knows(res, i) || !knows(i, res))) return -1;
        }
        return res;
    }
};
复制代码
 

参考资料：

https://leetcode.com/discuss/56413/java-solution-two-pass

https://leetcode.com/discuss/56770/solution-lines-easy-understanding-with-simple-explanation

==================================================


Graph
Each node denotes a person, and edge(A, B) means A knows B. So the celebrity should be the node with 00 out-degree and 
n−1n−1 in-degree. Also, in the graph, there is only possible one celebrity node. Therefore, we can find a 0-out-degree 
node first. If there is no such node, there is no celebrity neither. Then, we check if this node is celebrity, if not 
there is no celebrity node in the graph. Other nodes cannot be celebrity because at least 0-out-degree node does not 
know him/her.

Celebrity Candidate
However, the time complexity to find the 0-out-degree node is O(n2)O(n2). Taking a step back, we can find the celebrity 
candidate, we note that:

If One knows somebody else, then he cannot be a celebrity.
If somebody doesn’t know A, then A cannot be a celebrity.
Implementation
[-] Python code accepted by GeeksForGeeks
# You are required to complete this fucntion
# Function should return the an integer

def getId(arr, n):
    #Code here
    i = 0
    j = n - 1
    
    # Find the celebrity candidate
    while i < j:
        if arr[i][j] == 1:
            # i knows j ==> i cannot be a celebrity
            i += 1
        else:
            # i doesn't know j ==> j cannot be a celebrity
            j -= 1
            
    # Now i = j is the person who is possibly a celebrity
    # Check if candidate (j) is a celebrity by checking its relationships with all other people
    for i in xrange(n):
        # if i == j, skip; Otherwise, check the celebrity condition i is known by j but i doesn't know j.
        # If it is true, then continue to check next j, or return false
        if i != j and (arr[i][j] == 0 or arr[j][i] == 1):
            return -1
    return i    
    
Suppose the edge check arr[i][j] is an O(1)O(1) operation. Then the time to find the celebrity candidate tis O(n)O(n) 
and the time to check the candidate is O(n)O(n) too. Therefore, the total time complexity is O(n)O(n).


"""