from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep

desired_capabilities = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:21503',
    'platformVersion': '4.4.4',
    'appPackage': 'com.baidu.yuedu',
    'appActivity': 'com.baidu.yuedu.splash.SplashActivity',
    # 'browserName': 'Browser',
    # "automationName": "selendroid",
    'noReset': 'true',
    # 设置超时时间，如果不设置，1分钟appium没接收到新请求就会关闭链接
    'newCommandTimeout': 600
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

sleep(5)

driver.find_element_by_id('com.baidu.yuedu:id/righttitle').click()

con = driver.contexts

print(con)

# driver.find_element_by_css_selector('.huanyihuan').click()
# driver.find_element_by_css_selector('.c-see-more-button').click()

li = driver.find_elements_by_accessibility_id('换一换')
print(li)
li[0].click()
li_all = driver.find_elements_by_accessibility_id('查看全部')
print(li_all)
li_all[0].click()


# driver.switch_to.window(con[1])
# driver.switch_to.context(con[1])

