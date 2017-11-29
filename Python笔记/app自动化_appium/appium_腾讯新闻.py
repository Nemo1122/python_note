from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

desired_capabilities = {
    'platformName': 'Android',
    'deviceName': '7487096 unauthorized',
    'platformVersion': '7.1.1',
    'appPackage': 'com.tencent.news',
    'appActivity': 'com.tencent.news.activity.SplashActivity',
    'noReset': 'true',
    # 设置超时时间，如果不设置，1分钟appium没接收到新请求就会关闭链接
    'newCommandTimeout': 600,
    # 对于toast, 必须要用到Uiautomator2才能定位到
    'automationName': 'Uiautomator2'
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

# try:
#     driver.find_element_by_xpath('//android.widget.TextView[@text="跳过"]').click()
# except Exception:
#     print('no AD!')
WebDriverWait(driver, 10).until(lambda driver:
                                driver.find_element_by_xpath
                                ('//android.widget.TextView[@text="军事"]'))

driver.find_element_by_xpath('//android.widget.TextView[@text="军事"]').click()

# WebDriverWait(driver, 10).until(lambda driver:
#                                 driver.find_element_by_android_uiautomator
#                                 ('new UiSelector().textMatches("又发现了\d+条新内容")'))
#
# toast = driver.find_element_by_android_uiautomator(
#     'new UiSelector().textMatches("又发现了\d+条新内容")').text

driver.back()

WebDriverWait(driver, 10).until(lambda driver:
                                driver.find_element_by_xpath
                                ('//*[@text="再按一次退出腾讯新闻"]'))

toast = driver.find_element_by_xpath('//*[@text="再按一次退出腾讯新闻"]').text

print(toast)

driver.quit()

# driver.find_element_by_id('com.tencent.news:id/title_text')



