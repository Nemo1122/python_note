from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.get("http://localhost/WkCRM")

driver.implicitly_wait(10)

# driver.add_cookie({"name":"PHPSESSID", "value":"e75r6jdco5r9s7bh52hq1jflm4"})
# driver.add_cookie({"name":"BIDUPSID", "value":"4EF1FD2E831EC2A0D38AC776EF1A623E"})

driver.add_cookie({"name": "name", "value": "nemo"})
driver.add_cookie({"name": "salt_code", "value": "bf29236a9fe37255ec7e79b4f5a07193"})
driver.add_cookie({"name": "user_id", "value": "1"})

driver.refresh()

sleep(300)
driver.quit()