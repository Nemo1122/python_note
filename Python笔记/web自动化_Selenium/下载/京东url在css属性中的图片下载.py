from selenium import webdriver
import requests
from time import sleep
import re


driver = webdriver.Chrome()

driver.get('http://jd.com')
# driver.maximize_window()
driver.implicitly_wait(30)

try:
    # js = "return $('[href=\"//www.jd.com]\"').css('background-image')"
    # 在js中增加return，可以将js执行的值返回给selenium
    # $(obj).css(attr,attrvalue)，JQuery语法，获取页面对象obj的css属性值，或修改属性值
    js = """return $('[href="//www.jd.com"]').css('background-image')"""
    # js = """$('#key')[0].value='abc'"""
    url = driver.execute_script(js)
    # 匹配网址的正则表达式“(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]”
    url = re.search(r'(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]', url).group(0)
    r = requests.get(url)
    with open('jd.png', 'wb') as f:
        # r.content 返回压缩格式的数据，一般图片之类的都是通过r.content获取
        f.write(r.content)
finally:
    sleep(1)
    driver.quit()
