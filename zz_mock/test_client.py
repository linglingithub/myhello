"""
https://segmentfault.com/a/1190000002965620


找到要替换的对象：我们需要测试的是visit_ustack这个函数，那么我们需要替换掉send_request这个函数。

实例化Mock类得到一个mock对象，并且设置这个mock对象的行为。在成功测试中，我们设置mock对象的返回值为字符串“200”，在失败测试中，
我们设置mock对象的返回值为字符串"404"。

使用这个mock对象替换掉我们想替换的对象。我们替换掉了client.send_request

写测试代码。我们调用client.visit_ustack()，并且期望它的返回值和我们预设的一样。

上面这个就是使用mock对象的基本步骤了。在上面的例子中我们替换了自己写的模块的对象，其实也可以替换标准库和第三方模块的对象，方法是一样的：
先import进来，然后替换掉指定的对象就可以了。

activate pipenv first by 'pipenv shell'

"""

import unittest

from unittest import mock

import client


class TestClient(unittest.TestCase):
    def test_success_request(self):
        success_send = mock.Mock(return_value='200')
        # 实例化Mock类得到一个mock对象，并且设置这个mock对象的行为。
        # 在成功测试中，我们设置mock对象的返回值为字符串“200”，
        # 在失败测试中，我们设置mock对象的返回值为字符串"404"。
        client.send_request = success_send
        # 用这个mock对象替换掉我们想替换的对象, client.send_request
        self.assertEqual(client.visit_ustack(), '200')

    def test_fail_request(self):
        fail_send = mock.Mock(return_value='404')
        client.send_request = fail_send
        self.assertEqual(client.visit_ustack(), '404')

    def test_call_send_request_with_right_arguments(self):
        """
        Mock对象的called属性表示该mock对象是否被调用过。
        
        Mock对象的call_args表示该mock对象被调用的tuple，tuple的每个成员都是一个mock.call对象。mock.call这个对象代表了一次对mock
        对象的调用，其内容是一个tuple，含有两个元素，第一个元素是调用mock对象时的位置参数（*args），第二个元素是调用mock对象时的关键字
        参数（**kwargs）。
        
        现在来分析下上面的用例，我们要检查的项目有两个：
        
        visit_ustack()调用了send_request()
        
        调用的参数是一个字符串
        
        :return: 
        """
        client.send_request = mock.Mock()
        client.visit_ustack()
        self.assertEqual(client.send_request.called, True)
        call_args = client.send_request.call_args
        self.assertIsInstance(call_args[0][0], str)


    """
    patch和patch.object。这两个函数都会返回一个mock内部的类实例，这个类是class _patch。返回的这个类实例既可以作为函数的装饰器，
    也可以作为类的装饰器，也可以作为上下文管理器。使用patch或者patch.object的目的是为了控制mock的范围，意思就是在一个函数范围内，
    或者一个类的范围内，或者with语句的范围内mock掉一个对象。
    """
    def test_success_request_with_patch(self):
        status_code = '200'
        success_send = mock.Mock(return_value=status_code)
        # 使用了patch函数（作为上下文管理器使用）。
        with mock.patch('client.send_request', success_send):
            from client import visit_ustack
            self.assertEqual(visit_ustack(), status_code)

    def test_fail_request_with_patch(self):
        status_code = '404'
        fail_send = mock.Mock(return_value=status_code)
        with mock.patch('client.send_request', fail_send):
            from client import visit_ustack
            self.assertEqual(visit_ustack(), status_code)


    """
    patch.object和patch的效果是一样的，只不过用法有点不同。举例来说，同样是上面这个例子，换成patch.object的话是这样的：
    就是替换掉一个对象的指定名称的属性，用法和setattr类似。
    """
    def test_fail_request_with_patch_obj(self):
        status_code = '404'
        fail_send = mock.Mock(return_value=status_code)
        with mock.patch.object(client, 'send_request', fail_send):
            from client import visit_ustack
            self.assertEqual(visit_ustack(), status_code)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestClient)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()
