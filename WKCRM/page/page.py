from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page(object):
    """所有页面类的基类"""

    base_url = "http://localhost/WkCRM"

    def __init__(self, driver, url=base_url):
        self.driver = driver
        self.timeout = 30
        self.url = url

    def open(self):
        """打开网址"""
        self.driver.get(self.url)
        self.driver.implicitly_wait(self.timeout)

    def find_element(self, loc):
        """
        重新封装find_element方法，主要是为了能规划定位器，
        让find_element方法可以接收一个元组作为参数
        """
        return self.driver.find_element(*loc)

    def select(self, loc, value=0):
        """重新封装处理select的方式"""
        locator = self.find_element(loc)
        select = Select(locator)
        # 如果是数字，表示想通过index方式赋值
        if isinstance(value, int):
            select.select_by_index(value)
        # 如果是字符串，表示想通过可见文本赋值
        elif isinstance(value, str) and value:
            select.select_by_visible_text(value)
        else:
            # 默认选择第一个
            select.select_by_index(0)

    def wait_element_located(self, locator):
        """显式等待:等待元素加载"""
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(locator))

    def wait_element_visible(self, locator):
        """显式等待:等待元素可见"""
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(locator))

    def switch_to_frame(self, loc=None):
        """封装frame跳转方法"""
        # 不传任何参数，跳转到最外层
        if loc is None:
            self.driver.switch_to.default_content()
        # 传入定位器，表示想通过跳转到元素对象的方式
        elif isinstance(loc, tuple):
            locator = self.driver.find_element(loc)
            self.driver.switch_to.frame(locator)
        # 字符串或者数字，表示想通过index，id，name三种方式跳转
        elif isinstance(loc, str) or isinstance(loc, int):
            self.driver.switch_to.frame(loc)
        else:
            raise ValueError("输入的参数不正确, frame跳转只支持定位器（元组）、id、index、name方式。")



