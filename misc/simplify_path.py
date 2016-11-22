"""
71. Simplify Path

Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".

Subscribe to see which companies asked this question

Hide Tags Stack String


Medium


"""



import unittest


class Solution(object):
    def simplifyPath(self, path): #62ms, 43%, 45ms, 83%
        """
        :type path: str
        :rtype: str
        """
        if path is None or len(path)==0:
            return ""
        result = ""
        if path[0]=="/":
            result += "/"
        segs = path.split("/")
        seg_stack = []
        for seg in segs:
            if seg == "" or seg==".":
                continue
            if seg == "..":
                if len(seg_stack) > 0:
                    seg_stack.pop()
                else:
                    continue
            else:
                seg_stack.append(seg)
        path_str = "/".join(seg_stack)
        result += path_str
        return result


    def simplifyPath_ref(self, path): #code simple and nice, does not consider the case when first char is not "/"
        """
        :type path: str
        :rtype: str
        """
        stack, tokens = [], path.split("/")
        for token in tokens:
            if token == ".." and stack:
                stack.pop()
            elif token != ".." and token != "." and token:
                stack.append(token)
        return "/" + "/".join(stack)


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = "/home/"
        answer = "/home"
        result = self.sol.simplifyPath(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = "/a/./b/../../c/"
        answer = "/c"
        result = self.sol.simplifyPath(nums)
        self.assertEqual(answer, result)

    def test_case3(self):
        nums = "/../"
        answer = "/"
        result = self.sol.simplifyPath(nums)
        self.assertEqual(answer, result)

    def test_case4(self):
        nums = "/home//foo/"
        answer = "/home/foo"
        result = self.sol.simplifyPath(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8