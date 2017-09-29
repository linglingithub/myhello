

"""

130. Surrounded Regions

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X


Difficulty:Medium
Total Accepted:88.1K
Total Submissions:473.7K
Contributor: LeetCode
Subscribe to see which companies asked this question.

Related Topics 
Breadth-first Search Union Find 
Similar Questions 
Number of Islands Walls and Gates 


"""


import unittest


class Solution(object):
    def solve(self, nums):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not nums or not nums[0]:
            return
        from collections import deque
        m, n = len(nums), len(nums[0])
        queue = deque()
        # top, bottom
        for i in range(n):
            if nums[0][i] == 'O':
                nums[0][i] = 'G'
                queue.append((0,i))
            if nums[m-1][i] == 'O':
                nums[m-1][i] = 'G'
                queue.append((m-1, i))
        # left, right
        for i in range(m):
            if nums[i][0] == 'O':
                nums[i][0] = 'G'
                queue.append((i, 0))
            if nums[i][n - 1] == 'O':  # should be n-1, not m-1 here, typo, be careful
                nums[i][n - 1] = 'G'
                queue.append((i, m-1))
        # expand Good area
        while queue:
            x, y = queue.popleft()
            dx = [0,0,1,-1]
            dy = [1,-1,0,0]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<m and 0<=ny<n and nums[nx][ny] == 'O':
                    nums[nx][ny] = "G"
                    queue.append((nx,ny))
        # get updates for all 'O', revert 'G' to 'O'
        for i in range(m):
            for j in range(n):
                if nums[i][j] == 'O':
                    nums[i][j] = "X"
                if nums[i][j] == "G":
                    nums[i][j] = "O"





class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [
            ['X', 'X', 'X', 'X'],
            ['X', 'O', 'O', 'X'],
            ['X', 'X', 'O', 'X'],
            ['X', 'O', 'X', 'X']
        ]
        answer = [
            ['X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X'],
            ['X', 'O', 'X', 'X']
        ]
        result = self.sol.solve(nums)
        self.assertEqual(answer, nums)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

"""

board最外面四条边上的'O'肯定不会被'X'包围起来, 从这些'O'入手, 使用BFS求出所有相邻的'O', 把这些'O'改为另一种符号, 比如'$'。
然后再扫描一遍board, 把'O'换成'X', 把'$'换成'O'。


=======================================================


http://yucoding.blogspot.com/2013/08/leetcode-question-131-surrounded-regions.html

Analysis:

Search is a good way to solve this problem!
First and easy thought might, scan all the element, if meets 'O', looking for a path to the boundary, if not exist, put 
it to 'X'. To look for the path, if all the four directions all have no way out, this element has no way out. The DFS 
can be used.  See code(small case) below. Actually, it only cannot pass the last big test case (where 250x250 matrix is 
provided).

However, it will not pass the big test, because the complexity is too high. One common thought is to use BFS instead of 
DFS, which use more space, but less time.

So how BFS is conducted, we can think from out to inside. Because the boundary 'O' are definitely "live" (have a path 
out) element, so, we BFS from each 'O' in the boundary, mark all its four directions (where is also 'O') as "live". 
If you think here, you almost done, the standard BFS using a queue (here I use vector for simplicity) can solve the 
problem. Last step is to flip "O" to "X" because there is no way out, and flip "P"(live) to "O", because it has a path 
out. See code (big case) for details. All the test cases are passed.

Code (C++):
class Solution {
public:
     void solve(vector<vector<char>> &board) {
        int row = board.size();  //get row number
        if (row==0){return;}
        int col = board[0].size(); // get column number
         
        vector<vector<bool> > bb(row, vector<bool>(col)); //result vector
         
        queue<pair<int,int> > q; // queue for BFS
         
        //search "O" from 1st row
        for (int i=0;i<col;i++){
            if (board[0][i]=='O'){
                q.push(make_pair(0,i));
                bb[0][i]=true;
            }
        }
         
        //search "O" from 1st column
        for (int i=0;i<row;i++){
            if (board[i][0]=='O'){
                q.push(make_pair(i,0));
                bb[i][0]=true;
            }
        }
         
        //search "O" from last row
        for (int i=0;i<col;i++){
            if (board[row-1][i]=='O'){
                q.push(make_pair(row-1,i));
                bb[row-1][i]=true;
            }
        }
         
        //search "O" from last column
        for (int i=0;i<row;i++){
            if (board[i][col-1]=='O'){
                q.push(make_pair(i,col-1));
                bb[i][col-1]=true;
            }
        }
         
        //BFS
        int i,j; // current position
        while (!q.empty()){
            //get current live "O"
            i = q.front().first;
            j = q.front().second;
             
            //pop up queue
            q.pop(); 
             
            //search four directions
            if (i-1>0 && board[i-1][j]=='O' && bb[i-1][j]==false){bb[i-1][j]=true; q.push(make_pair(i-1,j));} //top
            if (i+1<row-1 && board[i+1][j]=='O'&& bb[i+1][j]==false){bb[i+1][j]=true; q.push(make_pair(i+1,j));} // bottom
            if (j-1>0 && board[i][j-1]=='O'&& bb[i][j-1]==false){bb[i][j-1]=true; q.push(make_pair(i,j-1));} // left
            if (j+1<col-1 && board[i][j+1]=='O'&& bb[i][j+1]==false){bb[i][j+1]=true; q.push(make_pair(i,j+1));} // right
        }
         
        //Get result
        for (int i=0;i<row;i++){
            for (int j=0;j<col;j++){
                if (board[i][j]=='O'&&bb[i][j]==false){
                    board[i][j]='X';
                }
            }
        }
         
        return;
            
    }
};


Code(Python):

class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        row = len(board)
        if row==0:
            return
        col = len(board[0])    
        bb = [[False for j in xrange(0,col)] for i in xrange(0,row)]
        que = []
        for i in xrange(0,col):
            if board[0][i]=='O':
                bb[0][i]=True
                que.append([0,i])
            if board[row-1][i]=='O':
                bb[row-1][i]=True
                que.append([row-1,i])
                 
        for i in xrange(0,row):
            if board[i][0]=='O':
                bb[i][0]=True
                que.append([i,0])
            if board[i][col-1]=='O':
                bb[i][col-1]=True
                que.append([i,col-1])
         
        while que:
            i = que[0][0]
            j = que[0][1]
            que.pop(0)
            if (i-1>0 and board[i-1][j]=='O' and bb[i-1][j]==False):
                bb[i-1][j]=True
                que.append([i-1,j])
            if (i+1<row-1 and board[i+1][j]=='O' and bb[i+1][j]==False):
                bb[i+1][j]=True
                que.append([i+1,j])
            if (j-1>0 and board[i][j-1]=='O' and bb[i][j-1]==False):
                bb[i][j-1]=True
                que.append([i,j-1])
            if (j+1<col-1 and board[i][j+1]=='O' and bb[i][j+1]==False):
                bb[i][j+1]=True
                que.append([i,j+1])
                 
        for i in xrange(0,row):
            for j in xrange(0,col):
                if board[i][j]=='O' and bb[i][j]==False:
                    board[i][j] = 'X'
         
        return
                 
        



"""

#-*- coding:utf-8 -*-
