#coding=utf-8

import unittest

"""


"""



class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        state = [
            {'sign': 1, 'digit': 2, 'dot': 3},  # 0
            {'dot': 3, 'digit': 2},  # 1
            {'digit': 2, 'e': 5, 'dot': 4},  # 2
            {'digit': 4},  # 3
            {'e': 5, 'digit': 4},  # 4
            {'sign': 7, 'digit': 6},  # 5
            {'digit': 6},  # 6
            {'digit': 6},  # 7

        ]
        current_state = 0
        s = s.strip()
        for char in s:
            if char in ['+', '-']:
                label = 'sign'
            elif '0' <= char <= '9':
                label = 'digit'
            elif char == '.':
                label = 'dot'
            elif char == 'e':
                label = 'e'
            else:
                return False
            next_state = state[current_state].get(label, -1)
            if next_state == -1:
                return False
            current_state = next_state
        if str(current_state) in ['2', '4', '6']:
            return True
        return False


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


"""

A simple solution in Python based on DFA
I was asked in the interview of linkedIn, writing it directly can be extremely complicated, for there are many special cases we have to deal with, and the code I wrote was messy. Then I failed to pass the interview.

Here's a clear solution. With DFA we can easily get our idea into shape and then debug, and the source code is clear and simple.

class Solution(object):
  def isNumber(self, s):

      #define a DFA
      state = [{}, 
              {'blank': 1, 'sign': 2, 'digit':3, '.':4}, 
              {'digit':3, '.':4},
              {'digit':3, '.':5, 'e':6, 'blank':9},
              {'digit':5},
              {'digit':5, 'e':6, 'blank':9},
              {'sign':7, 'digit':8},
              {'digit':8},
              {'digit':8, 'blank':9},
              {'blank':9}]
      currentState = 1
      for c in s:
          if c >= '0' and c <= '9':
              c = 'digit'
          if c == ' ':
              c = 'blank'
          if c in ['+', '-']:
              c = 'sign'
          if c not in state[currentState].keys():
              return False
          currentState = state[currentState][c]
      if currentState not in [3,5,8,9]:
          return False
      return True


==========================================================================================


All we need is to have a couple of flags so we can process the string in linear time:

public boolean isNumber(String s) {
    s = s.trim();
    
    boolean pointSeen = false;
    boolean eSeen = false;
    boolean numberSeen = false;
    boolean numberAfterE = true;
    for(int i=0; i<s.length(); i++) {
        if('0' <= s.charAt(i) && s.charAt(i) <= '9') {
            numberSeen = true;
            numberAfterE = true;
        } else if(s.charAt(i) == '.') {
            if(eSeen || pointSeen) {
                return false;
            }
            pointSeen = true;
        } else if(s.charAt(i) == 'e') {
            if(eSeen || !numberSeen) {
                return false;
            }
            numberAfterE = false;
            eSeen = true;
        } else if(s.charAt(i) == '-' || s.charAt(i) == '+') {
            if(i != 0 && s.charAt(i-1) != 'e') {
                return false;
            }
        } else {
            return false;
        }
    }
    
    return numberSeen && numberAfterE;
}
We start with trimming.

If we see [0-9] we reset the number flags.
We can only see . if we didn't see e or ..
We can only see e if we didn't see e but we did see a number. We reset numberAfterE flag.
We can only see + and - in the beginning and after an e
any other character break the validation.
At the and it is only valid if there was at least 1 number and if we did see an e then a number after it as well.

So basically the number should match this regular expression:

[-+]?(([0-9]+(.[0-9]*)?)|.[0-9]+)(e[-+]?[0-9]+)?

"""
#-*- coding:utf-8 -*-
