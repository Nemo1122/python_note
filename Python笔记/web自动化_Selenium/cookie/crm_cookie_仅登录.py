from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(30)

driver.get("http://localhost/WkCRM")

driver.delete_cookie("PHPSESSID")

driver.add_cookie({"name": "name", "value": "root"})
driver.add_cookie({"name": "PHPSESSID", "value": "ob6rbve877eeo3klm77qkki874"})


driver.refresh()

sleep(30)

driver.quit()