import unittest,time
from HTMLTestRunner import HTMLTestRunner
from model.function import send_mail

test_dir = "./testcase"
test_report = "./report"
# 组织测试用例
discover = unittest.defaultTestLoader.discover(test_dir, pattern="*_case.py")
smtp_dict = {
    "smtp_server": "smtp.126.com",       # 发送邮件服务器
    "send_user": "am1122@126.com",       # 发送邮件的邮箱账号
    "send_pwd": "password",              # 发送邮件的账号密码
    "sender": "am1122@126.com",          # 显示在邮件中的发件人
    "receiver": "zhangmin@hidtest.cn",   # 收件邮箱地址
    "subject": "自动化测试报告"            # 邮件主题
}

if __name__ == '__main__':
    # 格式化当前日期
    times = time.strftime("%Y%m%d%H%M%S")
    # 组装测试报告路径和文件名
    report_file = test_report + "/WkCRM" + times + "result.html"
    file = open(report_file, 'wb')
    # 实例化测试报告
    # runner = HTMLTestRunner(stream=file,
    #                         title="悟空CRM自动化测试报告",
    #                         description="运行环境：window 10， Chrome")
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(discover)
    file.close()
    # send_mail(smtp_dict, report_file)