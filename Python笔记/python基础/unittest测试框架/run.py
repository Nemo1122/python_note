import unittest

from python基础.unittest测试框架.case.最简单的框架代码 import MyTest
#
# # 实例化测试套件TestSuite
# suite = unittest.TestSuite()
# # 将用例添加到测试套件
# suite.addTest(MyTest("test_case_second"))
# suite.addTest(MyTest("test_case_first"))
# # 实例化测试运行TextTestRunner
# runner = unittest.TextTestRunner()
# # 运行测试套件
# runner.run(suite)


discover = unittest.defaultTestLoader.discover('')