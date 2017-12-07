# 实现斐波拉契数列

def fib(n):
    a, b = 1, 1
    while a < n:
        yield a
        a, b = b, a + b

# 调用
# for i, f in enumerate(fib(10), 1):
#     print(i, f)

f = fib(10)
# print(type(f))
# f为生成器
# <class 'generator'>

print(dir(f))
# dir() 函数算得上是Python比较常用也很好用的一个函数。它返回包含要查询对象的所有属性名称的列表。
# 使用dir()函数可以查看对像内所有属性及方法，在python中任何东西都是对像，一种数据类型，一个模块等，
# 都有自己的属性和方法，除了常用方法外，其它的你不需要全部记住它，交给dir()函数就好了。
# ['__class__', '__del__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
# '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__',
# '__iter__', '__le__', '__lt__', '__name__', '__ne__', '__new__', '__next__',
# '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
# '__sizeof__', '__str__', '__subclasshook__', 'close', 'gi_code', 'gi_frame',
# 'gi_running', 'gi_yieldfrom', 'send', 'throw']


