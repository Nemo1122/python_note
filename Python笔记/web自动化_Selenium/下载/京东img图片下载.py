# 配合requests下载图片
from selenium import webdriver
import requests


driver = webdriver.Chrome()

driver.implicitly_wait(30)

driver.get('http://baidu.com')

url = driver.find_element_by_css_selector('#lg>img').get_attribute('src')

#driver.quit()

r = requests.get(url)

with open('baidu.png', 'wb') as f:
    f.write(r.content)

