import smtplib, os, time
from email.mime.text import MIMEText
from email.header import Header
import xlrd
import pymysql


def send_mail(smtp_dict, report):
    """用于将测试报告发送到邮箱
    :param
    smtp_dict = {
        "smtp_server": "发送邮件的smtp ex:smtp.126.com",
        "send_user": "发送邮件的邮箱 ex:am1122@126.com",
        "send_pwd": "发送邮件的邮箱密码 ex:mima",
        "sender": "发件人邮箱用于显示收到邮件中的发件人 ex:am1122@126.com",
        "receiver": "收件人邮箱 ex:zhangmin@hidtest.cn",多个收件人可以写成list
        "subject": "邮件主题 ex:自动化测试报告"
    }    
    """

    # 获取测试报告的内容
    file = open(report, "rb")
    mail_body = file.read()
    file.close()
    # 组装邮件内容
    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['From'] = smtp_dict["send_user"]
    msg['Subject'] = Header(smtp_dict["subject"], 'utf-8')
    # 发送邮件
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtp_dict["smtp_server"])
        smtp.login(smtp_dict["send_user"], smtp_dict["send_pwd"])
        smtp.sendmail(smtp_dict["sender"], smtp_dict["receiver"], msg.as_string())
    except smtplib.SMTPException as se:
        print("邮件发送失败！！")
        print(se)


def screen_shot(driver, filename):
    """用于测试用例执行过程中的截图
    :param
    第一个当然是driver对象，
    第二个是保存的图片文件名，不用输.png"""
    top_dir = "./report/image/"
    times = time.strftime("%Y%m%d%H%M%S")
    image_file = top_dir + times + filename + ".png"
    driver.get_screenshot_as_file(image_file)


def excel_data(file, sheet_name):
    """读取excel中的数据，组装为字典
    ex:
        user    pwd     assert
        nemo    123     sucess
        nemo    321     fail
    :return [{'user': 'nemo', 'pwd': 123.0, 'islogin': 'success'},{'user': 'nemo', 'pwd': '', 'islogin': 'failed'}]
    """
    # 打开一个excel
    data = xlrd.open_workbook(file)
    # 通过sheet名称打开
    table = data.sheet_by_name(sheet_name)
    e_list = []
    header_row = table.row_values(0)
    for n_row in range(1, table.nrows):
        e_list.append(dict(zip(header_row, table.row_values(n_row))))
    return e_list


def parent_path(n):
    """获取当前文件目录的n层上级目录"""

    # 获取当前目录
    current_path = os.getcwd()
    # 拼接上级目录字符串
    p = ".."
    li = []

    if n > 1:
        for i in range(n):
            li.append(p)
        p = "/".join(li)
        p_path = os.path.abspath(os.path.join(current_path, p))
    elif n == 1:
        p_path = os.path.abspath(os.path.join(current_path, p))
    else:
        p_path = os.path.abspath(current_path)
    return p_path


def mysql_data(config, sql):
    """通过数据库获取数据，返回参数sql语句所能查出的所有数据
    :param  
    config = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': 'root',
        'db': 'ecshop',
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.DictCursor  # 加上这个参数会将查询结果变为[{"字段名":"字段值",...},{}]的形式
    }
    sql = "SELECT * FROM ecs_article_cat"
    :return 
    count, 语句执行的条数
    all_data, fetchall，也就是通过sql语句能查出的所有数据((),()),是一个二维元组
    """

    db = pymysql.connect(**config)
    try:
        cur = db.cursor()
        cur.execute(sql)
        all_data = cur.fetchall()
    except pymysql.err.DatabaseError as de:
        print(de)
        all_data = None
    finally:
        db.close()
    return all_data

