from selenium import webdriver
from time import sleep
from pywinauto import application

driver=webdriver.Chrome()
driver.implicitly_wait(30)
driver.get('http://localhost/ecshop/admin')

driver.find_element_by_name('username').send_keys('root')
driver.find_element_by_name('password').send_keys('nemo1985')
driver.find_element_by_class_name('button').click()
driver.switch_to.frame('menu-frame')
driver.find_element_by_name('menu').click()
driver.find_element_by_link_text('添加新商品').click()
driver.switch_to.parent_frame()
driver.switch_to.frame('main-frame')
driver.find_element_by_id('gallery-tab').click()
driver.find_element_by_name("img_url[]").click()
try:
    # 由于浏览器上传窗口打开需要时间
    sleep(2)
    # 实例化Application
    app = application.Application()

    # 连接要操作的Windows窗口，可以使用autoitv3工具查看，也可以使用spy++lite工具来查看
    # 这里用的class而没有加窗口title，主要为了保证兼容性
    app.connect(class_name='#32770')

    # 在输入框中输入值
    app["Dialog"]["Edit1"].TypeKeys("E:\\1.jpg")

    # 点击打开/保存按钮
    app["Dialog"]["Button1"].click()
finally:
    sleep(15)
    driver.quit()