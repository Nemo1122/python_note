import copy

# -----直接赋值------
# l1更改就会随着更改
l1 = [[1, 2, 3], 3, 4]
l2 = l1

l1[0][1] = 0
l1[1] = 100
print("直接赋值：", l2)

# -----copy方法------
# l1第一层元素改变，l2不会变化
# l1第二层元素改变，l2会随着更改
l1 = [[1, 2, 3], 3, 4]
l2 = l1.copy()

l1[0][1] = "a"
l1[1] = "aa"
print("copy方法：", l2)

# -----copy.copy------
# copy库中的copy，与copy方法等同
l1 = [[1, 2, 3], 3, 4]
l2 = copy.copy(l1)

l1[0][1] = "b"
l1[0][1] = "bb"
print("copy.copy：", l2)

# -----copy.deepcopy------
# copy库中的deepcopy(), 深度拷贝
# l2不会随着l1的值改变，不管l1层级多深
l1 = [[1, 2, 3], 3, 4]
l2 = copy.deepcopy(l1)

l1[0][1] = "c"
print("copy.deepcopy \n两层的情况：", l2)

l1 = [[1, 2, [4, 5, 6]], 3, 4]
l2 = copy.deepcopy(l1)

l1[0][2][1] = "x"
print("三层的情况：", l2)

l1 = [[1, 2, [4, 5, [7, 8, 9]]], 3, 4]
l2 = copy.deepcopy(l1)

l1[0][2][2][1] = "xx"
print("四层的情况：", l2)

# 再多层也是一样，所以不再演示
