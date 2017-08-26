#coding=utf-8

import unittest

"""

====== from ref ===>>>>>>>

locked

157. READ N CHARACTERS GIVEN READ4


The API: int read4(char *buf) reads 4 characters at a time from a file.
The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.
By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
The read function will only be called once for each test case.


Hint:
Consider which one is smaller, read4(buf) or n - num.




"""


# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution:
    # @param buf, Destination buffer (a list of characters)
    # @param n,   Maximum number of characters to read (an integer)
    # @return     The number of characters read (an integer)
    def read(self, buf, n):
        """
        Complexity:
            O(n) time
            O(1) space
        :param buf: 
        :param n: 
        :return: 
        """
        numBytes = 0

        while n > 0:
            buf4 = [None] * 4
            size = read4(buf4)
            minLen = min(size, n - numBytes)

            if minLen == 0:
                return numBytes

            for i in range(minLen):
                buf[numBytes] = buf4[i]
                numBytes += 1

        return numBytes

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



#-*- coding:utf-8 -*-

"""

157. Read N Characters Given Read4 Total Accepted: 17410 Total Submissions: 58870 Difficulty: Easy
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
The read function will only be called once for each test case.

Hide Company Tags
 Facebook
Hide Tags
 String
Hide Similar Problems
 (H) Read N Characters Given Read4 II - Call multiple times
思路：
一开始没看懂题。看了好几个人的blog才知道是怎么回事。首先输入数组的长度我们是不知道的。
read4这个API中的参数是读了的char，也就是每次read4之后返回的char[4]是从给定文件中读的。
然后为啥是两参数？char[] buf和上面的一个道理，是输出的数组，而不是源文件；给int n是因为这个文件的长度可能比我们给的大，这样我们只需要读入N个字符到 char[] buf中；也有可能短，那么我们只能读完所有的文件并且返回文件长度。
[java] view plain copy
/* The read4 API is defined in the parent class Reader4. 
      int read4(char[] buf); */  
  
public class Solution extends Reader4 {     
    /**   
     * @param buf Destination buffer   
     * @param n   Maximum number of characters to read   
     * @return    The number of characters read   
     */     
    public int read(char[] buf, int n) {     
        int count = 0;     
        char[] mybuf = new char[4];     
        while(count<n){     
            int num = read4(mybuf);     
            if(num == 0) break;     
            int index = 0;     
            while(index < num && count < n){     
                buf[count++] = mybuf[index++];     
            }     
        }     
        return count;     
    }     
}   
// case 1 有数据，n个了; while循环管  
// case 2 数据不够n个，read4返回了0。 有一行代码管  

158. Read N Characters Given Read4 II - Call multiple times
Total Accepted: 13840  Total Submissions: 57027 Difficulty: Hard
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
The read function may be called multiple times.

Hide Company Tags
 Bloomberg Google Facebook
Hide Tags
 String
Hide Similar Problems
 (E) Read N Characters Given Read4
思路：
又是一开始没看懂题。变化是这样：比如先call了n=3，然后call n=5，那么第一次就读入了4个char，第二次call应该把上一次的最后一个char拿来。也就是说要有个cache取缓存已读取的字符，然后从这个cache里面取。
每次读4个字符，放入 cache，然后
in = Math.min(n - total, buff.size()) 这个是精髓，这样就知道还需要多少个字符了。如果是in=0了，那么说明已经够了或者没字符了，这样就不用再读取了。否则无论哪个大，接下来都需要往buf中放入in个字符（可能是剩的少，也有可能要求的少）。
[java] view plain copy
/* The read4 API is defined in the parent class Reader4. 
      int read4(char[] buf); */  
  
public class Solution extends Reader4 {  
    /** 
     * @param buf Destination buffer 
     * @param n   Maximum number of characters to read 
     * @return    The number of characters read 
     */  
    LinkedList<Character> buff = new LinkedList<Character>();  
    public int read(char[] buf, int n) {  
        int total = 0;  
        while(true){  
            char[] temp = new char[4];  
            int in = read4(temp);  
            for(int i = 0; i < in; i++) buff.add(temp[i]);  
              
            // 判断还需要写入多少个到结果， 比如读了4个，但是只要3个；或者要4个，只有3个了。  
            in = Math.min(n - total, buff.size());  
              
            for(int i = 0; i < in; i++) buf[total++] = buff.poll();  
            if(in == 0) break;  
        }  
        return total;  
    }  
}  


"""