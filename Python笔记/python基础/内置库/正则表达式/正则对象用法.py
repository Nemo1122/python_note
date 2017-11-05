import re


str1 = "hi，您的会员编号为Nemo_2017，请注意保管，如果遗忘，可以登录www.xxx.cn查询"
str2 = "此次生成的订单号20170728010132111;订单号20170728010132112！请注意确认！"

# compile: 生成匹配对象
st1 = re.compile(r'[a-zA-Z0-9_]+')
st2 = re.compile(r'\d+')

# match: 从第一个字符开始匹配，如果没有则返回None
print(st1.match(str1))
# group获取查找到的组
print(st1.match(str1).group())

# search: 查找整个字符串，直到找到第一个匹配项，返回一个匹配结果对象，需要用group获取对象中的查找结果
print(st2.search(str2))
print(st2.search(str2).group())

# findall: 查找整个字符串，找到所有匹配项, 返回一个list，而不是re对象
print(st1.findall(str1))

# finditer: 查找整个字符串，找到所有匹配项，返回一个所有匹配对象的iter迭代器,
# 要获取内容则必须使用for循环，获取每个对象的group
print(st1.finditer(str1))
for r in st1.finditer(str1):
    print(r.group())

# split: 使用匹配对象拆分字符串，返回一个list
print(st2.split(str2))

# sub: 替换查找到的结果
print(st2.sub('hi', str2))

# subn: 替换查找到的结果，以元组形式返回替换后的内容和替换次数
print(st2.subn('hi', str2))