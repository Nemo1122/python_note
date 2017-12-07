# enumerate
"""
    enumerate()是python的内置函数
    enumerate在字典上是枚举、列举的意思
    对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate将其组成一个索引序列，
    利用它可以同时获得索引和值
    enumerate多用于在for循环中得到计数
"""
# for index, number in enumerate(range(10)):
#     print(index, number)
# enumerate还可以接收第二个参数，用于指定索引起始值
for index, number in enumerate(range(10), 1):
    print(index, number)