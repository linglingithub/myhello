#coding=utf-8

import unittest

"""
implement put and get in hashtable

"""



class Solution(object):
    def searchInsert(self, nums):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = ["{}[]()", "{[}]}", "({[]})", "{)["]
        answer = ["YES", "NO", "YES", "NO"]
        result = self.sol.searchInsert(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""

http://kells.tj/blog/2015/04/26/pure-python-hashtable.html

################################################################################


https://github.com/calebmadrigal/algorithms-in-python/blob/master/hashtable.py


############ HashTable helper functions
def hash_function(key_str, size):
    return sum([ord(c) for c in key_str]) % size


############ HashTable class
class HashTable:
    # Hash table which uses strings for keys. Value can be any object.
    Example usage:
        ht = HashTable(10)
        ht.set('a', 1).set('b', 2).set('c', 3)
        ht['c'] = 30
    #

    def __init__(self, capacity=1000):
        # Capacity defaults to 1000.#

        self.capacity = capacity
        self.size = 0
        self._keys = []
        # Storage format: [ [ [key1, value], [key2, value] ], [ [key3, value] ] ]
        # The outmost list is the one which the hash function maps the index to. The next inner
        # Array is the list of objects in that storage cell. The 3rd level is the individual
        # item array, where the 1st item is the key, and the 2nd item is the value.
        self.data = [[] for _ in range(capacity)]

    def _find_by_key(self, key, find_result_func):
        index = hash_function(key, self.capacity)
        hash_table_cell = self.data[index]
        found_item = None
        for item in hash_table_cell:
            if item[0] == key:
                found_item = item
                break

        return find_result_func(found_item, hash_table_cell)

    def set(self, key, obj):
         #Insert object with key into hash table. If key already exists, then the object will be
        updated. Key must be a string. Returns self. #

        def find_result_func(found_item, hash_table_cell):
            if found_item:
                found_item[1] = obj
            else:
                hash_table_cell.append([key, obj])
                self.size += 1
                self._keys.append(key)

        self._find_by_key(key, find_result_func)
        return self

    def get(self, key):
        # Get object with key (key must be a string). If not found, it will raise a KeyError. #

        def find_result_func(found_item, _):
            if found_item:
                return found_item[1]
            else:
                raise KeyError(key)

        return self._find_by_key(key, find_result_func)

    def remove(self, key):
        # Remove the object associated with key from the hashtable. If found, the object will
        be returned. If not found, KeyError will be raised. #

        def find_result_func(found_item, hash_table_cell):
            if found_item:
                hash_table_cell.remove(found_item)
                self._keys.remove(key)
                self.size -= 1
                return found_item[1]
            else:
                raise KeyError(key)

        return self._find_by_key(key, find_result_func)

    ####### Python's dict interface

    def keys(self):
        return self._keys

    def __setitem__(self, key, value):
        self.set(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        return self.remove(key)

    def __repr__(self):
        return '{ ' + ', '.join([key + ':' + str(self.get(key)) for key in self._keys]) + ' }'

if __name__ == "__main__":
    # Run unit tests
    import unittest
    testsuite = unittest.TestLoader().discover('test', pattern="*hashtable*")
    unittest.TextTestRunner(verbosity=1).run(testsuite)

========================================================================================================

http://pythonfiddle.com/implementing-a-python-hash-table/

#Implement a hash table using only arrays - in python, java

class HashTable(object):

    def __init__(self):
        self.size = 100
        self.value_array = []
        self.total_entries = 0
        for i in range(100):
            self.value_array.append(None)
        
    def __str__(self):
        output_lines = []
        for item in self.value_array:
            if item != None:
                output_lines.append("Key: " + str(item[0]) + " Value: " + str(item[1]))
        return "\n".join(output_lines)
    
    def resize(self):
        new_value_array = []
        new_size = 2 * self.size
        for i in range(self.size*2):
            new_value_array.append(None)
        for i in range(self.size):
            if self.value_array[i] != None:
                self.add_internal(self.value_array[i][0], self.value_array[i][1], new_value_array, new_size, True)
        self.value_array = new_value_array
        self.size = new_size
        
        
    def probe(self, key, position):
        # does the position have this key?
        return self.value_array[position] != None and self.value_array[position][0] == key
        
    def add(self, key, value):
        self.add_internal(key, value, self.value_array, self.size)
    
    def add_internal(self, key, value, value_array, size, during_resize = False):
        if value_array[self.hash1(key)] == None:
            value_array[self.hash1(key)] = key, value
        else:
            #find the next slot
            added = False
            attempt_count = 1
            while (not added):
                newhash = (self.hash1(key) + attempt_count*self.hash2(key)) % size
                if value_array[newhash] == None:
                    value_array[newhash] = key, value
                    added = True
                else:
                    attempt_count += 1
        if not during_resize:
            self.total_entries += 1
            if self.total_entries > size/2:
                self.resize()
        
    def remove(self, key):
        print "Failure - not implemented - remove"
    
    def get(self, key):
        got_value = self.value_array[self.hash1(key)]
        if got_value == None:
            return None
        retrieved_key, retrieved_value = got_value
        if retrieved_key != key:
            found = False
            attempt_count = 1
            while (not found and attempt_count < 50):
                newhash = (self.hash1(key) + attempt_count*self.hash2(key)) % self.size
                value_at_hash = self.value_array[newhash]
                if value_at_hash != None:
                    retrieved_key, retrieved_value = value_at_hash
                    if retrieved_key == key:
                        found = True
                    attempt_count += 1
                else:
                    attempt_count += 1
        return retrieved_value
    
    def hash1(self, key):
        return id(key) % self.size
    
    def hash2(self, key):
        hashval = (id(key) + 501) % self.size
        return hashval
    

def test_hashtable():
    ht = HashTable()
    ht.add("Meo", "Smith")
    ht.add("Kaga", "Garka")
    assert ht.get("Kaga") == "Garka"
    assert ht.get("Hitler") == None
    for i in range(250):
        ht.add(i,i*i)
    for i in range(250):
        print i
        print ht.get(i)
#        assert ht.get(i) == i*i
    print ht
    print "Passed all tests"

test_hashtable()

"""

#-*- coding:utf-8 -*-
