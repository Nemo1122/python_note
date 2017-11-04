import xlwt

# 新建一个excel对象
wb = xlwt.Workbook()

# 新建一个名为text的sheet页
sh = wb.add_sheet("test")

# 前两个参数为单元格位置
for i in range(5):
    sh.write(i, 0, i)

# 目前只能保存成xls后缀
wb.save("data.xls")