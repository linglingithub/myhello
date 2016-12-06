#coding=utf-8
"""
89. Gray Code

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code.

A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.

Subscribe to see which companies asked this question

Hide Tags Backtracking

Medium

"""

import unittest


class Solution(object):
    def grayCode(self, n): #46ms, 59%
        """
        :type n: int
        :rtype: List[int]
        """
        if n==0:
            return [0]
        result = self.grayCode(n-1)
        #flip = []
        for tmp in reversed(result):
            nextval = (1<< (n-1)) | tmp # (1<< (n-1)) + tmp
            result.append(nextval)
        #result += flip
        return result


    def grayCode1(self, n): #56ms, 36% --> 49ms, 52% if use | instead of + at line 46
        """
        :type n: int
        :rtype: List[int]
        """
        if n==0:
            return [0]
        result = self.grayCode(n-1)
        flip = []
        for tmp in result[::-1]:
            nextval = (1<< (n-1)) | tmp # (1<< (n-1)) + tmp
            flip.append(nextval)
        result += flip
        return result



    def grayCode_ref3(self, n): # math way
        res = []
        size = 1 << n
        for i in range(size):
            res.append((i >> 1) ^ i)  # ^ means binary XOR
        return res




    def grayCode_ref2(self, n): #59MS, 28%, recursive way
        res = [0]
        for i in xrange(n):
            res += (2 ** i + x for x in res[::-1])
        return res


    def grayCode_ref(self, n): #42ms, 69%
        if n == 0:
            return [0]
        result = self.grayCode(n - 1)
        seq = list(result)
        for i in reversed(result):
            seq.append((1 << (n - 1)) | i)
        return seq



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        n = 2
        answer = [0,1,3,2]
        result = self.sol.grayCode(n)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""
看到这个题时，首先做了一个模拟，当n=3时，gray code应该是
000
001
011
010
110
100
101
111
看了半天，也没看出来什么规律。后来上网一查GrayCode(http://en.wikipedia.org/wiki/Gray_code)才发现原来推导的gray code顺序错了。
第六个应该是111。
n=3时，正确的GrayCode应该是
000
001
011
010
110
111 //如果按照题意的话，只是要求有一位不同，这里也可以是100
101
100

这样的话，规律就出来了，n=k时的Gray Code，相当于n=k-1时的Gray Code的逆序 加上 1<<k。

n=k时的Gray Code，相当于n=k-1时的Gray Code的逆序 加上 1<<k。

[总结]
题意不清楚，如果每次只是与上一个数有一个位不同的话，其实有很多种组合出来。如果不是查了Gray Code的定义，根本看不出来什么规律。
而且，Gray Code这种东西，必然有数学解，否则在早期的工程界是没法应用的。想了一下，其实也可以这么做，第i个数可以由如下公式产生： (i>>1)^i，
所以代码也可以是：
1:  vector<int> grayCode(int n)
2:    {
3:      vector<int> ret;
4:      int size = 1 << n;
5:      for(int i = 0; i < size; ++i)
6:        ret.push_back((i >> 1)^i);
7:      return ret;
8:    }

不过这种数学解就失去了interview的意思了。


================================================>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The very comprehensive explanation:

http://www.cnblogs.com/grandyang/p/4315649.html


这道题是关于格雷码的，猛地一看感觉完全没接触过格雷码，但是看了维基百科后，隐约的感觉原来好像哪门可提到过，哎全还给老师了。这道题如果不了解
格雷码，还真不太好做，幸亏脑补了维基百科，格雷码的处理主要是位操作 Bit Operation，LeetCode中关于位操作的题也挺常见，比如 Repeated DNA
 Sequences 求重复的DNA序列， Single Number 单独的数字, 和  Single Number II 单独的数字之二 等等。三位的格雷码和二进制数如下：



复制代码
Int    Grey Code    Binary
 0  　　  000        000
 1  　　  001        001
 2   　 　011        010
 3   　 　010        011
 4   　 　110        100
 5   　 　111        101
 6   　 　101        110
 7   　　 100        111
复制代码


其实这道题还有多种解法。首先来看一种最简单的，是用到格雷码和二进制数之间的相互转化，可参见我之前的博客 Convertion of grey code and
binary 格雷码和二进制数之间的转换 ，明白了转换方法后，这道题完全没有难度，代码如下：



解法一：

复制代码
// Binary to grey code
class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> res;
        for (int i = 0; i < pow(2,n); ++i) {
            res.push_back((i >> 1) ^ i);
        }
        return res;
    }
};
复制代码


然后我们来看看其他的解法，参考维基百科上关于格雷码的性质，有一条是说镜面排列的，n位元的格雷码可以从n-1位元的格雷码以上下镜射后加上新位元的
方式快速的得到，如下图所示一般。



有了这条性质，我们很容易的写出代码如下：



解法二：

复制代码
// Mirror arrangement
class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> res{0};
        for (int i = 0; i < n; ++i) {
            int size = res.size();
            for (int j = size - 1; j >= 0; --j) {
                res.push_back(res[j] | (1 << i));
            }
        }
        return res;
    }
};
复制代码


维基百科上还有一条格雷码的性质是直接排列，以二进制为0值的格雷码为第零项，第一项改变最右边的位元，第二项改变右起第一个为1的位元的左边位元，
第三、四项方法同第一、二项，如此反复，即可排列出n个位元的格雷码。根据这条性质也可以写出代码，不过相比前面的略微复杂，代码如下：

0 0 0
0 0 1
0 1 1
0 1 0
1 1 0
1 1 1
1 0 1
1 0 0



解法三：

复制代码
// Direct arrangement
class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> res{0};
        int len = pow(2, n);
        for (int i = 1; i < len; ++i) {
            int pre = res.back();
            if (i % 2 == 1) {
                pre = (pre & (len - 2)) | ((~pre) & 1);
            } else {
                int cnt = 1, t = pre;
                while ((t & 1) != 1) {
                    ++cnt;
                    t >>= 1;
                }
                if ((pre & (1 << cnt)) == 0) pre |= (1 << cnt);
                else pre &= ~(1 << cnt);
            }
            res.push_back(pre);
        }
        return res;
    }
};
复制代码


上面三种解法都需要事先了解格雷码及其性质，假如我们之前并没有接触过格雷码，那么我们其实也可以用比较笨的方法来找出结果，比如下面这种方法用到了
一个set来保存已经产生的结果，我们从0开始，遍历其二进制每一位，对其取反，然后看其是否在set中出现过，如果没有，我们将其加入set和结果res中，
然后再对这个数的每一位进行遍历，以此类推就可以找出所有的格雷码了，参见代码如下：



解法四：

复制代码
class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> res;
        unordered_set<int> s;
        helper(n, s, 0, res);
        return res;
    }
    void helper(int n, unordered_set<int>& s, int out, vector<int>& res) {
        if (!s.count(out)) {
            s.insert(out);
            res.push_back(out);
        }
        for (int i = 0; i < n; ++i) {
            int t = out;
            if ((t & (1 << i)) == 0) t |= (1 << i);
            else t &= ~(1 << i);
            if (s.count(t)) continue;
            helper(n, s, t, res);
            break;
        }
    }
};
复制代码


既然递归方法可以实现，那么就有对应的迭代的写法，当然需要用stack来辅助，参见代码如下：



解法五：

复制代码
class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> res{0};
        unordered_set<int> s;
        stack<int> st;
        st.push(0);
        s.insert(0);
        while (!st.empty()) {
            int t = st.top(); st.pop();
            for (int i = 0; i < n; ++i) {
                int k = t;
                if ((k & (1 << i)) == 0) k |= (1 << i);
                else k &= ~(1 << i);
                if (s.count(k)) continue;
                s.insert(k);
                st.push(k);
                res.push_back(k);
                break;
            }
        }
        return res;
    }
};
复制代码



<<<<<<================================================================================================

The binary-reflected Gray code list for n bits can be generated recursively from the list for n−1 bits by reflecting
the list (i.e. listing the entries in reverse order), concatenating the original list with the reversed list, prefixing
the entries in the original list with a binary 0, and then prefixing the entries in the reflected list with a binary 1.
[6] For example, generating the n = 3 list from the n = 2 list:

2-bit list:	00, 01, 11, 10

Reflected:	10, 11, 01, 00

Prefix old entries with 0:	000, 001, 011, 010,

Prefix new entries with 1:	110, 111, 101, 100

Concatenated: 000, 001, 011, 010, 110, 111, 101, 100



"""


#-*- coding:utf-8 -*-
#coding=utf-8