#coding = utf-8
"""
给两个char array，其中有一些char为backspace就是删除前面的字符，要求输出一个boolean判断两个char array是否相同，
时间要求O(n) , 空间要求O(1)
例如：
[a,b,'\b',d,c] 和[a,d,c] true
[a,b,'\b','\b','\b',d,c] 和 [d,c] true
[a,b,d,'\b'] 和 [a,d] false

先给了用Stack的方法，TimeO(n), SpaceO(n)，没让写code.
之后要求TimeO(n), SpaceO(1)，po主试着从前往后parse没成功，好久之后小哥给提示从后往前parse


"""

import unittest
import functools

class Solution:

    def check_same_array(self, a, b):
        """
        use a stack, 
        Time: O(n)
        Space: O(n)
        :param a: 
        :param b: 
        :return: 
        """
        if a is None and b is None:
            return True
        elif a is None or b is None:
            return False
        a = self._simplify(a)
        b = self._simplify(b)
        return self._compare(a, b)

    def _simplify(self, a):
        stack = []
        for char in a:
            if char == '\b':
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return stack

    def _compare(self, a, b):
        if not a and not b:
            return True
        elif not a or not b:
            return False
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
        return True

    def check_same_array1(self, a, b):
        """
        do it reverse way,
        Time: O(n)
        Space: O(1)
        :param a: char array
        :param b:
        :return: boolean
        """
        if a is None and b is None:
            return True
        elif a is None or b is None:
            return False
        i, j = len(a) - 1, len(b) - 1
        # while i >= 0 and j >= 0:
        while True:
            i = self._go_to_prev_char(a, i)
            j = self._go_to_prev_char(b, j)
            if i < 0 and j < 0:
                return True
            elif i < 0 or j < 0:
                return False
            elif a[i] != b[j]:
                return False
            else:
                i -= 1
                j -= 1
        return True


    def _go_to_prev_char(self, a, i):
        """
        Think about when there are a lot of '/b'
        :param a: 
        :param i: 
        :return: 
        """
        cnt = 0
        while i >= 0:
            if a[i] == '\b':
                cnt += 1
                i -= 1
            else:
                cnt -= 1
                if cnt < 0:
                    break
                else:
                    i -= 1
        return i



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        a, b = ['a', 'b', '\b', 'd', 'c'], ['a', 'd', 'c']
        answer = True
        result = self.sol.check_same_array(a, b)
        self.assertEqual(answer, result)

    def test_case2(self):
        a, b = ['a', 'b', '\b', '\b', '\b', 'd', 'c'], ['d', 'c']
        answer = True
        result = self.sol.check_same_array(a, b)
        self.assertEqual(answer, result)

    def test_case3(self):
        a, b = ['a', 'b', 'd', '\b'], ['a', 'd']
        answer = False
        result = self.sol.check_same_array(a, b)
        self.assertEqual(answer, result)

    def test_case4(self):
        a, b = ['a', 'd'], ['a', 'd']
        answer = True
        result = self.sol.check_same_array(a, b)
        self.assertEqual(answer, result)

    def test_case5(self):
        a, b = ['a', '\b', 'd', '\b', '\b'], []
        answer = True
        result = self.sol.check_same_array(a, b)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()