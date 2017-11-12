from appium import webdriver


desired_capabilities = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:21503',
    'platformVersion': '4.4.4',  # 逍遥模拟器
    # 'platformVersion': '7.1.1',    # 小米真机
    # 通过hierarchyviewer.bat工具获取到的
    'appPackage': 'com.microvirt.launcher',
    # 默认的系统activity
    'appActivity': '.Launcher',
    # 'browserName': 'Browser',
    # api 17以下的版本需要显示申明使用selendroid
    # "automationName": "selendroid",
    'noReset': 'true',
    # 设置超时时间，如果不设置，1分钟appium没接收到新请求就会关闭链接
    'newCommandTimeout': 600
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
driver.implicitly_wait(30)
# 打开图库中的图片
# 点击图库
driver.find_element_by_xpath('//android.widget.TextView[@text="图库"]').click()
# 点击所有图片
driver.find_element_by_xpath('//android.widget.TextView[@resource-id=\"com.android.gallery:id/title\" and @text=\"所有照片 (5)\"]').click()
# 点击第一张图片
driver.tap([(100, 100)], 50)



