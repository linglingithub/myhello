#coding=utf-8
"""

49. Group Anagrams

Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.

Subscribe to see which companies asked this question

Hide Tags Hash Table String
Hide Similar Problems (E) Valid Anagram (E) Group Shifted Strings


"""


import unittest


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []
        groups = {}
        for anag in strs:
            # key = sorted(anag) # TypeError: unhashable type: 'list'
            key = "".join(sorted(anag))
            tmp = groups.get(key, [])
            tmp.append(anag)
            groups[key] = tmp
            # groups[key] = groups.get(key, []).append(anag)  #AttributeError: 'NoneType' object has no attribute 'append'
        return groups.values()

class Solution1(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if strs is None or len(strs)==0:
            return []
        word_map = {}
        for word in strs:
            sortedword = "".join(sorted(word))
            if sortedword in word_map:
                word_map[sortedword].append(word)
            else:
                word_map[sortedword] = [word]
        return word_map.values()


    def anagrams_ref(self, strs):
        dict = {}
        for word in strs:
            sortedword = ''.join(sorted(word))
            dict[sortedword] = [word] if sortedword not in dict else dict[sortedword] + [word]
        res = []
        for item in dict:
            if len(dict[item]) >= 2:
                res += dict[item]
        return res


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        input = ["eat", "tea", "tan", "ate", "nat", "bat"]
        answer = [
          ["ate", "eat","tea"],
          ["nat","tan"],
          ["bat"]
        ]
        result = self.sol.groupAnagrams(input)
        self.assertEqual(answer.sort(), result.sort())


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-
#coding=utf-8


"""

Given an array of strings, return all groups of strings that are anagrams.

Analysis

An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or 
phrase, using all the original letters exactly once; for example, Torchwood can be rearranged into Doctor Who.

If two strings are anagram to each other, their sorted sequence is the same.

Updated on 5/1/2016.

Java Solution

public List<List<String>> groupAnagrams(String[] strs) {
    List<List<String>> result = new ArrayList<List<String>>();
 
    HashMap<String, ArrayList<String>> map = new HashMap<String, ArrayList<String>>();
    for(String str: strs){
        char[] arr = new char[26];
        for(int i=0; i<str.length(); i++){
            arr[str.charAt(i)-'a']++;
        }
        String ns = new String(arr);
 
        if(map.containsKey(ns)){
            map.get(ns).add(str);
        }else{
            ArrayList<String> al = new ArrayList<String>();
            al.add(str);
            map.put(ns, al);
        }
    }
 
    result.addAll(map.values());
 
    return result;
}
Time Complexity

If the average length of verbs is m and array length is n, then the time is O(n*m).

=====================================================================================================

Java beat 100%!!! use prime number
public static List<List<String>> groupAnagrams(String[] strs) { 
   int[] prime = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103};
   //最多10609个z
    
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