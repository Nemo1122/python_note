from appium import webdriver
from time import sleep

desired_capabilities = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:21503',
    'platformVersion': '4.4.4',  # 逍遥模拟器
    # 'platformVersion': '7.1.1',    # 小米真机
    'appPackage': 'com.microsoft.bing',
    'appActivity': 'com.microsoft.clients.bing.app.MainActivity',
    # 'browserName': 'Browser',
    # "automationName": "selendroid",
    'noReset': True,
    # 设置超时时间，如果不设置，1分钟appium没接收到新请求就会关闭链接
    'newCommandTimeout': 600
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)