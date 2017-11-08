import xlrd, xlwt
import random

excel = xlrd.open_workbook('E:\工作\海德\晚间特训\晚自习前特训分组表.xlsx')
sheet = excel.sheet_by_index(0)

# 从excel中获取数据并组成一个list
s = []
for n_row in range(sheet.nrows):
    s += sheet.row_values(n_row)
# 去掉其中的空字符
s = [i for i in s if i]

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
print(s_end)
# print(len(s_end))

# 新建一个excel对象
wb = xlwt.Workbook()

# 新建一个名为text的sheet页
sh = wb.add_sheet("test")
print(s_end)
# 前两个参数为单元格位置
for i in range(len(s_end)):
    for j in range(len(s_end[i])):
        sh.write(i, j, s_end[i][j])

# 目前只能保存成xls后缀
wb.save("data.xls")