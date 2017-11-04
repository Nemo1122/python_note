from selenium import webdriver
from selenium.common import exceptions
from time import sleep

driver = webdriver.Chrome()
driver.get("file:///E:/%E5%B7%A5%E4%BD%9C/%E6%B5%B7%E5%BE%B7/%E9%99%84%E4%BB%B6/alert.html")

# driver.find_element_by_id('alert').click()

try:
    driver.switch_to.alert.accept()
except exceptions.NoAlertPresentException as na:
    print('没有弹出框')

sleep(3)
driver.quit()


# def is_alert():
#     try:
#         driver.switch_to.alert.text
#     except exceptions.NoAlertPresentException as e:
#         #print(e)
#         return False
#     else:
#         return True