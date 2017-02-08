#coding=utf-8

"""

227. Basic Calculator II

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division
should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
Note: Do not use the eval built-in library function.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

Subscribe to see which companies asked this question

Hide Tags String
Hide Similar Problems (H) Basic Calculator (H) Expression Add Operators

Medium

"""

import unittest


class Solution(object):
    def calculate_ref_good(self, s): #362ms, 35%
        import re, operator
        s = re.sub(r'\d+', ' \g<0> ', s)
        op = {'+': operator.add, '-': operator.sub,
              '*': operator.mul, '/': operator.floordiv}
        expression = s.split()
        total = d = idx = 0
        func = op['+']
        while idx < len(expression):
            e = expression[idx]
            if e in '+-':
                total = func(total, d)
                func = op[e]
            elif e in '*/':
                idx += 1
                d = op[e](d, int(expression[idx]))
            else:
                d = int(e)
            idx += 1
        return func(total, d)


    def calculate(self, s): #ref, stack way, 342ms, 41%
        """
        Use stack, for all the numbers, push to stack with the preceding sign, for * and /, pop number and cal, then
        push back. Last step sum up all the numbers in stack.
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        i = 0
        stack = []
        result = 0
        tmp = 0
        sign = 1
        pre = 0
        while i < len(s):
            char = s[i]
            if '9' >= char >= '0':
                tmp, i = self.get_number(s, i)
                stack.append(sign * tmp)
            elif char == "+":
                tmp,i = self.get_number(s, i+1)
                stack.append(tmp)
            elif char == "-":
                tmp,i = self.get_number(s, i+1)
                stack.append(-1 * tmp)
            elif char == "*":
                pre = stack.pop()
                tmp, i = self.get_number(s, i+1)
                tmp *= pre
                stack.append(tmp)
            elif char == "/":
                pre = stack.pop()
                tmp, i = self.get_number(s, i+1)
                #because python has different / for negative number, need to specially deal with it, test case 8
                tmp = pre / tmp if pre > 0 else -(-pre/tmp)
                stack.append(tmp)
            i += 1
        while stack:
            result += stack.pop()
        return result

    def get_number(self, s, idx):
        number = 0
        while idx < len(s):
            if "9" >= s[idx] >= "0":
                number = number * 10 + int(s[idx])
                idx += 1
            elif s[idx] == " ":
                idx += 1
                continue
            else:
                break
        idx -= 1
        return number, idx






    def calculate_ref_stack(self, s): #stack way, 375ms, 32%
        """
        :type s: str
        :rtype: int
        """
        operands, operators = [], []
        operand = ""
        for i in reversed(xrange(len(s))):
            if s[i].isdigit():
                operand += s[i]
                if i == 0  or not s[i-1].isdigit():
                    operands.append(int(operand[::-1]))
                    operand = ""
            elif s[i] == ')' or s[i] == '*' or s[i] == '/':
                operators.append(s[i])
            elif s[i] == '+' or s[i] == '-':
                while operators and \
                      (operators[-1] == '*' or operators[-1] == '/'):
                    self.compute(operands, operators)
                operators.append(s[i])
            elif s[i] == '(':
                while operators[-1] != ')':
                    self.compute(operands, operators)
                operators.pop()

        while operators:
            self.compute(operands, operators)

        return operands[-1]

    def compute(self, operands, operators):
        left, right = operands.pop(), operands.pop()
        op = operators.pop()
        if op == '+':
            operands.append(left + right)
        elif op == '-':
            operands.append(left - right)
        elif op == '*':
            operands.append(left * right)
        elif op == '/':
            operands.append(left / right)



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
        nums = "3+2*2"
        answer = 7
        result = self.sol.calculate(nums)
        self.assertEqual(answer, result)

    def test_case4(self):
        nums = "1+122"
        answer = 123
        result = self.sol.calculate(nums)
        self.assertEqual(answer, result)


    def test_case5(self):
        nums = "3/2"
        answer = 1
        result = self.sol.calculate(nums)
        self.assertEqual(answer, result)

    def test_case6(self):
        nums = "3+5 / 2"
        answer = 5
        result = self.sol.calculate(nums)
        self.assertEqual(answer, result)

    def test_case7(self):
        nums = "3+5 / 2*2"
        answer = 7
        result = self.sol.calculate(nums)
        self.assertEqual(answer, result)

    def test_case8(self): #=====>
        nums = "14-3/2"
        answer = 13
        result = self.sol.calculate(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""


这道题是之前那道Basic Calculator 基本计算器的拓展，不同之处在于那道题的计算符号只有加和减，而这题加上了乘除，那么就牵扯到了运算优先级的问
题，好在这道题去掉了括号，还适当的降低了难度，估计再出一道的话就该加上括号了。不管那么多，这道题先按木有有括号来处理，由于存在运算优先级，我
们采取的措施是使用一个栈保存数字，如果该数字之前的符号是加或减，那么把当前数字压入栈中，注意如果是减号，则加入当前数字的相反数，因为减法相当
于加上一个相反数。如果之前的符号是乘或除，那么从栈顶取出一个数字和当前数字进行乘或除的运算，再把结果压入栈中，那么完成一遍遍历后，所有的乘或
除都运算完了，再把栈中所有的数字都加起来就是最终结果了。代码如下：



复制代码
class Solution {
public:
    int calculate(string s) {
        int res = 0, d = 0;
        char sign = '+';
        stack<int> nums;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] >= '0') {
                d = d * 10 + s[i] - '0';
            }
            if ((s[i] < '0' && s[i] != ' ') || i == s.size() - 1) {
                if (sign == '+') nums.push(d);
                if (sign == '-') nums.push(-d);
                if (sign == '*' || sign == '/') {
                    int tmp = sign == '*' ? nums.top() * d : nums.top() / d;
                    nums.pop();
                    nums.push(tmp);
                }
                sign = s[i];
                d = 0;
            }
        }
        while (!nums.empty()) {
            res += nums.top();
            nums.pop();
        }
        return res;
    }
};


==============================================================================================================================


题目翻译： 实现一个简易的计算器来对简单的字符串表达式求值。 字符串表达式只包含非负整数，+，-，*，/四种运算符，以及空格。整数除法向零取整。
给出的表达式都是有效的。 不要使用内置的eval函数。

题目分析： 通常对算术表达式求值都是用栈来实现的，但是鉴于本题的情形比较简单，所以可以不用栈来实现。 总体思路是，依次读入字符串里的字符，遇到
符号的时候就进行运算。如果是乘除法，就把结果存入中间变量，如果是加减法就把结果存入最终结果。

用C++实现的时候，可以在循环中使用string类的find_first_not_of方法来跳过空格。 读到数字时，继续向后读，直到不是数字的字符，或者超出字符串
长度为止。


class Solution {
public:
    int calculate(string s) {
        int result = 0, inter_res = 0, num = 0;
        char op = '+';
        char ch;
        for (int pos = s.find_first_not_of(' '); pos < s.size(); pos = s.find_first_not_of(' ', pos)) {
            ch = s[pos];
            if (ch >= '0' && ch <= '9') {
                int num = ch - '0';
                while (++pos < s.size() && s[pos] >= '0' && s[pos] <= '9')
                    num = num * 10 + s[pos] - '0';
                switch (op) {
                case '+':
                    inter_res += num;
                    break;
                case '-':
                    inter_res -= num;
                    break;
                case '*':
                    inter_res *= num;
                    break;
                case '/':
                    inter_res /= num;
                    break;
                }
            }
            else {
                if (ch == '+' || ch == '-') {
                    result += inter_res;
                    inter_res = 0;
                }
                op = s[pos++];
            }
        }
        return result + inter_res;
    }
};


==============================================================================================================================


实现一个简易计算器，计算简单表达式字符串的值。

表达式字符串只包含非负整数， +， -， *， / 运算和空白字符。整数除法的得数应当舍去小数部分。

你可以假设给定的表达式总是有效的。

测试样例见题目描述。

注意：不要使用内置的库函数eval。

解题思路：
由于表达式字符串中不包含括号，因此问题可以简化为对乘除运算与加减运算优先级的处理。

参考：https://leetcode.com/discuss/41610/ac-python-solution-use-re-to-get-the-expression

使用辅助变量d记录当前待参与运算的运算数，func记录上一个加减运算符，total记录表达式的值。

若当前运算符为乘除法，则马上对d与下一个运算数执行乘除运算，赋值给d；

若当前运算符为加减法，则对total与d执行func（加减）运算，赋值给total，并更新func；

class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        s = re.sub(r'\d+', ' \g<0> ', s)
        op = {'+': operator.add, '-': operator.sub,
              '*': operator.mul, '/': operator.floordiv}
        expression = s.split()
        total = d = idx = 0
        func = op['+']
        while idx < len(expression):
            e = expression[idx]
            if e in '+-':
                total = func(total, d)
                func = op[e]
            elif e in '*/':
                idx += 1
                d = op[e](d, int(expression[idx]))
            else:
                d = int(e)
            idx += 1
        return func(total, d)

另外，在LeetCode Discuss还看到一段非常简洁的C++代码，思路同上。

class Solution {
public:
    int calculate(string s) {
        istringstream in(s + "+");
        long long total = 0, term, sign = 1, n;
        in >> term;
        char op;
        while (in >> op) {
            if (op == '+' || op == '-') {
                total += sign * term;
                sign = 44 - op; //op == '+' ? 1 : -1
                in >> term;
            } else {
                in >> n;
                if (op == '*')
                    term *= n;
                else
                    term /= n;
            }
        }
        return total;
    }
};

"""

#-*- coding:utf-8 -*-
