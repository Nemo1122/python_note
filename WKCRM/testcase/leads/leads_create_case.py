import ddt
import re
from model import function
from page.leads.leads_create_page import LeadsCreatePage
from page.leads.leads_list_page import LeadsListPage
from testcase.leads.leads_case_base import LeadsBaseCase


# 多重继承, 继承后, 可直接使用测试基类及页面类中的属性和方法
# 不过这种方法会存在一些问题, 尽可能用实例化的方式
@ddt.ddt
class LeadsCreateCase(LeadsBaseCase,
                      LeadsListPage,
                      LeadsCreatePage):
    """线索创建"""

    @ddt.data(*function.excel_data(".\data\leads.xlsx", "create"))
    @ddt.unpack
    def test_leads_create_case(self, **kw):
        """新建线索测试用例"""

        # 进入线索
        self.leads_create_button()
        self.create_leads_full(**kw)

        # 查询数据库的条数是否更新
        config = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': 'root',
            'db': '5kcrm',
            'charset': 'utf8mb4',
        }
        sql = "SELECT count(*) FROM 5kcrm_leads where is_deleted=0"
        count_sql = function.mysql_data(config, sql)[0][0]

        # 获取页面条数，用页面的条数与数据库条数对比断言
        count_page_str_ = self.assert_leads_count_span()
        count_page = int(re.search(r"\d+", count_page_str_).group())

        self.assertEqual(count_sql, count_page, "数据库与页面数量不等")









