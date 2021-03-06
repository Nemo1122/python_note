from appium import webdriver
from time import sleep

desired_capabilities = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:21503',
    'platformVersion': '4.4.4',  # 逍遥模拟器
    # 'platformVersion': '7.1.1',    # 小米真机
    'appPackage': 'com.autonavi.minimap',
    'appActivity': 'comtoggle_location_services.autonavi.map.activity.SplashActivity',
    # 'browserName': 'Browser',
    # api 17以下的版本需要显示申明使用selendroid
    # "automationName": "selendroid",
    'noReset': 'true',
    # 设置超时时间，如果不设置，1分钟appium没接收到新请求就会关闭链接
    'newCommandTimeout': 600
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

driver.drag_and_drop()
driver.set_location()
driver.toggle_location_services()