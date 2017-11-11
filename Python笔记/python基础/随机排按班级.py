import xlrd, xlwt
import random

excel = xlrd.open_workbook('E:\工作\海德\晚间特训\晚自习前特训分组表.xlsx')
sheet = excel.sheet_by_index(0)

# 从excel中获取数据并组成一个list
s = []
for n_row in range(sheet.nrows):
    # 去掉其中的空字符
    s.append([i for i in sheet.row_values(n_row) if i])

ls = []
for sx in s:
    ls.append(len(sx))

for i in range(min(ls)):
    pass

# 思路：由于班级人数不一致，以人数最少的班级为准，当组数小于最少的班级人数时，就每个班随机取一个，组成一个组。
# 超出的其他班级，集中在一起，随机取3个作为一组，当最后剩余的人数少于3时，就讲人随机安排到前面的几组中。
# 要实现输入每组人数，但是有个问题是如果组数与班级数不匹配，就不能一个个的取了，有点麻烦。
print(min(ls))
# 确定循环次数
len_s = len(s)
if len(s) % 3 == 0:
    count = 3
else:
    count = 4

# 循环从s列表中随机去3个
s_end = []
for i in range(count):
    # 不足完整一列的时候，不用随机取，直接全部取
    if len(s) < len_s//3:
        s_end.append(s)
    else:
        stu = random.sample(s, len_s//3)
        s_end.append(stu)
        for st in stu:
            s.remove(st)
# print(s_end)
for i in s_end:
    print(i)