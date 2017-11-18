from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep

desired_capabilities = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:21503',
    'platformVersion': '7.1.1',
    # 调用系统自带的浏览器
    # 'browserName': 'Browser',
    'browserName': 'Chrome',
    # 设置超时时间，如果不设置，1分钟appium没接收到新请求就会关闭链接
    'noReset': 'true',
    'newCommandTimeout': 600
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

driver.get('http://www.baidu.com')

driver.find_element_by_id('index-kw').send_keys('刘德华')
driver.find_element_by_id('index-bn').click()

# driver.find_element_by_id('x').value_of_css_property()
sleep(10)

driver.quit()
