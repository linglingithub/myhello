#coding=utf-8

import unittest

"""

406. Queue Reconstruction by Height
DescriptionHintsSubmissionsDiscussSolution
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.


Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

Difficulty:Medium
Total Accepted:47.9K
Total Submissions:84.6K
Contributor:LeetCode
Companies 

Related Topics 

Similar Questions 
Count of Smaller Numbers After Self


"""

from collections import defaultdict

class Solution(object):
    def reconstructQueue(self, people):
        """

        :param people:
        :return:
        """
        if not people:
            return []
        #people.sort(people, key = lambda x: (-x[0], x[1]))
        people.sort(key = lambda x: (-x[0], x[1]))
        res = []
        for ppl in people:
            res.insert(ppl[1], ppl)
        return res




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

"""

Explanation of the neat Sort+Insert solution
20.1K
VIEWS
107
Last Edit: June 8, 2018 12:13 PM

StefanPochmann
StefanPochmann
 21816
Below is my explanation of the following neat solution where we sort people from tall to short (and by increasing k-value) and then just insert them into the queue using their k-value as the queue index:

def reconstructQueue(self, people):
    people.sort(key=lambda (h, k): (-h, k))
    queue = []
    for p in people:
        queue.insert(p[1], p)
    return queue
I didn't come up with that myself, but here's my own explanation of it, as I haven't seen anybody explain it (and was asked to explain it):

People are only counting (in their k-value) taller or equal-height others standing in front of them. So a smallest person is completely irrelevant for all taller ones. And of all smallest people, the one standing most in the back is even completely irrelevant for everybody else. Nobody is counting that person. So we can first arrange everybody else, ignoring that one person. And then just insert that person appropriately. Now note that while this person is irrelevant for everybody else, everybody else is relevant for this person - this person counts exactly everybody in front of them. So their count-value tells you exactly the index they must be standing.

So you can first solve the sub-problem with all but that one person and then just insert that person appropriately. And you can solve that sub-problem the same way, first solving the sub-sub-problem with all but the last-smallest person of the subproblem. And so on. The base case is when you have the sub-...-sub-problem of zero people. You're then inserting the people in the reverse order, i.e., that overall last-smallest person in the very end and thus the first-tallest person in the very beginning. That's what the above solution does, Sorting the people from the first-tallest to the last-smallest, and inserting them one by one as appropriate.

Now that's my explanation. If you have a different one, I'm interested to see it :-)

"""