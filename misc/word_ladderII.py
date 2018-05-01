#coding=utf-8
"""

126. Word Ladder II

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from
beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
UPDATE (2017/1/20):
The wordList parameter had been changed to a list of strings (instead of a set of strings). Please reload the code
definition to get the latest changes.

Subscribe to see which companies asked this question.

Hide Tags Array Backtracking Breadth-first Search String

Hard

"""

import unittest

from collections import defaultdict, deque

class Solution:  # self, AC, ~75%
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if endWord not in wordList:
            return []  # !!! not 0
        if beginWord == endWord:
            return [endWord]
        word_pattern = self.process_words(wordList, len(beginWord))  # dict like {"_ot": ["hot", "dot"]}
        visited = {beginWord: None} # dict like {"dot": hot (the previous step, i.e. the parent)}
        queue = deque()
        queue.append(beginWord)
        matches = []  # show if there is matches (endWord)
        self.helper(word_pattern, endWord, queue, visited, matches, len(beginWord))
        # check level by level, stop at and finish the first level of finding matches
        result = []
        for match in matches:
            self.process_path(visited, match, [endWord, match], result)
        return result

    def process_words(self, wordList, wordlen):
        wordList = set(wordList)
        word_pattern = defaultdict(list)
        idx_tuples = [x for x in zip(range(wordlen), range(1, wordlen + 1))]
        for word in wordList:
            for i, j in idx_tuples:
                tmp = word[:i] + "_" + word[j:]
                word_pattern[tmp].append(word)
        return word_pattern

    def helper(self, word_pattern, endWord, queue, visited, matches, wordlen):
        idx_tuples = [x for x in zip(range(wordlen), range(1, wordlen + 1))]
        found = False   # flag to check if the endWord was found
        while queue and not found:
            level_size = len(queue)
            level_visit = {}
            for _ in range(level_size):
                cur = queue.popleft()
                for i, j in idx_tuples:
                    pattern = cur[:i] + "_" + cur[j:]
                    for nei in word_pattern[pattern]:
                        if nei == endWord:
                            found = True   # if found
                            if cur not in matches:  # otherwise duplicate in case 2
                                matches.append(cur)
                            break # the cur word loop, but current level candidate will continue checking
                        elif not found:
                            # havn't found matches, continue generating next level candidate
                            # if found, no need to expand next level
                            if nei not in visited:
                                if nei not in level_visit:
                                    level_visit[nei] = [cur]
                                elif cur not in level_visit[nei]:  # need to check level_visit[nei]'s val list duplicate or not
                                    level_visit[nei].append(cur)
                                queue.append(nei)
            visited.update(level_visit)

    def process_path(self, visited, node, path, result): # should consider multiple prev situation
        if not node or not visited[node]:
            tmp = [x for x in reversed(path)]
            result.append(tmp)
            return
        tmp_list = visited[node]
        # print(tmp_list)
        for nnode in tmp_list:
            self.process_path(visited, nnode, path + [nnode], result)


class Solution_Wcase2:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if endWord not in wordList:
            return []  # !!! not 0
        if beginWord == endWord:
            return [endWord]
        word_pattern = self.process_words(wordList, len(beginWord))  # dict like {"_ot": ["hot", "dot"]}
        visited = {beginWord: None} # dict like {"dot": hot (the previous step, i.e. the parent)}
        queue = deque()
        queue.append(beginWord)
        matches = []  # show if there is matches (endWord)
        self.helper(word_pattern, endWord, queue, visited, matches, len(beginWord))
        # check level by level, stop at and finish the first level of finding matches
        result = self.process_path(visited, matches, endWord)
        return result

    def process_words(self, wordList, wordlen):
        wordList = set(wordList)
        word_pattern = defaultdict(list)
        idx_tuples = [x for x in zip(range(wordlen), range(1, wordlen + 1))]
        for word in wordList:
            for i, j in idx_tuples:
                tmp = word[:i] + "_" + word[j:]
                word_pattern[tmp].append(word)
        return word_pattern

    def helper(self, word_pattern, endWord, queue, visited, matches, wordlen):
        idx_tuples = [x for x in zip(range(wordlen), range(1, wordlen + 1))]
        found = False   # flag to check if the endWord was found
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                cur = queue.popleft()
                for i, j in idx_tuples:
                    pattern = cur[:i] + "_" + cur[j:]
                    for nei in word_pattern[pattern]:
                        if nei == endWord:
                            found = True   # if found
                            matches.append(cur)
                            break # the cur word loop, but current level candidate will continue checking
                        elif not found:
                            # havn't found matches, continue generating next level candidate
                            # if found, no need to expand next level
                            if nei not in visited:
                                visited[nei] = cur
                                queue.append(nei)

    def process_path(self, visited, matches, endWord): # should consider multiple prev situation
        result = []
        for word in matches:
            path = [endWord]
            node = word
            while node:
                path.append(node)
                node = visited[node]
            path.reverse()
            result.append(path)
        return result




class Solution1(object):
    def findLadders(self, beginWord, endWord, wordList): #ref, leetcode has problem with this problem
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        results = []

        from collections import defaultdict, deque
        queue = deque([[beginWord, 1]])
        visited = set([beginWord])
        neighbors = defaultdict(list)
        for word in wordList:
            for x in range(len(word)):
                token = word[:x] + '_' + word[x+1:]
                neighbors[token] += word,
        while queue:
            word, length = queue.popleft()
            if self.wordDist(word, endWord) <= 1:
                return length + 1
            for x in range(len(word)):
                token = word[:x] + '_' + word[x+1:]
                for ladder in neighbors[token]:
                    if ladder not in visited:
                        visited.add(ladder)
                        queue += [ladder, length + 1],
        return results

    def wordDist(self, wordA, wordB):
        return sum([wordA[x] != wordB[x] for x in range(len(wordA))])


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        a = 'hit'
        b = 'cog'
        wordList = ["hot","dot","dog","lot","log","cog"]
        answer =  [
            ["hit","hot","dot","dog","cog"],
            ["hit","hot","lot","log","cog"]
        ]
        result = self.sol.findLadders(a, b, wordList)
        self.assertCountEqual(sorted(answer), sorted(result))

    def test_case2(self):
        a = 'red'
        b = 'tax'
        wordList = ["ted","tex","red","tax","tad","den","rex","pee"]
        answer = [
            ["red","ted","tad","tax"],
            ["red","ted","tex","tax"],
            ["red","rex","tex","tax"]
        ]
        result = self.sol.findLadders(a, b, wordList)
        self.assertCountEqual(sorted(answer), sorted(result))

    def test_case3(self):
        a = "a"
        b = "c"
        wordList = ["a", "b", "c"]
        answer = [
            ["a", "c"]
        ]
        result = self.sol.findLadders(a, b, wordList)
        self.assertCountEqual(sorted(answer), sorted(result))

    def test_case4(self):
        a = "cet"
        b = "ism"
        wordList = [
            "kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now",
            "boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid",
            "ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip",
            "fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig",
            "fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet",
            "too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old",
            "fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip",
            "jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei",
            "wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag",
            "ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his",
            "sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie",
            "mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam",
            "new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog",
            "nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six",
            "ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat",
            "sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw",
            "vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig",
            "rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir",
            "nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos",
            "son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit",
            "fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe",
            "our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep",
            "bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen",
            "odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw",
            "nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew",
            "hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub",
            "low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir",
            "sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow",
            "sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all",
            "pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big",
            "ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she",
            "sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid",
            "gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo",
            "win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol",
            "arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin",
            "dun","pat","ten","mob"
        ]
        answer = [
            ["cet","get","gee","gte","ate","ats","its","ito","ibo","ibm","ism"],
            ["cet","cat","can","ian","inn","ins","its","ito","ibo","ibm","ism"],
            ["cet","cot","con","ion","inn","ins","its","ito","ibo","ibm","ism"]
        ]
        result = self.sol.findLadders(a, b, wordList)
        self.assertCountEqual(sorted(answer), sorted(result))

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()


"""
LeetCode中为数不多的考图的难题。尽管题目看上去像字符串匹配题，但从“shortest transformation sequence from start to end”还是能透露出
一点图论中最短路径题的味道。如何转化？

1. 将每个单词看成图的一个节点。
2. 当单词s1改变一个字符可以变成存在于字典的单词s2时，则s1与s2之间有连接。
3. 给定s1和s2，问题I转化成了求在图中从s1->s2的最短路径长度。而问题II转化为了求所有s1->s2的最短路径。

无论是求最短路径长度还是求所有最短路径，都是用BFS。在BFS中有三个关键步骤需要实现:

1. 如何找到与当前节点相邻的所有节点。
这里可以有两个策略：
(1) 遍历整个字典，将其中每个单词与当前单词比较，判断是否只差一个字符。复杂度为：n*w，n为字典中的单词数量，w为单词长度。
(2) 遍历当前单词的每个字符x，将其改变成a~z中除x外的任意一个，形成一个新的单词，在字典中判断是否存在。复杂度为：26*w，w为单词长度。
这里可以和面试官讨论两种策略的取舍。对于通常的英语单词来说，长度大多小于100，而字典中的单词数则往往是成千上万，所以策略2相对较优。

2. 如何标记一个节点已经被访问过，以避免重复访问。
可以将访问过的单词从字典中删除。

3. 一旦BFS找到目标单词，如何backtracking找回路径？

"""
#-*- coding:utf-8 -*-
