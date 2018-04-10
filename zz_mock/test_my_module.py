# coding=utf-8

"""
https://www.cnblogs.com/fnng/p/5648247.html



实际生产中的项目是非常复杂的，对其进行单元测试的时候，会遇到以下问题：

接口的依赖
外部接口调用
测试环境非常复杂
　　
单元测试应该只针对当前单元进行测试, 所有的内部或外部的依赖应该是稳定的, 已经在别处进行测试过的.
使用mock 就可以对外部依赖组件实现进行模拟并且替换掉, 从而使得单元测试将焦点只放在当前的单元功能。

例如，我们要测试A模块，然后A模块依赖于B模块的调用。但是，由于B模块的改变，导致了A模块返回结果的改变，从而使A模块的测试用例失败。
其实，对于A模块，以及A模块的用例来说，并没有变化，不应该失败才对。

这个时候就是mock发挥作用的时候了。通过mock模拟掉影响A模块的部分（B模块）。至于mock掉的部分（B模块）应该由其它用例来测试。

"""

from unittest import mock
import unittest
from my_module import Count


class MockDemo(unittest.TestCase):
    def test_add(self):
        """
        side_effect参数和return_value是相反的。它给mock分配了可替换的结果，覆盖了return_value。 
        简单的说，一个模拟工厂调用将返回side_effect值，而不是return_value。
　　     所以，设置side_effect参数为Count类add()方法，那么return_value的作用失效。

        :return: 
        """
        count = Count()
        count.add = mock.Mock(return_value=13, side_effect=count.add)
        result = count.add(8, 8)
        print(result)
        count.add.assert_called_with(8, 8)
        self.assertEqual(result, 16)


if __name__ == '__main__':
    unittest.main()
