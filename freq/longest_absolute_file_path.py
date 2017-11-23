#coding=utf-8

import unittest

"""
388. Longest Absolute File Path
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Suppose we abstract our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to file in the abstracted file system. If there is no file in the system, return 0.

Note:
The name of a file contains at least a . and an extension.
The name of a directory or sub-directory will not contain a ..
Time complexity required: O(n) where n is the size of the input string.

Notice that a/aa/aaa/file1.txt is not the longest file path, if there is another path aaaaaaaaaaaaaaaaaaaaa/sth.png.


Difficulty:Medium
Total Accepted:38.3K
Total Submissions:103.3K
Contributor: LeetCode


==================================

[lintcode]

643. System Longest File Path 

 Description
 Notes
 Testcase
 Judge
Suppose we abstract our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string

"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to file in the abstracted file system. If there is no file in the system, return 0.

 Notice

The name of a file contains at least a . and an extension.
The name of a directory or sub-directory will not contain a ..
Time complexity required: O(n) where n is the size of the input string.
Notice that a/aa/aaa/file1.txt is not the longest file path, if there is another path aaaaaaaaaaaaaaaaaaaaa/sth.png.
Have you met this question in a real interview? Yes
Example
Give input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" return

Tags 
Google

"""


class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        if not input:
            return 0
        stack_path = []
        stack_level = []
        res = 0
        lines = input.split("\n")
        for line in lines:
            #tmp = line.strip() # can't do this, white space should be kept
            idx = 0
            for char in line:
                if char == '\t':
                    idx +=1
                else:
                    break
            tmp = line[idx:]
            curr_level = idx
            # find parent folder for current line !!! apply to not only folder, but ALSO FILES!!!, otherwise wrong
            while stack_level and stack_level[-1] >= curr_level:
                stack_path.pop()
                stack_level.pop()
            # deal with file
            if '.' in tmp:
                full_path = sum([len(path) for path in stack_path]) + \
                len(stack_path) + len(tmp)
                res = max(full_path, res)
                continue
            # deal with directory
            stack_path.append(tmp)
            stack_level.append(curr_level)
        return res


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = "dir\n        file.txt"
        answer = 16
        result = self.sol.lengthLongestPath(nums)
        self.assertEqual(answer, result)


    def test_case2(self):
        nums = "dir\n file.txt"
        answer = 9
        result = self.sol.lengthLongestPath(nums)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""


"""

#-*- coding:utf-8 -*-
