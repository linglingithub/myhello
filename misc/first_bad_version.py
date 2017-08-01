#coding=utf-8

import unittest

"""

278. First Bad Version

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of
your product fails the quality check. Since each version is developed based on the previous version, all the versions
after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following
ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find
the first bad version. You should minimize the number of calls to the API.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

Subscribe to see which companies asked this question.

Hide Tags Binary Search
Hide Similar Problems (M) Search for a Range (E) Search Insert Position (E) Guess Number Higher or Lower

Easy

"""



# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool



def isBadVersion(version):
    pass

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return -1
        l, r = 0, n
        last = -1
        while l <= r:
            mid = (l+r)/2
            if mid == last:
                return mid
            if isBadVersion(mid):
                r = mid
                last = mid
            else:
                l = mid + 1
        return last


class Solution1(object):
    def firstBadVersion(self, n): #39ms, 67%
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left < right:
            mid = (left+right)/2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = 1
        answer = 1
        result = self.sol.firstBadVersion(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""

A good warning to me to use start+(end-start)/2 to avoid overflow
Before this problem, I have always use

  mid = (start+end)) / 2;
To get the middle value, but this can caused OVERFLOW !

when start and end are all about INT_MAX , then (start+end) of course will be overflow !

To avoid the problem we can use

  mid =  start+(end-start)/2;
Here is the AC implementation

// Forward declaration of isBadVersion API.
bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int start=0, end=n;
        cout<<end-start<<end;
        while(end-start>1){
            int mid=start+(end-start)/2;
            /** mid = (start+end)) / 2; **/
            if(isBadVersion(mid))  end=mid;
            else  start=mid;
        }
        return end;
    }
};


"""

#-*- coding:utf-8 -*-
