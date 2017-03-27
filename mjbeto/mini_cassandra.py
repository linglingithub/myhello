#coding=utf-8

import unittest

"""
Mini Cassandra

 Description
 Notes
 Testcase
 Judge
Cassandra is a NoSQL storage. The structure has two-level keys.

Level 1: raw_key. The same as hash_key or shard_key.
Level 2: column_key.
Level 3: column_value
raw_key is used to hash and can not support range query. let's simplify this to a string.
column_key is sorted and support range query. let's simplify this to integer.
column_value is a string. you can serialize any data into a string and store it in column value.

implement the following methods:

insert(raw_key, column_key, column_value)
query(raw_key, column_start, column_end) // return a list of entries
Have you met this question in a real interview? Yes
Example
insert("google", 1, "haha")
query("google", 0, 1)
>> [（1, "haha")]

"""



"""
Definition of Column:
class Column:
    def __init__(self, key, value):
        self.key = key
        self.value = value
"""
class Column:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class MiniCassandra:

    def __init__(self):
        # initialize your data structure here.
        self.data = {}

    # @param {string} raw_key a string
    # @param {int} column_key an integer
    # @param {string} column_value a string
    # @return nothing
    def insert(self, raw_key, column_key, column_value):
        # Write your code here
        if raw_key not in self.data:
            self.data[raw_key] = {}
        self.data[raw_key][column_key] = column_value

    # @param {string} raw_key a string
    # @param {int} column_start an integer
    # @param {int} column_end an integer
    # @return {Column[]} a list of Columns
    def query(self, raw_key, column_start, column_end): # requires that the column key are sorted
        # Write your code here
        if raw_key not in self.data:
            return []
        result = [(k,v) for k, v in self.data[raw_key].items() if column_start <= k <= column_end]
        # ---> #1306ms
        result.sort(key=lambda x: x[0])
        result = [Column(x[0], x[1]) for x in result]
        # <---
        # ---> 1371ms
        # result = [Column(x[0], x[1]) for x in sorted(result, key=lambda k: k[0])]
        # <---
        return result




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = 1
        answer = 1
        result = self.sol.searchInsert(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

#jz sol: 2275ms