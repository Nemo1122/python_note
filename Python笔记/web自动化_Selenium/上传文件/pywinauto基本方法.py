"""
pywinauto是win32自动化库
可以使用pywinauto实现上传下载文件
"""
from pywinauto import application

# 实例化Application
app = application.Application()

# 连接要操作的Windows窗口，可以使用autoitv3工具查看，也可以使用spy++lite工具来查看
# 这里用的class而没有加窗口title，主要为了保证兼容性
app.connect(class_name='#32770', handle=0x00000000000D11CC)

# 在输入框中输入值
app["Dialog"]["Edit1"].TypeKeys(r"e:\jd1.jpg")

# 点击打开/保存按钮
app["Dialog"]["Button1"].click()


# 下面还有一些常用的操作
# app['Cy']['Edit2'].TypeKeys('aaa')#输入值,不会清空原来的数据
# app['Cy']['Edit3'].SetEditText('bbbb')
# app['Cy']['Edit3'].SetText('bbbb')
# app['Cy']['Edit4'].set_edit_text('你好')
# 3种输入值,与.TypeKeys区别在于，这个如果文本框禁止输入也可强制输入
# a=app['Cy']['Edit1'].WindowText()#获取值
# b=app['Cy']['Edit3'].texts()#获取值,返回一个数组
# c=app['Cy']['Edit4'].text_block()#获取值
# print (a)
# print (b)
# print (c)
# app['Cy'][u'启动'].click()#点击控件
# app['Cy'].close_alt_f4()#关闭窗口