#coding=utf-8
"""

Anagrams 

 Description
 Notes
 Testcase
 Judge
Given an array of strings, return all groups of strings that are anagrams.

 Notice

All inputs will be in lower-case

Have you met this question in a real interview? Yes
Example
Given ["lint", "intl", "inlt", "code"], return ["lint", "inlt", "intl"].

Given ["ab", "ba", "cd", "dc", "e"], return ["ab", "ba", "cd", "dc"].

Challenge 
What is Anagram?
- Two strings are anagram if they can be the same after change the order of characters.

Tags 
Hash Table String Uber Facebook
Related Problems 
Easy Strings Homomorphism 30 %
Easy Substring Anagrams 25 %
Medium Anagram (Map Reduce) 42 %
Easy Two Strings Are Anagrams



"""


import unittest


class Solution(object):
    def anagrams_ref(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        for word in strs:
            sortedword = ''.join(sorted(word))
            dict[sortedword] = [word] if sortedword not in dict else dict[sortedword] + [word]
        res = []
        for item in dict:
            if len(dict[item]) >= 2:
                res += dict[item]
        return res

    def anagrams(self, strs):
        if not strs:
            return []
        groups = {}
        for anag in strs:
            # key = sorted(anag) # TypeError: unhashable type: 'list'
            key = "".join(sorted(anag))
            # tmp = groups.get(key, [])
            # tmp.append(anag)
            # groups[key] = tmp
            # groups[key] = groups.get(key, []).append(anag)  #AttributeError: 'NoneType' object has no attribute 'append'
            groups[key] = groups.get(key, []) + [anag]
            # following part to output the result
        result = []
        for key, val in groups.items():
            if len(val) > 1:
                result.extend(val)
        return result
        result = []
        for key, val in groups.items():
            if len(val)>1:
                result.extend(val)
        return result




class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        input = ["",""]
        answer = ["",""
        ]
        result = self.sol.anagrams(input)
        self.assertEqual(answer.sort(), result.sort())

    def test_case2(self):
        input = ["lint", "intl", "inlt", "code"]
        answer = ["lint", "inlt", "intl"]
        result = self.sol.anagrams(input)
        self.assertEqual(answer.sort(), result.sort())

    def test_case3(self):
        input = ["ab", "ba", "cd", "dc", "e"]
        answer = ["ab", "ba", "cd", "dc"]
        result = self.sol.anagrams(input)
        self.assertEqual(answer.sort(), result.sort())

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8


"""

Java beat 100%!!! use prime number
public static List<List<String>> groupAnagrams(String[] strs) { 
   int[] prime = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103};//最多10609个z
    
            List<List<String>> res = new ArrayList<>();
            HashMap<Integer, Integer> map = new HashMap<>();
            for (String s : strs) {
                int key = 1;
                for (char c : s.toCharArray()) {
                    key *= prime[c - 'a'];
                }
                List<String> t;
                if (map.containsKey(key)) {
                    t = res.get(map.get(key));
                } else {
                    t = new ArrayList<>();
                    res.add(t);
                    map.put(key, res.size() - 1);
                }
                t.add(s);
            }
            return res;
    }

"""