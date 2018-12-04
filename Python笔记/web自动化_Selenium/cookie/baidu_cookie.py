from selenium import webdriver
from time import sleep
import logging, sys


logger = logging.getLogger('selenium')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))

driver = webdriver.Chrome()
driver.implicitly_wait(30)

driver.get("http://baidu.com")


driver.delete_cookie("BAIDUID")

driver.add_cookie({"name":"BAIDUID","value":"xx:FG=1"})
driver.add_cookie({"name":"BDUSS","value":"xx-xx"})

driver.refresh()

sleep(5)
driver.quit()
