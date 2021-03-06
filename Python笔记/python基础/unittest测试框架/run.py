import unittest
from HTMLTestRunner import HTMLTestRunner

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


discover = unittest.defaultTestLoader.discover('./case', '*.py')

with open('./report.html', 'wb') as f:
    run = HTMLTestRunner(stream=f,
                         title='学习测试框架',
                         description='unittest, discover, html报告'
    )

    run.run(discover)