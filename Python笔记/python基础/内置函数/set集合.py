#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 创建集合
# s = set('python')
# print(s)
# {'h', 't', 'p', 'n', 'y', 'o'}

# 集合添加、删除
# python 集合的添加有两种常用方法，分别是add和update。

# 集合add方法：是把要传入的元素做为一个整个添加到集合中，例如：
# s.add('c')
# print(s)
# {'y', 'p', 'n', 'c', 'h', 't', 'o'}

# 集合update方法：是把要传入的元素拆分，做为个体传入到集合中，例如：
# s.update('abc')
# print(s)
# {'h', 'c', 't', 'n', 'y', 'a', 'p', 'b', 'o'}

# 集合删除操作方法：remove
# s.remove('p')
# print(s)
# {'t', 'y', 'o', 'n', 'h'}

# pop方法，删除第一个元素
# s.pop()
# print(s)
# {'t', 'y', 'o', 'n', 'h'}


a = set('vwx')
b = set('xyz')
# 集合的交集、合集（并集）、差集，了解python集合set与列表list的这些非常好用的功能前，要先了解一些集合操作符号
# 差集、相对补集 -
# print(a - b)
# {'v', 'w'}

# 交集 &
# print(a & b)
# {'x'}

# 合集、并集 |
# print(a | b)
# {'x', 'v', 'w', 'y', 'z'}

# 不等于 !=
# print(a != b)
# True

# 等于 ==
# print(a == b)
# False

# 包含 in
# print(a in b)
# False

# 不包含 not in
# print(a not in b)
# True
