#coding=utf-8
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


class MinStack(object): #99ms, 47%

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.store = []
        self.min_store = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.store.append(x)
        if not self.min_store or x <= self.min_store[-1]:
            self.min_store.append(x)


    def pop(self):
        """
        :rtype: void
        """
        if not self.store:
            raise ValueError
        if self.min_store[-1] == self.store[-1]:
            del self.min_store[-1]
        del self.store[-1]  #for lintcode, this requires int return, then return self.store.pop()


    def top(self):
        """
        :rtype: int
        """
        if not self.store:
            raise ValueError
        return self.store[-1]


    def getMin(self):
        """
        :rtype: int
        """
        if not self.store:
            raise ValueError
        return self.min_store[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


class MinStack_old(object):

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
        self.minStack = MinStack()
        self.minStack.push(-2)
        self.minStack.push(0)
        self.minStack.push(-3)

    def test_case1(self):
        result = []
        result.append(self.minStack.getMin()) #-3
        self.minStack.pop()
        result.append(self.minStack.top()) #;      --> Returns 0.
        result.append(self.minStack.getMin()) #;   --> Returns -2.
        answer = [-3, 0, -2]

        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""

利用两个栈结构，其中一个是主要的正常stack，满足pop(), push()的O(1)时间要求，另外一个作为辅助的minStack，仅存入min的integer。
min = Integer.parseInt(minStack.peek().toString());+

push()时，如果number >= min，则push到minStack上 pop()时，如果number == min，也从minStack上pop
题中的例子，最终stack为[2, 3, 1], minStack为 [2, 1]


========================================================================================================================

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
