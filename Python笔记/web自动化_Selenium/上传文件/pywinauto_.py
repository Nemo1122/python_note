from pywinauto import application


# 实例化Application
app = application.Application()

# 连接要操作的Windows窗口，可以使用autoitv3工具查看，也可以使用spy++lite工具来查看
# 这里用的class而没有加窗口title，主要为了保证兼容性
app.connect(class_name='#32770')

# 在输入框中输入值
app["Dialog"]["Edit1"].TypeKeys("E:\\1.jpg")

# 点击打开/保存按钮
app["Dialog"]["Button1"].click()