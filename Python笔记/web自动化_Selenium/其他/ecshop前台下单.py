from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions as Error
from python_base.内置模块.log2_ import Log
import time
# import logging
# import logging.handlers


driver = webdriver.Chrome()

driver.get("http://localhost/ecshop")

driver.maximize_window()
driver.implicitly_wait(30)
log = Log()
log('x', '打开浏览器')

# driver.find_element(By.NAME, "username").send_keys("nemo")
# driver.find_element(By.NAME, "password").send_keys("nemo1985")
# driver.find_element(By.CSS_SELECTOR, ".button").click()

log('i', '登录')
try:
    driver.find_element_by_link_text("登录").click()
except Exception as e:
    log('e', e)
log2 = Log(file_name='test.log')
driver.find_element_by_name("username").send_keys("nemo")
log2('i', '输入用户名：nemo')
driver.find_element_by_name("password").send_keys("nemo1985")
log2('i', '输入nemo1985')
driver.find_element_by_name("submit").click()
log2('i', '点击登录')


driver.find_element_by_partial_link_text("女装").click()
driver.find_element_by_link_text("高质感毛呢大衣").click()

wait = WebDriverWait(driver, 10, 0.5)

try:
    pass
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "img[src*='images/goumai2.gif']")))
    driver.find_element_by_css_selector("img[src*='images/goumai2.gif']").click()
    driver.find_element_by_css_selector("img[alt=checkout]").click()

    driver.find_element_by_css_selector("input[src*='bnt_subOrder.gif']").click()
    # driver.find_element_by_css_selector("input[src*='bnt_subOrder.gif']").send_keys(Keys.ENTER)

finally:
    time.sleep(1)
    driver.quit()