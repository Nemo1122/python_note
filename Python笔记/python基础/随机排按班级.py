import xlrd, xlwt
import random

# 需要按班级列出学生，一个班一列
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

# 按照人数最少的班级，从每个班级中随机获取一个组成一个组
s_end = []
for i in range(min(ls)):
    s_t = []
    for sx in s:
        si = random.sample(sx, 1)
        sx.remove(si[0])
        s_t.append(si[0])
    # 将每组的人打乱
    random.shuffle(s_t)
    s_end.append(s_t)
# 处理剩余的人
s = [ii for i in s for ii in i if s]
# 如果人数是3的倍数，直接按3人分组
if len(s) % 3 == 0:
    for si in s:
        si = random.sample(s, 3)
        for i in si:
            s.remove(i)
        s_end.append(si)
# 如果人数不是3的倍数，
else:
    while len(s) >= 3:
        for si in s:
            si = random.sample(s, 3)
            for i in si:
                s.remove(i)
            s_end.append(si)
    else:
        for i in range(len(s)):
            s_end[i].append(s[i])
# 最后再将组打乱
random.shuffle(s_end)

# 写入文件
# 新建一个excel对象
wb = xlwt.Workbook()

# 新建一个名为text的sheet页
sh = wb.add_sheet("test")
# 前两个参数为单元格位置

for i in range(len(s_end)):
    for j in range(len(s_end[i])):
        sh.write(j, i, s_end[i][j])

# 目前只能保存成xls后缀
wb.save("data.xls")
