#coding=utf-8

import unittest

"""
526. Load Balancer 

 Description
 Notes
 Testcase
 Judge
Implement a load balancer for web servers. It provide the following functionality:

Add a new server to the cluster => add(server_id).
Remove a bad server from the cluster => remove(server_id).
Pick a server in the cluster randomly with equal probability => pick().
Have you met this question in a real interview? Yes
Example
At beginning, the cluster is empty => {}.

add(1)
add(2)
add(3)
pick()
>> 1         // the return value is random, it can be either 1, 2, or 3.
pick()
>> 2
pick()
>> 1
pick()
>> 3
remove(1)
pick()
>> 2
pick()
>> 3
pick()
>> 3

Tags 
Array Hash Table Google

"""


import random
class LoadBalancer:
    def __init__(self):
        # do intialization if necessary
        self._arr = []
        self._id_pos_dict = {}

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """
    def add(self, server_id):
        # write your code here
        self._arr.append(server_id)
        self._id_pos_dict[server_id] = len(self._arr)-1

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """
    def remove(self, server_id):
        # write your code here
        if server_id not in self._id_pos_dict:
            return
        pos = self._id_pos_dict[server_id]
        del self._id_pos_dict[server_id]
        last_server = self._arr[-1]
        self._arr[pos] = last_server
        self._id_pos_dict[last_server] = pos
        self._arr.pop()

    """
    @return: pick a server in the cluster randomly with equal probability
    """
    def pick(self):
        # write your code here
        pos = random.randint(0, len(self._arr)-1)
        return self._arr[pos]


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
