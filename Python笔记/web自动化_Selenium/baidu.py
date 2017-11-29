from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("http://baidu.com")
driver.find_elements_by_id("kw").click()

wait = WebDriverWait()