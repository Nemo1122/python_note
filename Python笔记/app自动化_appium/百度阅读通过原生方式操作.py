from appium import webdriver
from time import sleep

desired_capabilities = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:21503',
    'platformVersion': '4.4.4',
    'appPackage': 'com.baidu.yuedu',
    'appActivity': 'com.baidu.yuedu.splash.SplashActivity',
    # 设置每次不重置app状态
    'noReset': 'true',
    # 设置超时时间，如果不设置，1分钟appium没接收到新请求就会关闭链接
    'newCommandTimeout': 600
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
# 启动过程较慢，等待一下
sleep(3)
# 点击
driver.find_element_by_id('com.baidu.yuedu:id/righttitle').click()
# 点击第一个换一换按钮（图中看到的双十一特供）
driver.find_elements_by_accessibility_id('换一换').click()
# 观察一下执行后推荐的书有没有变化
# 点击第一个查看全部
driver.find_elements_by_accessibility_id('查看全部').click()
