import unittest

class Solution:
    def remove_repeat(self, arr):
        """
        in-place remove repeated elements (int array)
        :param arr: sorted int array
        :return: int , the good length of array, [0, int) is the good area of array
        """
        if not arr:
            return 0
        slow, fast = 0, 1 # [0, slow] is the good array
        for fast in range(1, len(arr)):
            if arr[fast] != arr[slow]:
                slow += 1
                arr[slow] = arr[fast]
        return slow + 1


    def repeat_at_most_two(self, arr):
        """
        in-place remove repeated elements (int array)
        :param arr: sorted int array
        :return: int , the good length of array, [0, int) is the good area of array
        """
        if not arr:
            return 0
        if len(arr) <= 2:
            return 2
        slow, fast = 1, 1 # [0, slow] is the good array
        for fast in range(2, len(arr)):
            if arr[fast] != arr[slow - 1]:
                slow += 1
                arr[slow] = arr[fast]
        return slow + 1


    # TODO
    def repeat_at_most_k(self, arr, k):
        """
        [1, 2,2,1,3,3,4] => []
        in-place remove repeated elements (int array)
        :param arr: sorted int array
        :return: int , the good length of array, [0, int) is the good area of array
        """
        if not arr:
            return 0
        if len(arr) <= 2:
            return 2
        slow = k - 1 # [0, slow] is the good array
        for fast in range(k, len(arr)):
            if arr[fast] != arr[slow - (k - 1)]:
                slow += 1
                arr[slow] = arr[fast]
        return slow + 1


    def no_repeat(self, arr):
        if not arr:
            return 0
        slow = 0 # [0, slow] is the good array
        repeated = False
        fast = 0
        while fast < len(arr):
            if slow == 0 or not repeated:
                arr[slow] = arr[fast]



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
