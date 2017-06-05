#coding=utf-8

import unittest

"""

Copy Books II

Given n books( the page number of each book is the same) and an array of integer with size k means k people to copy the
book and the i th integer is the time i th person to copy one book). You must distribute the continuous id books to one
people to copy. (You can give book A[1],A[2] to one people, but you cannot give book A[1], A[3] to one people, because
book A[1] and A[3] is not continuous.) Return the number of smallest minutes need to copy all the books.

Example
Given n = 4, array A = [3,2,4], .


Return 4( First person spends 3 minutes to copy book 1, Second person spends 4 minutes to copy book 2 and 3, Third
person spends 4 minutes to copy book 4. )


Hard

"""

class Solution:
    # @param n: an integer
    # @param times: a list of integers
    # @return: an integer
    def copyBooksII(self, n, times):
        # write your code here
        if not times:
            return -1
        if n < 1:
            return 0
        if len(times) >= n: # think about this case, case 2
            #return sorted(times)[n-1] # can't do this , check case 2
            times.sort()

        l, r = 1, (1<<31)-1
        while l < r:
            mid = (l+r)/2
            book = self.find_can_copy_books(mid, times, n)
            if book < n:
                l = mid+1
            else:
                r = mid
        return l

    def find_can_copy_books(self, total, times, n):
        cnt = 0
        single_time = 0
        for i in times:
            if i > total:
                return n - 1
            cnt += total / i
            if cnt > n:
                return cnt
        return cnt





class SolutionTester(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        n =4
        nums = [3,2,4]
        answer = 4
        result = self.sol.copyBooksII(n, nums)
        self.assertEqual(answer, result)

    def test_case3(self):
        n = 3
        nums = [3,2,4]
        answer = 4
        result = self.sol.copyBooksII(n, nums)
        self.assertEqual(answer, result)

    def test_case4(self):
        n = 5
        nums = [3,2,4]
        answer = 6
        result = self.sol.copyBooksII(n, nums)
        self.assertEqual(answer, result)


    def test_case2(self): #====> think of the case that far more people than book, then need to find the fastest people,
        # when some ppl are much faster than others, need to have faster people do multiple books, some slow people do nothing
        n = 53
        nums = [274,233,513,981,372,328,251,926,363,542,573,966,846,940,848,22,804,881,492,151,583,371,403,135,571,37,647,517,929,915,500,372,763,94,167,100,53,679,878,463,310,568,689,631,817,820,967,40,371,589,787,891,304,496,419,64,791,768,330,678,15,2,924,958,583,919,750,63,435,858,478,221,752,238,410,510,56,475,749,329,633,844,111,978,282,561,91,327,298,301,367,402,805,50,962,91,155,84,955,280]
        answer = 75
        result = self.sol.copyBooksII(n, nums)
        self.assertEqual(answer, result)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SolutionTester)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()



#-*- coding:utf-8 -*-

"""

public class Solution {
    /**
     * @param n: an integer
     * @param times: an array of integers
     * @return: an integer
     */
    public int copyBooksII(int n, int[] times) {
        int k = times.length;
        int[][] f = new int[2][n+1];
        for (int j = 0 ; j <= n; ++j) {
            f[0][j] = j * times[0];
        }
        for (int i = 1; i < k; ++i) {
            for (int j = 1; j <= n; ++j) {
                int a = i%2;
                int b = 1-a;
                
                f[a][j] = Integer.MAX_VALUE;
                for (int l = 0; l <= j; ++l) {
                    if (f[b][j-l] > times[i] * l) {
                        f[a][j] = Math.min(f[a][j], f[b][j-l]);
                    } else {
                        f[a][j] = Math.min(f[a][j], times[i] * l);
                        break;
                    }
                }
                
            }
        }
        return f[(k-1)%2][n];
    }
    
    # the 2D way will MLE 
    public int copyBooksII2D(int n, int[] times) {
        int k = times.length;
        int[][] f = new int[k][n+1];
        for (int j = 0 ; j <= n; ++j) {
            f[0][j] = j * times[0];
        }
        for (int i = 1; i < k; ++i) {
            for (int j = 1; j <= n; ++j) {
                f[i][j] = Integer.MAX_VALUE;
                for (int l = 0; l <= j; ++l) {
                    f[i][j] = Math.min(f[i][j], Math.max(f[i-1][j-l], times[i] * l));
                    if (f[i-1][j-l] <= times[i] * l) {
                        break;
                    }
                }
                
            }
        }
        return f[k-1][n];
    }
}



"""