#coding=utf-8

import unittest

"""
657. Judge Route Circle
DescriptionHintsSubmissionsDiscussSolution
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false

Difficulty:Easy
Total Accepted:79.7K
Total Submissions:116.5K
Contributor:maxsteel
Companies

Related Topics

Similar Questions
Friend Circles

"""

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        from collections import Counter
        move_count = Counter(moves)
        # return move_count['U'] == move_count['D'] == move_count['L'] == move_count['R']
        # !!!! (1) L not necessary == U (2) use get not [] to avoid None key error
        return move_count.get('U') == move_count.get('D') and move_count.get('L') == move_count.get('R')



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
