#coding=utf-8

import unittest
import ConfigParser
from util.string_to_list import string_to_int_list
"""


Given n pieces of wood with length L[i] (integer array). Cut them into small pieces to guarantee you could have equal or
 more than k pieces with the same length. What is the longest length you can get from the n pieces of wood? Given L & k,
  return the maximum length of the small pieces.

 Notice

You couldn't cut wood into float length.

If you couldn't get >= k pieces, return 0.

Have you met this question in a real interview? Yes
Example
For L=[232, 124, 456], k=7, return 114.

Challenge
O(n log Len), where Len is the longest length of the wood.

Tags
Binary Search


"""



class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """
    def woodCut(self, L, k):
        # write your code here
        if not L or k < 1:
            return 0 # expect 0, not -1 here
        # length = 0
        # for i in range(len(L)):
        #     length = max(length, L[i])
        length = max(L)
        left, right = 0, length  # starting point should be 0, not 1, see case 7
        while left < right:
            mid = (left+right)/2
            if mid == left:
                # return mid  # can NOT directly return here, check case 3, right maybe be lost out of possible right answer
                if sum(wood / right for wood in L) >= k:
                    return right
                else:
                    return left
            cnt = sum(wood/mid for wood in L)
            if cnt < k:
                right = mid - 1
            elif cnt >= k:
                #left = mid + 1  # wrong for case 6, after mid+1, cnt will be bigger(a lot bigger), but max will be excluded??
                left = mid
        #print ("reached out side")
        #return left #wrong for case 4, out when left > right
        # return min(left, right) #wrong for case 5
        return min(mid, right)

    def woodCut_wrong(self, L, k):
        # write your code here
        if not L or k < 1:
            return -1
        # length = 0
        # for i in range(len(L)):
        #     length = max(length, L[i])
        length = max(L)
        left, right = 1, length
        while left < right:
            mid = (left+right)/2
            cnt = sum(wood/mid for wood in L)
            if cnt < k:
                right = mid - 1
            elif cnt > k:
                #left = mid + 1  # wrong for case 6, after mid+1, cnt will be bigger(a lot bigger), but max will be excluded??
                left = mid # after modified, dead loop here for case 5 and 6
            else:
                if mid == left:
                    #return mid  # can NOT directly return here, check case 3, right maybe be lost out of possible right answer
                    if sum(wood/right for wood in L) == k:
                        return right
                    else:
                        return left
                else:
                    #left = mid + 1  # can't skip here, mid may still be included in answer, check case 1,2
                    left = mid

        #print ("reached out side")
        #return left #wrong for case 4, out when left > right
        # return min(left, right) #wrong for case 5
        return min(mid, right)


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [232, 124, 456]
        k = 7
        answer = 114
        result = self.sol.woodCut(nums, k)
        self.assertEqual(answer, result)

    def test_case2(self):  # !!! not necessarily every wood will be used, eg. 124
        nums = [232, 124, 456]
        k = 3
        answer = 228
        result = self.sol.woodCut(nums, k)
        self.assertEqual(answer, result)

    def test_case3(self):  #====>
        nums = [2147483644,2147483645,2147483646,2147483647]
        k = 4
        answer = 2147483644   # wrong output 2147483643
        result = self.sol.woodCut(nums, k)
        self.assertEqual(answer, result)

    def test_case4(self):  #====>
        config = ConfigParser.RawConfigParser(allow_no_value=True)
        data_file = "../data/wood_cut_case4.ini"
        with open(data_file) as fin:
            config.readfp(fin)
            nums = config.get("data", "L")
            nums = string_to_int_list(nums)
            k = config.get("data", "k")
            print type(nums), k

        k = 2500
        answer = 34   # wrong output 35
        result = self.sol.woodCut(nums, k)
        self.assertEqual(answer, result)

    def test_case5(self):  #====>
        config = ConfigParser.RawConfigParser(allow_no_value=True)
        data_file = "../data/wood_cut_case5.ini"
        with open(data_file) as fin:
            config.readfp(fin)
            nums = config.get("data", "L")
            nums = string_to_int_list(nums)
            k = config.get("data", "k")
            #print type(nums), k

        k = 80000
        answer = 5   # wrong output 6
        result = self.sol.woodCut(nums, k)
        self.assertEqual(answer, result)

    def test_case6(self):  #====>
        config = ConfigParser.RawConfigParser(allow_no_value=True)
        data_file = "../data/wood_cut_case6.ini"
        with open(data_file) as fin:
            config.readfp(fin)
            nums = config.get("data", "L")
            nums = string_to_int_list(nums)
            k = int(config.get("data", "k"))
            #print type(nums), k

        answer = 938   # wrong output 939
        result = self.sol.woodCut(nums, k)
        self.assertEqual(answer, result)

    def test_case7(self):  #====>
        config = ConfigParser.RawConfigParser(allow_no_value=True)
        data_file = "../data/wood_cut_case7.ini"
        with open(data_file) as fin:
            config.readfp(fin)
            nums = config.get("data", "L")
            nums = string_to_int_list(nums)
            k = int(config.get("data", "k"))
            #print type(nums), k

        answer = 0   # wrong output 1
        result = self.sol.woodCut(nums, k)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""
    def woodCut(self, L, k):
        if sum(L) < k:
            return 0
            
        maxLen = max(L)
        start, end = 1, maxLen
        while start + 1 < end:
            mid = (start + end) / 2
            pieces = sum([l / mid for l in L])
            if pieces >= k:
                start = mid
            else:
                end = mid
                
        if sum([l / end for l in L]) >= k:
            return end
        return start

"""