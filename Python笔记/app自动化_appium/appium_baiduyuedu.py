from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep

desired_capabilities = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:21503',
    # 'platformVersion': '4.4.4',  # 逍遥模拟器
    'platformVersion': '7.1.1',    # 小米真机
    'appPackage': 'com.baidu.yuedu',
    'appActivity': 'com.baidu.yuedu.splash.SplashActivity',
    # 'browserName': 'Browser',
    # "automationName": "selendroid",
    'noReset': 'true',
    # 设置超时时间，如果不设置，1分钟appium没接收到新请求就会关闭链接
    'newCommandTimeout': 600
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

sleep(5)

# driver.find_element_by_id('com.baidu.yuedu:id/righttitle').click()

# 切换context，进入HTML5
# con = driver.contexts
#
# print(con)
# for c in con:
#     if c == 'WEBVIEW_com.baidu.yuedu':
#         driver.switch_to.context(c)


# driver.find_element_by_css_selector('.huanyihuan').click()
# driver.find_element_by_css_selector('.c-see-more-button').click()

# li = driver.find_elements_by_accessibility_id('换一换')
# print(li)
# li[0].click()
# li_all = driver.find_elements_by_accessibility_id('查看全部')
# print(li_all)
# li_all[0].click()


# driver.switch_to.window(con[1])

# 滑动
# size = driver.get_window_size()


# 滑动
def slide(direction):
    size = driver.get_window_size()
    if direction == 'left':
        # 从右往左滑动, 相当于往右边翻页    y轴保持不变 x开始点大于x结束点
        start_x = int(size['width'] * 0.75)
        start_y = int(size['height'] * 0.5)
        end_x = int(size['width'] * 0.25)
        end_y = int(size['height'] * 0.5)
    elif direction == 'right':
        # 从左往右滑动,相当于向左翻页      y轴保持不变 x结束点大于x开始点
        start_x = int(size['width'] * 0.25)
        start_y = int(size['height'] * 0.5)
        end_x = int(size['width'] * 0.75)
        end_y = int(size['height'] * 0.5)
    elif direction == 'up':
        # 从下往上滑动,相当于向上翻页      x轴保持不变 y开始点大于y结束点
        start_x = int(size['width'] * 0.5)
        start_y = int(size['height'] * 0.75)
        end_x = int(size['width'] * 0.5)
        end_y = int(size['height'] * 0.25)
    elif direction == 'down':
        # 从下往上滑动,相当于向上翻页      x轴保持不变 y结束点大于y开始点
        start_x = int(size['width'] * 0.5)
        start_y = int(size['height'] * 0.25)
        end_x = int(size['width'] * 0.5)
        end_y = int(size['height'] * 0.75)
    else:
        raise ValueError('请输入left, right, up, down等方向！')
    # swipe与flick区别在于swipe是缓慢滑动,可以设置滑动时间;flick是快速滑动,不能设置滑动时间
    driver.swipe(start_x, start_y, end_x, end_y)




# driver.flick()
driver.tap()

