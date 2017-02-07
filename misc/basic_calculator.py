#coding=utf-8
"""
224. Basic Calculator

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers
and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
Note: Do not use the eval built-in library function.

Subscribe to see which companies asked this question

Hide Tags Stack Math
Hide Similar Problems (M) Evaluate Reverse Polish Notation (M) Basic Calculator II (M) Different Ways to Add Parentheses
 (H) Expression Add Operators

Hard

"""

import unittest


class Solution(object):
    def calculate(self, s): #ref, 378ms, 35%
        """
        s contains only # number, +/-, (), space, since only +/-, then () can actually be easier to process.
        use a sign stack to record what sign should be applied to the number inside brackets.
        eg. a+(....-(...-(3-5)...)...) , then the ultimate number before 3 should be +, for 5 should be -.
        calculation can still go from left to right, only thing that matters is to record the ultimate sign.
        :param s:
        :return:
        """
        res = 0
        sign_stack = [1]
        i = 0
        while i<len(s):
            c = s[i]
            if '9' >= c >= '0':
                num = 0
                while i < len(s) and s[i] >= '0':
                    num = 10 * num + int(s[i])
                    i += 1
                res += sign_stack.pop() * num
                i -= 1
            elif c == ')':
                sign_stack.pop()
            elif c != ' ':
                # ( , +, -, if + push the same sign as the last one, if - push the opposite of last sign,
                # if ( push the same sign as last one
                sign = sign_stack[-1] if sign_stack else 1
                sign_stack.append(-1 * sign if c == '-' else sign)
            i += 1
        return res


    def calculate1(self, s): #575ms, 6.27%
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        s = "".join(s.split())
        result = 0
        stack = []
        idx = 0
        while idx < len(s):
            char = s[idx]
            if char in ["+", "-"]:
                stack.append(char)
            elif "0" <= char <= "9":
                tmp, idx = self.get_number(s, idx)
                stack.append(tmp)
            elif char == "(":
                stack.append(char)
            elif char == ")":
                tmp = self.calc_bracket(stack)
                stack.append(tmp)
            idx += 1
        if stack:
            result = self.calc_all(stack)
        return result

    def get_number(self, s, idx):
        number = 0
        while idx < len(s) and "0"<=s[idx]<="9":
            number = number*10 + int(s[idx])
            idx += 1
        idx -= 1
        return number, idx

    def calc_bracket(self, stack):
        tmp_stack = []
        tmp = stack.pop()
        while tmp != "(":
            tmp_stack.insert(0, tmp)
            tmp = stack.pop()
        return self.calc_all(tmp_stack)

    def calc_all(self, stack):
        result = int(stack.pop(0))
        while stack:
            tmp_op = stack.pop(0)
            next_num = stack.pop(0)
            if tmp_op == "+":
                result += next_num
            else:
                result -= next_num

        return result









class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = "1 + 1"
        answer = 2
        result = self.sol.calculate(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = " 2-1 + 2 "
        answer = 3
        result = self.sol.calculate(nums)
        self.assertEqual(answer, result)

    def test_case3(self):
        nums = "(1+(4+5+2)-3)+(6+8)"
        answer = 23
        result = self.sol.calculate(nums)
        self.assertEqual(answer, result)

    def test_case4(self):
        nums = "1+122"
        answer = 123
        result = self.sol.calculate(nums)
        self.assertEqual(answer, result)

    def test_case5(self):
        nums = "1+(122)"
        answer = 123
        result = self.sol.calculate(nums)
        self.assertEqual(answer, result)

    def test_case6(self):
        nums = "1-((122))"
        answer = -121
        result = self.sol.calculate(nums)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""

这道题让我们实现一个基本的计算器来计算简单的算数表达式，而且题目限制了表达式中只有加减号，数字，括号和空格，没有乘除，那么就没啥计算的优先级
之分了。于是这道题就变的没有那么复杂了。我们需要一个一维的符号数组来记录加减号，然后我们开始遍历字符串表达式，如果遇到的是数字，则从符号数组
中取出最后一个符合和数字运算后更新结果，如果遇到右括号，则移除一个符号，如果遇到的不是空格，即有可能是加减号或是左括号，则符号数组中加1或-1，
做个判断，如果是负号，加个-1，其他情况加1。代码如下：



复制代码
class Solution {
public:
    int calculate(string s) {
        int res = 0;
        vector<int> sign(2, 1);
        for (int i = 0; i < s.size(); ++i) {
            char c = s[i];
            if (c >= '0') {
                int num = 0;
                while (i < s.size() && s[i] >= '0') {
                    num = 10 * num + s[i++] - '0';
                }
                res += sign.back() * num;
                sign.pop_back();
                --i;
            }
            else if (c == ')') sign.pop_back();
            else if (c != ' ') sign.push_back(sign.back() * (c == '-' ? -1 : 1));
        }
        return res;
    }
};



==========================================================================================================================================


很多人将该题转换为后缀表达式后（逆波兰表达式）求解，其实不用那么复杂。题目条件说明只有加减法和括号，由于加减法是相同顺序的，我们大可以直接把
所有数顺序计算。难点在于多了括号后如何处理正负号。我们想象一下如果没有括号这题该怎们做：因为只有加减号，我们可以用一个变量sign来记录上一次的
符号是加还是减，这样把每次读到的数字乘以这个sign就可以加到总的结果中了。有了括号后，整个括号内的东西可一看成一个东西，这些括号内的东西都会
受到括号所在区域内的正负号影响（比如括号前面是个负号，然后括号所属的括号前面也是个负号，那该括号的符号就是正号）。但是每多一个括号，都要记录
下这个括号所属的正负号，而每当一个括号结束，我们还要知道出来以后所在的括号所属的正负号。根据这个性质，我们可以使用一个栈，来记录这些括号所属
的正负号。这样我们每遇到一个数，都可以根据当前符号，和所属括号的符号，计算其真实值。


"""


#-*- coding:utf-8 -*-
