from selenium.webdriver.common.by import By
from .page import Page


class MainPage(Page):
    """主页"""

    # 定位器
    login_assert_text_loc = (By.CLASS_NAME, "alert-success")

    def assert_login_text(self):
        """登录成功字样"""
        return self.find_element(self.login_assert_text_loc).text
