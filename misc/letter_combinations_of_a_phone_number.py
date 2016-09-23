"""
Letter Combinations of a Phone Number


Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.


Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.

 Backtracking String
Hide Similar Problems (M) Generate Parentheses (M) Combination Sum (E) Binary Watch


"""

import unittest


class Solution(object):
    def letterCombinations1(self, digits): # non-recursive
        """
        :type digits: str
        :rtype: List[str]
        """
        digit_dict = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
            "0": ""
        }
        result = []
        for digit in digits:
            chars = digit_dict[digit]
            tmp = []
            for char in chars:
                if len(result):
                    for one_str in result:
                        tmp.append(one_str + char)
                else:
                    tmp.append(char)
            result = tmp
        return result

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digit_dict = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
            "0": ""
        }

        def dfs(current_idx, one_str, result):
            if current_idx == len(digits):
                if len(one_str):
                    result.append(one_str)
                return
            else:
                for letter in digit_dict[digits[current_idx]]:
                    #one_str += letter # -- can not do it here, will cause wrong answer, because it changes the string when backtracking
                    dfs(current_idx+1, one_str+letter, result)

        result = []
        dfs(0, "", result)
        return result


    def letterCombinations_wrong_dfs(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digit_dict = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
            "0": ""
        }

        def dfs(current_idx, one_str, result):
            if current_idx == len(digits):
                if len(one_str):
                    result.append(one_str)
                return result # wrong, if return result here, the whole recursive will stop and return, no backtracking will be done
            else:
                for letter in digit_dict[digits[current_idx]]:
                    one_str += letter
                    return dfs(current_idx + 1, one_str, result) # can not return result this way

        result = []
        return dfs(0, "", result)






class SolutionTestor(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        digits = "23"
        answer = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].sort()
        result = self.sol.letterCombinations(digits).sort()
        self.assertEqual(answer, result)

    def test_case2(self): # =======>
        digits = ""
        answer = []
        result = self.sol.letterCombinations(digits)
        self.assertEqual(answer, result)


    def test_case3(self): # =======>
        digits = "2"
        answer = ['a','b','c'].sort()
        result = self.sol.letterCombinations(digits).sort()
        self.assertEqual(answer, result)




def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTestor)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()