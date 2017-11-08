from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common import exceptions as se
from selenium.webdriver.common.keys import Keys
import time


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


# def browser():
#     WIDTH = 360
#     HEIGHT = 640
#     PIXEL_RATIO = 3.0
#     UA = 'Mozilla/5.0 (Linux; U; Android 4.3; en-us; SM-N900T Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
#     options = webdriver.ChromeOptions()
#     mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}, "userAgent": UA}
#     options.add_experimental_option('mobileEmulation', mobileEmulation)
#     options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
#     driver = webdriver.Chrome(chrome_options=options)
#     return driver
driver = browser()
# 测试
# driver.get("http://m.xiaomicache.com/")
# 生产
driver.get("http://m.xiaomicp.com/")

# driver.find_element_by_class_name('logo-ssq').click()
try:
    driver.find_element_by_class_name('logo-ssq').click()
    # time.sleep(3)
    # driver.find_element(By.CLASS_NAME, "logo-rxj").click()
    # driver.find_element(By.CSS_SELECTOR, '[ontap="togoucai(\'shopmicai/shoppage/ctzc/sfcr9.html\')"]').click()
except se.NoSuchElementException as nse:
    print(nse)

except se.WebDriverException as we:
    print(se)
    # size = driver.find_element(By.TAG_NAME, 'html').size
    driver.execute_script('window.scroll(0, 200)')
    # action = ActionChains(driver)
    # source = driver.find_element(By.CLASS_NAME, "logo-jldg")
    # target = driver.find_element(By.CLASS_NAME, "logo-dlt")
    # action.click_and_hold(source).move_to_element(target).release().perform()
    # # action.drag_and_drop_by_offset(source, 50, 50).perform()
    # action.move_by_offset(0, 50)
    # action.perform()
    # action.release()
    # action.perform()

    # driver.find_element_by_tag_name('body').send_keys(Keys.SPACE)
    # driver.find_element(By.CLASS_NAME, "logo-rxj").click()
    # driver.find_element(By.CSS_SELECTOR, '[ontap="togoucai(\'shopmicai/shoppage/ctzc/sfcr9.html\')"]').click()


finally:
    time.sleep(10)
    driver.quit()