#coding=utf-8

import unittest

"""

Expression Expand

Given an expression s includes numbers, letters and brackets. Number represents the number of repetitions inside the 
brackets(can be a string or another expression)．Please expand expression to be a string.

Example
s = abc3[a] return abcaaa
s = 3[abc] return abcabcabc
s = 4[ac]dy, return acacacacdy
s = 3[2[ad]3[pf]]xyz, return adadpfpfpfadadpfpfpfadadpfpfpfxyz

Challenge 
Can you do it without recursion?

Tags 
Divide and Conquer Recursion Stack Non Recursion Yahoo
Related Problems 
Hard Expression Tree Build 21 %
Hard Expression Evaluation

"""


class Solution:
    # @param {string} s  an expression includes numbers, letters and brackets
    # @return {string} a string
    def expressionExpand(self, s): #349ms
        # Write your code here
        if not s:
            return ""
        stack = []
        result = []
        i = 0
        while i < len(s):
            char = s[i]
            if stack:
                if char != "]":
                    if '0' <= char <= '9':
                        repeat_cnt, idx = self.get_number(s, i)
                        stack.append(repeat_cnt)
                        i = idx
                        continue
                    else:
                        stack.append(char)
                else:
                    self.pop_string(stack, result)
            else:
                if '0' <= char <= '9':
                    repeat_cnt, idx = self.get_number(s, i)
                    stack.append(repeat_cnt)
                    i = idx
                    continue
                else:
                    result.append(char)
            i += 1
        return "".join(result)

    def pop_string(self, stack, result):
        tmp = ""
        while stack:
            char = stack.pop()
            if char != '[':
                tmp = char + tmp
            else:
                repeat_cnt = stack.pop()
                new_str = tmp * repeat_cnt
                if stack:
                    stack.append(new_str)
                    return   # don't forget to return here
                else:
                    result.append(new_str)
                    return   # don't forget to return here

    def get_number(self, s, idx):
        cnt = int(s[idx])
        for i in range(idx+1, len(s)):
            char = s[i]
            if '0' <= char <= '9':
                cnt = cnt * 10 + int(char)
            else:
                return cnt, i


    def expressionExpand_ref(self, s): #stack way, 282ms, all result is stored in stack, very good way to solve
        # Write your code here

        stack = []
        number = 0
        for char in s:
            if char.isdigit():
                number = number * 10 + ord(char) - ord('0')
            elif char == '[':
                stack.append(number)
                number = 0
            elif char == ']':
                strs = []
                while len(stack):
                    top = stack.pop()
                    if type(top) == int:
                        stack.append(''.join(reversed(strs)) * top)
                        break
                    strs.append(top)
            else:
                stack.append(char)
        return ''.join(stack)

    def expressionExpand_ref2(self, s): # recursive way, 354ms, every call of the method will process one pair of [] or no []
        # Write your code here
        if '[' not in s:
            return s

        if not s[0].isdigit():
            index = 0
            while not s[index].isdigit():
                index += 1

            left_str = s[0: index]
            right_str = s[index:]
            times = 1
        else:
            left = s.find('[')
            times = int(s[0: left])
            pair = 0
            for index in xrange(left, len(s)):
                if s[index] == '[':
                    pair += 1
                elif s[index] == ']':
                    pair -= 1
                if pair == 0:
                    right = index
                    break

            left_str = s[left + 1: right]
            right_str = s[right + 1:]

        return self.expressionExpand(left_str) * times + \
               self.expressionExpand(right_str)



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = "abc3[a]"
        answer = "abcaaa"
        result = self.sol.expressionExpand(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = "3[abc]"
        answer = "abcabcabc"
        result = self.sol.expressionExpand(nums)
        self.assertEqual(answer, result)

    def test_case3(self):
        nums = "4[ac]dy"
        answer = "acacacacdy"
        result = self.sol.expressionExpand(nums)
        self.assertEqual(answer, result)

    def test_case4(self):   # ===>
        nums = "3[2[ad]3[pf]]xyz"
        answer = "adadpfpfpfadadpfpfpfadadpfpfpfxyz"
        result = self.sol.expressionExpand(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
