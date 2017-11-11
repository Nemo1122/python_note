from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common import exceptions as se
from selenium.webdriver.common.keys import Keys
from time import sleep


def browser():
    """默认以设备Galaxy S5机型的方式打开浏览器，主要用于chrome模拟手机上的H5页面"""
    mobileEmulation = {'deviceName': 'Galaxy Note 3'}
    options = webdriver.ChromeOptions()
    # options.add_argument(r'--user-data-dir=C:\Users\NemoZhang\AppData\Local\Google\Chrome\User Data')
    # options.add_argument('--user-agent=Android')
    options.add_experimental_option('mobileEmulation', mobileEmulation)
    options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    driver = webdriver.Chrome(chrome_options=options)
    return driver


driver = browser()

driver.get("https://yd.baidu.com/ydnode/tushu/recommend30.html?h5v=1510384265689")

driver.find_element_by_css_selector('.huanyihuan').click()

driver.find_element_by_css_selector('.c-see-more-button').click()

sleep(5)

driver.quit()