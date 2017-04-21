#coding=utf-8

import unittest

"""
165. Compare Version Numbers

Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the
second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
Credits:
Special thanks to @ts for adding this problem and creating all test cases.

Subscribe to see which companies asked this question.

Hide Tags String

Medium

"""



class Solution(object):
    def compareVersion(self, version1, version2): #62ms, 10%
        """
        Before answering the question, ask what's the format of all possible inputs.
        Without any dot? With multiple dots? NONE or '' inputs? etc.

        :type version1: str
        :type version2: str
        :rtype: int
        """
        if not version1 or not version2:
            raise ValueError("Inputs should be two non-emtpy strings.")
        a1 = version1.split(".")
        a2 = version2.split(".")

        n = min(len(a1), len(a2))
        for i in range(n):
            if int(a1[i]) == int(a2[i]): # need to add int here, dealing with leading zero, see case9
                continue
            else:
                a = int(a1[i])
                b = int(a2[i])
                return 1 if a>b else -1

        if len(a1)>len(a2):
            for i in range(n, len(a1)): # for trailing zeros, see case 10
                if int(a1[i])==0:
                    continue
                else:
                    return 1
            return 0
        elif len(a1) == len(a2):
            return 0
        else:
            for i in range(n, len(a2)):
                if int(a2[i])==0:
                    continue
                else:
                    return -1
            return 0


    def compareVersion_ref(self, version1, version2): #39ms, 80%, nice and clean
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1Arr = version1.split(".")
        v2Arr = version2.split(".")
        len1 = len(v1Arr)
        len2 = len(v2Arr)
        lenMax = max(len1, len2)
        for x in range(lenMax):
            v1Token = 0
            if x < len1:
                v1Token = int(v1Arr[x])
            v2Token = 0
            if x < len2:
                v2Token = int(v2Arr[x])
            if v1Token < v2Token:
                return -1
            if v1Token > v2Token:
                return 1
        return 0

    def compareVersion_ref2(self, version1, version2): #52ms, 26%
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = [int(x) for x in version1.split('.')]
        v2 = [int(x) for x in version2.split('.')]
        while len(v1) != len(v2):
            if len(v1) > len(v2):
                v2.append(0)
            else:
                v1.append(0)
        return cmp(v1, v2)

    def compareVersion_ref3(self, version1, version2): #46ms, 45%
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        main1, _, rest1 = ('0' + version1).partition('.')
        main2, _, rest2 = ('0' + version2).partition('.')
        return cmp(int(main1), int(main2)) or len(rest1 + rest2) and self.compareVersion_ref3(rest1, rest2)


    def compareVersion_wrong(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        if version1 == version2:
            return 0
        idx1 = version1.find(".")   #used find() instead of index(), returns -1, index() return ValueError
        idx2 = version2.find(".")
        if idx1 == -1:
            v11 = int(version1)
            v12 = 0
        else:
            v11 = int(version1[:idx1])
            v12 = int(version1[idx1+1:])
        if idx2 == -1:
            v21 = int(version2)
            v22 = 0
        else:
            v21 = int(version2[:idx2])
            v22 = int(version2[idx2+1:])
        if v11 == v22:
            return 1 if v12>v22 else -1
        else:
            return 1 if v11>v21 else -1


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        v1 = '0.1'
        v2 = '0.10'
        answer = -1
        result = self.sol.compareVersion(v1,v2)
        self.assertEqual(answer, result)

    def test_case2(self):
        v1 = '1.9'
        v2 = '2.0'
        answer = -1
        result = self.sol.compareVersion(v1,v2)
        self.assertEqual(answer, result)

    def test_case3(self):
        v1 = '1.1'
        v2 = '0.10'
        answer = 1
        result = self.sol.compareVersion(v1,v2)
        self.assertEqual(answer, result)

    def test_case4(self):
        v1 = '1.1'
        v2 = '1.1'
        answer = 0
        result = self.sol.compareVersion(v1,v2)
        self.assertEqual(answer, result)

    def test_case5(self): # ===>
        v1 = '1'
        v2 = '0'
        answer = 1
        result = self.sol.compareVersion(v1,v2)
        self.assertEqual(answer, result)

    def test_case6(self): # ===>
        v1 = '0.1'
        v2 = "0.0.1"
        answer = 1
        result = self.sol.compareVersion(v1,v2)
        self.assertEqual(answer, result)

    def test_case7(self): # ===>
        v1 = '0.1'
        v2 = "0.1.1"
        answer = -1
        result = self.sol.compareVersion(v1,v2)
        self.assertEqual(answer, result)

    def test_case8(self): # ===>
        v1 = None
        v2 = "0.1.1"
        exceptClass = ValueError("Inputs should be two non-emtpy strings.")
        #with self.assertRaises(exceptClass): # should pass a class, not an instance of class
        with self.assertRaises(ValueError):
            self.sol.compareVersion(v1,v2)

    def test_case9(self): # ===>
        v1 = "01"
        v2 = "1"
        answer = 0
        result = self.sol.compareVersion(v1,v2)
        self.assertEqual(answer, result)

    def test_case10(self): # ===>
        v1 = "1"
        v2 = "1.1"
        answer = -1
        result = self.sol.compareVersion(v1,v2)
        self.assertEqual(answer, result)

    def test_case11(self): # ===>
        v1 = "1"
        v2 = "1.0"
        answer = 0
        result = self.sol.compareVersion(v1,v2)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
