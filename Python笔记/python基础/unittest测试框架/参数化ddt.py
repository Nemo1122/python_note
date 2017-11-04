import unittest
import ddt


@ddt.ddt
class MyTest(unittest.TestCase):

    # 只有一个参数时
    @ddt.data(3, 6, 9)
    def test_add1(self, a):
        print('a的值为：', a)

    # 有两个参数时
    # @ddt.data([3, 5])
    @ddt.data([5, 6], [3, 4], [1, 2])
    @ddt.unpack
    def test_add2(self, a, b):
        print('a = ', a)
        print('b = ', b)
        print('a + b = ', a + b)

    # 有两个以上参数时
    @ddt.data([5, 6, 7], [3, 4, 5], [1, 2, 3])
    @ddt.unpack
    def test_add2(self, a, b, c):
        print('a, b, c 分别为：', a, b, c)
        print('a + b = ', a + b + c)