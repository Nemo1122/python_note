from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.PhantomJS()

try:
    driver.get("http://www.baidu.com")
    driver.find_element(By.ID, "kw").send_keys("刘德华")
    driver.find_element(By.ID, "su").click()

    driver.save_screenshot(".\phantomjs_baidu.png")
finally:
    driver.quit()