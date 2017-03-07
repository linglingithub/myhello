__author__ = 'linglin'


"""

155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
Subscribe to see which companies asked this question.

Hide Tags Stack Design
Hide Similar Problems (H) Sliding Window Maximum

Easy

"""

import unittest


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.store = []
        self.min_val = None


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if type(x) is not int:
            raise ValueError
        else:
            self.store.append(x)
            self.min_val = min(self.min_val, x) if self.min_val is not None else x


    def pop(self):
        """
        :rtype: void
        """
        if self.store:
            del self.store[-1]
            #todo:
            if not self.store:
                self.min_val = None
            else:
                self.min_val = self.store[0]
                for x in self.store[1:]:
                    self.min_val = min(x, self.min_val)
        else:
            raise ValueError



    def top(self):
        """
        :rtype: int
        """
        return self.store[-1] if self.store else None


    def getMin(self):
        """
        :rtype: int
        """
        return self.min_val



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


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

"""
class MinStack(object):

    def __init__(self):
        # do some intialize if necessary
        self.stack = []
        self.minstack = []

    def push(self, number):
        # write yout code here
        self.stack.append(number)
        if len(self.minstack) == 0 or number <= self.minstack[-1]:
            self.minstack.append(number)

    def pop(self):
        # pop and return the top item in stack
        if self.stack[-1] == self.minstack[-1]:
            self.minstack.pop()
        return self.stack.pop()

    def min(self):
        # return the minimum number in stack
        return self.minstack[-1]

"""

#-*- coding:utf-8 -*-
#coding=utf-8