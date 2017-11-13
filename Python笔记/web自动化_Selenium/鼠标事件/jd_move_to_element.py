from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.maximize_window()

driver.get('http://www.jd.com')
# 定位鼠标需要移动到的元素
# locator = driver.find_element_by_xpath("//li[contains(.,'家用电器')]")
locator = driver.find_element_by_link_text('家用电器')
# 移动鼠标
# 实例化ActionChains
action = ActionChains(driver)
# 移动鼠标
action.move_to_element(locator)
# 提交鼠标移动事件
action.perform()

# 找到展示出来的元素，点击
# driver.find_element_by_xpath("//a[contains(.,'电视配件')]").click()
driver.find_element_by_link_text('电视配件').rect
sleep(10)
driver.quit()

