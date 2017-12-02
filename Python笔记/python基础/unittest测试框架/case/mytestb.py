import unittest


class MyTestB(unittest.TestCase):
    """测试"""

    def setUp(self):
        print('初始化，每个用例执行之前都会执行')

    def test_case_first(self):
        """第一个测试"""
        print('我是测试B中的第一个测试用例')
        # self.assertEqual('x', 'y', '测试不通过')

    def test_case_second(self):
        print('我是测试B中的第二个测试用例')

    def tearDown(self):
        print('清理，每个用例执行之后都会执行')


# # 实例化测试套件TestSuite
# suite = unittest.TestSuite()
# # 将用例添加到测试套件
# suite.addTest(MyTest("test_case_second"))
# suite.addTest(MyTest("test_case_first"))
# # 实例化测试运行TextTestRunner
# runner = unittest.TextTestRunner()
# # 运行测试套件
# runner.run(suite)
