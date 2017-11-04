import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send_mail(report):
    """用于将测试报告发送到邮箱"""

    # 定义发送的字段
    smtp_dict = {
        "smtp_server": "smtp.126.com",
        "send_user": "am1122@126.com",
        "send_pwd": "***",
        "sender": "am1122@126.com",
        "receiver": ["zhangmin@hidtest.cn", "40103519@qq.com"],  # 多个邮箱地址，用list
        "subject": "自动化测试报告"
    }
    # 获取测试报告的内容
    file = open(report, "rb")
    mail_body = file.read()
    file.close()
    # 组装邮件内容
    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header(smtp_dict["subject"], 'utf-8')
    msg['From'] = smtp_dict["send_user"]
    # 发送邮件
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtp_dict["smtp_server"])
        smtp.login(smtp_dict["send_user"], smtp_dict["send_pwd"])
        smtp.sendmail(smtp_dict["sender"], smtp_dict["receiver"], msg.as_string())
    except smtplib.SMTPException as se:
        print("邮件发送失败！！")
        print(se)


send_mail(r'E:\Pythonproj\wukCRM\report\WkCRM20171002224959result.html')