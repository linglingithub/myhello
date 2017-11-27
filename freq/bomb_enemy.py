#coding=utf-8

import unittest

"""
[lintcode]

553. Bomb Enemy 

 Description
 Notes
 Testcase
 Judge
Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.

 Notice

You can only put the bomb at an empty cell.

Have you met this question in a real interview? Yes
Example
Given a grid:

0 E 0 0
E 0 W E
0 E 0 0
return 3. (Placing a bomb at (1,1) kills 3 enemies)

Tags 
Dynamic Programming Google

"""



class Solution:
    """
    run 1612ms
    @param: grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
    @return: an integer, the maximum enemies you can kill using one bomb
    """
    def maxKilledEnemies(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        col_cnts = [0 for _ in range(n)]
        up_bounds = [0 for _ in range(n)]
        res = 0
        # looks like bomb can only be put on '0' place
        for i in range(m):
            row_cnt = 0
            left_bound = 0
            for j in range(n):
                if grid[i][j] == 'E':
                    row_cnt += 1
                    col_cnts[j] += 1
                elif grid[i][j] == 'W':
                    # update when hit wall, reset row_cnt, reset col_cnts[j]
                    for k in range(left_bound, j):
                        dp[i][k] = row_cnt
                    for k in range(up_bounds[j], i):
                        dp[k][j] += col_cnts[j]
                        if grid[k][j] == 'E':
                            dp[k][j] -= 1
                    row_cnt = 0
                    left_bound = j + 1    # don't forget this one
                    col_cnts[j] = 0
                    up_bounds[j] = i + 1
            # update on the end of row
            if grid[i][n-1] != 'W':
                for k in range(left_bound, n):
                    dp[i][k] = row_cnt
        # update on the end of last row
        for j in range(n):
            if grid[m - 1][j] != 'W':
                for k in range(up_bounds[j], m):
                    dp[k][j] += col_cnts[j]
                    if grid[k][j] == 'E':
                        dp[k][j] -= 1

        # res = max([max([dp[i][j] for j in range(n)]) for i in range(m)])
        # looks like bomb can only be put on '0' place  ==> case 2
        # res = max([max([dp[i][j] for j in range(n) if grid[i][j] == '0']) for i in range(m)]) ==> can't handle empty sequence
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    res = max(res, dp[i][j])
        return res


class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [
            '0E00',
            'E0WE',
            '0E00',
        ]
        answer = 3
        result = self.sol.maxKilledEnemies(nums)
        self.assertEqual(answer, result)

    def test_case2(self):   # ===> 42% cases passed, looks like bomb can only be put on '0' place
        nums = [
            'E'
        ]
        answer = 0
        result = self.sol.maxKilledEnemies(nums)
        self.assertEqual(answer, result)

    def test_case03(self):   # ===>
        nums = [
            "W00000EEEEEEEE000000WWW0WWW00W0W0WEEEE0000EW00W"
        ]
        answer = 8
        result = self.sol.maxKilledEnemies(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""

http://www.cnblogs.com/grandyang/p/5599289.html

这道题相当于一个简单的炸弹人游戏，让我想起了小时候玩的红白机的炸弹人游戏，放一个炸弹，然后爆炸后会炸出个‘十’字，上下左右的东西都炸掉了。
这道题是个简化版，字母E代表敌人，W代表墙壁，这里说明了炸弹无法炸穿墙壁。数字0表示可以放炸弹的位置，让我们找出一个放炸弹的位置可以炸死最多的
敌人。那么我最开始想出的方法是建立四个累加数组v1, v2, v3, v4，其中v1是水平方向从左到右的累加数组，v2是水平方向从右到左的累加数组，v3是竖
直方向从上到下的累加数组，v4是竖直方向从下到上的累加数组，我们建立好这个累加数组后，对于任意位置(i, j)，其可以炸死的最多敌人数就是
v1[i][j] + v2[i][j] + v3[i][j] + v4[i][j]，最后我们通过比较每个位置的累加和，就可以得到结果，参见代码如下：

 

解法一：

复制代码
class Solution {
public:
    int maxKilledEnemies(vector<vector<char>>& grid) {
        if (grid.empty() || grid[0].empty()) return 0;
        int m = grid.size(), n = grid[0].size(), res = 0;
        vector<vector<int>> v1(m, vector<int>(n, 0)), v2 = v1, v3 = v1, v4 = v1;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int t = (j == 0 || grid[i][j] == 'W') ? 0 : v1[i][j - 1];
                v1[i][j] = grid[i][j] == 'E' ? t + 1 : t;
            }
            for (int j = n - 1; j >= 0; --j) {
                int t = (j == n - 1 || grid[i][j] == 'W') ? 0 : v2[i][j + 1];
                v2[i][j] = grid[i][j] == 'E' ? t + 1 : t;
            }
        }
        for (int j = 0; j < n; ++j) {
            for (int i = 0; i < m; ++i) {
                int t = (i == 0 || grid[i][j] == 'W') ? 0 : v3[i - 1][j];
                v3[i][j] = grid[i][j] == 'E' ? t + 1 : t;
            }
            for (int i = m - 1; i >= 0; --i) {
                int t = (i == m - 1 || grid[i][j] == 'W') ? 0 : v4[i + 1][j];
                v4[i][j] = grid[i][j] == 'E' ? t + 1 : t;
            }
        }
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == '0') {
                    res = max(res, v1[i][j] + v2[i][j] + v3[i][j] + v4[i][j]);
                }
            }
        }
        return res;
    }
};
复制代码
 

我在论坛里看到了史蒂芬大神提出的另一种解法，感觉挺巧妙，就搬了过来。这种解法比较省空间，写法也比较简洁，需要一个rowCnt变量，用来记录到下一
个墙之前的敌人个数。还需要一个数组colCnt，其中colCnt[j]表示第j列到下一个墙之前的敌人个数。算法思路是遍历整个数组grid，对于一个位置
grid[i][j]，对于水平方向，如果当前位置是开头一个或者前面一个是墙壁，我们开始从当前位置往后遍历，遍历到末尾或者墙的位置停止，计算敌人个数。
对于竖直方向也是同样，如果当前位置是开头一个或者上面一个是墙壁，我们开始从当前位置向下遍历，遍历到末尾或者墙的位置停止，计算敌人个数。有了水
平方向和竖直方向敌人的个数，那么如果当前位置是0，表示可以放炸弹，我们更新结果res即可，参见代码如下：

 

解法二：

复制代码
class Solution {
public:
    int maxKilledEnemies(vector<vector<char>>& grid) {
        if (grid.empty() || grid[0].empty()) return 0;
        int m = grid.size(), n = grid[0].size(), res = 0, rowCnt, colCnt[n];
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (j == 0 || grid[i][j - 1] == 'W') {
                    rowCnt = 0;
                    for (int k = j; k < n && grid[i][k] != 'W'; ++k) {
                        rowCnt += grid[i][k] == 'E';
                    }
                }
                if (i == 0 || grid[i - 1][j] == 'W') {
                    colCnt[j] = 0;
                    for (int k = i; k < m && grid[k][j] != 'W'; ++k) {
                        colCnt[j] += grid[k][j] == 'E';
                    }
                }
                if (grid[i][j] == '0') {
                    res = max(res, rowCnt + colCnt[j]);
                }
            }
        }
        return res;
    }
};
复制代码


========================

# Time:  O(m * n)
# Space: O(m * n)

class Solution(object):
    def maxKilledEnemies(self, grid):
        result = 0
        if not grid or not grid[0]:
            return result

        down = [[0 for _ in xrange(len(grid[0]))] for _ in xrange(len(grid))]
        right = [[0 for _ in xrange(len(grid[0]))] for _ in xrange(len(grid))]
        for i in reversed(xrange(len(grid))):
            for j in reversed(xrange(len(grid[0]))):
                if grid[i][j] != 'W':
                    if i + 1 < len(grid):
                        down[i][j] = down[i + 1][j]
                    if j + 1 < len(grid[0]):
                        right[i][j] = right[i][j + 1]
                    if grid[i][j] == 'E':
                        down[i][j] += 1
                        right[i][j] += 1

        up = [0 for _ in xrange(len(grid[0]))]
        for i in xrange(len(grid)):
            left = 0
            for j in xrange(len(grid[0])):
                if grid[i][j] == 'W':
                    up[j], left = 0, 0
                elif grid[i][j] == 'E':
                    up[j] += 1
                    left += 1
                else:
                    result = max(result, left + up[j] + right[i][j] + down[i][j])

        return result

=======================

思路: 昨天(8-22)一个美国小哥同学面了这题, 要求在O(m*n)内时间解决, 所以我原来的方法虽然可以过的了测试数据, 其实是不符合要求的, 而且这篇
文章的阅读量居然已经有一千多了, 我深感抱歉, 我也无法我的所有答案就是对的, 大家参考一下, 并且欢迎指正.
正确的做法是可以在O(m*n)内做到的, 比较naive的做法是每个空位都向前后左右搜索, 但是这样的搜索包含了大量的重复搜索, 所以如何利用已经搜索过的
信息就是本题的考点了. 对于每一行来说, 我们可以在第0列或者当前位置前一列为墙的时候从第当前列开始往右搜索直到撞到墙. 对于每一列来说, 可以在
第0行的时候或者在当前行前一行为墙的时候从当前行往下搜索, 直到碰到墙为止. 这样就可以一次计算出一行直到碰到墙之前有几个敌人, 一列在没有碰到墙
之前有几个敌人. 直到当某个某位之前位置墙的时候才会重新计算. 
代码如下:
[python] view plain copy
class Solution {  
public:  
    int maxKilledEnemies(vector<vector<char>>& grid) {  
        if(grid.size()==0) return 0;  
        int row = grid.size(), col = grid[0].size(), rowHits, colHits[col], ans =0;  
        for(int i = 0; i < row; i++)  
        {  
            for(int j =0; j < col; j++)  
            {  
                if(!i || grid[i-1][j]=='W')  
                {  
                    colHits[j] = 0;  
                    for(int k = i; k < row && grid[k][j]!='W'; k++)  
                        colHits[j] += grid[k][j]=='E';  
                }  
                if(!j || grid[i][j-1]=='W')  
                {  
                    rowHits = 0;  
                    for(int k = j; k < col && grid[i][k]!='W'; k++)  
                        rowHits += grid[i][k] == 'E';  
                }  
                if(grid[i][j] == '0')  
                    ans = max(ans, colHits[j] + rowHits);  
            }  
        }  
        return ans;  
    }  
};  



"""