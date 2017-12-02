from selenium.webdriver.common.by import By
from .page import Page


class MenuPage(Page):
    """菜单栏由于所有页面通用，因此单独作为一个类"""

    # 定位器
    menu_leads = (By.LINK_TEXT, "线索")

    def in_leads(self):
        self.find_element(self.menu_leads).click()

