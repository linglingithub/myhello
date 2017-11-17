#coding=utf-8

import unittest

"""

Input:
2d grid, with some numbers and blank space, to solve it, fill the blank places with . or #
'.': water
'#': island

constraits:
no 2*2 blocks of water
no other characters in the grid (only ., #, number), no space left
all water is connected ( up-down-left-right, not diagonally)
each connected group of islands contains exactly one number (say n) square, and n-1 *squares


the problem is not to solve, but to check if the input is a valid solve.


Output:
True or False ( if the puzzle is valid )

"""

from collections import deque


class Solution(object):
    def check_nurikabe(self, nums):
        """
        BASIC idea: iterate through nums to check the board if the contraints are met.
        maintain a visited map to avoid repeated visit.
        
        questions:
        'no 2*2 blocks of water anywhere': is 2*3 also invalid, here I assume 2*2 and bigger are invalid?
        ''
        
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or not nums[0]:
            return True
        m, n = len(nums), len(nums[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        found_water = False
        for i in range(m):
            for j in range(n):
                if visited[i][j]:
                    continue
                char = nums[i][j]
                if char == ".":
                    if found_water:
                        return False
                    else:
                        valid = self.search_and_check_water(nums, i, j, visited)
                        if not valid:
                            return False
                        found_water = True
                elif char == "#" or ord('1') <= ord(char) <= ord('9'):
                    valid = self.search_and_check_island(nums, i, j, visited)
                    if not valid:
                        return False
                else:
                    # other chars are invalid
                    return False
        return True

    def search_and_check_water(self, nums, i, j, visited):
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        queue = deque()
        queue.append((i, j))
        while queue:
            x, y = queue.popleft()
            visited[x][y] = True
            # check water area
            area = 0
            for a in range(2):
                for b in range(2):
                    if nums[i+a][j+b] == '.':
                        area += 1
            if area == 4:
                return False
            # expand water
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < len(nums) and 0 <= ny < len(nums[0]) and not visited[nx][ny] and nums[nx][ny] == ".":
                    queue.append((nx, ny))
        return True

    def search_and_check_island(self, nums, i, j, visited):
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        queue = deque()
        queue.append((i, j))
        num_found = False
        island_num = -1
        island_size = 0
        while queue:
            x, y = queue.popleft()
            visited[x][y] = True
            island_size += 1
            if nums[x][y] == "#":
                pass
            else:
                if num_found:
                    return False
                island_num = int(nums[x][y])
                num_found = True
            # check island size
            if num_found and island_size > island_num:
                return False
            # expand island
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < len(nums) and 0 <= ny < len(nums[0]) and not visited[nx][ny] \
                    and (nums[nx][ny] == "." or ord('1') <= ord(nums[nx][ny]) <= ord('9')):
                    queue.append((nx, ny))

        return True




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()


    def test_case1(self):
        nums = [
            '.#2.1',
            '.....',
            '#2.#.',
            '...2.',
            '#2..1',
        ]
        answer = True
        result = self.sol.check_nurikabe(nums)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [
            '..2.1',
            '..#..',
            '#2.#.',
            '...2.',
            '#2..1',
        ]
        answer = False  # there is 2*2 water, and the water group is disconnected with other water
        result = self.sol.check_nurikabe(nums)
        self.assertEqual(answer, result)



def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
