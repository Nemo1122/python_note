class StaticClass:

    class_var = 'nemo'

    def __init__(self):
        self.name = 'abc'

    # 静态方法，无法访问实例相关的属性和方法，只能通过类名访问当前类的类方法和类属性
    @staticmethod
    def static_method():
        print('静态方法！')
        print('静态方法访问类变量', StaticClass.class_var)

    # 类方法, 必须带参数cls, 只能访问类相关的内容, 无法访问实例属性和方法
    @classmethod
    def class_method(cls):
        print('类方法')
        print('类方法访问类变量', cls.class_var)
        print('类方法访问静态方法：')
        StaticClass.static_method()

    def method_(self):
        self.static_method()
        self.class_method()

        StaticClass.class_method()
        StaticClass.static_method()

        print('实例方法访问类变量', self.class_var)


s = StaticClass()
# 实例可以调用实例方法、类方法、静态方法
s.method_()
s.class_method()
s.static_method()
# 类可以调用类方法
StaticClass.class_method()
# 类可以调用静态方法
StaticClass.static_method()
# StaticClass.method_()   # 类名无法调用实例方法
