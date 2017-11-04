# 1. 对可迭代函数'iterable'中的每一个元素应用‘function’方法，将结果作为list返回。
# map用list循环为方法赋值，并将结果存在list中。


def add100(x):
    x += 100
    return x


for i in map(add100, [5, 6, 7, 8, 9, 10]):
    print(i)


# 2. 如果给出了额外的可迭代参数，则对每个可迭代参数中的元素‘并行’的应用‘function’。
def add(a, b, c):
    return a+b+c


l1 = [3, 4, 5]
l2 = [6, 5, 7]
l3 = [8, 9, 3]

for i in map(add, l1, l2, l3):
    print(i)


for i in map(add100, [5, 6, 7, 8, 9, 10]):
    print(i)
