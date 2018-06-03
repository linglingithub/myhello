#coding=utf-8

import unittest

"""

383. Ransom Note
DescriptionHintsSubmissionsDiscussSolution
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function
that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

Difficulty:Easy
Total Accepted:81.3K
Total Submissions:169.9K
Contributor:LeetCode
Companies

Related Topics

Similar Questions
Stickers to Spell Word

"""



from collections import Counter

class Solution:
    """
    Assumptions:
    all data can fit into memory
    magazine data is larger than ransomNote, note as n

    Time: O(n)  --
    Space: O(n)
    """
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if not ransomNote:
            return True
        if not magazine:
            return False
        note_counter = Counter(ransomNote)
        mag_counter = Counter(magazine)
        for char in note_counter:
            if char not in mag_counter or note_counter[char] > mag_counter[char]:
                return False
        return True



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
