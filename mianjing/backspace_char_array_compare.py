#coding = utf-8
"""
给两个char array，其中有一些char为backspace就是删除前面的字符，要求输出一个boolean判断两个char array是否相同，
时间要求O(n) , 空间要求O(1)
例如：
[a,b,'\b',d,c] 和[a,d,c] true
[a,b,'\b','\b','\b',d,c] 和 [d,c] true
[a,b,d,'\b'] 和 [a,d] false

先给了用Stack的方法，TimeO(n), SpaceO(n)，没让写code.
之后要求TimeO(n), SpaceO(1)，po主试着从前往后parse没成功，好久之后小哥给提示从后往前parse


"""

class Solution:

    def check_same_array(self, a, b):
        """
        :param a: char array
        :param b:
        :return: boolean
        """
        if a is None and b is None:
            return True
        else:
            return not (a is None or b is None)
        i, j = len(a) - 1, len(b) - 1




