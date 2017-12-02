#coding=utf-8

import unittest

"""

541. Zigzag Iterator II 

 Description
 Notes
 Testcase
 Judge
Follow up Zigzag Iterator: What if you are given k 1d vectors? How well can your code be extended to such cases? The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic".

Have you met this question in a real interview? Yes
Example
Given k = 3 1d vectors:

[1,2,3]
[4,5,6,7]
[8,9]
Return [1,4,8,2,5,9,3,6,7].

Tags 
Google
Related Problems 
Medium Zigzag Iterator 43 %
Medium Flatten Nested List Iterator 28 %
Hard Binary Search Tree Iterator

"""

from collections import deque


class ZigzagIterator2:
    """
    @param: vecs: a list of 1d vectors
    """

    def __init__(self, vecs):
        # do intialization if necessary
        self.queue = deque()
        for vec in vecs:
            if vec:
                self.queue.append((0, vec))

    """
    @return: An integer
    """

    def next(self):
        # write your code here
        idx, vals = self.queue.popleft()
        res = vals[idx]
        idx += 1
        if idx < len(vals):
            self.queue.append((idx, vals))
        return res

    """
    @return: True if has next
    """

    def hasNext(self):
        # write your code here
        while self.queue:
            if self.queue[0][0] < len(self.queue[0][1]):
                return True
            self.queue.popleft()
        return False


# Your ZigzagIterator object will be instantiated and called as such:
# solution, result = ZigzagIterator(v1, v2), []
# while solution.hasNext(): result.append(solution.next())
# Output result



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = 1
        answer = 1
        result = self.sol.testm(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
