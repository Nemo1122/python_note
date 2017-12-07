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

driver.add_cookie({"name":"BAIDUID","value":"14E4089547E699A390EAADBBCED77308:FG=1"})
driver.add_cookie({"name":"BDUSS","value":"lZVTNZSmNmUTBVQzhDcWloTUFFWmFudDd3c0pEVFVFY3h3WHB1bzk5SnpYYk5aSVFBQUFBJCQAAAAAAAAAAAEAAAA-JuRLwMHDqE5lbW8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHPQi1lz0ItZTj"})

driver.refresh()

sleep(5)
driver.quit()