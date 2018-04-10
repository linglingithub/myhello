#coding=utf-8

"""
https://www.cnblogs.com/fnng/p/5648247.html

目前运行一切正确常，然而，add_and_multiply()函数依赖了multiply()函数的返回值。如果这个时候修改multiply()函数的代码。

……
def multiply(x, y):
    return x * y + 3
　　这个时候，multiply()函数返回的结果变成了x*y加3。

测试用例运行失败了，然而，add_and_multiply()函数以及它的测试用例并没有做任何修改，
罪魁祸首是multiply()函数引起的，我们应该把 multiply()函数mock掉。

"""

import unittest
from unittest.mock import patch
import my_function


class MyTestCase(unittest.TestCase):

    # def test_add_and_multiply_no_mock(self):
    #     x = 3
    #     y = 5
    #     addition, multiple = my_function.add_and_multiply(x, y)
    #     self.assertEqual(8, addition)
    #     self.assertEqual(15, multiple)


    @patch("my_function.multiply")   # which to mock
    def test_add_and_multiply2(self, mock_multiply):
        """
        
        　　@patch("function.multiply")

　　patch()装饰/上下文管理器可以很容易地模拟类或对象在模块测试。在测试过程中，您指定的对象将被替换为一个模拟（或其他对象），并在测试结束时还原。

　　这里模拟function.py文件中multiply()函数。

在定义测试用例中，将mock的multiply()函数（对象）重命名为 mock_multiply对象。
        
        :param mock_multiply: 
        :return: 
        """
        x = 3
        y = 5
        mock_multiply.return_value = 15   # rename as mock_multiply, mock it with return_value = 15
        addition, multiple = my_function.add_and_multiply(x, y)
        mock_multiply.assert_called_once_with(3, 5)   # 检查ock_multiply方法的参数是否正确。

        self.assertEqual(8, addition)
        self.assertEqual(15, multiple)


if __name__ == "__main__":
    unittest.main()