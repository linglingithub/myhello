#coding=utf-8

import unittest

"""

314.	Binary Tree Vertical Order Traversal  (locked)
题目：

Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
 

return its vertical order traversal as:

[
  [9],
  [3,15],
  [20],
  [7]
]
 

Given binary tree [3,9,20,4,5,2,7],

    _3_
   /   \
  9    20
 / \   / \
4   5 2   7
 

return its vertical order traversal as:

[
  [4],
  [9],
  [3,5,2],
  [20],
  [7]
]
"""



class Solution(object):
    def searchInsert(self, nums):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """


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



#-*- coding:utf-8 -*-

"""


def verticalOrder(self, root):
    cols = collections.defaultdict(list)
    queue = [(root, 0)]
    for node, i in queue:
        if node:
            cols[i].append(node.val)
            queue += (node.left, i - 1), (node.right, i + 1)
    return [cols[i] for i in sorted(cols)]


B bryan.chou.121 
Reputation:  14
changing a list while iterating over it feels like anti-pattern to me. (I know you are just appending items to it, not removing items from it, but I still think use an extra counter variable with len(queue) is a bit better.

Dec 11, 2015, 4:41 AM reply quote 
0
  StefanPochmann  
Reputation:  17,734
@bryan.chou.121 Yeah, I know... I just prefer focusing on the actual algorithm, so I like doing it this short way. I'm sure I've mentioned before that to my knowledge this isn't guaranteed to work, but while I'm always aware of it, I really don't feel like explaining it every time. Maybe I should just stop using it...
Ok I just wrote the two obvious clean replacements. Meh... I wish they'd just define my iteration to work.

def verticalOrder(self, root):
    cols = collections.defaultdict(list)
    queue = collections.deque([(root, 0)])
    while queue:
        node, i = queue.popleft()
        if node:
            cols[i].append(node.val)
            queue += (node.left, i - 1), (node.right, i + 1)
    return [cols[i] for i in sorted(cols)]

def verticalOrder(self, root):
    cols = collections.defaultdict(list)
    queue = [(root, 0)]
    i = 0
    while i < len(queue):
        node, x = queue[i]
        i += 1
        if node:
            cols[x].append(node.val)
            queue += (node.left, x - 1), (node.right, x + 1)
    return [cols[x] for x in sorted(cols)]

"""