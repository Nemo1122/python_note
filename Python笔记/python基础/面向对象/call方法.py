class Count:
    # init方法
    def __init__(self, x):
        self.x = x

    # call方法，有了call方法可以把类和其实例当成函数调用
    def __call__(self, y):
        return self.x+y


print("Count(3)结果是%r" % Count(3))  # 通过类名调用，返回一个对象
a = Count(3)       # 实例化类Count

print("A实例化的对象作为方法调用，结果为%r" % a(2))     # 实例可以作为方法使用


def fun(method):         # 设置一个函数用于接收一个函数或方法
    return method(5)        # 给方法传一个参数


print("把A作为方法传入fun函数，得到的结果是%r" % (fun(Count(3)))) # 相当于把类A当成一个方法传入这个参数
# print("把A的实例a作为方法传入fun函数，得到的结果是%r" % (fun(a(3))))#相当于把类A当成一个方法传入这个参数,这一句会报错
# 由此可以看出A和a分别作为函数调用的时候的区别，A(3)返回的是一个方法对象，a(3)直接执行的是call方法体，也就是返回的是运算结果
