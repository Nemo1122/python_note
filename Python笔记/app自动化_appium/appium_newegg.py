from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

desired_capabilities = {
    'platformName': 'Android',
    'deviceName': '192.168.199.101:5555',
    'platformVersion': '7.0',
    'appPackage': 'com.neweggcn.app',
    'appActivity': 'com.neweggcn.app.MainActivity',
    'noReset': 'true'
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
try:
    driver.find_element_by_id('android:id/button2')
except NoSuchElementException:
    print('no alert!')
else:
    driver.find_element_by_id('android:id/button2').click()

# driver.find_element_by_id('com.neweggcn.app:id/tools_order_tracking').click()
# driver.find_element_by_name('订单追踪').click()
driver.find_element_by_xpath('//*[@text="订单追踪"]').click()

driver.find_element_by_class_name('android.widget.TextView')
driver.find_element_by_accessibility_id('menu_add_note_description')
driver.find_element_by_xpath('//android.widget.LinearLayout[@resource-id="com.neweggcn.app:id/home_frag_container"]/android.widget.LinearLayout[2]/android.view.View[1]')
