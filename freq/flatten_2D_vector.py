#coding=utf-8

import unittest

"""
[lock in leet, OK in lint ]

Flatten 2D Vector

Implement an iterator to flatten a 2d vector.

Example
Given 2d vector =

[
  [1,2],
  [3],
  [4,5,6]
]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].

Tags 
Airbnb Google Zenefits Twitter
Related Problems 
Medium Zigzag Iterator 43 %
Medium Flatten Nested List Iterator 28 %
Easy Flatten Binary Tree to Linked List 33 %
Easy Flatten List

====================

Implement an iterator to flatten a 2d vector.

For example,
Given 2d vector =

[
  [1,2],
  [3],
  [4,5,6]
]
 

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].

Hint:

How many variables do you need to keep track?
Two variables is all you need. Try with x and y.
Beware of empty rows. It could be the first few rows.
To write correct code, think about the invariant to maintain. What is it?
The invariant is x and y must always point to a valid point in the 2d vector. Should you maintain your invariant ahead of time or right when you need it?
Not sure? Think about how you would implement hasNext(). Which is more complex?
Common logic in two different places should be refactored into a common method.
Follow up:
As an added challenge, try to code it using only iterators in C++ or iterators in Java.

 


"""


class Vector2D(object):
    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        # Initialize your data structure here
        self._data = vec2d
        self._rid = 0
        self._cid = 0

    # @return {int} a next element
    def next(self):
        # Write your code here
        tmp = self._data[self._rid][self._cid]
        # !!! don't forget to increase the cid, rid --> no need for rid
        self._cid += 1
        # if self._cid >= len(self._data[self._rid]):
        #     self._cid = 0
        #     self._rid += 1
        # this part can be omitted here, cause hasNext will handle it
        # and a simple _cid check will not cover the empty row case
        # for a better function separation design, better just let hasNext handle it
        # and here only need to mark the increase of the _cid.
        # in the case when required to do check right after get next, just call hasNext() after the cid increase.
        return tmp

        # @return {boolean} true if it has next element

    # or false
    def hasNext(self):
        # Write your code here
        while self._rid < len(self._data):
            if self._cid < len(self._data[self._rid]):
                return True
            else:
                self._rid += 1
                self._cid = 0
        return False


        # Your Vector2D object will be instantiated and called as such:


# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())

class Vector2D1(object):
    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        # Initialize your data structure here
        from collections import deque
        self._data = deque()
        for item in vec2d:
            if isinstance(item, int):
                self._data.append(item)
            else:
                for nest_item in item:
                    self._data.append(nest_item)

    # @return {int} a next element
    def next(self):
        # Write your code here
        _tmp = self._data.popleft()
        return _tmp

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        # Write your code here
        if self._data:
            return True
        else:
            return False


# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = 1
        answer = 1
        result = self.sol.searchInsert(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

'''

example code Java using iterator


public class Vector2D {
    private Iterator<List<Integer>> outer;
    private Iterator<Integer> inner;
 
    public Vector2D(List<List<Integer>> vec2d) {
        outer = vec2d.iterator();
        inner = Collections.emptyIterator(); //inner = outer.iterator(); wrong: if outer is null, then exception
    }
 
    public int next() {
        return inner.next();
    }
 
    public boolean hasNext() {
        if (inner.hasNext()) {
            return true;
        }
        if (!outer.hasNext()) {
            return false;
        }
        inner = outer.next().iterator();
        while(!inner.hasNext() && outer.hasNext()) {
            inner = outer.next().iterator();
        }
        return inner.hasNext();
    }
}
 
/**
 * Your Vector2D object will be instantiated and called as such:
 * Vector2D i = new Vector2D(vec2d);
 * while (i.hasNext()) v[f()] = i.next();
 */



====================

这道题让我们压平一个二维向量数组，并且实现一个iterator的功能，包括next和hasNext函数，那么最简单的方法就是将二维数组按顺序先存入到一个一维
数组里，然后此时只要维护一个变量i来记录当前遍历到的位置，hasNext函数看当前坐标是否小于元素总数，next函数即为取出当前位置元素，坐标后移一
位，参见代码如下：                      

 

解法一：

复制代码
class Vector2D {
public:
    Vector2D(vector<vector<int>>& vec2d) {
        for (auto a : vec2d) {
            v.insert(v.end(), a.begin(), a.end());
        }    
    }
    int next() {
        return v[i++];
    }
    bool hasNext() {
        return i < v.size();
    }
private:
    vector<int> v;
    int i = 0;
};
复制代码
 

下面我们来看另一种解法，不直接转换为一维数组，而是维护两个变量x和y，我们将x和y初始化为0，对于hasNext函数，我们检查当前x是否小于总行数，y是否和当前行的列数相同，如果相同，说明要转到下一行，则x自增1，y初始化为0，若此时x还是小于总行数，说明下一个值可以被取出来，那么在next函数就可以直接取出行为x，列为y的数字，并将y自增1，参见代码如下：

 

解法二：

复制代码
class Vector2D {
public:
    Vector2D(vector<vector<int>>& vec2d) {
        v = vec2d;
        x = y = 0;
    }
    int next() {
        return v[x][y++];
    }
    bool hasNext() {
        while (x < v.size() && y == v[x].size()) {
            ++x; 
            y = 0;
        }
        return x < v.size();
    }    
private:
    vector<vector<int>> v;
    int x, y;
};
复制代码
 

题目中的Follow up让我们用interator来做，C++中iterator不像Java中的那么强大，自己本身并没有包含next和hasNext函数，所以我们得自己来实现，我们将x定义为行的iterator，再用个end指向二维数组的末尾，定义一个整型变量y来指向列位置，实现思路和上一种解法完全相同，只是写法略有不同，参见代码如下：

 

解法三：

复制代码
class Vector2D {
public:
    Vector2D(vector<vector<int>>& vec2d) {
        x = vec2d.begin();
        end = vec2d.end();
    }
    int next() {
        return (*x)[y++];
    }
    bool hasNext() {
        while (x != end && y == (*x).size()) {
            ++x; 
            y = 0;
        }
        return x != end;
    }
private:
    vector<vector<int>>::iterator x, end;
    int y = 0;
};
复制代码
 

'''

#-*- coding:utf-8 -*-
