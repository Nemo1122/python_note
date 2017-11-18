from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep


desired_capabilities = {
    'platformName': 'Android',
    'deviceName': '192.168.199.101:5555',
    'platformVersion': '4.4.4',
    'appPackage': 'com.neweggcn.app',
    'appActivity': 'com.neweggcn.app.MainActivity',
    'noReset': True,
    # 设置超时时间，如果不设置，1分钟appium没接收到新请求就会关闭链接
    'newCommandTimeout': 600,
    # 以Unicode发送字符，才能通过send_keys发送中文
    'unicodeKeyboard': True,
    # 关闭系统软键盘，否则影响输入
    'resetKeyboard' : True,
    # 4.4以下系统用Selendroid
    # 'automationName': 'Selendroid'
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
wait = WebDriverWait(driver, 10)
try:
    driver.find_element_by_id('android:id/button2')
except NoSuchElementException:
    print('no alert!')
else:
    driver.find_element_by_id('android:id/button2').click()

# 等待页面加载出订单追踪
locator_tracking = (By.ID, 'com.neweggcn.app:id/tools_order_tracking')
wait.until(EC.presence_of_element_located(locator_tracking))
driver.find_element_by_id('com.neweggcn.app:id/tools_order_tracking').click()
# driver.find_element_by_name('订单追踪').click()        #已失效
# driver.find_element_by_xpath('//*[@text="订单追踪"]').click()     #通过xpath方式定位


# 通过元素再次查找定位今日炸蛋
# locator = driver.find_element_by_id('com.neweggcn.app:id/shellshocker_watch_more')
# locator.find_element_by_xpath('//android.widget.TextView[@text="今日炸蛋"]')

# 等待元素加载
locator_username = (By.ID, 'com.neweggcn.app:id/login_name')
wait.until(EC.presence_of_element_located(locator_username))

# 登录
driver.find_element_by_id('com.neweggcn.app:id/login_name').send_keys('13408568554')
driver.find_element_by_id('com.neweggcn.app:id/login_password').send_keys('test_selenium1')
driver.find_element_by_id('com.neweggcn.app:id/btn_login').click()

sleep(5)
driver.quit()


