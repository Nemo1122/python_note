import unittest
from model.driver import browser
from page.login_page import LoginPage


class MyTest(unittest.TestCase):
    """测试用例的基类"""

    driver = browser()
    # 请更换为你自己的账号密码
    login_data = ("nemo", "nemo1985")

    @classmethod
    def setUpClass(cls):
        cls.driver.maximize_window()

        # 初始化直接登录
        login = LoginPage(cls.driver)
        login.open()
        login.login(*cls.login_data)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()