from appium import webdriver
from time import sleep

desired_capabilities = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:21503',
    'platformVersion': '4.4.4',
    'appPackage': 'com.tencent.news',
    'appActivity': 'com.tencent.news.activity.SplashActivity',
    'noReset': 'true',
    # 设置超时时间，如果不设置，1分钟appium没接收到新请求就会关闭链接
    'newCommandTimeout':600
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

sleep(3)

driver.find_element_by_id('com.tencent.news:id/title_text')
driver.drag_and_drop()