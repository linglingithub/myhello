#coding=utf-8

import unittest

"""
Implement Queue by Two Stacks

As the title described, you should only use two stacks to implement a queue's actions.

The queue should support push(element), pop() and top() where pop is pop the first(a.k.a front) element in the queue.

Both pop and top methods should return the value of first element.

Example
push(1)
pop()     // return 1
push(2)
push(3)
top()     // return 2
pop()     // return 2


Challenge 
implement it by two stacks, do not use any other data structure and push, pop and top should be O(1) by AVERAGE.

Tags 
LintCode Copyright Stack Queue
Related Problems 
Medium Min Stack

"""


class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, element):
        # write your code here
        self.stack1.append(element)  #append, not push

    def top(self):
        # write your code here
        # return the top element
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1] # should be -1 here, not 0

    def pop(self):
        # write your code here
        # pop and return the top element
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


    # write your code here
# pop and return the top element



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = MyQueue()

    def test_case1(self):
        result = []
        answer = [1,2,2]
        self.sol.push(1)
        result.append(self.sol.pop())
        self.sol.push(2)
        self.sol.push(3)
        result.append(self.sol.top())
        result.append(self.sol.pop())
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
