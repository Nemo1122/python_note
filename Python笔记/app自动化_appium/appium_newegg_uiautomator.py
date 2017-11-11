from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep

desired_capabilities = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:21503',
    'platformVersion': '4.4.4',
    'appPackage': 'com.neweggcn.app',
    'appActivity': 'com.neweggcn.app.MainActivity',
    'noReset': 'true',
    # 设置超时时间，如果不设置，1分钟appium没接收到新请求就会关闭链接
    'newCommandTimeout':600
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
sleep(2)
driver.find_element_by_id('com.neweggcn.app:id/tools_order_tracking').click()
# driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.neweggcn.app:id/tools_order_tracking")')


#driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.neweggcn.app:id/tools_order_tracking")')
sleep(5)
driver.quit()