# coding=utf-8

"""

Insert Delete GetRandom O(1) 

Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
Have you met this question in a real interview? Yes
Example
// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
Tags 
Twitter Hash Table Array Facebook Amazon Yelp Data Structure Design Google

"""

import unittest


class RandomizedSet(object):
    def __init__(self):
        # do initialize if necessary
        self.data = {}
        self.arr = []

    # @param {int} val Inserts a value to the set
    # Returns {bool} true if the set did not already contain the specified element or false
    def insert(self, val):
        # Write your code here
        if val in self.data:
            return False
        else:
            self.data[val] = len(self.arr)
            self.arr.append(val)
            return True

    # @param {int} val Removes a value from the set
    # Return {bool} true if the set contained the specified element or false
    def remove(self, val):
        # Write your code here
        if val in self.data:
            idx = self.data[val]
            last = self.arr.pop()
            #if idx < len(self.arr)-1: # then this also need to change, because already pop
            if idx < len(self.arr):
                #last = self.arr.pop()  # should put higher, not inside the if loop, always need to delete
                self.arr[idx] = last
                self.data[last] = idx
            del self.data[val]
            return True
        else:
            return False

    # return {int} a random number from the set
    def getRandom(self):
        # Write your code here
        import random
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()


class RandomizedSet_wrong_randomNotO1(object):
    def __init__(self):
        # do initialize if necessary
        self.data = {}

    # @param {int} val Inserts a value to the set
    # Returns {bool} true if the set did not already contain the specified element or false
    def insert(self, val):
        # Write your code here
        if val in self.data:
            return False
        else:
            self.data[val] = 1
            return True

    # @param {int} val Removes a value from the set
    # Return {bool} true if the set contained the specified element or false
    def remove(self, val):
        # Write your code here
        if val in self.data:
            del self.data[val]
            return True
        else:
            return False

    # return {int} a random number from the set
    def getRandom(self):
        # Write your code here
        import random
        return random.choice(self.data.keys())


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [1, 2, 3, 4]
        answer = [24, 12, 8, 6]
        result = self.sol.productExceptSelf(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner.run(suite)


if __name__ == '__main__':
    main()

"""




"""