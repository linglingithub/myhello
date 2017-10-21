"""



"""

import unittest

class Solution(object):
    def gen_parentheses(self, cnt):
        def test_recur(res, rleft, rright, path):
            if rleft == 0 and rright == 0:
                res.append(path)
                return
            else:
                if rleft <= rright and rleft > 0:
                    test_recur(res, rleft - 1, rright, path + "(")
                if rleft <= rright - 1 and rright > 0:
                    test_recur(res, rleft, rright - 1, path + ")")

        res = []
        test_recur(res, cnt, cnt, "")
        return res




    def gen_parentheses1(self, cnt):

        def test_recur(res, cnt, path, open_cnt):
            if len(path) >= cnt * 2:  # need to add this , otherwise will continue for case like "path=((),  open_cnt=1"
                if len(path) == cnt * 2 and open_cnt == 0:
                    res.append(path)
                return
            if open_cnt == 0:
                test_recur(res, cnt, path + "(", open_cnt + 1)
            elif open_cnt == cnt:
                test_recur(res, cnt, path + ")", open_cnt - 1)
            else:
                test_recur(res, cnt, path + "(", open_cnt + 1)
                test_recur(res, cnt, path + ")", open_cnt - 1)

        res = []
        test_recur(res, cnt, "", 0)
        return res



    def test_recur_wrong(res, cnt, path, open_cnt):
        if len(path) == cnt * 2 and open_cnt == 0:
            res.append("".join(path))
            return
        if open_cnt == 0:
            test_recur(res, cnt, path.append("("), open_cnt + 1)  # path.append("(") itself is None
        elif open_cnt == cnt:
            test_recur(res, cnt, path.append(")"), open_cnt - 1)
        else:
            test_recur(res, cnt, path.append("("), open_cnt + 1)
            test_recur(res, cnt, path.append(")"), open_cnt - 1)







class SolutionTestor(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        n = 1
        answer = ["()"]
        result = self.sol.gen_parentheses(n)
        self.assertEqual(sorted(answer), sorted(result))


    def test_case2(self):
        n = 2
        answer = ["()()", "(())"]
        result = self.sol.gen_parentheses(n)
        self.assertEqual(sorted(answer), sorted(result))


    def test_case3(self):
        n = 3
        answer = ["((()))", "(()())", "(())()", "()(())","()()()"]
        result = self.sol.gen_parentheses(n)
        self.assertEqual(sorted(answer), sorted(result))


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTestor)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()