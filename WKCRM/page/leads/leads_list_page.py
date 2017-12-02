from selenium.webdriver.common.by import By
from page.page import Page


class LeadsListPage(Page):
    """线索列表页面"""

    # 定位器
    leads_create_button_loc = (By.PARTIAL_LINK_TEXT, "新建线索")
    assert_leads_count_span_loc = (By.CSS_SELECTOR,
                                   "#td_colspan > div.pagination > div:nth-child(1)")
    
    def leads_create_button(self):
        """新建线索按钮"""
        self.find_element(self.leads_create_button_loc).click()

    def assert_leads_count_span(self):
        """获取左下角条数统计：'共9 条记录 1/1 页'"""
        return self.find_element(self.assert_leads_count_span_loc).text






