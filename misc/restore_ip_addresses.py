"""
93. Restore IP Addresses

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

Subscribe to see which companies asked this question

Hide Tags Backtracking String

Medium

"""


import unittest


class Solution(object):
    def restoreIpAddresses(self, s): #45ms, 82%
        """
        :type s: str
        :rtype: List[str]
        """
        if s is None or 4>len(s) or len(s)>12: #add length protection here otherwise TLE for super long string
            return []
        result = []
        self.dfs_ip(result, s, '', 0, 1)
        return result

    def dfs_ip(self, result, s, current, idx, level):
        if idx>=len(s) or level>=5:
            if level == 5 and idx==len(s):
                current = current[1:]  # to remove the first . added, otherwise result like ['.255.255.11.135', '.255.255.111.35']
                result.append(current)
            return

        length = 3
        if s[idx]=='0': # add this for case2
            length=1

        for i in range(length): #note the index here
            if idx+i < len(s):
                tmp = s[idx:idx+i+1]
                if 0<=int(tmp)<=255:
                        self.dfs_ip(result, s, current+"."+tmp, idx+i+1, level+1)





class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case2(self): #=====> this case means that extra leading zero is not allowed.
        s = "010010"
        answer = ["0.10.0.10","0.100.1.0"]
        # answer = ['0.1.0.010',  '0.1.00.10', '0.1.001.0',  '0.10.0.10',
        #      '0.10.01.0',
        #       '0.100.1.0',
        #       '01.0.0.10',
        #       '01.0.01.0',
        #       '01.00.1.0',
        #       '010.0.1.0']
        result = self.sol.restoreIpAddresses(s)
        self.assertEqual(sorted(answer), sorted(result))

    def test_case1(self):
        s = "25525511135"
        answer = ["255.255.11.135", "255.255.111.35"]
        result = self.sol.restoreIpAddresses(s)
        self.assertEqual(sorted(answer), sorted(result))


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8