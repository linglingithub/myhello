import unittest

class Solution:
    def find_left_most_column_of_one(self, matrix):
        """
        Start from right-up corner,
        Time: O(m + n)
        :param matrix:
        :return:
        """
        if not matrix or not matrix[0]:
            return -1
        m, n = len(matrix), len(matrix[0])
        x, y = 0, n - 1
        has_one = False
        while x < m and y >= 0:
            if matrix[x][y] == 1:
                has_one = True
                y -= 1
                continue
            x += 1
        return y + 1 if has_one else -1

    def find_left_most_column_of_one1(self, matrix):
        """
        binary search on column
        time: O(mlogn)
        :param matrix:
        :return:
        """
        if not matrix or not matrix[0]:
            return -1
        m, n = len(matrix), len(matrix[0])
        l, r = 0, n - 1
        col = n
        while l <= r:
            m = l + (r - l) // 2
            has_one = self.__check_col(matrix, m)
            if has_one:
                col = m
                r = m - 1
            else:
                l = m + 1
        return col if 0 <= col < n else -1

    def __check_col(self, matrix, col):
        for i in range(len(matrix)):
            if matrix[i][col] == 1:
                return True
        return False

class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        matrix = [[0, 0, 0, 1], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 1, 1]]
        answer = 0
        result = self.sol.find_left_most_column_of_one(matrix)
        self.assertEqual(answer, result)

    def test_case2(self):
        matrix = [[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]
        answer = 3
        result = self.sol.find_left_most_column_of_one(matrix)
        self.assertEqual(answer, result)

    def test_case3(self):
        matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        answer = -1
        result = self.sol.find_left_most_column_of_one(matrix)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

