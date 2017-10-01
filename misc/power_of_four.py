#coding=utf-8

import unittest

"""
342. Power of Four

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?

Credits:
Special thanks to @yukuairoy for adding this problem and creating all test cases.

Difficulty:Easy
Total Accepted:71.4K
Total Submissions:184.9K
Contributor: LeetCode
Subscribe to see which companies asked this question.

Related Topics 
Bit Manipulation 
Similar Questions 
Power of Two Power of Three 

"""

import math
class Solution(object):
    def isPowerOfFour(self, num):  #  50%, can's use num&1 ==0, that's for even number, not for power of 2
        #return num >0 and (num == 1 or num & 1 == 0) and num & 0x55555555 == num
        return num >0 and (num & (num-1) == 0) and num & 0x55555555 == num

    def isPoswerOfFour2(self, num):  #%50
        if num <= 0:
            return False
        while num % 4 == 0:
            num = num / 4
        return True if num == 1 else False


    def isPowerOfFour1(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and 4 ** int(math.log(num, 4)) == num  # note, need int() here, otherwise wrong, case1



class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):   # ====>
        nums = 2
        answer = False
        result = self.sol.isPowerOfFour(nums)
        self.assertEqual(answer, result)

    def test_case2(self):   # ====> to test 0x55555555 way, add num&1==0
        nums = 5
        answer = False
        result = self.sol.isPowerOfFour(nums)
        self.assertEqual(answer, result)

    def test_case3(self):   # ====> to test 0x55555555 way, add num==1 or num&1==0
        nums = 1
        answer = True
        result = self.sol.isPowerOfFour(nums)
        self.assertEqual(answer, result)

    def test_case4(self):   # ====> to test 0x55555555 way,
        nums = 20
        answer = False
        result = self.sol.isPowerOfFour(nums)
        self.assertEqual(answer, result)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()


"""
Java 1-line (cheating for the purpose of not using loops)
    public boolean isPowerOfFour(int num) {
        return num > 0 && (num&(num-1)) == 0 && (num & 0x55555555) != 0;
        //0x55555555 is to get rid of those power of 2 but not power of 4
        //so that the single 1 bit always appears at the odd position 
    }

============
    
O(1) one-line solution without loops
public class Solution {
    public boolean isPowerOfFour(int num) {
        return (num > 0) && ((num & (num - 1)) == 0) && ((num & 0x55555555) == num);
    }
}
The basic idea is from power of 2, We can use "n&(n-1) == 0" to determine if n is power of 2. For power of 4, the additional restriction is that in binary form, the only "1" should always located at the odd position. For example, 4^0 = 1, 4^1 = 100, 4^2 = 10000. So we can use "num & 0x55555555==num" to check if "1" is located at the odd position.
    
  
=============    

Simple C++ O(1) solution without 0x55555555
class Solution {
public:
    bool isPowerOfFour(int num) {
        return ((num-1)&num)==0 && (num-1)%3==0;
    }
};



"""
#-*- coding:utf-8 -*-
