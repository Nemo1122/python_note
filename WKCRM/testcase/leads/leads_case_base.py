from page.menu_page import MenuPage
from testcase import test_case_base


class LeadsBaseCase(test_case_base.MyTest, MenuPage):
    """对于线索独有的测试用例需要用到的内容再进行抽象"""

    def setUp(self):
        """初始化进入线索列表页面"""
        self.in_leads()

