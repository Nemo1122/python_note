# com.tencent.mm
# com.tencent.mm.ui.LauncherUI

from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep

desired_capabilities = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:21503',
    'platformVersion': '4.4.4',
    'appPackage': 'com.tencent.mm',
    'appActivity': 'com.tencent.mm.ui.LauncherUI',
    'noReset': 'true',
    # 设置超时时间，如果不设置，1分钟appium没接收到新请求就会关闭链接
    'newCommandTimeout':600
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

sleep(5)

# 点击订阅号
driver.find_element_by_id('com.tencent.mm:id/ajz').click()

sleep(0.5)

# 点击美食菜谱
driver.find_element_by_id('com.tencent.mm:id/ajz').click()

sleep(0.5)

# 点击学做饭
driver.find_element_by_id('com.tencent.mm:id/a7g').click()

sleep(0.5)

# 点击生活技巧
driver.find_element_by_xpath('//android.widget.TextView[@text="生活技巧"]').click()

sleep(0.5)

con = driver.contexts


driver.find_elements_by_accessibility_id('健康养生').click()

# driver.switch_to.context(con[2])