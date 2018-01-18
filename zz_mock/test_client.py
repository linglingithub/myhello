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
        client.send_request = success_send
        self.assertEqual(client.visit_ustack(), '200')

    def test_fail_request(self):
        fail_send = mock.Mock(return_value='404')
        client.send_request = fail_send
        self.assertEqual(client.visit_ustack(), '404')


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestClient)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()
