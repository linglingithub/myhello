#coding=utf-8

import unittest

"""

Build Post Office

Given a 2D grid, each cell is either an house 1 or empty 0 (the number zero, one), find the place to build a post 
office, the distance that post office to all the house sum is smallest. Return the smallest distance. Return -1 if it is
 not possible.

 Notice

You can pass through house and empty.
You only build post office on an empty.
Have you met this question in a real interview? Yes
Example
Given a grid:

0 1 0 0
1 0 1 1
0 1 0 0
return 6. (Placing a post office at (1,1), the distance that post office to all the house sum is smallest.)

Tags 
Binary Search Sort
Related Problems 
Hard Build Post Office II

Hard

"""



class Solution:
    # @param {int[][]} grid a 2D grid
    # @return {int} an integer

    def shortestDistance(self, grid):  # according to ref idea, cal prefix_cnt_sum and prefix_dist_sum and post_ parts
        if not grid or not grid[0]:
            return -1
        if not self.has_empty(grid):
            return -1
        row, col = len(grid), len(grid[0])

        # get how many houses in each row, col
        row_sum = [0 for _ in range(row)]
        col_sum = [0 for _ in range(col)]
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    row_sum[i] += 1
                    col_sum[j] += 1

        # get distance sum of all houses to each row, col
        dist_sum_row = [0 for _ in range(row)]
        dist_sum_col = [0 for _ in range(col)]
        self.get_dist_sum(row_sum, dist_sum_row, row)
        self.get_dist_sum(col_sum, dist_sum_col, col)

        # find the minimum dist sum (col and row) of possible best post office
        import sys
        res = sys.maxint
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    tmp = dist_sum_row[i] + dist_sum_col[j]
                    if tmp < res:
                        res = tmp
        return res if res != sys.maxint else -1

    def get_dist_sum(self, cnt_sum, dist_sum, k):
        # find the prefix sum, from left
        prefix_cnt_sum = [cnt_sum[i] for i in range(k)]
        prefix_dist_sum = [0 for _ in range(k)]
        for i in range(1, k):
            prefix_cnt_sum[i] += prefix_cnt_sum[i-1]
        for i in range(1, k):
            prefix_dist_sum[i] = prefix_dist_sum[i-1] + prefix_cnt_sum[i-1]

        # find the postfix sum, from right
        post_cnt_sum = [cnt_sum[i] for i in range(k)]
        post_dist_sum = [0 for _ in range(k)]
        for i in range(k-2, -1, -1):
            post_cnt_sum[i] += post_cnt_sum[i+1]
        for i in range(k-2, -1, -1):
            post_dist_sum[i] = post_dist_sum[i+1] + post_cnt_sum[i+1]

        # get the total dist sum into dist_sum, then reutrn
        for i in range(k):
            dist_sum[i] = prefix_dist_sum[i] + post_dist_sum[i]

    def has_empty(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    return True
        return False


    #=============================================

    def shortestDistance_self_TLE(self, grid):  # TLE, 93% cases passed
        # Write your code here
        if not grid or not grid[0]:
            return -1
        m, n = len(grid), len(grid[0])
        houses = []
        emptys = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    emptys.append((i,j))
                else:
                    houses.append((i,j))

        result = None
        for pos in emptys:
            dis = 0
            for house in houses:
                dis += abs(pos[0]-house[0]) + abs(pos[1]-house[1])
            result = min(result, dis) if result is not None else dis
        return result





class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [
            [0, 1, 0, 0],
            [1, 0, 1, 1],
            [0, 1, 0, 0]
        ]
        answer = 6  # [1, 1]
        result = self.sol.shortestDistance(nums)
        self.assertEqual(answer, result)

    def test_case2(self):  # TLE, local runs 1h2m +, and wrong output as 1600040000
        from util.ini_file_util import IniFileUtil
        params = IniFileUtil.read_into_dict("build_post_office_case2.ini")
        nums = IniFileUtil.string_to_int_list_list(params.get("grid"))
        #answer = int(params.get("answer")) # 16000000
        answer = 1600040000
        result = self.sol.shortestDistance(nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-


"""

from jiuzhang
c++, use prefix sum idea, runs quickly

   int shortestDistance(vector<vector<int>>& grid) {
        // Write your code here
        int row = grid.size(), column = grid[0].size();
        if(row == 0 || column == 0 || !haveZero(grid, row, column)) {
            return -1;
        }

        vector<int> rowSum(row);
        vector<int> columnSum(column);
        for(int i = 0; i < row; i++)
            for(int j = 0; j < column; j++)
                if (grid[i][j] == 1) {
                    rowSum[i]++;
                    columnSum[j]++;
                }

        vector<int> costRow(row);
        vector<int> costColumn(column);
        getSumDistance(rowSum,row,costRow);
        getSumDistance(columnSum,column,costColumn);

        int cost = INT_MAX;
        for(int i = 0; i < row; i++)
            for(int j = 0; j < column; j++)
                if(grid[i][j] == 0 && cost > costRow[i] + costColumn[j]) {
                    cost = costRow[i] + costColumn[j];
                }
        return cost;
    }

    void getSumDistance(vector<int>& a, int n, vector<int>& cost) {
        vector<int> prefixSum1(n);
        vector<int> prefixSum2(n);
    	/*
    	第一阶段，处理前缀。
    	prefixSum1记录数组 a 的前缀和，即:prefixSum1[i]=a[0]+a[1]+..+a[i].
    	prefixSum2记录数组 prefixSum1 前缀和，prefixSum2即为前 i 个点到第 i 个点的代价和。
    	*/
    	prefixSum1[0] = a[0];
    	for(int i = 1; i < n; i++) {
    		prefixSum1[i] = prefixSum1[i - 1] + a[i];
    	}
    	prefixSum2[0] = 0;
    	for(int i = 1; i < n; i++) {
    		prefixSum2[i] = prefixSum2[i - 1] + prefixSum1[i - 1];
     	}

     	for(int i = 0; i < n; i++) {
     		cost[i] = prefixSum2[i];
     	}

    	/*
    	第二阶段，处理后缀。
    	prefixSum1记录数组 a 的后缀和，即:prefixSum1[i]=a[n-1]+a[n-2]+..+a[i].
    	prefixSum2记录数组 prefixSum1 的后缀和，prefixSum2即为 i 之后的点到第 i 个点的代价和。
    	*/
    	prefixSum1[n - 1] = a[n - 1];
    	for(int i = n - 2; i >= 0; i--) {
    		prefixSum1[i] = prefixSum1[i + 1] + a[i];
    	}
    	prefixSum2[n - 1] = 0;
    	for(int i = n - 2; i >= 0; i--) {
    		prefixSum2[i] = prefixSum2[i + 1] + prefixSum1[i + 1];
     	}

     	for(int i = 0; i < n; i++) {
     		cost[i] += prefixSum2[i];
     	}

     	/*
     	cost[i] 即为a数组中所有点到第 i 点的代价和
     	*/
    }

    bool haveZero(vector<vector<int>>& grid, int row, int column) {
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < column; j++) {
                if (grid[i][j] == 0) {
                    return true;
                }
            }
        }
        return false;
    }

=======
c++, TLE with 99% cases passed

Idea: 
先考虑对于一维数组，计算数x到各个数值的距离
for example: A = [1， 2, 5, 4，6]
x = 3时： dis(A, 3) = ｜1 － 3｜＋ |2 - 3| + |4 - 3| + |5 - 3| + |6 - 3|
优化方法是：
1. 先排序A
2. 二分搜索找到3 应该插入的位置： A： ［1， 2， 4 ， 5， 6］，二分搜索得知3应该插入到index = 2 的位置
3. 对于A中位于index = 2之前的数，它们到3的距离是：
  smallPartDis = （3 －1） ＋ （3 － 2） ＝ 3 ＊ 2 － （1 ＋ 2）= 3 * id - (1 +  2)

对于A中位于index = 2之后的数，它们到3的距离是：
 largePartDis = （4 －3） ＋ （5 － 3） ＋ （6 － 3）＝ （4 ＋ 5 ＋ 6） － 3 ＊ 3  
  = (4 ＋ 5 ＋ 6) - 3 * (A.size() - id)

4. 为方便计算，我们算出A的prefix sum, 初始化preSum size 为A.size() + 1, preSum[0] = 0
其中，prefixSum[i]记录范围 [0,i] 之间点的个数。

这样： 
smallPartDis ＝ 3 ＊ 2 － preSum[2]
largePartDis = preSum.back() - preSum[id] - 3 *  (A.size() - id)

对于二维数组, (x, y) 到各个post office的距离是：
dis = |x1 - x| + |y1 - y| + |x2 - x| + |y2 - y| + |x3 - x| + |y3 - y|
可以转化为两个对于x 和y的一维数组：
dis = （|x1 - x| + + |x2 - x| ＋ |x3 - x|） +  （|y1 - y|  ＋ |y2 - y| +  |y3 - y|）


int shortestDistance(vector<vector<int>>& grid) {
        // Write your code here
        if(grid.empty())
            return -1;
        vector<int> PosX, PosY;
        vector<pair<int, int>> emptyPlace;
        int m = grid.size(), n = grid[0].size();
       //find all post office positions and empty place 
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(grid[i][j] == 1){
                    PosX.push_back(i);
                    PosY.push_back(j);
                }
                else
                    emptyPlace.push_back(pair<int, int>(i, j));
            }
        }
        //must sort PosX and PosY  
        sort(PosX.begin(), PosX.end());
        sort(PosY.begin(), PosY.end());
        int postOfficeCnt = PosX.size();
        vector<int> preSumX(postOfficeCnt + 1, 0);
        vector<int> preSumY(postOfficeCnt + 1, 0);
        //pre-processing: compute prefix sum for x and y coordinations
        for(int i = 0; i < postOfficeCnt; i++){
            preSumX[i + 1] = preSumX[i] + PosX[i];
            preSumY[i + 1] = preSumY[i] + PosY[i];
        }
        
        int result = INT_MAX;
        for(auto p: emptyPlace){
            int x = p.first;
            int y = p.second;
            //get distance on x and y direction separately. 用一维数组方法分别计算
            int dis = help(x, PosX, preSumX) + help(y, PosY, preSumY);
            result = min(dis, result);
        }
        return result == INT_MAX ? -1 : result;
    }
    
    int help(int x, vector<int> &position, vector<int> & preSum){
        int id = findPlace(x, position); //find the place where x should be inserted in position
        int dis = x * id - preSum[id];
        dis += preSum.back() - preSum[id] - ((int)position.size() - id) * x;
        return dis;
    }

     //binary search to find the correct index for value v in a sorted array
    int findPlace(int v, vector<int> &position){
        int left = 0, right = position.size() - 1;
        while(left + 1 < right){
            int mid = (left + right) / 2;
            if(position[mid] >= v)
                right = mid;
            else
                left = mid;
        }
        if(position[left] >= v)  //can be equal 
            return left;
        if(position[right] >= v) //can be equal 
            return right;
        return right + 1;
    }



========================================================================================================================

http://blog.hyoung.me/cn/2017/02/build-post-office/

在该题设中，因为房子并不会充当一个阻碍物，所以并不需要用 BFS 等算法来计算最短路径，简单地计算两个格子之间在网格上的曼哈顿距离
（Manhattan distance）就好了，即

d(P,Q)=|P.x−Q.x|+|P.y−Q.y|
最先想到的就是暴力算法：穷举网格上的每一个空地，并计算所有房子到它的距离，最后取最小的一个即可。实现起来就是几个嵌套循环，就此略过。最糟糕的
情况下时间复杂度为

O(m2n2)。

如果我们进一步观察，可以发现，若我们在同一行上移动，所有房子(H）到该行（r）的垂直距离（Y 轴方向）不变，其和也因此不变，即 

∑abs(H(i).y−r) 不变。同理，对于每一列也是如此。在同一列上移动，所有房子到该列的水平距离之和也不变。

充分利用上面的观察，我们就可以提出一个更好的算法，即先算出所有房子到每一行的距离之和以及每一列的距离之和，最后在网格上就可以很快的算出所有房
子到某点的距离之和了。

想要算出所有房子到每一行或每一列的距离之和，我们可以进一步抽象，把问题转换成一维上的问题。以到每一行的距离之和为例。首先很直观就可以发现，对
于任意两行上的点而言，其垂直距离都是固定不变的。于是我们可以进行水平方向的压缩（不需要水平坐标的信息了），即统计出每一行上的房子数目。而后，
问题就变成了，在这个一维的线上算出所有点到任意一点的距离之和。利用前缀和（prefix sum），我们可以在

O(n)的时间里解决。具体思路就是先从左边扫一遍，记录 

[0,i) 范围内的点到 
i 的距离之和，又是一个简单的动态规划了，其状态转移方程为

prefixCost[i] = prefixCost[i - 1] + prefixSum[i - 1]
其中，prefixSum[i]记录范围 [0,i] 之间点的个数。

类似的，再从右边扫一遍，记录 

(i,n−1] 范围内的点到 i 的距离之和。最后把左右结果相加即可。

整体而言，该算法的时间复杂度为
O(mn)。具体代码实现如下

int shortestDistance(vector<vector<int>>& grid) {
   int row = grid.size();
   if (row == 0)
       return -1;
   int col = grid[0].size();
   if (col == 0)
       return -1;
   
   vector<int> rowSum(row, 0);
   vector<int> colSum(col, 0);
   for (int i = 0; i < row; ++i)
       for (int j = 0; j < col; ++j)
           if (grid[i][j] == 1) {
               rowSum[i]++;
               colSum[j]++;
           }
   
   vector<int> rowCost(row, 0);
   vector<int> colCost(col, 0);
   calculateCost(rowSum, row, rowCost);
   calculateCost(colSum, col, colCost);
   
   int minCost = INT_MAX;
   for (int i = 0; i < row; ++i)
       for (int j = 0; j < col; ++j)
           if (grid[i][j] == 0)
               minCost = min(minCost, rowCost[i] + colCost[j]);
               
   if (minCost == INT_MAX)
       return -1;
   return minCost;
}
void calculateCost(vector<int>& nums, int n, vector<int>& cost) {
   vector<int> prefixSum(n, 0);
   vector<int> prefixCost(n, 0);
   
   // calculate forward cost - from [0,i) to i
   prefixSum[0] = nums[0];
   for (int i = 1; i < n; ++i)
       prefixSum[i] = prefixSum[i - 1] + nums[i];
       
   prefixCost[0] = 0;
   for (int i = 1; i < n; ++i)
       prefixCost[i] = prefixCost[i - 1] + prefixSum[i - 1];
   
   // add up forward cost
   for (int i = 0; i < n; ++i)
       cost[i] = prefixCost[i];
   
   // calculate backward cost - from (i, n) to i
   prefixSum[n - 1] = nums[n - 1];
   for (int i = n - 2; i >= 0; --i)
       prefixSum[i] = prefixSum[i + 1] + nums[i];
       
   prefixCost[n - 1] = 0;
   for (int i = n - 2; i >= 0; --i)
       prefixCost[i] = prefixCost[i + 1] + prefixSum[i + 1];
   
   // add up backward cost
   for (int i = n - 1; i >= 0; --i)
       cost[i] += prefixCost[i];
}


"""


"""

// 方法一 
public class Solution {
    /**
     * @param grid a 2D grid
     * @return an integer
     */
    public int shortestDistance(int[][] grid) {
        // Write your code here
        int n = grid.length;
        if (n == 0)
            return -1;

        int m = grid[0].length;
        if (m == 0)
            return -1;

        List<Integer> sumx = new ArrayList<Integer>();
        List<Integer> sumy = new ArrayList<Integer>();
        List<Integer> x = new ArrayList<Integer>();
        List<Integer> y = new ArrayList<Integer>();

        int result = Integer.MAX_VALUE;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                if (grid[i][j] == 1) {
                    x.add(i);
                    y.add(j);
                }
        
        Collections.sort(x);
        Collections.sort(y);

        int total = x.size();

        sumx.add(0);
        sumy.add(0);
        for (int i = 1; i <= total; ++i) {
            sumx.add(sumx.get(i-1) + x.get(i-1));
            sumy.add(sumy.get(i-1) + y.get(i-1));
        }

        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                if (grid[i][j] == 0) {
                    int cost_x = get_cost(x, sumx, i, total);
                    int cost_y = get_cost(y, sumy, j, total);
                    if (cost_x + cost_y < result)
                        result = cost_x + cost_y;
                }

        return result;
    }

    public int get_cost(List<Integer> x, List<Integer> sum, int pos, int n) {
        if (n == 0)
            return 0;
        if (x.get(0) > pos)
            return sum.get(n) - pos * n;

        int l = 0, r = n - 1;
        while (l + 1 < r) {
            int mid = l + (r - l) / 2;
            if (x.get(mid) <= pos)
                l = mid;
            else
                r = mid - 1;
        }
        
        int index = 0;
        if (x.get(r) <= pos)
            index = r;
        else
            index = l;
        return sum.get(n) - sum.get(index + 1) - pos * (n - index - 1) + 
               (index + 1) * pos - sum.get(index + 1);
    }
}

// 方法二
public class Solution {
    /**
     * @param grid a 2D grid
     * @return an integer
     */
    public int shortestDistance(int[][] grid) {
        // Write your code here
        int row = grid.length, column = grid[0].length;
        if(row == 0 || column == 0 || !haveZero(grid,row,column)) {
        	return -1;
        }

        int[] rowSum = new int[row];
        int[] columnSum = new int[column]; 
        for(int i = 0; i < row; i++)
        	for(int j = 0; j < column; j++)
        		if(grid[i][j] == 1) {
        			rowSum[i]++;
        			columnSum[j]++;
        		}

        int[] ansRow = new int[row];
        int[] ansColumn = new int[column];
        getSumDistance(rowSum,row,ansRow);
        getSumDistance(columnSum,column,ansColumn);

        int ans = Integer.MAX_VALUE;
        for(int i = 0; i < row; i++)
        	for(int j = 0; j < column; j++)
        		if(grid[i][j] == 0 && ans > ansRow[i] + ansColumn[j]) {
        			ans = ansRow[i] + ansColumn[j];
        		}
        return ans;
    }

    void getSumDistance(int[] a,int n,int[] ans) {
    	int[] prefixSum1 = new int[n];
    	int[] prefixSum2 = new int[n];
    	/*
    	第一阶段，处理前缀。
    	prefixSum1记录数组 a 的前缀和，即:prefixSum1[i]=a[0]+a[1]+..+a[i].
    	prefixSum2记录数组 prefixSum1 前缀和，prefixSum2即为前 i 个点到第 i 个点的代价和。
    	*/
    	prefixSum1[0] = a[0];
    	for(int i = 1; i < n; i++) {
    		prefixSum1[i] = prefixSum1[i - 1] + a[i];
    	}
    	prefixSum2[0] = 0;
    	for(int i = 1; i < n; i++) {
    		prefixSum2[i] = prefixSum2[i - 1] + prefixSum1[i - 1];
     	}

     	for(int i = 0; i < n; i++) {
     		ans[i] = prefixSum2[i];
     	}

    	/*
    	第二阶段，处理后缀。
    	prefixSum1记录数组 a 的后缀和，即:prefixSum1[i]=a[n-1]+a[n-2]+..+a[i].
    	prefixSum2记录数组 prefixSum1 的后缀和，prefixSum2即为 i 之后的点到第 i 个点的代价和。
    	*/
    	prefixSum1[n - 1] = a[n - 1];
    	for(int i = n - 2; i >= 0; i--) {
    		prefixSum1[i] = prefixSum1[i + 1] + a[i];
    	}
    	prefixSum2[n - 1] =0;
    	for(int i = n - 2; i >= 0; i--) {
    		prefixSum2[i] = prefixSum2[i + 1] + prefixSum1[i + 1];
     	}

     	for(int i = 0; i < n; i++) {
     		ans[i] += prefixSum2[i];
     	}

     	/*
     	ans[i] 即为a数组中所有点到第 i 点的代价和
     	*/
    }

    boolean haveZero(int[][] grid, int row, int column) {
    	for(int i = 0; i < row; i++) {
    		for(int j = 0; j < column; j++){
    			if(grid[i][j] == 0) {
    				return true;
    			}
    		}
    	}
    	return false;
    }
}


"""


"""

from jiuzhang, java, two ways


// 方法一 
public class Solution {
    /**
     * @param grid a 2D grid
     * @return an integer
     */
    public int shortestDistance(int[][] grid) {
        // Write your code here
        int n = grid.length;
        if (n == 0)
            return -1;

        int m = grid[0].length;
        if (m == 0)
            return -1;

        List<Integer> sumx = new ArrayList<Integer>();
        List<Integer> sumy = new ArrayList<Integer>();
        List<Integer> x = new ArrayList<Integer>();
        List<Integer> y = new ArrayList<Integer>();

        int result = Integer.MAX_VALUE;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                if (grid[i][j] == 1) {
                    x.add(i);
                    y.add(j);
                }
        
        Collections.sort(x);
        Collections.sort(y);

        int total = x.size();

        sumx.add(0);
        sumy.add(0);
        for (int i = 1; i <= total; ++i) {
            sumx.add(sumx.get(i-1) + x.get(i-1));
            sumy.add(sumy.get(i-1) + y.get(i-1));
        }

        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                if (grid[i][j] == 0) {
                    int cost_x = get_cost(x, sumx, i, total);
                    int cost_y = get_cost(y, sumy, j, total);
                    if (cost_x + cost_y < result)
                        result = cost_x + cost_y;
                }

        return result;
    }

    public int get_cost(List<Integer> x, List<Integer> sum, int pos, int n) {
        if (n == 0)
            return 0;
        if (x.get(0) > pos)
            return sum.get(n) - pos * n;

        int l = 0, r = n - 1;
        while (l + 1 < r) {
            int mid = l + (r - l) / 2;
            if (x.get(mid) <= pos)
                l = mid;
            else
                r = mid - 1;
        }
        
        int index = 0;
        if (x.get(r) <= pos)
            index = r;
        else
            index = l;
        return sum.get(n) - sum.get(index + 1) - pos * (n - index - 1) + 
               (index + 1) * pos - sum.get(index + 1);
    }
}

// 方法二
public class Solution {
    /**
     * @param grid a 2D grid
     * @return an integer
     */
    public int shortestDistance(int[][] grid) {
        // Write your code here
        int row = grid.length, column = grid[0].length;
        if(row == 0 || column == 0 || !haveZero(grid,row,column)) {
        	return -1;
        }

        int[] rowSum = new int[row];
        int[] columnSum = new int[column]; 
        for(int i = 0; i < row; i++)
        	for(int j = 0; j < column; j++)
        		if(grid[i][j] == 1) {
        			rowSum[i]++;
        			columnSum[j]++;
        		}

        int[] ansRow = new int[row];
        int[] ansColumn = new int[column];
        getSumDistance(rowSum,row,ansRow);
        getSumDistance(columnSum,column,ansColumn);

        int ans = Integer.MAX_VALUE;
        for(int i = 0; i < row; i++)
        	for(int j = 0; j < column; j++)
        		if(grid[i][j] == 0 && ans > ansRow[i] + ansColumn[j]) {
        			ans = ansRow[i] + ansColumn[j];
        		}
        return ans;
    }

    void getSumDistance(int[] a,int n,int[] ans) {
    	int[] prefixSum1 = new int[n];
    	int[] prefixSum2 = new int[n];
    	/*
    	第一阶段，处理前缀。
    	prefixSum1记录数组 a 的前缀和，即:prefixSum1[i]=a[0]+a[1]+..+a[i].
    	prefixSum2记录数组 prefixSum1 前缀和，prefixSum2即为前 i 个点到第 i 个点的代价和。
    	*/
    	prefixSum1[0] = a[0];
    	for(int i = 1; i < n; i++) {
    		prefixSum1[i] = prefixSum1[i - 1] + a[i];
    	}
    	prefixSum2[0] = 0;
    	for(int i = 1; i < n; i++) {
    		prefixSum2[i] = prefixSum2[i - 1] + prefixSum1[i - 1];
     	}

     	for(int i = 0; i < n; i++) {
     		ans[i] = prefixSum2[i];
     	}

    	/*
    	第二阶段，处理后缀。
    	prefixSum1记录数组 a 的后缀和，即:prefixSum1[i]=a[n-1]+a[n-2]+..+a[i].
    	prefixSum2记录数组 prefixSum1 的后缀和，prefixSum2即为 i 之后的点到第 i 个点的代价和。
    	*/
    	prefixSum1[n - 1] = a[n - 1];
    	for(int i = n - 2; i >= 0; i--) {
    		prefixSum1[i] = prefixSum1[i + 1] + a[i];
    	}
    	prefixSum2[n - 1] =0;
    	for(int i = n - 2; i >= 0; i--) {
    		prefixSum2[i] = prefixSum2[i + 1] + prefixSum1[i + 1];
     	}

     	for(int i = 0; i < n; i++) {
     		ans[i] += prefixSum2[i];
     	}

     	/*
     	ans[i] 即为a数组中所有点到第 i 点的代价和
     	*/
    }

    boolean haveZero(int[][] grid, int row, int column) {
    	for(int i = 0; i < row; i++) {
    		for(int j = 0; j < column; j++){
    			if(grid[i][j] == 0) {
    				return true;
    			}
    		}
    	}
    	return false;
    }
}



"""