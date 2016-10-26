"""
Count and Say

The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

Subscribe to see which companies asked this question

Hide Tags String
Hide Similar Problems (M) Encode and Decode Strings


"""

import unittest


class Solution(object):
    def countAndSay(self, n): # 39ms, 97.92%
        """
        :type n: int
        :rtype: str
        """
        if n < 1:
            return ""
        current = "1"
        idx = 1
        while idx < n:
            next = ""
            char = current[0]
            cnt = 1
            for i in range(1,len(current)):
                if char == current[i]:
                    cnt += 1
                if char != current[i]:
                    next += str(cnt)+char
                    char = current[i]
                    cnt = 1
            next += str(cnt)+char
            current = next
            idx +=1
        return current






class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self): # self test wrong, then correct it
        n = 5
        answer = "111221"
        result = self.sol.countAndSay(n)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()
