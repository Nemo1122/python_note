from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from page.page import Page


class LeadsCreatePage(Page):
    """线索新建页面"""

    # 定位器
    owner_name_text_loc = (By.ID, "owner_name")
    company_name_text_loc = (By.ID, "name")
    source_select_loc = (By.ID, "source")
    contacts_name_text_loc = (By.ID, "contacts_name")
    position_text_loc = (By.ID, "position")
    saltname_select_loc = (By.ID, "saltname")
    mobile_text_loc = (By.ID, "mobile")
    email_text_loc = (By.ID, "email")
    address_state_select_loc = (By.NAME, "address['state']")
    address_city_select_loc = (By.NAME, "address['city']")
    address_area_select_loc = (By.NAME, "address['area']")
    address_street_text_loc = (By.NAME, "address['street']")
    nextstep_time_loc = (By.ID, "nextstep_time")
    nextstep_text_loc = (By.ID, "nextstep")
    description_text_loc = (By.ID, "description")
    save_button_loc = (By.CSS_SELECTOR, "input[value = '保存']")
    save_and_create_button_loc = (By.CSS_SELECTOR, "input[value = '保存并新建']")
    cancel_button_loc = (By.CSS_SELECTOR, "input[value = '返回']")

    def owner_name_text(self, text):
        """负责人输入框"""
        self.find_element(self.owner_name_text_loc).clear()
        self.find_element(self.owner_name_text_loc).send_keys(text)

    def company_name_text(self, text):
        """公司名"""
        self.find_element(self.company_name_text_loc).send_keys(text)

    def source_select(self, value):
        """来源下拉框"""
        self.select(self.source_select_loc, value)

    def contacts_name_text(self, text):
        """联系人姓名"""
        self.find_element(self.contacts_name_text_loc).send_keys(text)

    def position_text(self, text):
        """职位"""
        self.find_element(self.position_text_loc).send_keys(text)

    def saltname_select(self, value):
        """尊称下拉菜单"""
        self.select(self.saltname_select_loc, value)

    def mobile_text(self, text):
        """手机号"""
        self.find_element(self.mobile_text_loc).send_keys(text)

    def email_text(self, text):
        """邮箱"""
        self.find_element(self.mobile_text_loc).send_keys(text)

    def address_select(self, state, city, area, street=" "):
        """地址级联下拉菜单"""
        self.select(self.address_state_select_loc, state)
        self.select(self.address_city_select_loc, city)
        self.select(self.address_area_select_loc, area)

        self.find_element(self.address_street_text_loc).send_keys(street)

    def nextstep_time(self, text):
        """下次联系时间"""
        self.find_element(self.nextstep_time_loc).send_keys(text)

    def nextstep_text(self, text):
        """下次联系内容"""
        self.find_element(self.nextstep_text_loc).send_keys(text)

    def description_text(self, text):
        """描述"""
        self.find_element(self.description_text_loc).send_keys(text)

    def save_button(self):
        """保存按钮"""
        self.find_element(self.save_button_loc).click()

    def save_and_create_button(self):
        """保存并新建"""
        self.find_element(self.save_and_create_button_loc).click()

    def cancel_button(self):
        """返回按钮"""
        self.find_element(self.cancel_button_loc).click()

    def create_leads_just_required(self, contacts_name):
        """新建线索仅填必填项"""
        self.contacts_name_text(contacts_name)
        self.save_button()

    def create_leads_full(self, owner_name="", company_name="",
                          source=0, contacts_name="", position="",
                          saltname=0, mobile="", email="",
                          state=0, city=0, area=0, street="",
                          nextstep_time="", nextstep="",
                          description=""
                          ):
        """新建线索填入全部项"""
        self.owner_name_text(owner_name)
        self.company_name_text(company_name)
        self.source_select(source)
        self.contacts_name_text(contacts_name)
        self.position_text(position)
        self.saltname_select(saltname)
        self.mobile_text(mobile)
        self.email_text(email)
        self.address_select(state, city, area, street)
        self.nextstep_time(nextstep_time)
        self.nextstep_text(nextstep)
        self.description_text(description)
        self.save_button()




