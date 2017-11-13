# 腾讯手机管家的九宫格
"""
x1,y1    x2,y2   x3,y3
x4,y4    x5,y5   x6,y6
x7,y7    x8,y8   x9,y9
计算的基准是逍遥安卓模拟器的分辨率576*1024
"""
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
from time import sleep


desired_capabilities = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:21503',
    'platformVersion': '4.4.4',
    'appPackage': 'com.tencent.mm',
    'appActivity': 'com.tencent.mm.ui.LauncherUI',
    'noReset': 'true',
    # 设置超时时间，如果不设置，1分钟appium没接收到新请求就会关闭链接
    'newCommandTimeout': 600
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)


def gesture(action, size, s):
    """
    :param size: 当前窗口的分辨率,通过driver.get_window_size()获取
    :return:
    """
    # 九宫格第一个点的x轴大小
    # x1上下左右边界的位置，当然实际使用范围时会略大于该值
    x1_start = 88 / 576
    x1_end = 158 / 576
    y1_start = 261 / 1024
    y1_end = 330 / 1024

    # 每个点的xy大小
    x_w = size['width'] * abs(x1_end - x1_start)
    y_w = size['height'] * abs(y1_end - y1_start)
    print(x_w, y_w)

    # 取其中点
    x = x_w / 2
    y = y_w / 2

    # 左右两点的距离
    x_to_x = size['width'] * (abs(243 - 152) / 576)
    # 上下两点的距离
    y_to_y = size['height'] * (abs(421 - 333) / 1024)

    x1_end_pos = size['width'] * (154 / 576)
    y1_end_pos = size['height'] * (330 / 1024)

    # 横向第二个点, 第三个点
    x1 = x1_end_pos - x
    x2 = x1_end_pos + x_to_x + x
    x3 = x1_end_pos + 2 * x_to_x + x_w + x

    # 纵向第二个点, 第三个点
    y1 = y1_end_pos - y
    # 由于y值计算偏差有点大, 增加点偏移量
    y4 = y1_end_pos + y_to_y + y + 10
    # 由于y值计算偏差有点大, 增加点偏移量
    y5 = y1_end_pos + 2 * y_to_y + y_w + y + 30

    p = {
        1: {'x': x1, 'y': y1},
        2: {'x': x2, 'y': y1},
        3: {'x': x3, 'y': y1},
        4: {'x': x1, 'y': y4},
        5: {'x': x2, 'y': y4},
        6: {'x': x3, 'y': y4},
        7: {'x': x1, 'y': y5},
        8: {'x': x2, 'y': y5},
        9: {'x': x3, 'y': y5},

    }
    print(p)
    action.press(x=p[s[0]]['x'], y=p[s[0]]['y'])
    print(p[s[0]]['x'], p[s[0]]['y'])
    for i in range(1, len(s)):
        # 判断当前点在上一个点的位置
        x = p[s[i]]['x'] - p[s[i - 1]]['x']
        y = p[s[i]]['y'] - p[s[i - 1]]['y']
        action.move_to(x=x, y=y)
        print(x, y)
        action.wait(300)

    action.release()
    action.perform()


sleep(10)
size = driver.get_window_size()


action = TouchAction(driver)
s = [7, 4, 1, 5, 9, 6, 3]
gesture(action, size, s)

# 逍遥安卓成功的例子
# action.press(x=121.0, y=600.0).wait(500).move_to(x=0,y=-150.0).wait(500).move_to(x=0,y=-150.0).wait(500).move_to(x=150,y=150.0).wait(500).move_to(x=150,y=180.0).wait(500).move_to(x=10,y=-150).wait(500).move_to(x=10,y=-180).release().perform()

