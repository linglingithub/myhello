#coding=utf-8

"""
Multiply Strings

Given two numbers represented as strings, return multiplication of the numbers as a string.

Note:
The numbers can be arbitrarily large and are non-negative.
Converting the input string to integer is NOT allowed.
You should NOT use internal library such as BigInteger.
Subscribe to see which companies asked this question

Hide Tags Math String
Hide Similar Problems (M) Add Two Numbers (E) Plus One (E) Add Binary (E) Add Strings


"""

import unittest


class Solution(object):
    """
    -- One important note: a * b, result will be no longer than len(a)+len(b) digits.

    Mulitplying two non-negative numbers, usually called "da shu xiang cheng", one typical operation is to reverse
    both nums strings. Second step is to do mulitiplication digit by digit, but don't hurry to do carry on. Tmp result
    of each digit mulitiplication can be stored in an array. Do the tmp array carry-on after all multiplication done.
    Remove excessive leading zeron in result array of len(a)+len(b)

    """

    def multiply(self, num1, num2): # around 350 ~400 ms, 50%
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]
        result = [0]*(len(num1)+len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                result[i+j] += int(num1[i]) * int(num2[j]) # don't forget to convert to int
        carry = 0
        for i in range(len(result)):
            tmp = result[i] + carry
            result[i] = str(tmp % 10) # don't forget to convert to str
            carry = tmp / 10
        # if carry > 0: # this actually won't got executed because result won't be larger than len(a)+len(b)
        #     result.append(carry)
        result = result[::-1]
        while result[0] == '0' and len(result)>1:  # don't forget to remove extra leading 0 here. !!! don't forget the case of result '0'
            del result[0]
        return "".join(result)



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        num1 = "123"
        num2 = "456"
        answer = '56088'
        result = self.sol.multiply(num1, num2)
        self.assertEqual(answer, result)

    def test_case2(self): # ====> error if don't add protection when removing leading 0
        num1 = "0"
        num2 = "456"
        answer = '0'
        result = self.sol.multiply(num1, num2)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""

这道题让我们求两个字符串数字的相乘，输入的两个数和返回的数都是以字符串格式储存的，这样做的原因可能是这样可以计算超大数相乘，可以不受int或
long的数值范围的约束，那么我们该如何来计算乘法呢，我们小时候都学过多位数的乘法过程，都是每位相乘然后错位相加，那么这里就是用到这种方法，参
见网友JustDoIt的博客，把错位相加后的结果保存到一个一维数组中，然后分别每位上算进位，最后每个数字都变成一位，然后要做的是去除掉首位0，最后
把每位上的数字按顺序保存到结果中即可

http://www.cnblogs.com/grandyang/p/4395356.html

========


几个要点：

直接乘会溢出，所以每次都要两个single digit相乘，最大81，不会溢出。
比如385 * 97, 就是个位=5 * 7，十位=8 * 7 + 5 * 9 ，百位=3 * 7 + 8 * 9 …
可以每一位用一个Int表示，存在一个int[]里面。
这个数组最大长度是num1.len + num2.len，比如99 * 99，最大不会超过10000，所以4位就够了。
这种个位在后面的，不好做（10的0次方，可惜对应位的数组index不是0而是n-1），
所以干脆先把string reverse了代码就清晰好多。
最后结果前面的0要清掉。



"""