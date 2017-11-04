from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.get('http://jd.com')
h=0
while h != driver.find_element_by_tag_name('body').size['height']:
    h = driver.find_element_by_tag_name('body').size['height']
    driver.execute_script('window.scroll(0,%d)'% h)
    sleep(1)
    print(h, driver.find_element_by_tag_name('body').size['height'])