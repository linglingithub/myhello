"""
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

For example,

add(1); add(3); add(5);
find(4) -> true
find(7) -> false

"""

import unittest

class TwoSum(object):
    def __init__(self):
        self.vals = {}

    def add(self, number):
        self.vals[number] = self.vals.get(number, 0) + 1

    def find(self, target):
        for key in self.vals.keys():
            if self.vals.get(target - key) > 0 and key != target - key or key == target - key and self.vals.get(key) > 1:
                return True
        return False


class SolutionTestor(unittest.TestCase):
    def setUp(self):
        self.sol = TwoSum()
        self.sol.add(1)
        self.sol.add(3)
        self.sol.add(5)

    def test_case1(self):
        answer = True
        result = self.sol.find(4)
        self.assertEqual(answer, result)

    def test_case2(self):
        answer = False
        result = self.sol.find(7)
        self.assertEqual(answer, result)


def main():
    test_suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTestor)
    unittest.TextTestRunner(verbosity=2).run(test_suite)


if __name__ == '__main__':
    main()

