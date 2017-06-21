#coding=utf-8

import unittest

"""
Flatten List 

 Description
 Notes
 Testcase
 Judge
Given a list, each element in the list can be a list or integer. flatten it into a simply list with integers.

 Notice

If the element in the given list is a list, it can contain list too.

Have you met this question in a real interview? Yes
Example
Given [1,2,[1,2]], return [1,2,1,2].

Given [4,[3,[2,[1]]]], return [4,3,2,1].

Challenge 
Do it in non-recursive.

Tags 
LintCode Copyright Recursion Non Recursion
Related Problems 
Medium Flatten 2D Vector

"""


class Solution(object):
    # @param nestedList a list, each element in the list
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer

    def flatten(self, nestedList):  # ref idea, similar to use a stack
        # Write your code here
        if isinstance(nestedList, int):
            return [nestedList]
        result = []
        stack = []

        while nestedList:
            tmp = nestedList.pop(0)
            if isinstance(tmp, int):
                result.append(tmp)
            else:
                for idx, ele in enumerate(tmp):
                    nestedList.insert(idx, ele)
        return result


    def flatten2(self, nestedList): #ref recursive
        if isinstance(nestedList, int):
            return [nestedList]
        result = []
        for ele in nestedList:
            result.extend(self.flatten(ele))
        return result




    def flatten_recursive(self, nestedList):
        # Write your code here
        if not nestedList:
            return []
        result = []
        self.helper(nestedList, result)
        return result

    def helper(self, intlist, result):
        if intlist is None or intlist == []:
            return result
        if type(intlist) == int:
            result.append(intlist)
        else:
            for ele in intlist:
                self.helper(ele, result)


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case2(self):
        nums = [4,[3,[2,[1]]]]
        answer = [4,3,2,1]
        result = self.sol.flatten(nums)
        self.assertEqual(answer, result)


    def test_case1(self):
        nums = [1,2,[1,2]]
        answer = [1,2,1,2]
        result = self.sol.flatten(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
