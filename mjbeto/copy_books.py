#coding=utf-8

import unittest
from util.ini_file_util import IniFileUtil

"""

Copy Books

Given n books and the ith book has A[i] pages. You are given k people to copy the n books.

n books list in a row and each person can claim a continous range of the n books. For example one copier can copy the
books from ith to jth continously, but he can not copy the 1st book, 2nd book and 4th book (without 3rd book).

They start copying books at the same time and they all cost 1 minute to copy 1 page of a book. What's the best strategy
to assign books so that the slowest copier can finish at earliest time?

Example
Given array A = [3,2,4], k = 2.

Return 5( First person spends 5 minutes to copy book 1 and book 2 and second person spends 4 minutes to copy book 3. )

Hard

"""


class Solution:
    # @param pages: a list of integers
    # @param k: an integer
    # @return: an integer
    def copyBooks(self, pages, k):  #276ms, according to ref
        if not pages:
            return 0
        if k >= len(pages):
            return max(pages)
        if k < 1:
            return -1
        l, r = 0, (1 << 31) - 1
        while l < r:
            mid = (l+r)/2
            ppl = self.count_required_ppl(mid, pages, k)
            if ppl > k:
                l = mid + 1
            elif ppl <= k:    # should be <= here instead of <
                r = mid
            # else:
            #     return mid
            # can't return here, because even if the ppl need k, does not mean mid is the min time,
            # may exist a time range that makes ppl the same as k
        return l

    def count_required_ppl(self, time, pages, k):
        cnt = 1
        single_time = 0
        for i in pages:
            if single_time + i <= time:
                single_time += i
            elif i > time:  # need to add check if time is even smaller than a book
                return k+1  # time too small, return required ppl as bigger than k not k-1
            else:
                cnt += 1
                single_time = i
                if cnt > k:
                    return k+1
        return cnt


    def copyBooks_TLE_javagood(self, pages, k): # dp way, runs around 31.458s locally, java version accepted
        if not pages:
            return 0
        if k >= len(pages):
            return max(pages)
        if k < 1:
            return -1
        n = len(pages)
        dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
        # dp[i][j] means the min time for first i books copied by j people
        dp[1][1] = pages[0]
        for i in range(1, n+1):
            dp[i][1] = pages[i-1]+dp[i-1][1]
        for j in range(1, k+1):
            dp[1][j] = pages[0]
        for i in range(2, n+1):
            for j in range(2, k+1):
                if i <= j:
                    #dp[i][j] = max(dp[i-1][j], pages[i-1])
                    dp[i][j] = max(dp[i-1][j], pages[i-1])
                else:
                    val = (1 << 31) -1
                    for l in range(j-1,i): # because j-1 people can do j-1 books at least
                        tmp = max(dp[l][j-1], dp[i][1]-dp[l][1])
                        val = min(tmp, val)
                    dp[i][j] = val
            #print "dp[{}][{}] = {}".format(i, j, dp[i][j])
        return dp[n][k]



    def copyBooks_TLE(self, pages, k): # _TLE, 80% cases passed
        # write your code here
        if not pages:
            return 0
        if k >= len(pages):
            return max(pages)
        if k < 1:
            return -1
        n = len(pages)
        dp = [[0 for _ in range(n+1)] for _ in range(k+1)]
        # dp[i][j] means the min time for i people to copy j books
        dp[1][1] = pages[0]
        for i in range(1, n+1):
            dp[1][i] = pages[i-1]+dp[1][i-1]
        for i in range(2, k+1):
            dp[i][0] = 0
            dp[i][1] = pages[0]
            for j in range(2, n+1):
                if j <= i:
                    dp[i][j] = max(pages[:j])
                else:
                    for l in range(1,j):
                        #tmp = dp[i-1][l]+ sum(pages[l:j]) # not looking for sum here, should be max
                        #tmp = max(dp[i - 1][l], sum(pages[l:j])) #TLE if clac sum here
                        tmp = max(dp[i - 1][l], dp[1][j]-dp[1][l])
                        dp[i][j] = min(tmp, dp[i][j]) if dp[i][j] != 0 else tmp
            print "dp[{}][{}] = {}".format(i, j, dp[i][j])
        return dp[k][n]









class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        nums = [2,3,4]
        k = 2
        answer = 5
        result = self.sol.copyBooks(nums, k)
        self.assertEqual(answer, result)

    def test_case2(self):
        nums = [2,3,4]
        k = 3
        answer = 4
        result = self.sol.copyBooks(nums, k)
        self.assertEqual(answer, result)

    def test_case3(self):
        nums = [2,3,4]
        k = 4
        answer = 4
        result = self.sol.copyBooks(nums, k)
        self.assertEqual(answer, result)

    def test_case4(self):
        nums = [2,3,4]
        k = 1
        answer = 9
        result = self.sol.copyBooks(nums, k)
        self.assertEqual(answer, result)

    def test_case5(self):  #====> TLE, local around 48.693s
        params = IniFileUtil.read_into_dict("copy_books_case5.ini")
        nums = IniFileUtil.string_to_int_list(params.get("nums"))
        k = int(params.get("k"))
        answer = 33871
        result = self.sol.copyBooks(nums, k)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()

    # from util.ini_file_util import IniFileUtil
    # params = IniFileUtil.read_into_dict("copy_books_case5.ini")
    # nums = IniFileUtil.string_to_int_list(params.get("nums"))
    # k = int(params.get("k"))
    # answer = 33871
    # sol = Solution()
    # result = sol.copyBooks(nums, k)



#-*- coding:utf-8 -*-

"""


这道题有两种解法。第一种是基本的DP，第二种是用二分法搜索可能最小时间。
第一种DP建立一个二维数组(n+1 * k+1)，T[i][j]表示前i本书分配给j个人copy。
初始化T[1][j]=pages[0]，初始化T[i][1]= pages[0] + pages[1] + ... + pages[i-1]
然后从2本书开始到n本书为止，依次计算分配给2～k个人的最小时间。当人数比书大时，有些人不干活也不会影响速度，因此和少一个人情况相同。
对于新加进来的人j，考虑让前j－1个人copy的书的数量h（0～n），则新进来的人相应的copy的数量为n～0本，前者的时间为T[h][j-1]，后者的时间为
T[i][1]-T[h][1]（即一个人copy从h＋1到i本需要的时间），两者的较大值即为T[i][j]的一个后选项。选择所有后选项中的最小值即为T[i][j]的值。
这里可以优化，即我们知道如果前j－1个人copy的书的数量少于j－1必然有人不干活，而所有人都干活的结果一定会更快，所以h的范围可以从j－1～n，因为
我们知道h为0～j－1时的结果一定不会是最优的答案。
第二种方法很巧妙地用到了二分搜索的方法。我们要找的最优解是某一个时间的临界点，当时间小于这个值时，k个人一定不可能完成任务，当时间大于等于这
个值时，则可以完成。
首先将时间的范围设为所有整数（0～99999999）。计算中点作为这次的假设时间临界点，尽量让每个人的工作时间都接近这个临界点。
假设当前某个人之前分配的书的页数加上当前书的页数小于当前临界点，则直接把这本书分配给这个人而不会影响最优解；
若大于，则看当前书的页数是否大于临界点： 1）若大于，则说明当前的临界值太小，连这本书都不能copy完全，所以最优解一定大于当前临界点，因此要增
大临界点再重复2 2）若小于，则将书分配给下一个人copy
若所有书分配完时，所需要的人数比k小（即还剩下人没用），则说明每个人干活的时间太多，最优时间一定比当前值小，反之则说明每个人干活的时间太少，
最优时间比当前值大
考虑3-4中的所有情况，若最优解比当前临界点小，则向当前临界点左半边搜索，否则向当前临界点右半边搜索，直到左右边界重合，此时的临界点（即左右边
界）即为最优解。

代码如下：

DP

public class Solution {
    /**
     * @param pages: an array of integers
     * @param k: an integer
     * @return: an integer
     */
    public int copyBooks(int[] pages, int k) {
        // write your code here
        // if(pages == null || pages.length == 0){
        //     return 0;
        // }

        // if(k < 1){
        //     return -1;
        // }

        // int n = pages.length;
        // int[][] T = new int[n + 1][k + 1];

        // for(int j = 1; j <= k; j++){
        //     T[1][j] = pages[0];
        // }

        // int sum = 0;
        // for(int i = 1; i <= n; i++){
        //     sum += pages[i - 1];
        //     T[i][1] = sum;
        // }

        // for(int i = 2; i <= n; i++){
        //     for(int j = 2; j <= k; j++){
        //         if(j > i){
        //             T[i][j] = T[i][j - 1];
        //             continue;
        //         }
        //         int min = Integer.MAX_VALUE;
        //         for(int h = j - 1; h <= i; h++){
        //             int temp = Math.max(T[h][j - 1], T[i][1] - T[h][1]);
        //             min = Math.min(min, temp);
        //         }
        //         T[i][j] = min;
        //     }
        // }

        // return T[n][k];
    }
}
Binary search
public class Solution {
    /**
     * @param pages: an array of integers
     * @param k: an integer
     * @return: an integer
     */
    public int copyBooks(int[] pages, int k) {
        // write your code here
        //O(n*logM)? O(n*k)
        int l = 0;
        int r = 9999999;
        while( l <= r){
            int mid = l + (r - l) / 2;
            if(search(mid,pages,k))
                r = mid-1;
            else
                l = mid+1;
        }
        return l;
    }

    private boolean search(int total, int[] page, int k){
    //至少有一个人copy，所以count从1开始
        int count = 1;
        int sum = 0;
        for(int i = 0; i < page.length;) {
            if(sum + page[i] <= total){
                sum += page[i++];
            }else if(page[i] <= total){
                sum = 0;
                count++;
            }else{
                return false;
            }
        }

        return count <= k;
    }
}


"""